# #steve/test_main.py

import pytest
import os
import subprocess
from unittest.mock import patch
from steve.sitemaps_handler import discover_pages_sitemaps
from steve.sitemap_db_handler import create_json


# Mock function to simulate create_json
def mock_create_json(website_url, pages):
    return os.path.join('website', f"{website_url.split('//')[-1].replace('.', '_')}.json")

# Mock function to simulate discover_pages_sitemaps
def mock_discover_pages_sitemaps(website_url):
    return {
        "page": [
            ('https://mysitefaster.com/page1/', 'https://mysitefaster.com/sitemap1.xml'),
            ('https://mysitefaster.com/page2/', 'https://mysitefaster.com/sitemap2.xml')
        ],
        "sitemaps": ['https://mysitefaster.com/sitemap1.xml', 'https://mysitefaster.com/sitemap2.xml'],
        "discovered": "2024-08-10T12:41:45.637740+00:00"
    }

def test_main(monkeypatch):
    # Mock the functions in sitemap_db_handler and sitemaps_handler
    monkeypatch.setattr('steve.sitemap_db_handler.create_json', mock_create_json)
    monkeypatch.setattr('steve.sitemaps_handler.discover_pages_sitemaps', mock_discover_pages_sitemaps)
    
    # Set the WEBSITE_URL environment variable
    env = os.environ.copy()
    env['WEBSITE_URL'] = 'https://mysitefaster.com'
    
    # Run the script using the -m switch to handle the package correctly
    result = subprocess.run(['python3', '-m', 'steve.main'],
                            capture_output=True, text=True, cwd=os.path.dirname(__file__), env=env)
    
    # Expected JSON file path
    expected_filepath = os.path.join('website', 'mysitefaster_com.json')
    
    # Check the output
    assert f"JSON file created and populated: {expected_filepath}" in result.stdout
    assert result.returncode == 0
