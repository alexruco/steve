# #steve/sitemaps_handler.py

from dourado import pages_from_sitemaps
from datetime import datetime, timezone

def discover_pages_sitemaps(website_url):
    # Get the pages from the sitemaps
    pages = pages_from_sitemaps(website_url)
    
    # Extract sitemaps and structure the data
    sitemaps = list(set([sitemap for _, sitemap in pages]))
    structured_data = {
        "page": pages,
        "sitemaps": sitemaps,
        "discovered": datetime.now(timezone.utc).isoformat()
    }
    
    return structured_data

website_url = "https://mysitefaster.com"
pages_from_sitemap = discover_pages_sitemaps(website_url)
print(pages_from_sitemap)
