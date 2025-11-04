#!/usr/bin/env python3
"""
Debian Wiki Packaging Documentation Scraper

This script recursively scrapes the Debian wiki's Packaging documentation,
converting pages to Markdown and preserving the wiki's hierarchy.
"""

import argparse
import logging
import os
import re
import time
from pathlib import Path
from typing import Set, Dict, Optional
from urllib.parse import urljoin, urlparse, unquote
from collections import deque

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


class DebianWikiScraper:
    """Scraper for Debian Wiki Packaging documentation."""

    def __init__(
        self,
        start_url: str = "https://wiki.debian.org/Packaging",
        output_dir: str = "docs",
        delay: float = 1.5,
        max_depth: int = 10,
        max_retries: int = 3
    ):
        """
        Initialize the scraper.

        Args:
            start_url: Starting URL for scraping
            output_dir: Directory to save scraped content
            delay: Delay between requests in seconds
            max_depth: Maximum depth for recursive scraping
            max_retries: Maximum number of retries for failed requests
        """
        self.start_url = start_url
        self.output_dir = Path(output_dir)
        self.delay = delay
        self.max_depth = max_depth
        self.max_retries = max_retries

        # Track visited URLs to avoid duplicates
        self.visited: Set[str] = set()

        # Queue for BFS traversal: (url, depth)
        self.queue: deque = deque([(start_url, 0)])

        # Statistics
        self.stats: Dict[str, int] = {
            "pages_scraped": 0,
            "pages_failed": 0,
            "pages_skipped": 0
        }

        # Setup logging
        self._setup_logging()

        # Setup session with headers
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Debian-Wiki-Docs-Scraper/1.0 (Educational/Research Purpose)"
        })

    def _setup_logging(self):
        """Configure logging."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('scraper.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)

    def is_valid_wiki_url(self, url: str) -> bool:
        """
        Check if URL is a valid Debian wiki URL within scope.

        Args:
            url: URL to validate

        Returns:
            True if URL should be scraped, False otherwise
        """
        parsed = urlparse(url)

        # Must be wiki.debian.org
        if parsed.netloc != "wiki.debian.org":
            return False

        # Must be within Packaging namespace or related
        path = parsed.path

        # Include main Packaging page and subpages
        if path.startswith("/Packaging") or path == "/Packaging":
            return True

        # Exclude special wiki pages
        if any(pattern in path for pattern in [
            "?action=", "Special:", "RecentChanges",
            "FindPage", "TitleIndex", "WordIndex"
        ]):
            return False

        return False

    def normalize_url(self, url: str) -> str:
        """
        Normalize URL by removing fragments and query parameters.

        Args:
            url: URL to normalize

        Returns:
            Normalized URL
        """
        parsed = urlparse(url)
        # Remove fragment and query
        normalized = f"{parsed.scheme}://{parsed.netloc}{parsed.path}"
        return normalized

    def url_to_filepath(self, url: str) -> Path:
        """
        Convert URL to filesystem path, mirroring wiki structure.

        Args:
            url: URL to convert

        Returns:
            Path object for the file
        """
        parsed = urlparse(url)

        # Remove leading slash and decode URL encoding
        path = unquote(parsed.path.lstrip('/'))

        # Replace slashes with OS-specific separator
        # Create nested directory structure
        parts = path.split('/')

        # The last part is the filename
        if parts:
            # Add .md extension
            parts[-1] = f"{parts[-1]}.md"
        else:
            parts = ["index.md"]

        # Construct full path
        filepath = self.output_dir / parsed.netloc / Path(*parts)

        return filepath

    def fetch_page(self, url: str) -> Optional[str]:
        """
        Fetch a page with retry logic.

        Args:
            url: URL to fetch

        Returns:
            HTML content or None if failed
        """
        for attempt in range(self.max_retries):
            try:
                self.logger.info(f"Fetching: {url} (attempt {attempt + 1}/{self.max_retries})")
                response = self.session.get(url, timeout=30)
                response.raise_for_status()
                return response.text
            except requests.RequestException as e:
                self.logger.warning(f"Failed to fetch {url}: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay * 2)  # Wait longer on retry
                else:
                    self.logger.error(f"Failed to fetch {url} after {self.max_retries} attempts")
                    return None

    def extract_content(self, html: str, url: str) -> tuple[str, Set[str]]:
        """
        Extract main content and links from HTML.

        Args:
            html: HTML content
            url: Source URL (for resolving relative links)

        Returns:
            Tuple of (markdown content, set of discovered links)
        """
        soup = BeautifulSoup(html, 'lxml')

        # Extract main content area (MoinMoin wiki structure)
        content_div = soup.find('div', id='content')

        if not content_div:
            # Fallback to body if content div not found
            content_div = soup.find('body')

        if not content_div:
            self.logger.warning(f"No content found for {url}")
            return "", set()

        # Remove navigation, footer, and other non-content elements
        for element in content_div.find_all(['div'], class_=['header', 'footer', 'sidebar']):
            element.decompose()

        # Extract all links before conversion
        links = set()
        for link in content_div.find_all('a', href=True):
            href = link['href']
            absolute_url = urljoin(url, href)
            links.add(absolute_url)

        # Convert to markdown
        markdown_content = md(str(content_div), heading_style="ATX")

        # Clean up markdown (remove excessive newlines)
        markdown_content = re.sub(r'\n{3,}', '\n\n', markdown_content)

        # Add header with source URL
        header = f"# {soup.title.string if soup.title else 'Debian Wiki'}\n\n"
        header += f"**Source:** {url}\n\n"
        header += "---\n\n"

        markdown_content = header + markdown_content

        return markdown_content, links

    def save_page(self, content: str, filepath: Path):
        """
        Save content to file, creating directories as needed.

        Args:
            content: Content to save
            filepath: Path to save to
        """
        # Create parent directories
        filepath.parent.mkdir(parents=True, exist_ok=True)

        # Write content
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        self.logger.info(f"Saved: {filepath}")

    def scrape(self):
        """Main scraping loop using BFS traversal."""
        self.logger.info(f"Starting scrape from {self.start_url}")
        self.logger.info(f"Output directory: {self.output_dir.absolute()}")

        while self.queue:
            url, depth = self.queue.popleft()

            # Normalize URL
            url = self.normalize_url(url)

            # Skip if already visited
            if url in self.visited:
                self.stats["pages_skipped"] += 1
                continue

            # Skip if exceeds max depth
            if depth > self.max_depth:
                self.logger.info(f"Skipping {url} (max depth reached)")
                self.stats["pages_skipped"] += 1
                continue

            # Skip if not a valid wiki URL
            if not self.is_valid_wiki_url(url):
                self.stats["pages_skipped"] += 1
                continue

            # Mark as visited
            self.visited.add(url)

            # Fetch page
            html = self.fetch_page(url)
            if not html:
                self.stats["pages_failed"] += 1
                continue

            # Extract content and links
            markdown_content, discovered_links = self.extract_content(html, url)

            # Save page
            filepath = self.url_to_filepath(url)
            self.save_page(markdown_content, filepath)
            self.stats["pages_scraped"] += 1

            # Add discovered links to queue
            for link in discovered_links:
                normalized_link = self.normalize_url(link)
                if normalized_link not in self.visited and self.is_valid_wiki_url(normalized_link):
                    self.queue.append((normalized_link, depth + 1))

            # Rate limiting
            time.sleep(self.delay)

        # Print final statistics
        self.print_statistics()

    def print_statistics(self):
        """Print scraping statistics."""
        self.logger.info("=" * 60)
        self.logger.info("SCRAPING COMPLETE")
        self.logger.info("=" * 60)
        self.logger.info(f"Pages scraped: {self.stats['pages_scraped']}")
        self.logger.info(f"Pages failed: {self.stats['pages_failed']}")
        self.logger.info(f"Pages skipped: {self.stats['pages_skipped']}")
        self.logger.info(f"Total URLs visited: {len(self.visited)}")
        self.logger.info(f"Output directory: {self.output_dir.absolute()}")
        self.logger.info("=" * 60)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Scrape Debian Wiki Packaging documentation"
    )
    parser.add_argument(
        "--url",
        default="https://wiki.debian.org/Packaging",
        help="Starting URL (default: https://wiki.debian.org/Packaging)"
    )
    parser.add_argument(
        "--output",
        default="docs",
        help="Output directory (default: docs)"
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=1.5,
        help="Delay between requests in seconds (default: 1.5)"
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=10,
        help="Maximum recursion depth (default: 10)"
    )
    parser.add_argument(
        "--max-retries",
        type=int,
        default=3,
        help="Maximum retries for failed requests (default: 3)"
    )

    args = parser.parse_args()

    scraper = DebianWikiScraper(
        start_url=args.url,
        output_dir=args.output,
        delay=args.delay,
        max_depth=args.max_depth,
        max_retries=args.max_retries
    )

    try:
        scraper.scrape()
    except KeyboardInterrupt:
        print("\nScraping interrupted by user")
        scraper.print_statistics()
    except Exception as e:
        logging.error(f"Fatal error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
