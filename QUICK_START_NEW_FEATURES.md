# Quick Start Guide - New Features

Test drive all 6 new improvements in under 5 minutes!

---

## Step 1: Install Dependencies (30 seconds)

```bash
cd /Users/weipan/Documents/_My\ Products/seo-geo-blog-writer
pip install -r requirements.txt
```

**What you'll see:**
```
Successfully installed requests-2.31.0 beautifulsoup4-4.12.0 lxml-4.9.0 jsonschema-4.20.0
```

---

## Step 2: Test Keyword Caching (1 minute)

**First run (API call):**
```bash
python scripts/keyword_research.py "email marketing" --limit 3 --format simple
```

**What you'll see:**
```
⚠ API key not found. Using heuristic fallback.
✓ Cached results for 'email marketing'

1. email marketing (Vol: 5,000, Diff: 70, Score: 100)
2. best email marketing (Vol: 5,000, Diff: 70, Score: 90)
3. how to email marketing (Vol: 5,000, Diff: 70, Score: 80)
```

**Second run (cache hit - instant!):**
```bash
python scripts/keyword_research.py "email marketing" --limit 3 --format simple
```

**What you'll see:**
```
✓ Cache hit for 'email marketing' (age: 0 days)
[Same results, but instant - no API call]
```

---

## Step 3: Test Enhanced Error Messages (30 seconds)

**Trigger an error intentionally:**
```bash
python scripts/keyword_research.py "test" --api-key "invalid:credentials" --limit 2
```

**What you'll see:**
```
============================================================
ERROR: Invalid API Credentials (401 Unauthorized)
============================================================

Your API credentials are incorrect or expired.

Checklist:
  1. Verify format: 'login:password' (colon-separated)
  2. Check credentials in DataForSEO dashboard:
     https://app.dataforseo.com/
  ...

Falling back to heuristic mode.
============================================================
```

**Notice:** Clear, actionable guidance instead of cryptic error!

---

## Step 4: Test Competitor Analysis (1 minute)

**Analyze a few example URLs:**
```bash
python scripts/competitor_analysis.py \
  --urls \
    "https://www.hubspot.com/marketing/email-marketing" \
    "https://mailchimp.com/marketing-glossary/email-marketing/" \
  --format markdown
```

**What you'll see:**
```
Analyzing 2 competitor pages...
  [1/2] Analyzing: https://www.hubspot.com/...
  [2/2] Analyzing: https://mailchimp.com/...

✓ Successfully analyzed 2/2 pages

# Competitor Analysis: manual_analysis

**Pages Analyzed:** 2

## Content Metrics

- **Average Word Count:** 2,847
- **Word Count Range:** 1,823 - 3,871
- **Average Images:** 6
- **FAQ Usage:** 50% of competitors
- **TOC Usage:** 50% of competitors

## Common Content Sections

- **What is Email Marketing** (used by 2 pages)
- **Email Marketing Benefits** (used by 2 pages)
...

## Content Gap Opportunities

- ✨ Case studies/examples (rarely covered)
- ✨ Pricing comparison (competitive advantage)
...
```

---

## Step 5: Test Internal Linking (1 minute)

**Create test files:**

```bash
# Create a draft blog post
cat > /tmp/test_draft.md << 'EOF'
# Email Marketing Guide

Email marketing is one of the most effective digital marketing strategies.

## What is Email Marketing

Email marketing automation helps businesses...

## Best Practices

Email segmentation is crucial for success...
EOF

# Create existing site content
cat > /tmp/existing_post.md << 'EOF'
# Email Marketing Automation Guide

Complete guide to email marketing automation...

## Automation Tools
## Segmentation Strategies
EOF
```

**Run internal linking analysis:**
```bash
python scripts/internal_linking.py /tmp/test_draft.md \
  --site-content /tmp/existing_post.md \
  --base-url "https://example.com/blog" \
  --max-suggestions 3
```

**What you'll see:**
```
✓ Loaded 1 site pages

# Internal Linking Suggestions

**Total Suggestions:** 1

## 1. Link to: Email Marketing Automation Guide

**Keyword:** email marketing automation
**Target URL:** https://example.com/blog/email-marketing-automation-guide
**Anchor Text:** `Email Marketing Automation`
**Placement:** What is Email Marketing section
**Relevance:** 75.0/100
**Reason:** Strong relevance: 'email marketing automation' mentioned and topics align well

**Context:**
> Email marketing automation helps businesses...

**Action:**
Replace `email marketing automation` with `[Email Marketing Automation](https://example.com/blog/email-marketing-automation-guide)`
```

---

## Step 6: Test Schema Validation (1 minute)

**Create test post with schema:**

```bash
cat > /tmp/test_with_schema.md << 'EOF'
# Best Email Marketing Tools 2024

Complete guide to email marketing tools.

## Top Tools
## Pricing

## Frequently Asked Questions

### What is email marketing?
Email marketing is...

## Schema Markup

```json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Best Email Marketing Tools 2024",
  "author": {
    "@type": "Person",
    "name": "John Doe"
  },
  "datePublished": "2024-01-15"
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is email marketing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Email marketing is a digital marketing strategy..."
      }
    }
  ]
}
```
EOF
```

**Run validation:**
```bash
python scripts/validate_structure.py /tmp/test_with_schema.md
```

**What you'll see:**
```
============================================================
SEO/GEO VALIDATION RESULTS
============================================================

Word Count: 45
Overall Score: 58/100

✓ PASSED (7 checks):
  ✓ Title length optimal: 32 chars
  ✓ H2 count optimal: 4
  ✓ FAQ section with 1 questions
  ✓ Schema markup valid (2 schemas)
  ...

⚠ WARNINGS (3 items):
  ⚠ Word count: 45 (target: 1,500-3,000)
  ...

🔍 SCHEMA VALIDATION WARNINGS:
  ⚠ Schema 1 (BlogPosting): BlogPosting missing recommended field: 'description' (warning)
  ⚠ Schema 2 (FAQPage): FAQPage has only 1 questions (recommend 4+)

============================================================
⚠ Good, but address warnings for better optimization.
============================================================
```

**Notice:** Schema validation caught missing fields and low FAQ count!

---

## 🎉 Success!

You've tested all 6 improvements:

1. ✅ **Requirements.txt** - One-command install
2. ✅ **Keyword caching** - Instant repeat queries
3. ✅ **Error messages** - Helpful troubleshooting
4. ✅ **Competitor analysis** - Strategic insights
5. ✅ **Internal linking** - Automated suggestions
6. ✅ **Schema validation** - Markup quality checks

---

## Next: Real-World Usage

### Production Workflow

```bash
# 1. Research keywords (cached for 30 days)
python scripts/keyword_research.py "your topic" --limit 5 > keywords.md

# 2. Analyze competitors (strategic intel)
python scripts/competitor_analysis.py \
  --urls [top 3 ranking URLs] \
  --format markdown > competitor_insights.md

# 3. Write your draft (using insights from steps 1-2)

# 4. Add internal links (SEO boost)
python scripts/internal_linking.py your_draft.md \
  --site-content ../your-blog/*.md \
  --max-suggestions 5 > link_suggestions.md

# 5. Validate everything (quality check)
python scripts/validate_structure.py your_draft.md
```

---

## 📚 Full Documentation

See `IMPROVEMENTS.md` for complete technical details and advanced usage.
