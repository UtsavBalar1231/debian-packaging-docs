# Debian Wiki Packaging Documentation Scraper

A Python-based web scraper that recursively downloads and converts Debian Wiki packaging documentation to Markdown format, preserving the wiki's hierarchical structure.

## Features

- **Recursive Scraping**: Automatically follows all links within the Debian Wiki Packaging namespace
- **Markdown Conversion**: Converts HTML content to clean, readable Markdown
- **Hierarchy Preservation**: Mirrors the wiki's URL structure in the local filesystem
- **Rate Limiting**: Respects server resources with configurable delays between requests
- **Error Handling**: Robust retry logic for failed requests
- **Progress Tracking**: Detailed logging to both console and log file
- **URL Deduplication**: Tracks visited pages to avoid duplicate downloads
- **Depth Control**: Configurable maximum recursion depth to prevent infinite loops

## Requirements

- Python 3.11+
- uv by astral

## Installation

1. Clone or download this repository:
```bash
git clone https://github.com/UtsavBalar1231/debian-packaging-docs
cd debian-packaging-docs
```

2. Install deps using uv
```bash
uv sync
```

## Usage

### Basic Usage

Run the scraper with default settings:
```bash
uv run python scraper.py
```

This will:
- Start from `https://wiki.debian.org/Packaging`
- Save content to `docs/` directory
- Use 1.5 second delay between requests
- Recurse up to 10 levels deep

### Command-Line Options

```bash
uv run python scraper.py [OPTIONS]
```

**Options:**

- `--url URL`: Starting URL (default: `https://wiki.debian.org/Packaging`)
- `--output DIR`: Output directory (default: `docs`)
- `--delay SECONDS`: Delay between requests in seconds (default: `1.5`)
- `--max-depth N`: Maximum recursion depth (default: `10`)
- `--max-retries N`: Maximum retries for failed requests (default: `3`)

## Output Structure

The scraper creates a directory structure that mirrors the Debian Wiki's URL hierarchy:

```
docs/
└── wiki.debian.org/
    ├── Packaging.md
    ├── Packaging/
    │   ├── Intro.md
    │   ├── Basics.md
    │   ├── SourcePackage.md
    │   └── ...
    └── ...
```

Each Markdown file includes:
- Page title
- Source URL for reference
- Converted content with preserved formatting

## License

This tool is for educational and research purposes. Please respect the Debian Wiki's terms of use and copyright notices.

## Contributing

Suggestions and improvements are welcome! Please feel free to submit issues or pull requests.

## Acknowledgments

- Debian Wiki for providing excellent packaging documentation
- Built with: requests, BeautifulSoup4, markdownify
