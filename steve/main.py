# #steve/main.py

import sys
from utils import create_json
from sitemaps_handler import discover_pages_sitemaps

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <website_url>")
        sys.exit(1)
    
    website_url = sys.argv[1]
    
    # Discover pages from sitemaps
    pages_from_sitemap = discover_pages_sitemaps(website_url)
    
    # Create the JSON file and populate it
    filepath = create_json(website_url, pages_from_sitemap["page"])
    
    print(f"JSON file created and populated: {filepath}")

if __name__ == "__main__":
    main()
