# #steve/sitemap_json_handler.py

import os
import json
from urllib.parse import urlparse
from datetime import datetime, timezone

def create_json(website_url, pages):
    parsed_url = urlparse(website_url)
    domain = parsed_url.hostname.split('.')[0]
    tld = parsed_url.hostname.split('.')[-1]
    filename = f"{domain}_{tld}.json"
    
    # Create the 'website' directory if it doesn't exist
    if not os.path.exists('website'):
        os.makedirs('website')
    
    filepath = os.path.join('website', filename)
    
    # Load existing data if the JSON file exists
    if os.path.exists(filepath):
        with open(filepath, 'r') as json_file:
            data = json.load(json_file)
    else:
        data = {}

    # Update the JSON data with discovered pages
    for page, sitemap in pages:
        if page not in data:
            data[page] = {
                "sitemaps": [sitemap],
                "discovered": datetime.now(timezone.utc).isoformat(),
                "referring_pages": [],  # Initial empty list for referring pages
                "crawled": "",  # Initial empty string for crawled status
                "crawl_allowed": None,  # Placeholder value
                "indexing_allowed": None,  # Placeholder value
                "user_declared_canonical": "",  # Placeholder value
                "status_code": None  # Placeholder value
            }
        else:
            if sitemap not in data[page]["sitemaps"]:
                data[page]["sitemaps"].append(sitemap)
    
    # Write the updated data back to the JSON file
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    return filepath
