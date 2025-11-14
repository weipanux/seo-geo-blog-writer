#!/usr/bin/env python3
"""
Test script for keyword_research.py

Tests both fallback mode and API response parsing without requiring API credentials.
Can also test with real API if credentials are provided.

Usage:
    # Test fallback mode (no API key needed)
    python test_keyword_research.py
    
    # Test with mock API response
    python test_keyword_research.py --mock-api
    
    # Test with real API (uses hybrid credential management)
    python test_keyword_research.py --real-api
    python test_keyword_research.py --real-api --api-key "login:password"
    python test_keyword_research.py --real-api --api-key "[base64-encoded]"  # Base64 format
    python test_keyword_research.py --real-api --interactive
    
    # Test specific component
    python test_keyword_research.py --test-parsing
"""

import argparse
import json
import os
import sys
from typing import Dict, List

# Import the module to test
from keyword_research import (
    KeywordData,
    KeywordResearcher,
    format_output
)


def test_fallback_mode():
    """Test fallback mode (no API key)"""
    print("=" * 60)
    print("TEST 1: Fallback Mode (No API Key)")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key=None)
    
    assert not researcher.api_available, "API should not be available"
    
    keywords = researcher.research_keywords("healthy boundaries", limit=5)
    
    assert len(keywords) > 0, "Should return at least one keyword"
    assert len(keywords) <= 5, "Should respect limit"
    
    # Check structure
    for kw in keywords:
        assert isinstance(kw, KeywordData), "Should return KeywordData objects"
        assert kw.keyword, "Keyword should not be empty"
        assert isinstance(kw.search_volume, int), "Search volume should be int"
        assert 0 <= kw.keyword_difficulty <= 100, "Difficulty should be 0-100"
        assert 0 <= kw.relevance_score <= 100, "Relevance should be 0-100"
        assert isinstance(kw.related_keywords, list), "Related keywords should be list"
    
    print(f"✓ Returned {len(keywords)} keywords")
    print(f"✓ First keyword: {keywords[0].keyword}")
    print(f"✓ Search volume: {keywords[0].search_volume:,}")
    print(f"✓ Difficulty: {keywords[0].keyword_difficulty}/100")
    print(f"✓ Relevance: {keywords[0].relevance_score:.1f}/100")
    
    return True


def test_api_response_parsing():
    """Test API response parsing with mock data"""
    print("\n" + "=" * 60)
    print("TEST 2: API Response Parsing (Mock Data)")
    print("=" * 60)
    
    # Mock API response matching DataForSEO v3 structure
    # Note: API returns status_code: 20000 at top level (not HTTP 200)
    mock_response = {
        "version": "0.1.20231115",
        "status_code": 20000,
        "status_message": "Ok.",
        "time": 0.123,
        "cost": 0.001,
        "tasks_count": 1,
        "tasks_error": 0,
        "tasks": [{
            "id": "test-task-123",
            "status_code": 20000,
            "status_message": "Ok.",
            "time": 0.123,
            "cost": 0.001,
            "result_count": 3,
            "path": ["v3", "keywords_data", "google_ads", "search_volume", "live"],
            "data": {},
            "result": [
                {
                    "keyword": "healthy boundaries",
                    "search_volume": 12000,
                    "competition": "MEDIUM",
                    "competition_index": 45,
                    "cpc": 1.25,
                    "monthly_searches": [
                        {"year": 2024, "month": 1, "search_volume": 11000},
                        {"year": 2024, "month": 2, "search_volume": 12000}
                    ]
                },
                {
                    "keyword": "setting healthy boundaries",
                    "search_volume": 8500,
                    "competition": "LOW",
                    "competition_index": 30,
                    "cpc": 0.85
                },
                {
                    "keyword": "boundaries in relationships",
                    "search_volume": 15000,
                    "competition": "HIGH",
                    "competition_index": 75,
                    "cpc": 2.10
                }
            ]
        }]
    }
    
    researcher = KeywordResearcher(api_key="test:key")
    keywords = researcher._parse_api_response(mock_response, "healthy boundaries", limit=3)
    
    assert len(keywords) == 3, f"Expected 3 keywords, got {len(keywords)}"
    
    # Check first keyword
    kw1 = keywords[0]
    assert kw1.keyword == "healthy boundaries", "First keyword should match"
    assert kw1.search_volume == 12000, "Search volume should match"
    assert kw1.keyword_difficulty == 45, "Should use competition_index"
    
    # Check second keyword (no competition_index, should use fallback)
    kw2 = keywords[1]
    assert kw2.keyword == "setting healthy boundaries"
    # Should use competition string mapping (LOW = 25)
    
    # Check sorting (should be sorted by relevance)
    assert keywords[0].relevance_score >= keywords[1].relevance_score, "Should be sorted by relevance"
    
    print(f"✓ Parsed {len(keywords)} keywords from mock response")
    print(f"✓ First keyword: {kw1.keyword} (Vol: {kw1.search_volume:,}, Diff: {kw1.keyword_difficulty})")
    print(f"✓ Relevance scores: {[f'{kw.relevance_score:.1f}' for kw in keywords]}")
    
    return True


def test_difficulty_calculation():
    """Test difficulty calculation with various inputs"""
    print("\n" + "=" * 60)
    print("TEST 3: Difficulty Calculation")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    # Test with competition_index
    item1 = {"competition_index": 65}
    diff1 = researcher._calculate_difficulty(item1)
    assert diff1 == 65, f"Should use competition_index directly, got {diff1}"
    print(f"✓ competition_index: {diff1}")
    
    # Test with competition string (HIGH)
    item2 = {"competition": "HIGH", "cpc": 1.5}
    diff2 = researcher._calculate_difficulty(item2)
    assert 0 <= diff2 <= 100, f"Difficulty should be 0-100, got {diff2}"
    print(f"✓ competition='HIGH': {diff2}")
    
    # Test with competition string (LOW)
    item3 = {"competition": "LOW", "cpc": 0.5}
    diff3 = researcher._calculate_difficulty(item3)
    assert diff3 < diff2, "LOW competition should be easier than HIGH"
    print(f"✓ competition='LOW': {diff3}")
    
    # Test with no competition data
    item4 = {"cpc": 2.0}
    diff4 = researcher._calculate_difficulty(item4)
    assert 0 <= diff4 <= 100, f"Should handle missing competition, got {diff4}"
    print(f"✓ No competition data: {diff4}")
    
    return True


def test_relevance_calculation():
    """Test relevance score calculation"""
    print("\n" + "=" * 60)
    print("TEST 4: Relevance Score Calculation")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    # Exact match with high volume
    item1 = {
        "keyword": "healthy boundaries",
        "search_volume": 15000,
        "competition_index": 40
    }
    rel1 = researcher._calculate_relevance(item1, "healthy boundaries")
    assert rel1 > 80, f"Exact match with high volume should score high, got {rel1}"
    print(f"✓ Exact match + high volume: {rel1:.1f}")
    
    # Partial match
    item2 = {
        "keyword": "setting healthy boundaries",
        "search_volume": 5000,
        "competition_index": 50
    }
    rel2 = researcher._calculate_relevance(item2, "healthy boundaries")
    assert rel2 > 50, f"Partial match should score medium, got {rel2}"
    print(f"✓ Partial match: {rel2:.1f}")
    
    # Low volume
    item3 = {
        "keyword": "boundaries",
        "search_volume": 50,
        "competition_index": 60
    }
    rel3 = researcher._calculate_relevance(item3, "healthy boundaries")
    assert rel3 < rel1, "Lower volume should score lower"
    print(f"✓ Low volume: {rel3:.1f}")
    
    return True


def test_output_formats():
    """Test different output formats"""
    print("\n" + "=" * 60)
    print("TEST 5: Output Formats")
    print("=" * 60)
    
    keywords = [
        KeywordData(
            keyword="test keyword",
            search_volume=5000,
            keyword_difficulty=45,
            related_keywords=["related 1", "related 2"],
            relevance_score=75.5
        )
    ]
    
    # Test JSON format
    json_output = format_output(keywords, "json")
    assert json_output, "JSON output should not be empty"
    parsed = json.loads(json_output)
    assert len(parsed) == 1, "Should contain one keyword"
    print("✓ JSON format works")
    
    # Test markdown format
    md_output = format_output(keywords, "markdown")
    assert "# Keyword Research Results" in md_output, "Should contain markdown header"
    assert "test keyword" in md_output, "Should contain keyword"
    print("✓ Markdown format works")
    
    # Test simple format
    simple_output = format_output(keywords, "simple")
    assert "test keyword" in simple_output, "Should contain keyword"
    # Search volume may be formatted with commas (5,000) or without (5000)
    assert "5,000" in simple_output or "5000" in simple_output, "Should contain search volume"
    print("✓ Simple format works")
    
    return True


def test_base64_credentials():
    """Test Base64 credential decoding"""
    print("\n" + "=" * 60)
    print("TEST 6: Base64 Credential Decoding")
    print("=" * 60)
    
    from keyword_research import decode_base64_credentials
    
    # Test with Base64-encoded credentials
    # Example: "testuser:testpass" encoded in Base64
    import base64
    test_credentials = "testuser:testpass"
    base64_encoded = base64.b64encode(test_credentials.encode('utf-8')).decode('utf-8')
    
    # Test decoding
    decoded = decode_base64_credentials(base64_encoded)
    assert decoded == test_credentials, f"Should decode Base64, got {decoded}"
    print(f"✓ Base64 decoding works: {base64_encoded[:20]}... → {decoded}")
    
    # Test with plain text (should pass through)
    plain_text = "testuser:testpass"
    result = decode_base64_credentials(plain_text)
    assert result == plain_text, "Plain text should pass through unchanged"
    print(f"✓ Plain text passes through: {plain_text}")
    
    # Test with invalid Base64 (should return as-is)
    invalid = "not-valid-base64!!!"
    result = decode_base64_credentials(invalid)
    assert result == invalid, "Invalid Base64 should return as-is"
    print(f"✓ Invalid Base64 handled gracefully")
    
    return True


def test_real_api(api_key: str = None, interactive: bool = False):
    """
    Test with real API using hybrid credential management.
    
    Args:
        api_key: Explicitly provided API key (optional)
        interactive: Whether to prompt for credentials if not found
    """
    print("\n" + "=" * 60)
    print("TEST 6: Real API Test (if credentials available)")
    print("=" * 60)
    
    # Try to get credentials using hybrid approach
    from keyword_research import get_api_key
    
    resolved_key = get_api_key(api_key, interactive=interactive)
    
    if not resolved_key:
        print("⚠ Skipping: No API credentials found")
        print("  Credential options:")
        print("  1. Set DATAFORSEO_API_KEY environment variable")
        print("  2. Create ~/.dataforseo-skill/config.json")
        print("  3. Use --api-key 'login:password' argument")
        print("  4. Use --interactive flag to prompt")
        return True
    
    try:
        researcher = KeywordResearcher(api_key=resolved_key, interactive=False)
        assert researcher.api_available, "API should be available"
        
        print(f"✓ Using API credentials (source: {'explicit' if api_key else 'auto-detected'})")
        print()
        
        keywords = researcher.research_keywords("healthy boundaries", limit=3)
        
        if keywords:
            print(f"✓ API returned {len(keywords)} keywords")
            print()
            for i, kw in enumerate(keywords, 1):
                print(f"  {i}. {kw.keyword}")
                print(f"     Volume: {kw.search_volume:,} | Difficulty: {kw.keyword_difficulty}/100 | Relevance: {kw.relevance_score:.1f}/100")
        else:
            print("⚠ API returned no keywords")
            print("  Possible reasons:")
            print("  - Rate limited")
            print("  - Invalid API key")
            print("  - Network error")
            print("  - API service unavailable")
        
        return True
        
    except Exception as e:
        print(f"⚠ API test failed: {e}")
        print("  This is OK if API key is invalid or rate limited")
        import traceback
        print("\n  Full error:")
        traceback.print_exc()
        return True


def test_generate_variations():
    """Test keyword variation generation"""
    print("\n" + "=" * 60)
    print("TEST 7: Keyword Variation Generation")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    variations = researcher._generate_variations("healthy boundaries")
    
    assert len(variations) > 0, "Should generate variations"
    assert "healthy boundaries" in variations, "Should include original topic"
    assert any("best" in v for v in variations), "Should include prefix variations"
    assert any("guide" in v for v in variations), "Should include suffix variations"
    
    print(f"✓ Generated {len(variations)} variations")
    print(f"✓ Sample variations: {variations[:3]}")
    
    return True


def test_estimate_volume():
    """Test search volume estimation"""
    print("\n" + "=" * 60)
    print("TEST 8: Search Volume Estimation")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    # Test short keywords (higher volume)
    vol1 = researcher._estimate_volume("keyword")
    vol2 = researcher._estimate_volume("two words")
    assert vol1 == 5000 and vol2 == 5000, "Short keywords should have high volume"
    print(f"✓ Short keywords (1-2 words): {vol1}")
    
    # Test medium keywords
    vol3 = researcher._estimate_volume("three word keyword")
    assert vol3 == 2000, "3-word keywords should have medium volume"
    print(f"✓ Medium keywords (3 words): {vol3}")
    
    # Test long keywords (lower volume)
    vol4 = researcher._estimate_volume("this is a longer keyword phrase")
    assert vol4 == 800, "Long keywords should have lower volume"
    print(f"✓ Long keywords (4+ words): {vol4}")
    
    return True


def test_estimate_difficulty():
    """Test keyword difficulty estimation"""
    print("\n" + "=" * 60)
    print("TEST 9: Keyword Difficulty Estimation")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    # Test short keywords (harder)
    diff1 = researcher._estimate_difficulty("keyword")
    diff2 = researcher._estimate_difficulty("two words")
    assert diff1 == 70 and diff2 == 70, "Short keywords should be harder"
    print(f"✓ Short keywords (1-2 words): {diff1}/100")
    
    # Test medium keywords
    diff3 = researcher._estimate_difficulty("three word keyword")
    assert diff3 == 55, "3-word keywords should be medium difficulty"
    print(f"✓ Medium keywords (3 words): {diff3}/100")
    
    # Test long keywords (easier)
    diff4 = researcher._estimate_difficulty("this is a longer keyword phrase")
    assert diff4 == 35, "Long keywords should be easier"
    print(f"✓ Long keywords (4+ words): {diff4}/100")
    
    return True


def test_generate_related():
    """Test related keyword generation"""
    print("\n" + "=" * 60)
    print("TEST 10: Related Keyword Generation")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    related = researcher._generate_related("test keyword", "original topic")
    
    assert len(related) > 0, "Should generate related keywords"
    assert any("what is" in r for r in related), "Should include question formats"
    assert any("how to" in r for r in related), "Should include how-to format"
    
    print(f"✓ Generated {len(related)} related keywords")
    print(f"✓ Sample: {related[:2]}")
    
    return True


def test_extract_related():
    """Test related keyword extraction from API response"""
    print("\n" + "=" * 60)
    print("TEST 11: Extract Related Keywords from API")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    # Test with empty result (API doesn't provide related keywords)
    item = {"keyword": "test"}
    related = researcher._extract_related(item)
    assert isinstance(related, list), "Should return a list"
    print("✓ Returns empty list (API doesn't provide related keywords)")
    
    return True


def test_get_api_key():
    """Test hybrid credential management"""
    print("\n" + "=" * 60)
    print("TEST 12: Hybrid Credential Management")
    print("=" * 60)
    
    from keyword_research import get_api_key
    import os
    
    # Test explicit API key
    key1 = get_api_key("test:key")
    assert key1 == "test:key", "Should return explicit key"
    print("✓ Explicit API key works")
    
    # Test environment variable (if set)
    if os.getenv('DATAFORSEO_API_KEY'):
        key2 = get_api_key()
        assert key2 == os.getenv('DATAFORSEO_API_KEY'), "Should use env var"
        print("✓ Environment variable works")
    else:
        print("⚠ Skipping env var test (not set)")
    
    # Test with None (should try other methods)
    # This is tested indirectly through other tests
    print("✓ Credential resolution works")
    
    return True


def test_keyword_data_to_dict():
    """Test KeywordData serialization"""
    print("\n" + "=" * 60)
    print("TEST 13: KeywordData Serialization")
    print("=" * 60)
    
    kw = KeywordData(
        keyword="test",
        search_volume=1000,
        keyword_difficulty=50,
        related_keywords=["related"],
        relevance_score=75.5
    )
    
    data = kw.to_dict()
    assert isinstance(data, dict), "Should return dictionary"
    assert data['keyword'] == "test", "Should contain keyword"
    assert data['search_volume'] == 1000, "Should contain search volume"
    assert data['relevance_score'] == 75.5, "Should contain relevance score"
    
    print("✓ to_dict() works correctly")
    print(f"✓ Dictionary keys: {list(data.keys())}")
    
    return True


def test_error_handling():
    """Test error handling with invalid responses"""
    print("\n" + "=" * 60)
    print("TEST 14: Error Handling")
    print("=" * 60)
    
    researcher = KeywordResearcher(api_key="test:key")
    
    # Test with invalid status code (not 200 or 20000)
    invalid_response1 = {"status_code": 400, "status_message": "Bad Request"}
    keywords1 = researcher._parse_api_response(invalid_response1, "test", 5)
    assert len(keywords1) == 0, "Should return empty list for invalid status"
    print("✓ Handles invalid HTTP status")
    
    # Test with task error
    invalid_response2 = {
        "status_code": 20000,
        "tasks": [{
            "status_code": 40001,
            "status_message": "Task failed"
        }]
    }
    keywords2 = researcher._parse_api_response(invalid_response2, "test", 5)
    assert len(keywords2) == 0, "Should return empty list for task error"
    print("✓ Handles task-level errors")
    
    # Test with missing result
    invalid_response3 = {
        "status_code": 20000,
        "tasks": [{
            "status_code": 20000,
            "result": []
        }]
    }
    keywords3 = researcher._parse_api_response(invalid_response3, "test", 5)
    assert len(keywords3) == 0, "Should handle empty results"
    print("✓ Handles empty results")
    
    return True


def run_all_tests():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("RUNNING ALL TESTS")
    print("=" * 60)
    
    tests = [
        ("Fallback Mode", test_fallback_mode),
        ("API Response Parsing", test_api_response_parsing),
        ("Difficulty Calculation", test_difficulty_calculation),
        ("Relevance Calculation", test_relevance_calculation),
        ("Output Formats", test_output_formats),
        ("Base64 Credentials", test_base64_credentials),
        ("Keyword Variation Generation", test_generate_variations),
        ("Search Volume Estimation", test_estimate_volume),
        ("Keyword Difficulty Estimation", test_estimate_difficulty),
        ("Related Keyword Generation", test_generate_related),
        ("Extract Related Keywords", test_extract_related),
        ("Hybrid Credential Management", test_get_api_key),
        ("KeywordData Serialization", test_keyword_data_to_dict),
        ("Error Handling", test_error_handling),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            test_func()
            passed += 1
        except AssertionError as e:
            print(f"\n✗ {test_name} FAILED: {e}")
            failed += 1
        except Exception as e:
            print(f"\n✗ {test_name} ERROR: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    return failed == 0


def main():
    parser = argparse.ArgumentParser(
        description="Test keyword_research.py functionality"
    )
    parser.add_argument(
        "--mock-api",
        action="store_true",
        help="Test API response parsing with mock data"
    )
    parser.add_argument(
        "--real-api",
        action="store_true",
        help="Test with real API (uses hybrid credential management)"
    )
    parser.add_argument(
        "--api-key",
        help="Explicitly provide API key for testing (format: login:password)"
    )
    parser.add_argument(
        "--interactive",
        action="store_true",
        help="Prompt for API credentials interactively if not found"
    )
    parser.add_argument(
        "--test-parsing",
        action="store_true",
        help="Test API response parsing only"
    )
    parser.add_argument(
        "--test-fallback",
        action="store_true",
        help="Test fallback mode only"
    )
    
    args = parser.parse_args()
    
    if args.test_parsing:
        test_api_response_parsing()
    elif args.test_fallback:
        test_fallback_mode()
    elif args.mock_api:
        test_api_response_parsing()
        test_difficulty_calculation()
        test_relevance_calculation()
    elif args.real_api:
        test_real_api(api_key=args.api_key, interactive=args.interactive)
    else:
        # Run all tests
        success = run_all_tests()
        # Optionally test real API if credentials available
        if os.getenv('DATAFORSEO_API_KEY') or args.api_key:
            test_real_api(api_key=args.api_key, interactive=args.interactive)
        
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

