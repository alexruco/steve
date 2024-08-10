# #steve/utils.py

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
    
    # Prepare the data to be written to the JSON file
    data = {
        "page": pages,
        "sitemaps": list(set([sitemap for _, sitemap in pages])),
        "discovered": datetime.now(timezone.utc).isoformat()
    }
    
    # Create or update the JSON file within the 'website' directory
    filepath = os.path.join('website', filename)
    with open(filepath, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    return filepath
