# #steve/test_functions.py

import pytest
import os
from datetime import datetime, timezone
from utils import create_json
from sitemaps_handler import discover_pages_sitemaps

# Mock function to simulate pages_from_sitemaps
def mock_pages_from_sitemaps(website_url):
    return [
        ('https://mysitefaster.com/page1/', 'https://mysitefaster.com/sitemap1.xml'),
        ('https://mysitefaster.com/page2/', 'https://mysitefaster.com/sitemap2.xml')
    ]

def test_discover_pages_sitemaps(monkeypatch):
    website_url = "https://mysitefaster.com"
    
    # Use monkeypatch to replace pages_from_sitemaps with the mock function
    monkeypatch.setattr('sitemaps_handler.pages_from_sitemaps', mock_pages_from_sitemaps)
    
    # Call the discover_pages_sitemaps function
    result = discover_pages_sitemaps(website_url)
    
    # Expected structure
    expected_result = {
        "page": mock_pages_from_sitemaps(website_url),
        "sitemaps": sorted(['https://mysitefaster.com/sitemap1.xml', 'https://mysitefaster.com/sitemap2.xml']),
        "discovered": result["discovered"]  # This should match the current time
    }
    
    # Check if the result matches the expected structure
    assert result["page"] == expected_result["page"]
    assert sorted(result["sitemaps"]) == expected_result["sitemaps"]
    assert datetime.strptime(result["discovered"], "%Y-%m-%dT%H:%M:%S.%f%z")
