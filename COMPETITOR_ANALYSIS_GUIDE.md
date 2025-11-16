# Competitor Analysis Tool - Quick Start

**Purpose**: Analyze top-ranking pages with professional SEO metrics to write better content

**Cost**: ~$0.05125 per keyword (SERP + OnPage API)

**Powered By**: DataForSEO SERP + OnPage APIs (no fragile scraping!)

**For**: Claude to use this tool to get competitive insights before writing

---

## Simple Workflow

```
Your Keyword → Top 10 URLs → OnPage Analysis → Rich Metrics → Claude Writes Article
```

---

## Usage Examples

### Basic Analysis
```bash
python scripts/competitor_analysis.py "best wireless earbuds 2025"
```

**What it does:**
1. Gets top 10 ranking URLs from Google (DataForSEO SERP API - $0.05)
2. Analyzes each page with OnPage API ($0.00125 for 10 pages)
3. Extracts professional metrics: readability, SEO scores, social tags, etc.
4. Returns structured competitive intelligence for Claude to use

### Quick Analysis (Top 5)
```bash
python scripts/competitor_analysis.py "meditation tips" --limit 5
```

### Different Location
```bash
python scripts/competitor_analysis.py "coffee machines" --location "United Kingdom"
```

### Save to File
```bash
python scripts/competitor_analysis.py "productivity hacks" --output analysis.md
```

### JSON Output (for programmatic use)
```bash
python scripts/competitor_analysis.py "seo tips" --format json
```

---

## Output Example

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
- **Target SEO Score**: 92.3/100
- **Common Topics to Cover**: best, earbuds, sound, battery, quality
- **Schema Markup**: Article, Review, Product
- **SEO Focus**: Use 'best wireless earbuds 2025' in H1, introduction, and naturally throughout
- **Content Strategy**: Go deeper than competitors with unique insights, data, and examples
- **Quality Targets**: Match or exceed 60.6 readability and 92.3 SEO score

## 🏆 Top Ranking Pages

### 1. wirecutter.com
- **URL**: https://...
- **Title**: The 8 Best Wireless Earbuds for 2025
- **Word Count**: 3,245
- **Readability**: 62.4 (Flesch-Kincaid)
- **SEO Score**: 95.0/100
- **H1**: Best Wireless Earbuds
- **Top H2s**: How We Tested, Best Overall, Best Budget Pick
- **Schema**: Review, Product
- **Social**: ✅ OG | ✅ Twitter

### 2. techradar.com
- **URL**: https://...
- **Title**: Best wireless earbuds 2025: top tested
- **Word Count**: 2,890
- **Readability**: 58.9 (Flesch-Kincaid)
- **SEO Score**: 89.5/100
...
```

**Note**: Claude reads this rich data directly and uses it to write articles that match or exceed competitor quality!

---

## One-Time Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure API Key

**Option A: Environment Variable** (Recommended)
```bash
export DATAFORSEO_API_KEY="login:password"
```

**Option B: Config File**
```bash
mkdir -p ~/.dataforseo-skill
echo '{"api_key": "login:password"}' > ~/.dataforseo-skill/config.json
```

**Option C: Command Line**
```bash
python scripts/competitor_analysis.py "keyword" --api-key "login:password"
```

---

## What Makes This Focused

### ✅ What It DOES
- Get top-ranking URLs for your keyword (SERP API)
- Professional page analysis with OnPage API:
  - Word count (accurate)
  - 5 readability metrics (Flesch-Kincaid, SMOG, etc.)
  - SEO health scores (0-100)
  - Content consistency metrics
  - Social media tag analysis
  - 50+ automated quality checks
- Extract common patterns and benchmarks
- Return structured data for Claude to use

### ❌ What It DOESN'T Do
- Keyword gap analysis (that's pre-writing research)
- Domain ranking analysis (wrong stage)
- Competitor keyword sets (wrong stage)
- Backlink analysis (wrong stage)

**Why?** This tool is for the **writing phase** (you already have the keyword).
The excluded features belong to the **keyword research phase** (before writing).

---

## Cost Breakdown

| Operation | Tool | Cost |
|-----------|------|------|
| Get top 10 URLs | DataForSEO SERP API | $0.05 |
| Analyze 10 pages | DataForSEO OnPage API (10 × $0.000125) | $0.00125 |
| **Total per keyword** | | **$0.05125** |

**Compare to:**
- Comprehensive approach: $4.80 (96% cheaper!)
- Homebrew scraping: Free but unreliable, no metrics

---

## Why OnPage API vs Scraping?

### Homebrew BeautifulSoup Scraping ❌
- ❌ Breaks when sites change structure
- ❌ No readability metrics
- ❌ No SEO scoring
- ❌ No consistency analysis
- ❌ Gets blocked by anti-scraping
- ❌ Manual word counting (inaccurate)

### DataForSEO OnPage API ✅
- ✅ 100% reliable (never breaks)
- ✅ 5 readability metrics (Flesch-Kincaid, SMOG, etc.)
- ✅ SEO health scores (0-100)
- ✅ Content consistency metrics
- ✅ Social media tag analysis
- ✅ 50+ automated quality checks
- ✅ Professional-grade accuracy
- ✅ Cost: $0.000125 per page (tenth of a cent!)

---

## How Claude Uses This Tool

When you ask Claude to write an SEO article:

1. **You provide**: Keyword/topic
2. **Claude runs**: `python scripts/competitor_analysis.py "your keyword"`
3. **Claude reads**: Structured competitive data (word counts, topics, schema)
4. **Claude writes**: Article using those insights to outrank competitors

**Example conversation:**
```
You: "Write an SEO article about 'best wireless earbuds 2025'"

Claude:
1. Runs competitor analysis script
2. Reads: "Target 3,416 words, cover: sound quality, battery, top picks"
3. Writes article with those specifications
4. Returns your SEO-optimized content
```

No manual copy-pasting needed - Claude handles the entire workflow!

---

## Troubleshooting

**Error: DataForSEO API key required**
→ Set up credentials (see Setup above)

**No SERP results found**
→ Check API credentials or try different keyword

**"Skipped (HTTPError)" messages**
→ Normal - some sites block scraping, tool continues with others

**Dependencies missing**
→ `pip install -r requirements.txt`

---

## Advanced Options

### Custom User Agent
```bash
# Set custom user agent in Python code if needed
# See line 270 in scripts/competitor_analysis.py
```

### Output Formats
- `--format markdown` (default, human-readable analysis)
- `--format json` (machine-readable structured data)

### Location Targeting
Use any location DataForSEO supports:
- "United States" (default)
- "United Kingdom"
- "Canada"
- "Australia"
- See: https://docs.dataforseo.com/v3/appendix/locations/

---

## Next Steps

1. **Ask Claude**: "Write an SEO article about [your keyword]"
2. **Claude runs**: This tool automatically to gather competitive insights
3. **Claude writes**: Article using those insights to outrank competitors
4. **You publish**: Your SEO-optimized content 🎯

---

## Manual Testing (for debugging)

If you want to test the tool directly:
```bash
python scripts/competitor_analysis.py "your keyword"
```

This shows you the competitive data Claude will use when writing articles.
