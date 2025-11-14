#!/usr/bin/env python3
"""
SEO/GEO Blog Post Structure Validator

This script validates blog posts against SEO and GEO best practices.
Usage: python validate_structure.py <markdown_file>
"""

import re
import sys
from typing import Dict, List, Tuple

def analyze_readability(text: str) -> float:
    """Calculate Flesch Reading Ease score (simplified)"""
    sentences = len(re.findall(r'[.!?]+', text))
    words = len(text.split())
    syllables = sum(count_syllables(word) for word in text.split())
    
    if sentences == 0 or words == 0:
        return 0
    
    score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return max(0, min(100, score))

def count_syllables(word: str) -> int:
    """Estimate syllable count"""
    word = word.lower()
    count = len(re.findall(r'[aeiouy]+', word))
    return max(1, count)

def validate_blog_post(content: str) -> Dict:
    """Validate blog post structure and SEO elements"""
    
    results = {
        'word_count': len(content.split()),
        'warnings': [],
        'passed': [],
        'failed': [],
        'score': 0
    }
    
    # Extract title
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else ""
    
    # Check 1: Title length (50-60 chars optimal)
    if 50 <= len(title) <= 60:
        results['passed'].append(f"✓ Title length optimal: {len(title)} chars")
    elif len(title) > 0:
        results['warnings'].append(f"⚠ Title length: {len(title)} chars (target: 50-60)")
    else:
        results['failed'].append("✗ No H1 title found")
    
    # Check 2: H2 headings (4-8 recommended)
    h2_count = len(re.findall(r'^##\s+', content, re.MULTILINE))
    if 4 <= h2_count <= 8:
        results['passed'].append(f"✓ H2 count optimal: {h2_count}")
    else:
        results['warnings'].append(f"⚠ H2 count: {h2_count} (target: 4-8)")
    
    # Check 3: Word count (1,500-3,000 typical)
    word_count = results['word_count']
    if 1500 <= word_count <= 3000:
        results['passed'].append(f"✓ Word count good: {word_count}")
    elif word_count < 1000:
        results['failed'].append(f"✗ Word count too low: {word_count} (min: 1,500)")
    else:
        results['warnings'].append(f"⚠ Word count: {word_count}")
    
    # Check 4: FAQ section
    if "## Frequently Asked Questions" in content or "## FAQ" in content:
        faq_questions = len(re.findall(r'###\s+.*\?', content))
        if faq_questions >= 4:
            results['passed'].append(f"✓ FAQ section with {faq_questions} questions")
        else:
            results['warnings'].append(f"⚠ FAQ section has only {faq_questions} questions (target: 4-8)")
    else:
        results['failed'].append("✗ No FAQ section found")
    
    # Check 5: Internal links (3-5 recommended)
    internal_links = len(re.findall(r'\[.+?\]\((?!http).*?\)', content))
    if 3 <= internal_links <= 5:
        results['passed'].append(f"✓ Internal links: {internal_links}")
    else:
        results['warnings'].append(f"⚠ Internal links: {internal_links} (target: 3-5)")
    
    # Check 6: External links (2-4 recommended)
    external_links = len(re.findall(r'\[.+?\]\(https?://.*?\)', content))
    if 2 <= external_links <= 4:
        results['passed'].append(f"✓ External links: {external_links}")
    else:
        results['warnings'].append(f"⚠ External links: {external_links} (target: 2-4)")
    
    # Check 7: Images
    images = len(re.findall(r'!\[.*?\]\(.*?\)', content))
    if images >= 5:
        results['passed'].append(f"✓ Images: {images}")
    else:
        results['warnings'].append(f"⚠ Images: {images} (target: 5-8)")
    
    # Check 8: Author bio
    if "## About the Author" in content or "**Author:**" in content[:500]:
        results['passed'].append("✓ Author bio present")
    else:
        results['failed'].append("✗ No author bio found")
    
    # Check 9: Table of Contents (for long content)
    if word_count > 1500:
        if "## Table of Contents" in content:
            results['passed'].append("✓ Table of contents present")
        else:
            results['warnings'].append("⚠ Consider adding table of contents (1,500+ words)")
    
    # Check 10: Schema markup reference
    if "schema" in content.lower() or "json-ld" in content.lower():
        results['passed'].append("✓ Schema markup mentioned")
    else:
        results['warnings'].append("⚠ No schema markup reference found")
    
    # Check 11: Meta description
    if "Meta Description" in content:
        meta_desc = re.search(r'Meta Description.*?:(.+)', content, re.IGNORECASE)
        if meta_desc:
            desc_length = len(meta_desc.group(1).strip())
            if 145 <= desc_length <= 155:
                results['passed'].append(f"✓ Meta description length: {desc_length} chars")
            else:
                results['warnings'].append(f"⚠ Meta description: {desc_length} chars (target: 145-155)")
    
    # Check 12: Readability
    readability = analyze_readability(content)
    if 60 <= readability <= 70:
        results['passed'].append(f"✓ Readability score: {readability:.1f}")
    else:
        results['warnings'].append(f"⚠ Readability: {readability:.1f} (target: 60-70)")
    
    # Calculate overall score
    total_checks = len(results['passed']) + len(results['warnings']) + len(results['failed'])
    if total_checks > 0:
        results['score'] = int((len(results['passed']) / total_checks) * 100)
    
    return results

def print_results(results: Dict):
    """Print validation results"""
    print("\n" + "="*60)
    print(f"SEO/GEO VALIDATION RESULTS")
    print("="*60)
    print(f"\nWord Count: {results['word_count']}")
    print(f"Overall Score: {results['score']}/100")
    
    if results['passed']:
        print(f"\n✓ PASSED ({len(results['passed'])} checks):")
        for item in results['passed']:
            print(f"  {item}")
    
    if results['warnings']:
        print(f"\n⚠ WARNINGS ({len(results['warnings'])} items):")
        for item in results['warnings']:
            print(f"  {item}")
    
    if results['failed']:
        print(f"\n✗ FAILED ({len(results['failed'])} checks):")
        for item in results['failed']:
            print(f"  {item}")
    
    print("\n" + "="*60)
    
    if results['score'] >= 80:
        print("✓ Excellent! Blog post meets SEO/GEO standards.")
    elif results['score'] >= 60:
        print("⚠ Good, but address warnings for better optimization.")
    else:
        print("✗ Needs improvement. Address failed checks and warnings.")
    print("="*60 + "\n")

def main():
    if len(sys.argv) != 2:
        print("Usage: python validate_structure.py <markdown_file>")
        sys.exit(1)
    
    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            content = f.read()
        
        results = validate_blog_post(content)
        print_results(results)
        
        # Exit code based on score
        sys.exit(0 if results['score'] >= 60 else 1)
        
    except FileNotFoundError:
        print(f"Error: File '{sys.argv[1]}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
PYTHON_EOF

chmod +x scripts/validate_structure.py
echo "✓ Validation script created"