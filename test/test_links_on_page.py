# test_links_on_page.py

from hellen import links_on_page

def test_links_on_page():
    url = "https://www.example.com"  # Replace with a valid URL
    links = links_on_page(url)
    
    # Print the retrieved links
    print(links)
    
    # Assert the results are as expected
    assert isinstance(links, list)
    assert all(isinstance(link, str) for link in links)

# Run the test function
if __name__ == "__main__":
    test_links_on_page()
