from dourado import pages_from_sitemaps

def discover_pages_sitemaps(website_url):
    get_pages_from_sitemaps = pages_from_sitemaps(website_url)
    return get_pages_from_sitemaps

    
website_url = "https://mysitefaster.com"
pages_from_sitemap = discover_pages_sitemaps(website_url)
print(pages_from_sitemap)