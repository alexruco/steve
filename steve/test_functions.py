# #steve/test_functions.py

import pytest
import os
from utils import create_json

def test_create_json():
    website_url = "https://mysitefaster.com"
    expected_filename = "mysitefaster_com.json"
    expected_filepath = os.path.join('website', expected_filename)
    
    # Call the function
    filepath = create_json(website_url)
    
    # Check if the returned filepath is correct
    assert filepath == expected_filepath
    
    # Check if the file was created
    assert os.path.exists(filepath)
    
    # Clean up the created files and directory after the test
    if os.path.exists(filepath):
        os.remove(filepath)
    if os.path.exists('website') and not os.listdir('website'):
        os.rmdir('website')
