# #steve/utils.py

import os
import json
from urllib.parse import urlparse

def create_json(website_url):
    parsed_url = urlparse(website_url)
    domain = parsed_url.hostname.split('.')[0]
    tld = parsed_url.hostname.split('.')[-1]
    filename = f"{domain}_{tld}.json"
    
    # Create the 'website' directory if it doesn't exist
    if not os.path.exists('website'):
        os.makedirs('website')
    
    # Create the JSON file within the 'website' directory if it doesn't exist
    filepath = os.path.join('website', filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as json_file:
            json.dump({}, json_file)  # Create an empty JSON file
    
    return filepath
