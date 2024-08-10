# #steve/main.py

import os
import sys
from utils import create_json
from sitemaps_handler import discover_pages_sitemaps

def main():
    # Get the website URL from the environment variable
    website_url = os.getenv('WEBSITE_URL')
    
    if not website_url:
        print("Error: WEBSITE_URL environment variable is not set")
        sys.exit(1)
    
    # Discover pages from sitemaps
    pages_from_sitemap = discover_pages_sitemaps(website_url)
    
    # Create the JSON file and populate it
    filepath = create_json(website_url, pages_from_sitemap["page"])
    
    print(f"JSON file created and populated: {filepath}")

if __name__ == "__main__":
    main()
