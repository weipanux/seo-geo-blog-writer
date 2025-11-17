# SEO-GEO Blog Writer Skill v2.2

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-green.svg)]()
[![Version](https://img.shields.io/badge/Version-2.2-blue.svg)]()

Claude skill for creating blog posts optimized for both traditional search engines (SEO) and generative AI citations (GEO). Content ranks in Google AND gets cited by ChatGPT, Perplexity, and Claude.

**License:** This project is licensed under [CC BY-NC-SA 4.0](LICENSE) - free for personal and educational use, commercial use prohibited. See [License](#license) section for details.

## 🚀 Quick Start (30 seconds)

**What it does:** Creates SEO and AI-optimized blog posts with full automation
**New in v2.2:** Iterative validation + auto internal linking + AI image generation
**Available modes:** Keyword-driven (Mode A) OR topic expansion with research (Mode B)

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
- `jsonschema` - Schema validation

**Time:** ~30 seconds | **No configuration needed** for basic features

---

## File Structure

```
seo-geo-blog-writer/
├── SKILL.md                          # Main workflow instructions for Claude
├── README.md                         # This file - comprehensive documentation
├── requirements.txt                  # Python dependencies (one-command install)
│
├── planning/                         # Planning and historical documentation
│   ├── IMPLEMENTATION_PLAN.md        # 3-week implementation history (v2.2)
│   ├── COST_ANALYSIS.md              # Detailed cost breakdown and ROI analysis
│   └── CHANGELOG.md                  # Version history and migration guide
│
├── references/                       # SEO/GEO best practices
│   ├── seo-checklist.md              # Keyword research, meta, headers, linking
│   ├── geo-optimization.md           # Citation formatting, answer-box, structured data
│   ├── eeat-guidelines.md            # Expertise, authoritativeness, trustworthiness
│   └── content-patterns.md           # Proven structures that rank well
│
├── scripts/                          # Automation scripts
│   ├── validate_structure.py         # Structure validation against best practices
│   ├── iterative_validation.py       # Auto-fix validation issues (v2.2 Week 1)
│   ├── content_sources.py            # Multi-source content discovery (v2.2 Week 2)
│   ├── auto_internal_linking.py      # Auto-insert internal links (v2.2 Week 2)
│   ├── image_generation.py           # AI image generation (v2.2 Week 3)
│   ├── keyword_research.py           # DataForSEO API keyword research
│   ├── competitor_analysis.py        # Top-ranking page analysis
│   ├── internal_linking.py           # Internal linking suggestions
│   └── setup_credentials.py          # Interactive credential setup
│
└── assets/                           # Templates and examples
    ├── blog-template.md              # Starter blog post template
    ├── structured-data-examples.json # Schema.org markup patterns
    └── .seo-geo-config.json.template # Configuration template (copy to ~/.seo-geo-skill/config.json)
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

## Image Generation (NEW v2.2)

**Automated blog post image generation using AI APIs**

Generate professional, SEO-optimized images automatically for your blog posts using Google Imagen or OpenAI DALL-E 3. No more searching stock photo sites or hiring designers.

### Features

✨ **Auto-generates missing images:**
- Featured/hero images (photorealistic, 1792x1024px)
- Section illustrations (vector/illustration style, 1024x1024px)
- Diagrams and infographics (technical style, 1024x1024px)

🎨 **Smart image classification:**
- Detects image type from context and alt text
- Chooses appropriate style (photorealistic, illustration, diagram)
- Optimizes prompts for each image type

💰 **Multi-API support with fallback:**
- **Google Imagen** (priority 1): $0.02/image
- **OpenAI DALL-E 3** (priority 2): $0.04-$0.08/image
- Automatic failover between APIs

📊 **Cost tracking:** Shows per-image and total generation costs

### Quick Start

**1. Install dependencies:**
```bash
pip install openai  # For DALL-E 3
# OR
pip install google-cloud-aiplatform  # For Google Imagen (requires Google Cloud setup)
```

**2. Add image placeholders to your draft** (optional):
```markdown
# My Blog Post Title

![Professional marketing dashboard showing analytics](placeholder)

## Section Title

![Email workflow diagram showing automation steps](placeholder)
```

**Note:** Featured image is auto-generated from title if not present.

**3. Generate images:**

**Option A - OpenAI DALL-E 3 (easiest):**
```bash
export OPENAI_API_KEY=sk-proj-...

python scripts/image_generation.py draft.md \
  --output draft-with-images.md \
  --max-images 5
```

**Option B - Google Imagen:**
```bash
export GOOGLE_API_KEY=...
export GOOGLE_PROJECT_ID=my-project

python scripts/image_generation.py draft.md \
  --output draft-with-images.md \
  --max-images 5
```

**Option C - Use configuration file:**
```json
// .seo-geo-config.json
{
  "image_generation": {
    "enabled": true,
    "google_api_key": "...",
    "google_project_id": "...",
    "openai_api_key": "sk-...",
    "max_images_per_post": 5,
    "output_dir": "./generated_images"
  }
}
```

### Usage Examples

#### Basic Usage
```bash
python scripts/image_generation.py my-draft.md --output final-draft.md
```

#### Dry-Run (test without API keys)
```bash
python scripts/image_generation.py my-draft.md --dry-run

# Output:
# 🔍 DRY-RUN MODE: Extracting image needs...
#
# Found 4 image placeholder(s):
#
# 1. Type: featured | Style: photorealistic
#    Alt: Ultimate Email Marketing Guide 2024
#    Context: # The Ultimate Email Marketing Guide...
#
# 2. Type: section | Style: illustration
#    Alt: Email dashboard showing analytics
#    ...
```

#### Custom output directory
```bash
python scripts/image_generation.py draft.md \
  --output draft-with-images.md \
  --output-dir ./blog-images \
  --max-images 8
```

#### With specific API
```bash
# Force OpenAI even if Google credentials exist
python scripts/image_generation.py draft.md \
  --openai-api-key sk-... \
  --output result.md
```

### How It Works

#### 1. Extract Image Needs

The script analyzes your markdown draft to find:
- **Placeholders:** `![Alt text](placeholder)` patterns
- **Missing featured image:** Auto-adds if first image isn't present
- **Context:** Extracts surrounding text for better prompts

#### 2. Classify Images

Each image is classified by type and style:

| Image Type | Style | Size | Trigger |
|------------|-------|------|---------|
| Featured/Hero | Photorealistic | 1792x1024 | First image or auto-generated |
| Section | Illustration | 1024x1024 | Images within content sections |
| Diagram | Technical | 1024x1024 | Keywords: diagram, flowchart, workflow |

**Classification logic:**
```python
# Featured image
if is_first_image or "featured" in alt_text.lower():
    type = ImageType.FEATURED
    style = ImageStyle.PHOTOREALISTIC

# Diagram
elif any(kw in alt_text.lower() for kw in ["diagram", "flowchart", "workflow", "infographic"]):
    type = ImageType.DIAGRAM
    style = ImageStyle.DIAGRAM

# Default section image
else:
    type = ImageType.SECTION
    style = ImageStyle.ILLUSTRATION
```

#### 3. Generate Images

**API Priority:**
1. Try Google Imagen ($0.02/image)
2. Fallback to OpenAI DALL-E 3 ($0.04-$0.08/image)
3. Report error if both fail

**Prompt optimization by style:**

**Photorealistic:**
```
Professional [subject], photorealistic, professional photography,
high quality, detailed, 4K, sharp focus, [context]
```

**Illustration:**
```
Digital illustration of [subject], vector art, clean, modern,
professional, flat design, [context]
```

**Diagram:**
```
Technical diagram showing [subject], infographic style, clean lines,
clear labels, professional, [context]
```

#### 4. Insert Into Draft

Replaces placeholders with actual image paths:
```markdown
Before: ![Dashboard](placeholder)
After:  ![Professional marketing dashboard](./generated_images/image_abc123.png)
```

### Example Output

**Input draft:**
```markdown
# Email Marketing Guide 2024

![Email marketing overview](placeholder)

Email marketing delivers $42 ROI per $1 spent...

## Building Your List

![List building strategy flowchart](placeholder)
```

**After generation:**
```markdown
# Email Marketing Guide 2024

![Ultimate Email Marketing Guide 2024](./generated_images/image_featured_abc123.png)

Email marketing delivers $42 ROI per $1 spent...

## Building Your List

![List building strategy flowchart](./generated_images/image_section_def456.png)
```

**Console output:**
```
============================================================
IMAGE GENERATION SUMMARY

✓ Ultimate Email Marketing Guide 2024
  File: ./generated_images/image_featured_abc123.png
  API: openai-dalle3
  Cost: $0.08
  Prompt: Professional email marketing guide cover, photorealistic, profession...

✓ List building strategy flowchart
  File: ./generated_images/image_section_def456.png
  API: openai-dalle3
  Cost: $0.04
  Prompt: Digital illustration of email list building strategy flowchart, vec...

Total cost: $0.12
============================================================

✓ Updated draft saved to: draft-with-images.md
```

### Configuration Options

| Option | Description | Default |
|--------|-------------|---------|
| `--max-images` | Maximum images to generate | 5 |
| `--output` | Save updated draft to file | stdout |
| `--output-dir` | Image output directory | `./generated_images` |
| `--google-api-key` | Google API key | `$GOOGLE_API_KEY` |
| `--google-project-id` | Google project ID | `$GOOGLE_PROJECT_ID` |
| `--openai-api-key` | OpenAI API key | `$OPENAI_API_KEY` |
| `--dry-run` | Extract needs without generating | false |

### API Setup

#### OpenAI DALL-E 3 (Recommended for Getting Started)

**Pros:**
- Simple setup (just API key)
- High-quality images
- No infrastructure needed

**Cons:**
- More expensive ($0.04-$0.08 per image)
- Rate limits on free tier

**Setup:**
```bash
# Get API key from https://platform.openai.com/api-keys
export OPENAI_API_KEY=sk-proj-...

# Install SDK
pip install openai
```

#### Google Imagen (Best for Scale)

**Pros:**
- Cheapest ($0.02 per image)
- Enterprise-grade

**Cons:**
- Requires Google Cloud setup
- More complex authentication

**Setup:**

**Option 1: Using gcloud CLI (Recommended)**
```bash
# 1. Install gcloud CLI from https://cloud.google.com/sdk/docs/install
# 2. Authenticate and set project
gcloud auth application-default login
gcloud config set project YOUR-PROJECT-ID

# 3. Enable Vertex AI API
gcloud services enable aiplatform.googleapis.com

# 4. Set environment variable
export GOOGLE_PROJECT_ID=YOUR-PROJECT-ID

# 5. Install SDK
pip install google-cloud-aiplatform
```

**Option 2: Using Service Account (for CI/CD)**
```bash
# 1. Create service account in Google Cloud Console
# 2. Grant "Vertex AI User" role
# 3. Download JSON key file
# 4. Set environment variables
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
export GOOGLE_PROJECT_ID=YOUR-PROJECT-ID

# 5. Install SDK
pip install google-cloud-aiplatform
```

### Cost Management

**Typical blog post costs:**

| Image Count | Google Imagen | OpenAI DALL-E 3 (Standard) | OpenAI DALL-E 3 (HD) |
|-------------|---------------|---------------------------|---------------------|
| 3 images | $0.06 | $0.12 | $0.24 |
| 5 images | $0.10 | $0.20 | $0.40 |
| 10 images | $0.20 | $0.40 | $0.80 |

**Budget optimization:**
```bash
# Limit images per post
python scripts/image_generation.py draft.md --max-images 3

# Use Google Imagen for scale (after gcloud auth setup)
export GOOGLE_PROJECT_ID=YOUR-PROJECT-ID

# Test with dry-run first
python scripts/image_generation.py draft.md --dry-run
```

### Troubleshooting

**"No image generation APIs configured"**
```bash
# Solution: Set at least one API key

# OpenAI:
export OPENAI_API_KEY=sk-...

# OR Google Imagen (after gcloud auth):
export GOOGLE_PROJECT_ID=YOUR-PROJECT-ID
```

**"No image placeholders found"**
```bash
# Solution 1: Add placeholders to your draft
![Description](placeholder)

# Solution 2: Featured image is still auto-generated
# The script will create a hero image from your title
```

**"API rate limit exceeded"**
```bash
# Solution: Wait and retry, or switch APIs
python scripts/image_generation.py draft.md \
  --openai-api-key sk-different-key...
```

**Images don't match content**
```bash
# Solution: Improve alt text with context
# Bad:  ![Diagram](placeholder)
# Good: ![Email automation workflow diagram showing trigger sequences](placeholder)
```

**"Google Imagen content safety filter blocked"**
```bash
# Error: "The prompt could not be submitted. This prompt contains sensitive words..."
#
# Cause: Google's Responsible AI filters may block prompts with sensitive topics
# (e.g., mental health terms, relationship issues, medical conditions)
#
# Solution: The script automatically filters sensitive words from prompts
# and uses abstract visual descriptions. If images still don't generate:
#
# 1. Check alt text for sensitive keywords
# 2. Use more abstract, neutral descriptions in image placeholders:
#    Bad:  ![Person being manipulated and gaslighted](placeholder)
#    Good: ![Professional illustration about self-awareness](placeholder)
#
# 3. Consider switching to OpenAI DALL-E 3 for sensitive topics:
export OPENAI_API_KEY=sk-...
python scripts/image_generation.py draft.md --openai-api-key sk-...
```

### Integration with Workflow

**Complete blog post workflow:**
```bash
# 1. Write draft (Phase 4)
claude-code "Write blog post: email marketing tips"
# Outputs: /tmp/blog_draft.md

# 2. Add internal links (Phase 5)
python scripts/auto_internal_linking.py /tmp/blog_draft.md \
  --output /tmp/blog_draft_linked.md

# 3. Generate images (Phase 6)
python scripts/image_generation.py /tmp/blog_draft_linked.md \
  --output /tmp/blog_draft_final.md \
  --max-images 5

# 4. Final validation (Phase 7)
python scripts/iterative_validation.py /tmp/blog_draft_final.md \
  --output /tmp/blog_post_complete.md \
  --target-score 80
```

### Best Practices

**Alt text optimization:**
```markdown
# ❌ Bad - too vague
![Dashboard](placeholder)

# ✅ Good - descriptive and keyword-rich
![Professional email marketing dashboard showing open rates and click-through analytics](placeholder)
```

**Strategic image placement:**
```markdown
# Featured image (auto-generated)
# [Title automatically becomes featured image]

## Section 1
[Content paragraph]

![Section-specific illustration](placeholder)  ← Add after introducing concept

## Section 2 (with complex concept)
[Content paragraph]

![Diagram explaining the workflow](placeholder)  ← Use diagrams for technical content
```

**Cost optimization:**
- Start with `--dry-run` to preview
- Use `--max-images 3` for budget-conscious posts
- Featured image + 2-3 section images is optimal
- Diagrams should be reserved for complex explanations

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
3. **Project-local config** (`.seo-geo-config.json`) - Works in containers (see below)
4. **User home config** (`~/.dataforseo-skill/config.json`) - Persistent storage
5. **Interactive prompt** (`--interactive` flag) - User-friendly fallback

This ensures the script works for everyone, regardless of their technical level or environment.

### 🐳 Claude Code / Container Usage

**Issue:** Claude Code runs in a container that can't access `~/.dataforseo-skill/config.json` in your local filesystem.

**Solution Options:**

**Option 1: Project-Local Config (Easiest for containers)**
```bash
# Create config in project root (gitignored automatically)
cat > .seo-geo-config.json << EOF
{
  "api_key": "your_login:your_password"
}
EOF

# Secure permissions
chmod 600 .seo-geo-config.json
```

⚠️ **Security Trade-off:** Config is in project directory (even though gitignored). Claude has access to it.

**Option 2: Environment Variable (Most Secure)**

Configure Claude Code to pass environment variables to container (method varies by setup).

**Trade-offs:**
- **Project-local config:** ✅ Easy to set up, ❌ File in project dir (even if gitignored)
- **Environment variable:** ✅ Most secure, ❌ Requires container configuration

**Recommendation:** Use project-local config for convenience, ensure `.seo-geo-config.json` is in `.gitignore`.

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

---

### Sanity CMS, Google Imagen & OpenAI Setup

**🔐 Security-First Configuration**

API credentials for Sanity, Google Imagen, and OpenAI are stored in your **home directory** (outside the skill folder) to prevent accidental exposure when zipping or uploading the skill to Claude.

**Config Location:** `~/.seo-geo-skill/config.json` (same pattern as DataForSEO)

**Why this location?**
- ✅ Secure: Outside skill directory, won't be included in skill zip files
- ✅ Persistent: Survives skill updates and reinstalls
- ✅ Shared: Can be used across multiple skill versions
- ✅ Safe: Never accidentally committed to GitHub or uploaded to Claude

#### Configuration File Format

Create `~/.seo-geo-skill/config.json`:

```json
{
  "sanity": {
    "project_id": "your-sanity-project-id",
    "dataset": "production",
    "api_version": "2023-05-03",
    "token": null
  },

  "content_sources": {
    "local_markdown_dir": null
  },

  "internal_linking": {
    "min_confidence_auto_insert": 90,
    "max_links_per_post": 5,
    "cache_ttl_hours": 24
  },

  "validation": {
    "target_score": 80,
    "max_iterations": 3
  },

  "image_generation": {
    "enabled": true,
    "google_api_key": "YOUR_GOOGLE_API_KEY_HERE",
    "google_project_id": "your-gcp-project-id",
    "openai_api_key": "sk-proj-YOUR_OPENAI_KEY_HERE",
    "max_images_per_post": 5,
    "output_dir": "./generated_images"
  }
}
```

#### Credential Priority

Scripts use this priority order:
1. **CLI arguments** (highest) - Passed directly to scripts
2. **Environment variables** - `export VARIABLE_NAME=value`
3. **Config file** - `~/.seo-geo-skill/config.json` in home directory
4. **Defaults** (lowest) - Fallback values

#### Setup: Sanity CMS (for Internal Linking)

**What you need:**
- `project_id` - Your Sanity project ID (required)
- `dataset` - Usually "production" (optional, defaults to "production")
- `token` - Read token for private datasets (optional, use null for public)

**Where to find:**
1. Log in to https://sanity.io
2. Go to your project settings
3. Find "Project ID" in the dashboard
4. For token: Settings → API → Tokens (only if dataset is private)

**Test it:**
```bash
python scripts/content_sources.py --sanity-test
```

#### Setup: Google Imagen (for Image Generation)

**What you need:**
- `google_project_id` - Your GCP project ID
- Authentication via gcloud CLI OR service account JSON

**Setup Option 1: gcloud CLI (Recommended)**
1. Install gcloud CLI from https://cloud.google.com/sdk/docs/install
2. Authenticate and set project:
   ```bash
   gcloud auth application-default login
   gcloud config set project YOUR-PROJECT-ID
   ```
3. Enable Vertex AI API:
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```
4. Set environment variable:
   ```bash
   export GOOGLE_PROJECT_ID=YOUR-PROJECT-ID
   ```

**Setup Option 2: Service Account (for CI/CD)**
1. Create service account in Google Cloud Console
2. Grant "Vertex AI User" role
3. Download JSON key file
4. Set environment variables:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
   export GOOGLE_PROJECT_ID=YOUR-PROJECT-ID
   ```

**Install library:**
```bash
pip install google-cloud-aiplatform
```

**Test it:**
```bash
python scripts/image_generation.py test-draft.md --dry-run
# Should show: "✓ Google Imagen configured (priority 1)"
```

**Cost:** $0.02/image, $2,000 startup credit available

**Important:** Google Imagen has content safety filters that may block sensitive topics. See troubleshooting section for details.

#### Setup: OpenAI DALL-E 3 (Fallback for Images)

**What you need:**
- `openai_api_key` - Your OpenAI API key (starts with `sk-proj-`)

**Where to find:**
1. Go to https://platform.openai.com/api-keys
2. Create new secret key or use existing
3. Copy the key (starts with `sk-proj-`)

**Install library:**
```bash
pip install openai
```

**Test it:**
```bash
python scripts/image_generation.py test-draft.md --dry-run
# Should show: "✓ OpenAI DALL-E 3 configured (priority 2)"
```

**Cost:** $0.04-$0.08/image (1024x1024 standard quality)

#### Verification Checklist

**1. Create config directory:**
```bash
mkdir -p ~/.seo-geo-skill
```

**2. Create config file:**
```bash
# Copy from template
cp assets/.seo-geo-config.json.template ~/.seo-geo-skill/config.json
# Then edit with your credentials: nano ~/.seo-geo-skill/config.json
```

**3. Verify config exists:**
```bash
ls -la ~/.seo-geo-skill/config.json
```

**4. Validate JSON format:**
```bash
python3 -m json.tool ~/.seo-geo-skill/config.json
# Should pretty-print your config without errors
```

**5. Test config loading:**
```bash
python scripts/config_loader.py
# Should show all your config sections
```

**6. Security check:**
```bash
# Verify config is NOT in skill directory
ls -la .seo-geo-config.json
# Should show "No such file or directory" ✅
```

#### Troubleshooting

**"No image generation APIs configured"**
```bash
# Check file exists
ls -la ~/.seo-geo-skill/config.json

# Verify credentials are set (not null)
cat ~/.seo-geo-skill/config.json | grep -A5 image_generation

# Test config loading
python scripts/config_loader.py
```

**"Sanity API error: Project not found"**
```bash
# Verify your project ID
cat ~/.seo-geo-skill/config.json | grep project_id

# Test Sanity connection
python scripts/content_sources.py
```

**"Google Imagen not configured"**
```bash
# Install library if needed
pip install google-cloud-aiplatform

# Verify credentials
cat ~/.seo-geo-skill/config.json | grep google_api_key
```

#### Environment Variable Override (Optional)

If you prefer environment variables instead of config file:

```bash
# Sanity
export SANITY_PROJECT_ID="your-project-id"
export SANITY_DATASET="production"

# Google Imagen
export GOOGLE_API_KEY="your-api-key"
export GOOGLE_PROJECT_ID="your-gcp-project"

# OpenAI
export OPENAI_API_KEY="sk-proj-your-key"
```

**Note:** Environment variables override config file values.

---

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

## Iterative Validation with Auto-Fix (NEW v2.2)

**Automated quality improvement through iterative fixing**

The iterative validation script automatically fixes common blog post issues through multiple validation iterations, eliminating manual correction work.

### Usage

```bash
python scripts/iterative_validation.py your-draft.md \
  --max-iterations 3 \
  --target-score 80 \
  --output your-draft-fixed.md
```

### How It Works

The script performs a 3-step cycle:
1. **Validate** current draft state
2. **Auto-fix** common issues
3. **Re-validate** to measure improvement

**Stops when:**
- Score ≥ 80 (target threshold)
- Max 3 iterations reached
- No more auto-fixable issues

### Auto-Fixable Issues

**✅ FAQ Section Missing**
- Generates 4-6 questions from H2 headings
- Converts headings to question format
- Extracts first 100 words from each section as answers
- Example: "Best Practices" → "What are the best practices?"

**✅ Author Bio Missing**
- Adds structured author bio template at end
- Placeholders for user to complete: `[Author Name]`, `[job title]`, `[experience]`
- Includes social media and website links

**✅ Short Title (<50 chars)**
- Adds year for guides: "Marketing Guide" → "Marketing Guide 2025"
- Adds descriptors: "Tips" → "Complete Tips Guide"
- Keeps under 60 chars limit

**✅ Schema Markup Missing**
- Adds BlogPosting schema template
- Adds FAQPage schema (if FAQ section present)
- Placeholders for user to complete: dates, URLs, descriptions

### Non-Auto-Fixable Issues

**⚠️ Low Word Count**
- Identifies thin sections (<150 words)
- Notes sections needing expansion
- Requires manual content writing

**⚠️ Missing Links/Images**
- Cannot auto-source content
- Requires research or generation (see Week 2 & 3 roadmap)

**⚠️ Low Readability**
- Complex content restructuring needed
- Requires manual editing

### Example Output

```
🔄 Iteration 1/3
   Score: 30/100
   ✓ Added FAQ section with 6 questions
   ✓ Added author bio template (requires user completion)
   ✓ Expanded title: 'Email Tips' → 'Complete Email Tips Guide 2025'
   ✓ Added schema markup templates (requires completion)

🔄 Iteration 2/3
   Score: 45/100
   No auto-fixable warnings remaining

============================================================
ITERATIVE VALIDATION RESULTS
============================================================

Final Score: 45/100

Fixes Applied (4):
  ✓ Added FAQ section with 6 questions
  ✓ Added author bio template (requires user completion)
  ✓ Expanded title: 'Email Tips' → 'Complete Email Tips Guide 2025'
  ✓ Added schema markup templates (requires completion)

✓ PASSED (5 checks):
  ✓ Title length optimal: 40 chars
  ✓ FAQ section with 6 questions
  ✓ Author bio present
  ...

⚠ WARNINGS (3 items):
  ⚠ Internal links: 0 (target: 3-5)
  ⚠ Images: 0 (target: 5-8)
  ⚠ Word count: 520 (target: 1,500+)

============================================================
```

### Integration with Workflow

In the SEO-GEO skill workflow, Claude automatically uses iterative validation in **Phase 5** after drafting. This eliminates manual correction of:
- Missing FAQ sections
- Missing author bios
- Short titles
- Missing schema markup

Remaining warnings (links, images, word count) are noted for manual attention or handled by upcoming features (Weeks 2-3).

## Auto Internal Linking (NEW v2.2)

**Automated internal link discovery and insertion**

The auto internal linking system discovers existing blog posts from multiple sources and automatically inserts high-confidence internal links (≥90 relevance) into new drafts.

### Features

**Multi-Source Content Discovery:**
- ✅ **Sanity CMS API** (priority 1) - Query published posts via GROQ
- ✅ **Local Markdown Files** (priority 2) - Scan directory for .md files
- ✅ **24hr Caching** - Minimize API calls and improve performance
- ✅ **Graceful Fallback** - Sanity fails → Local → Empty (no errors)

**Intelligent Link Insertion:**
- Relevance-based scoring (keyword overlap, topic similarity, context matching)
- Auto-insert only high-confidence links (≥90 relevance by default)
- First occurrence replacement (avoids over-linking)
- Markdown link format preservation
- Configurable thresholds and limits

### Quick Start

**1. Configure Content Source:**

```bash
# Option A: Sanity CMS (recommended for production)
export SANITY_PROJECT_ID=your-project-id
export SANITY_DATASET=production  # or 'staging'

# Option B: Local markdown directory
# (no env vars needed, pass via --local-content flag)
```

**2. Test Content Discovery:**

```bash
# With Sanity
python scripts/content_sources.py --sanity-project-id your-project-id

# With local markdown
python scripts/content_sources.py --local-content ./blog-posts

# Both sources (Sanity takes priority)
python scripts/content_sources.py \
  --sanity-project-id your-project-id \
  --local-content ./blog-posts
```

**Example output:**
```
✓ Fetched 50 items from SanitySource

✓ Discovered 50 content items

1. Complete Email Marketing Guide 2025
   URL: /blog/email-marketing-guide
   Keywords: email marketing, automation, campaigns
   Source: sanity
   Published: 2025-01-15
...
```

**3. Auto-Insert Internal Links:**

```bash
# Dry run (show suggestions without inserting)
python scripts/auto_internal_linking.py draft.md \
  --sanity-project-id your-project-id \
  --dry-run

# Actual insertion
python scripts/auto_internal_linking.py draft.md \
  --sanity-project-id your-project-id \
  --output draft-with-links.md
```

### Usage Examples

**With Sanity CMS:**
```bash
python scripts/auto_internal_linking.py my-draft.md \
  --sanity-project-id abc123xyz \
  --sanity-dataset production \
  --min-confidence 90 \
  --max-links 5 \
  --output my-draft-linked.md
```

**With Local Markdown:**
```bash
python scripts/auto_internal_linking.py my-draft.md \
  --local-content ./content/blog \
  --min-confidence 85 \
  --max-links 7 \
  --output my-draft-linked.md
```

**Dry Run (Preview):**
```bash
python scripts/auto_internal_linking.py draft.md \
  --local-content ./posts \
  --dry-run
```

### Configuration Options

#### Command Line Flags

| Flag | Description | Default |
|------|-------------|---------|
| `--sanity-project-id` | Sanity project ID | `$SANITY_PROJECT_ID` |
| `--sanity-dataset` | Sanity dataset name | `production` |
| `--sanity-token` | Read token for private datasets | `$SANITY_TOKEN` |
| `--local-content` | Local markdown directory | None |
| `--min-confidence` | Min relevance for auto-insert | `90` |
| `--max-links` | Max links to insert | `5` |
| `--output` | Save to file (default: stdout) | None |
| `--dry-run` | Show suggestions without inserting | `False` |
| `--no-cache` | Skip content cache | `False` |

#### Configuration File

**📍 Config Location:** `~/.seo-geo-skill/config.json`

See the **[API Setup & Credential Management](#api-setup--credential-management)** section above for:
- Complete configuration file format
- Sanity CMS credential setup
- Google Imagen / OpenAI DALL-E setup
- Verification checklist and troubleshooting

### How It Works

**1. Content Discovery:**
```
Priority Chain:
  ├─ Sanity API (if configured) ✓
  ├─ Local Markdown (if provided) ✓
  └─ Empty list (graceful fallback)
```

**2. Relevance Scoring:**
- **Keyword Prominence (40%)**: How prominent is the keyword in target page?
- **Keyword Overlap (30%)**: How many keywords overlap between draft and target?
- **Context Matching (30%)**: How well do topics align?

**3. Link Insertion:**
- Find first occurrence of target keyword in draft
- Check if already inside a link (skip if yes)
- Replace with markdown link: `[keyword](url)`
- Track inserted links to avoid duplicates

### Example Output

**Dry Run:**
```
============================================================
DRY RUN - Internal Link Suggestions
============================================================

High-confidence links (≥90 relevance):

1. Keyword: 'email marketing'
   → Link to: /blog/email-marketing-guide
   → Anchor: Email marketing
   → Relevance: 95/100
   → Reason: Highly relevant: 'email marketing' appears multiple times

2. Keyword: 'marketing automation'
   → Link to: /blog/automation-best-practices
   → Anchor: Marketing automation
   → Relevance: 92/100
   → Reason: Strong topic overlap and keyword prominence

Medium-confidence links (80-89 relevance):
...
============================================================
```

**Actual Insertion:**
```
🔗 Auto-inserting 5 high-confidence links...

  ✓ Inserted: Email marketing → /blog/email-marketing-guide (95)
  ✓ Inserted: Marketing automation → /blog/automation-best-practices (92)
  ✓ Inserted: Customer segmentation → /blog/segmentation-guide (91)
  ✓ Inserted: Email campaigns → /blog/campaign-optimization (90)
  ✓ Inserted: ROI tracking → /blog/marketing-metrics (90)

============================================================
INTERNAL LINKING RESULTS
============================================================

✓ Successfully inserted 5 links
✓ Updated draft saved to: draft-with-links.md
============================================================
```

### Content Sources Setup

#### Sanity CMS Setup

**1. Get Sanity Credentials:**
- Log in to [sanity.io](https://www.sanity.io/)
- Navigate to your project settings
- Copy **Project ID** from project settings
- (Optional) Generate **Read Token** if dataset is private

**2. Configure:**
```bash
export SANITY_PROJECT_ID=abc123xyz
export SANITY_DATASET=production
# Only if private dataset:
export SANITY_TOKEN=sk...
```

**3. Test Connection:**
```bash
python scripts/content_sources.py --sanity-project-id $SANITY_PROJECT_ID
```

#### Local Markdown Setup

**1. Organize Blog Posts:**
```
blog-posts/
├── email-marketing-guide.md
├── automation-best-practices.md
└── customer-segmentation.md
```

**2. Frontmatter Format (Optional but recommended):**
```markdown
---
title: Complete Email Marketing Guide 2025
date: 2025-01-15
tags: email marketing, automation, campaigns
description: Comprehensive guide to email marketing
---

# Content starts here
```

**3. Test Discovery:**
```bash
python scripts/content_sources.py --local-content ./blog-posts
```

### Caching Behavior

**24-Hour Cache:**
- First query: Fetches from API/filesystem (~2-5 seconds)
- Subsequent queries: Loads from cache (<1 second)
- Cache expires after 24 hours
- Cache location: `~/.seo-geo-blog-writer/content-cache/`

**Cache Management:**
```bash
# Clear cache
python scripts/content_sources.py --clear-cache

# Force fresh fetch (skip cache)
python scripts/auto_internal_linking.py draft.md \
  --local-content ./posts \
  --no-cache
```

### Troubleshooting

**No content found:**
```
❌ No existing content found.

Please configure at least one content source:
  --sanity-project-id <project_id>  (Sanity CMS)
  --local-content <directory>        (Local markdown)
```

**Solution:**
- Verify `SANITY_PROJECT_ID` is set correctly
- Check local markdown directory exists and contains .md files
- Ensure Sanity dataset contains published posts (not drafts)

**No linking opportunities:**
```
ℹ️  No internal linking opportunities found

Possible reasons:
  - Draft content doesn't match existing page topics
  - Existing content library too small
  - Keywords don't overlap sufficiently
```

**Solution:**
- Lower `--min-confidence` threshold (try 80-85)
- Expand existing content library
- Ensure draft uses keywords present in existing content

### Integration with Workflow

In the SEO-GEO skill workflow, Claude automatically uses auto internal linking in **Phase 5** after drafting and before validation.

**Complete Workflow:**
1. Research & Keyword Selection
2. Outline Creation
3. Draft Writing
4. Content Optimization
5. **Auto Internal Linking** ← Inserts 3-5 high-confidence links
6. Image Generation (Week 3)
7. Final Validation (checks links present)

This eliminates manual link research and insertion, saving 10-15 minutes per post while ensuring optimal internal linking structure.

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

### API Errors
If DataForSEO API has issues:
- No API key is set → Uses fallback mode (estimates)
- API key is invalid → Falls back gracefully to heuristics
- Rate limited → Automatically uses cached/fallback mode

The script is designed to work with or without API credentials.

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

---

## 💰 Cost & Pricing

### Per-Post Cost Summary

| Configuration | Cost Per Post | Best For |
|---------------|---------------|----------|
| **Budget Mode** | $0.36-$0.66 | High-volume content (100+ posts/month) |
| **Balanced Mode** ⭐ | $0.40-$0.95 | Most users (recommended) |
| **Premium Mode** | $1.03-$1.45 | Professional blogs, agencies |

### Component Breakdown (Balanced Mode)

| Component | Provider | First Post | Cached/Repeat | Notes |
|-----------|----------|------------|---------------|-------|
| **Content Writing** | Claude Sonnet 4.5 | $0.30-$0.60 | $0.30-$0.60 | Required - main content generation |
| **Keyword Research** | DataForSEO API | $0.15-$0.25 | $0.00 | Optional - 30-day cache, Mode B only |
| **Competitor Analysis** | DataForSEO OnPage | $0.50 | $0.00 | Optional - reuse across topic clusters |
| **Internal Linking** | Sanity/Local | $0.00 | $0.00 | Free tier or local markdown |
| **Image Generation** | Google Imagen | $0.08 | $0.08 | 4 images @ $0.02 each |
| **Validation Loop** | Local | $0.00 | $0.00 | No API calls |
| **TOTAL** | | **$0.53-$1.45** | **$0.38-$0.70** | With aggressive caching |

### Volume Pricing

| Posts/Month | First Month | Ongoing (90% cached) | Avg Cost/Post |
|-------------|-------------|----------------------|---------------|
| 10 posts | $5-$10 | $4-$7 | **$0.40-$0.70** |
| 50 posts | $27-$48 | $20-$36 | **$0.40-$0.72** |
| 100 posts | $36-$66 | $36-$66 | **$0.36-$0.66** |

### API Pricing Details

**Claude Sonnet 4.5** (required for content generation)
- Input: $3.00 per 1M tokens
- Output: $15.00 per 1M tokens
- Typical post: ~62K input + ~18K output = $0.30-$0.60

**Image Generation** (optional but recommended)
- **Google Imagen** (priority 1): $0.02/image
  - 4 images/post = $0.08
- **OpenAI DALL-E 3** (fallback): $0.04-$0.08/image
  - Standard 1024x1024: $0.04
  - Featured 1792x1024: $0.08

**DataForSEO API** (optional)
- Keyword research: $0.05/keyword (3-5 keywords = $0.15-$0.25)
- Competitor analysis: ~$0.05/page (10 pages = $0.50)
- **Caching:** 30-day TTL = 90% cost savings on repeat topics
- **Fallback:** Free heuristic mode if no API key

**Sanity CMS** (optional for internal linking)
- Free tier: 100,000 API requests/month
- Effectively $0.00 for typical usage
- **Fallback:** Local markdown file scanning (free)

### Cost Optimization Tips

1. **Use caching aggressively** - 30-day keyword cache saves $0.15-$0.25/post
2. **Batch related posts** - Reuse research across topic clusters
3. **Choose Mode A when possible** - Skip keyword research API if you know the target
4. **Limit images to 3-4** - Balance quality with cost ($0.06-$0.08 vs $0.10)

### ROI Comparison

**SEO-GEO Tool Cost:** $0.40-$1.45/post

**vs. Manual Creation:**
- Freelance writer: $50-$200
- Stock images: $10-$30
- Keyword research: $25-$100
- **Manual total: $85-$330**
- **Savings: 99.5%+**

**vs. Competing Tools:**
- Jasper.ai: $49-$125/month
- Copy.ai: $49/month
- Surfer SEO: $89-$219/month
- **Advantage:** Pay-per-use, lower cost at any volume

### Recommended Configuration

**For most users (Balanced Mode):**
```yaml
keyword_research: DataForSEO API (with 30-day cache)
competitor_analysis: Selective (once per topic cluster)
internal_linking: Local markdown or Sanity free tier
image_generation: Google Imagen (4 images)
validation: 3 iterations (local, free)

Expected cost: $0.40-$0.95/post
ROI: 100-500x (vs manual creation)
```

**Detailed cost breakdown:** See `planning/COST_ANALYSIS.md`

---

## Version History

**v2.2** - November 16, 2025 ✅
- ✅ **Week 1:** Iterative validation with auto-fix (`iterative_validation.py`)
  - Auto-fixes FAQ, author bio, short titles, missing schema
  - Stops at score ≥80 or 3 iterations
  - Saves 30-45 minutes of manual fixes per post
- ✅ **Week 2:** Auto internal linking (`auto_internal_linking.py`, `content_sources.py`)
  - Multi-source content discovery (Sanity CMS → Local → Fallback)
  - Auto-inserts links ≥90 confidence score
  - 24-hour caching for content discovery
- ✅ **Week 3:** AI image generation (`image_generation.py`)
  - Google Imagen + OpenAI DALL-E 3 support
  - Smart image classification (featured/section/diagram)
  - Style-optimized prompts (photorealistic/illustration/technical)
  - Cost tracking and dry-run mode
- ✅ Complete 7-phase workflow (research → links → images → validation)
- ✅ Comprehensive documentation (400+ lines per feature)
- See `planning/IMPLEMENTATION_PLAN.md` for detailed implementation history

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

See `planning/CHANGELOG.md` for detailed version history.

## Support & Documentation

**Quick Reference:**
1. **SKILL.md** - Complete workflow instructions for Claude
2. **references/** - SEO/GEO best practices and content patterns
3. **planning/COST_ANALYSIS.md** - Detailed API costs and ROI breakdown
4. **planning/IMPLEMENTATION_PLAN.md** - v2.2 development history

**For Issues:**
1. Run validation: `python scripts/validate_structure.py your-post.md`
2. Review troubleshooting section above
3. Check git history for recent changes

**For API Setup:**
- DataForSEO: See "API Setup & Credential Management" section
- Google Imagen: Requires Google Cloud setup
- OpenAI DALL-E: Get API key from platform.openai.com

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

## License

### CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike 4.0 International)

**Copyright © 2025 Wei Pan**

This work is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

#### ✅ You ARE allowed to:
- **Use** this skill for personal blog writing and content creation
- **Fork** and modify for your own projects
- **Learn** from the code and build your own tools
- **Share** with others (with attribution)
- **Contribute** improvements back to the community
- **Use** in educational or research contexts

#### ❌ You are NOT allowed to:
- **Sell** this skill or modified versions as a product
- **Offer** this skill as a paid service or SaaS platform
- **Use** this skill as part of a commercial offering for profit
- **Monetize** derivatives or forks of this work
- **Remove** attribution or claim this work as your own

#### 📋 Requirements:
- **Attribution**: You must give appropriate credit and link to this license
- **ShareAlike**: Derivatives must use the same CC BY-NC-SA 4.0 license
- **Indicate Changes**: If you modify the work, you must indicate what was changed

#### 💡 Want to use this commercially?
If you're interested in commercial use, please contact the author to discuss licensing options.

**Full License Text:** See [LICENSE](LICENSE) file

---

**Version:** 2.2
**Date:** November 16, 2025
**Author:** Wei Pan
**Compatibility:** Claude Skills Framework
**Status:** Production Ready ✅

**Note:** This skill creates professional SEO/GEO content but should be reviewed by subject matter experts before publication, especially for YMYL (Your Money Your Life) topics.
