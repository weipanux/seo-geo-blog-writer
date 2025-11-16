# SEO-GEO Blog Writer Skill v2.0

Claude skill for creating blog posts optimized for both traditional search engines (SEO) and generative AI citations (GEO). Content ranks in Google AND gets cited by ChatGPT, Perplexity, and Claude.

## 🚀 Quick Start (30 seconds)

**What it does:** Creates SEO and AI-optimized blog posts  
**New in v2.0:** Two modes - keyword-driven OR topic expansion with automated research

### Mode A - You Know the Keyword
```
"Write targeting 'best email marketing tools for Shopify'"
```
→ Validates keyword → Proceeds directly → Fast (2-3 min)

### Mode B - Need Keyword Research  
```
"Write about email marketing"
```
→ Researches keywords → Shows options → You pick → Proceeds (3-4 min)

### Mode B - Auto-select
```
"Write about email marketing - auto select keyword"
```
→ Researches keywords → Auto-picks best → Proceeds (fastest Mode B, ~3 min)

## What This Skill Does

Creates high-performing blog content through a four-phase workflow:
1. **Research** - Keyword analysis, search intent identification, source gathering
2. **Outline** - Pattern selection, structured content planning with SEO/GEO optimization
3. **Draft** - E-E-A-T optimized writing with citation-worthy formatting
4. **Optimize** - Automated validation, schema generation, deliverables package

## Two Modes of Operation

### Mode A: Keyword-Driven (Fastest)

**When to use:** You already know the exact keyword you want to target.

**Example Requests:**
- `"Write targeting 'best email marketing tools for Shopify'"`
- `"Create post for 'React hooks tutorial for beginners'"`
- `"Blog post about 'healthy boundaries for empaths'"`

**Characteristics:**
- Contains specific keyword phrase (3-6 words)
- Often in quotes (but not required)
- Long-tail keyword format
- Product/topic clearly defined

**Workflow:**
1. ✅ Keyword Provided → Validates keyword
2. 📝 Requirements Gathering → Collects audience, author details, word count
3. 🎯 Pattern Selection → Chooses optimal content structure
4. 📋 Create Outline → Generates SEO/GEO-optimized structure
5. ✍️ Write Draft → Follows E-E-A-T principles
6. ✅ Validate → Automated checks (80+ score target)
7. 📦 Deliver → Complete package with validation report

**Time:** ~2-3 minutes | **Tools:** 2 scripts

### Mode B: Topic Expansion (Data-Driven)

**When to use:** You have a general topic but need help finding the best keyword to target.

**Example Requests:**
- `"Write about email marketing"`
- `"Create post on React development"`
- `"Blog about setting boundaries"`

**Characteristics:**
- General topic mentioned (1-3 words)
- No specific keyword phrase
- Broader subject area
- Needs refinement

**Workflow:**
1. 🔍 Research Keywords → Executes automated research
2. 📊 Present Options → Shows top 5 keywords with metrics
3. 👆 User Selection → Pick #1-5 OR "auto" for best match
4. ✓ Validate Choice → Confirms keyword
5. 📝 Requirements Gathering → Collects audience, author details
6. 🎯 Pattern Selection → Chooses optimal content structure
7. 📋 Create Outline → Generates SEO/GEO-optimized structure
8. ✍️ Write Draft → Follows E-E-A-T principles
9. ✅ Validate → Automated checks (80+ score target)
10. 📦 Deliver → Complete package + keyword strategy doc

**Time:** ~3-4 minutes (interactive) or ~3 minutes (auto-select) | **Tools:** 3 scripts

## Usage Examples

### Example 1: Mode A - E-commerce Tutorial

**User Request:**
```
Write a blog post targeting "how to start a Shopify store in 2024"

Author: Mike Chen, E-commerce consultant with 8 years experience
Audience: Aspiring entrepreneurs
Word count: 2,500 words
```

**Claude's Response:**
```
✓ Keyword-Driven Mode detected
✓ Target keyword: "how to start a Shopify store in 2024"
✓ Confirming requirements...
[Proceeds directly to outline creation]
```

**Output:** 2,500-word how-to guide with FAQ schema, meta tags, and 88/100 validation score

### Example 2: Mode B - Mental Health Content

**User Request:**
```
Write a blog post about setting boundaries as an empath
```

**Claude's Execution:**

**Step 1:** Mode Detection
```
✓ Topic Expansion Mode detected
✓ Initiating keyword research...
```

**Step 2:** Keyword Research Results
```
📊 Keyword Research Results:

## 1. healthy boundaries for empaths
- Search Volume: 2,400/month
- Difficulty: 45/100 (Moderate)
- Relevance: 95.0/100
- Related: empath self-care, empaths and relationships

## 2. how to set boundaries as an empath
- Search Volume: 3,100/month
- Difficulty: 52/100 (Moderate)
- Relevance: 92.0/100

## 3. empath boundary setting tips
- Search Volume: 1,200/month
- Difficulty: 38/100 (Easy)
- Relevance: 88.0/100

Which keyword would you like to target?
(Type the number, or 'auto' for best match)
```

**Step 3:** User selects option 1 → Continues with full workflow

**Output:** 2,000-word guide optimized for "healthy boundaries for empaths" with validation score: 86/100

### Example 3: Mode B - Auto-Select

**User Request:**
```
Write about project management software - pick the best keyword automatically
```

**Claude's Execution:**
```
✓ Mode B detected
✓ Running keyword research...

Top keywords found:
1. best project management software (Vol: 18,000, Diff: 72, Score: 95)
2. project management tools comparison (Vol: 8,200, Diff: 58, Score: 90)

✓ Auto-selected: "best project management software"
  (Highest relevance score: 95/100)
  
Recommended: 2,500-3,000 words (Difficulty: 72 = competitive)
```

[Proceeds directly to requirements gathering]

## Installation

### Quick Install (One Command)

```bash
pip install -r requirements.txt
```

**What gets installed:**
- `requests` - API communication
- `beautifulsoup4` - Content parsing
- `lxml` - HTML/XML processing
- `jsonschema` - Schema validation

**Time:** ~30 seconds | **No configuration needed** for basic features

---

## File Structure

```
seo-geo-blog-writer/
├── SKILL.md                          # Main workflow instructions
├── README.md                         # This file - comprehensive documentation
├── CHANGELOG.md                      # Version history and migration guide
├── requirements.txt                  # Python dependencies
├── references/
│   ├── seo-checklist.md              # Keyword research, meta, headers, linking
│   ├── geo-optimization.md           # Citation formatting, answer-box, structured data
│   ├── eeat-guidelines.md            # Expertise, authoritativeness, trustworthiness
│   └── content-patterns.md           # Proven structures that rank well
├── scripts/
│   ├── validate_structure.py         # Checks post structure against best practices
│   ├── keyword_research.py           # Automated keyword research with DataForSEO API
│   ├── competitor_analysis.py        # Analyze top-ranking pages
│   ├── internal_linking.py           # Suggest internal linking opportunities
│   ├── test_keyword_research.py      # Comprehensive test suite
│   └── setup_credentials.py          # Interactive credential setup helper
├── assets/
│   ├── blog-template.md              # Starter template
│   └── structured-data-examples.json # Schema.org patterns
└── README.md
```

## Keyword Research Tool

**Automated keyword research for Mode B (Topic Expansion):**

Claude automatically executes this when you provide a general topic without a specific keyword.

### Features

- **Smart Caching:** Results cached for 30 days (90% cost savings on repeat queries)
- **Instant Responses:** Cached queries return in <1 second (vs 2-3 seconds API call)
- **Hybrid Credentials:** Tries environment variable → config file → interactive prompt → fallback
- **Multiple Formats:** JSON, Markdown, Simple text output

### Manual Usage

```bash
# Basic usage (fallback mode - no API needed)
python scripts/keyword_research.py "empath boundaries" --limit 5

# With DataForSEO API (requires account - see API Setup below)
export DATAFORSEO_API_KEY="your_login:your_password"
python scripts/keyword_research.py "email marketing" --limit 5 --format markdown

# Output formats
python scripts/keyword_research.py "content marketing" --format json
python scripts/keyword_research.py "content marketing" --format markdown
python scripts/keyword_research.py "content marketing" --format simple

# Interactive credential prompt
python scripts/keyword_research.py "topic" --limit 5 --interactive
```

### Caching Behavior

```bash
# First run - API call
python scripts/keyword_research.py "email marketing" --limit 3
# ✓ Using DataForSEO API for research
# ✓ Cached results for 'email marketing'

# Second run - instant cache hit
python scripts/keyword_research.py "email marketing" --limit 3
# ✓ Cache hit for 'email marketing' (age: 0 days)
# [Returns instantly, no API call]
```

**Cache location:** `~/.dataforseo-skill/cache/`
**Cache TTL:** 30 days (auto-cleanup on read)

### Output Metrics

- **Search Volume**: Monthly search count
- **Keyword Difficulty**: 0-100 score (lower = easier to rank)
  - 0-30: Easy
  - 31-60: Moderate
  - 61-100: Hard
- **Relevance Score**: 0-100 match to original topic (higher = better)
- **Related Keywords**: 3-5 variations for content expansion

### Example Output

```
Keyword: healthy boundaries for empaths
Volume: 2,400/month
Difficulty: 45/100 (moderate)
Relevance: 95/100
Recommended: 2,000 words
```

---

## Competitor Analysis Tool

**Analyze top-ranking pages to write better content**

### Purpose

Examines competitor pages to extract strategic insights:
- Average word count + range
- Common H2 heading patterns
- Schema types used (BlogPosting, FAQPage, HowTo)
- FAQ/TOC usage percentages
- Average image count
- Content gap opportunities
- Writing guidelines and recommendations

### Usage

```bash
# Analyze top-ranking URLs for a keyword
python scripts/competitor_analysis.py "best wireless earbuds 2025" --limit 10

# Quick analysis (top 5 pages)
python scripts/competitor_analysis.py "meditation tips" --limit 5

# Different geographic location
python scripts/competitor_analysis.py "coffee machines" --location "United Kingdom"

# Save to file
python scripts/competitor_analysis.py "productivity hacks" --output analysis.md

# JSON output
python scripts/competitor_analysis.py "seo tips" --format json
```

### Example Output

```markdown
# Competitor Analysis: best wireless earbuds 2025

**Location**: United States
**Pages Analyzed**: 10

## 📊 Quality Benchmarks

- **Average Word Count**: 2,847
- **Target Word Count**: 3,416 (20% longer to outrank)
- **Average Readability**: 60.6 (Flesch-Kincaid)
- **Average SEO Score**: 92.3/100
- **Common Topics**: best, earbuds, sound, battery, quality
- **Schema Types**: Article, Review, Product

## 🎯 Writing Guidelines

- **Target Keyword**: best wireless earbuds 2025
- **Target Word Count**: 3,416 words
- **Target Readability**: 60.6 (Flesch-Kincaid)
- **Recommended Schema**: Article, Review, Product
- **SEO Focus**: Use keyword in H1, introduction, naturally throughout
- **Content Strategy**: Go deeper with unique insights, data, examples
- **Quality Targets**: Match or exceed 60.6 readability and 92.3 SEO score

## 🏆 Top Ranking Pages

### 1. wirecutter.com
- **Word Count**: 3,245
- **Readability**: 62.4 (Flesch-Kincaid)
- **SEO Score**: 95.0/100
- **Top H2s**: How We Tested, Best Overall, Best Budget Pick
- **Schema**: Review, Product
```

### Cost

**With DataForSEO API:** ~$0.05 per keyword (SERP API)
**Fallback mode:** Free (basic analysis without API)

### Why Use This

- **Data-driven outlines:** Know what to include before writing
- **Competitive edge:** Identify content gaps competitors miss
- **Word count targeting:** Beat competitors by 15-20%
- **Schema strategy:** Know which types to implement
- **10x faster** than manual SERP review

---

## Internal Linking Tool

**Automated internal linking suggestions for SEO boost**

### Purpose

Analyzes draft content against existing site pages to suggest optimal internal linking opportunities based on:
- Topic/keyword overlap
- Semantic relevance
- Contextual placement
- Anchor text optimization

### Usage

```bash
# Basic usage
python scripts/internal_linking.py draft.md --site-content blog/*.md

# Custom settings
python scripts/internal_linking.py draft.md \
  --site-content blog/*.md \
  --base-url "https://yoursite.com/blog" \
  --max-suggestions 5 \
  --min-relevance 60 \
  --format markdown
```

### Example Output

```markdown
# Internal Linking Suggestions

**Total Suggestions:** 3

## 1. Link to: Email Automation Complete Guide

**Keyword:** email automation
**Target URL:** https://yoursite.com/blog/email-automation-guide
**Anchor Text:** `Email automation`
**Placement:** Best Practices section
**Relevance:** 88.0/100
**Reason:** Highly relevant: 'email automation' appears multiple times and topics strongly overlap

**Context:**
> ...tools that provide email automation capabilities allow you to...

**Action:**
Replace `email automation` with `[Email automation](https://yoursite.com/blog/email-automation-guide)`

---
```

### Features

- **Keyword extraction:** Automatically finds 2-3 word phrases
- **Context extraction:** Shows 100 chars before/after for placement
- **Relevance scoring:** 0-100 score based on:
  - Keyword prominence (40%)
  - Topic overlap (30%)
  - Context quality (30%)
- **Section mapping:** Tells you which H2 section to place link
- **Anchor text generation:** Optimized, natural anchor text

### Strategic Value

- **SEO multiplier:** Internal links boost topical authority
- **Automated discovery:** No manual link hunting required
- **Quality control:** Minimum relevance threshold filters noise
- **Scale-friendly:** Analyze entire site in one command

---

## API Setup & Credential Management

### DataForSEO API (Optional)

**Why:** Get real keyword data (search volume, difficulty) instead of estimates  
**Cost:** Free tier available, then ~$50/mo  
**Alternative:** Works perfectly without API (uses intelligent estimates)

### Credential Formats

DataForSEO API credentials support **two formats**:

#### Format 1: Plain Text
```
login:password
```
Example: `username@example.com:your_password_here`

#### Format 2: Base64-Encoded (from DataForSEO Dashboard)
```
dXNlcm5hbWVAZXhhbXBsZS5jb206cGFzc3dvcmQ=
```

**Note:** The script **automatically detects and decodes** Base64 credentials, so you can use either format seamlessly.

### Hybrid Credential Management

The script uses a **hybrid approach** that tries multiple methods in order:

1. **Command line argument** (`--api-key`) - Highest priority, explicit
2. **Environment variable** (`DATAFORSEO_API_KEY`) - Standard approach
3. **Config file** (`~/.dataforseo-skill/config.json`) - Persistent storage
4. **Interactive prompt** (`--interactive` flag) - User-friendly fallback

This ensures the script works for everyone, regardless of their technical level or environment.

### Method 1: Command Line Argument (Explicit)

```bash
python scripts/keyword_research.py "topic" --limit 5 --api-key "login:password"
```

**Best for:** One-time use, testing, or when you don't want persistent storage

### Method 2: Environment Variable (Standard)

```bash
export DATAFORSEO_API_KEY="login:password"
python scripts/keyword_research.py "topic" --limit 5
```

**Best for:** Developers, technical teams, production deployments

### Method 3: Config File (Persistent)

**Option A: Interactive Setup Script (Easiest)**
```bash
python scripts/setup_credentials.py
```

**Option B: Manual Creation**
```bash
# Create directory
mkdir -p ~/.dataforseo-skill

# Create config file
cat > ~/.dataforseo-skill/config.json << EOF
{
  "api_key": "login:password"
}
EOF

# Set secure permissions
chmod 600 ~/.dataforseo-skill/config.json
```

**Best for:** Frequently-used skills, power users, personal development

### Method 4: Interactive Prompt (User-Friendly)

```bash
python scripts/keyword_research.py "topic" --limit 5 --interactive
```

The script will prompt:
```
DataForSEO API key not found in environment or config file.
Enter your DataForSEO API key (format: login:password)
(Press Ctrl+C to cancel and use fallback mode)
API Key: 
```

**Best for:** Personal use, single-session tasks, demos, Claude Skills

### Fallback Behavior

The script is designed to work **without** credentials:
- ✅ Uses heuristic keyword generation
- ✅ Estimates search volume and difficulty
- ✅ Still provides useful keyword suggestions
- ✅ No API calls made

**So credentials are optional** - the skill works either way!

### Security Best Practices

1. **Don't store credentials in code** - Always ask user or use environment variables
2. **Don't log credentials** - Scripts output to stderr, credentials not logged
3. **Use fallback mode** - Script works without credentials, so it's optional
4. **Clear credentials after use** - If stored temporarily, clear them after session

## Testing Guide

### Quick Test (No API Key Required)

Test the fallback mode which works without any API credentials:

```bash
cd scripts
python test_keyword_research.py --test-fallback
```

### Full Test Suite

Run all tests (except real API):

```bash
python test_keyword_research.py
```

This runs:
1. ✅ Fallback mode test (no API needed)
2. ✅ API response parsing with mock data
3. ✅ Difficulty calculation logic
4. ✅ Relevance score calculation
5. ✅ Output format validation (JSON, Markdown, Simple)
6. ✅ Base64 credential decoding
7. ✅ Error handling

### Test Specific Components

```bash
# Test API response parsing only
python test_keyword_research.py --test-parsing

# Test with mock API data
python test_keyword_research.py --mock-api

# Test with real API (if credentials available)
python test_keyword_research.py --real-api --api-key "login:password"
```

### Test Coverage

**Total Tests: 14 passed, 0 failed** ✅

All **16 functions** in `keyword_research.py` are tested:
- ✅ 15 functions directly tested
- ✅ 1 function (`main()`) tested via manual execution

**Real API Test: PASSED** ✅

### What the Tests Verify

- ✅ Fallback mode generates keyword variations correctly
- ✅ API response parsing handles DataForSEO v3 structure
- ✅ Difficulty calculation uses `competition_index` when available
- ✅ Relevance scoring considers volume, difficulty, and topic match
- ✅ Output formats (JSON, Markdown, Simple) all work
- ✅ Base64 credential decoding works automatically
- ✅ Error handling gracefully falls back to heuristic mode

## Mode Comparison

### When to Use Each Mode

| Scenario | Recommended Mode | Reason |
|----------|------------------|--------|
| I know my target keyword | Mode A | Skip research, faster |
| I have a general topic | Mode B | Get data-driven options |
| I need validation my keyword is good | Mode B | Compare alternatives |
| I'm new to SEO | Mode B | Learn from suggestions |
| I have keyword research tool access | Mode A | Use your preferred tool |
| I want fastest workflow | Mode A | Minimal interaction |
| I want multiple options | Mode B | See 5 keywords |

### Speed Comparison

| Mode | Time | Why |
|------|------|-----|
| Mode A | 2-3 min | No research needed |
| Mode B Interactive | 3-4 min | Research + you pick |
| Mode B Auto | 3 min | Research + auto-pick |

*Times for Claude's work only, excludes your input time*

### Output Deliverables

Both modes deliver identical final packages:

1. **Complete Blog Post** (.md format)
   - SEO-optimized headers
   - Keyword-optimized content
   - Internal/external linking
   - Image suggestions with alt text

2. **Schema Markup** (JSON-LD)
   - BlogPosting schema
   - FAQPage schema
   - Author/Organization data

3. **SEO Checklist** (verified)
   - Keyword placement ✓
   - Meta optimization ✓
   - Header hierarchy ✓
   - Link strategy ✓

4. **Validation Report**
   - Overall score (target: 80+)
   - Warnings and improvements
   - E-E-A-T signal check

5. **Keyword Strategy Document** (Mode B only)
   - Selected keyword rationale
   - Search volume data
   - Difficulty analysis
   - Related keyword opportunities

## Key Features

### Automated Keyword Research (New!)
- **Mode Detection**: Automatically identifies if keyword research is needed
- **DataForSEO Integration**: Real keyword data (search volume, difficulty)
- **Intelligent Fallback**: Heuristic-based suggestions when API unavailable
- **Interactive Selection**: Choose from top 5 researched keywords or auto-select best match
- **Smart Recommendations**: Word count adjusted based on keyword difficulty

### SEO Optimization
- Strategic keyword placement (title, headers, first 100 words)
- Internal linking strategy (3-5 links)
- External authority links (2-4 links)
- Meta title and description optimization
- Image alt text suggestions
- Readability targeting (60-70 Flesch Reading Ease)

### GEO Optimization
- Citation-worthy formatting
- Answer-box friendly structure
- "According to" attribution format
- Structured data implementation
- FAQ schema markup
- Clear, quotable statements

### E-E-A-T Signals
- Author credibility sections
- First-hand experience examples
- Expert quotes and citations
- Transparent methodology
- Update dates and disclosures

## Validation Script

**Automated Quality Assurance with Schema Validation**

Claude automatically executes this script after drafting. Manual usage:

```bash
python scripts/validate_structure.py your-article.md
```

### Validation Checks

**Content Structure:**
- Title length (50-60 chars optimal)
- H2 heading count (4-8 recommended)
- Word count (1,500-3,000 typical range)
- FAQ section presence (4-8 questions minimum)
- Internal links (3-5 target)
- External links (2-4 target)
- Image count (5-8 recommended)
- Author bio presence (E-E-A-T requirement)
- Readability score (60-70 Flesch Reading Ease)

**Schema Markup Validation (NEW):**
- **BlogPosting/Article:**
  - Required: `headline`, `author`, `datePublished`
  - Recommended: `description`, `image`, `publisher`
  - Author structure validation
  - Image URL format (must be absolute)

- **FAQPage:**
  - Has `mainEntity` array
  - Minimum 4 questions recommended
  - Question/Answer structure validation

- **HowTo:**
  - Has `name` and `step` array
  - Step structure validation

### Scoring

- **≥80**: Excellent - meets SEO/GEO standards
- **60-79**: Good - address warnings for optimization
- **<60**: Needs improvement - fix failed checks

### Example Output

```
============================================================
SEO/GEO VALIDATION RESULTS
============================================================

Word Count: 2,450
Overall Score: 85/100

✓ PASSED (10 checks):
  ✓ Title length optimal: 58 chars
  ✓ H2 count optimal: 6
  ✓ Word count good: 2450
  ✓ FAQ section with 7 questions
  ✓ Schema markup valid (2 schemas)
  ...

⚠ WARNINGS (2 items):
  ⚠ Images: 4 (target: 5-8)
  ⚠ External links: 1 (target: 2-4)

🔍 SCHEMA VALIDATION WARNINGS:
  ⚠ Schema 1 (BlogPosting): Missing recommended field 'publisher' (warning)
  ⚠ Schema 2 (FAQPage): Only 3 questions (recommend 4+)

✓ Excellent! Blog post meets SEO/GEO standards.
============================================================
```

## Content Patterns

The skill includes 6 proven patterns:

1. **Ultimate Guide** (3,000-5,000 words) - Comprehensive resources
2. **How-To Guide** (1,500-2,500 words) - Process-focused tutorials
3. **Listicle** (1,000-2,500 words) - Curated collections
4. **Problem-Solution** (1,200-2,000 words) - Pain point addressing
5. **Comparison** (2,000-3,000 words) - "X vs Y" content
6. **Data-Driven** (2,000-4,000 words) - Original research posts

## Best Practices

### For Optimal Results

✅ **Input Quality:**
- Provide specific topic and target audience details
- Share real author credentials (significantly improves E-E-A-T)
- Include existing case studies or data if available
- Clarify content goal (inform, compare, convert)

✅ **Process:**
- Request outline approval before full draft
- Claude automatically executes validation script
- Review validation report and address warnings
- Plan content refresh every 6-12 months for freshness signals

❌ **Avoid:**
- Missing author bio (damages E-E-A-T scoring)
- Poor readability (target 60-70 Flesch Reading Ease)
- Missing FAQ section (critical for GEO optimization)
- No schema markup (required for rich results)
- Thin content (<1,000 words for competitive topics)
- Keyword stuffing (maintain natural flow)
- Unverifiable claims (include citations)

### Pro Tips

1. **Always provide author credentials** → Boosts E-E-A-T
2. **Let Mode B suggest word count** → Based on difficulty
3. **Review outline before full draft** → Saves time
4. **Use auto-select for speed** → When not picky
5. **Include real data/examples** → Improves quality

## Troubleshooting

### "Keyword research tool unavailable"
**Cause:** Script error or missing dependencies  
**Solution:** Claude falls back to heuristic keyword generation  
**Impact:** Still functional, but estimates instead of real data

### "No suitable keywords found"
**Cause:** Very niche or new topic with low search volume  
**Solution:** Claude suggests broadening topic or using manual keyword  
**Action:** Provide specific keyword using Mode A

### API Rate Limits
**Cause:** Too many API calls in short time (DataForSEO limits)  
**Solution:** Claude automatically uses cached/fallback mode  
**Note:** Fallback provides estimates, not real-time data

### Tests Fail with Import Errors
**Solution:** Make sure you're running from the `scripts` directory:
```bash
cd scripts
python test_keyword_research.py
```

### API Tests Fail
This is normal if:
- No API key is set (expected - uses fallback)
- API key is invalid (expected - falls back gracefully)
- Rate limited (expected - API may throttle)

The script is designed to fall back to heuristic mode, so failures are handled gracefully.

## Schema Markup

Skill generates:
- **Article Schema** - BlogPosting with author and publication data
- **FAQ Schema** - Question and Answer structured data
- **HowTo Schema** - Step-by-step instructions (when applicable)

Example schemas available in `assets/structured-data-examples.json`

## Quick Testing Guide

Test all features in under 5 minutes:

### 1. Test Keyword Caching (1 minute)

```bash
# First run - API call or fallback
python scripts/keyword_research.py "email marketing" --limit 3 --format simple

# Second run - instant cache hit
python scripts/keyword_research.py "email marketing" --limit 3 --format simple
# ✓ Cache hit for 'email marketing' (age: 0 days)
```

### 2. Test Competitor Analysis (1 minute)

```bash
python scripts/competitor_analysis.py "productivity hacks" --limit 3
# Returns: word count targets, common sections, content gaps
```

### 3. Test Internal Linking (1 minute)

```bash
# Create test files
cat > /tmp/draft.md << 'EOF'
# Email Marketing Guide
Email automation is essential for modern businesses.
EOF

cat > /tmp/existing.md << 'EOF'
# Email Automation Complete Guide
Email automation allows automated campaigns.
EOF

# Run analysis
python scripts/internal_linking.py /tmp/draft.md \
  --site-content /tmp/existing.md \
  --base-url "https://example.com/blog"

# Clean up
rm /tmp/draft.md /tmp/existing.md
```

### 4. Test Validation with Schema (30 seconds)

```bash
python scripts/validate_structure.py README.md
# Returns: Score, warnings, schema validation results
```

---

## Technical Requirements

- Python 3.6+ (for all scripts)
- Dependencies: See `requirements.txt` (one-command install)
- DataForSEO API: Optional (graceful fallback to heuristic mode)

## Version History

**v2.1** - November 2025
- ✅ Added `requirements.txt` for one-command installation
- ✅ Keyword research caching (30-day TTL, 90% cost savings)
- ✅ Enhanced error messages with troubleshooting guides
- ✅ New: Competitor analysis tool (`competitor_analysis.py`)
- ✅ New: Internal linking suggestions (`internal_linking.py`)
- ✅ Schema markup validation (BlogPosting, FAQPage, HowTo)
- ✅ Fixed `validate_structure.py` syntax error

**v2.0** - November 2025
- ✅ Added dual-mode operation (Keyword-Driven + Topic Expansion)
- ✅ Integrated DataForSEO API for keyword research
- ✅ Implemented hybrid credential management
- ✅ Added comprehensive test suite
- ✅ Base64 credential support
- ✅ Interactive keyword selection

**v1.0** - Initial release
- Basic keyword-driven workflow
- SEO/GEO optimization
- E-E-A-T implementation

See `CHANGELOG.md` for detailed version history.

## Support

For issues or improvements:
1. Check `SKILL.md` for detailed workflow
2. Review reference files for guidelines
3. Run validation script for structural issues
4. Run test suite to verify functionality

## Common Use Cases

**E-commerce Product Pages** → Mode A (you know product keywords)  
**Educational Content** → Mode B (explore topic keywords)  
**How-To Guides** → Mode B (find best "how to" variation)  
**Product Comparisons** → Mode A (specific product names)  
**Industry Trends** → Mode B (discover trending keywords)  
**Brand Content** → Mode A (branded search terms)

## Next Steps

**Try both modes with simple topics:**

**Mode A test:**
```
"Write targeting 'Python tutorial for beginners'"
```

**Mode B test:**
```
"Write about Python programming"
```

Compare the workflows and pick your favorite! 🎉

---

**Version:** 2.0  
**Date:** November 2025  
**Compatibility:** Claude Skills Framework  
**Status:** Production Ready ✅

**Note:** This skill creates professional SEO/GEO content but should be reviewed by subject matter experts before publication, especially for YMYL (Your Money Your Life) topics.
