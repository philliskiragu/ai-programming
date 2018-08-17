from urllib.request import urlopen
from urllib.error import URLError

checked_sites = []
def get_content(url):
    """Get content of a url."""
    if url.startswith("http://") or url.startswith("https://"):
        url = url
    else:
        url = "http://{0}".format(url)

    try:
        return str(urlopen(url).read())
    except URLError as error:
        print("Error during getting of {0}: {1}".format(url, error.__repr__()))
        return None


def get_urls_from_content(content):
    """Get absolute urls from string content."""
    anchor = "<a href="
    url_links = set()
    start_idx = 0
    found = content.find(anchor, start_idx)
    while found != -1:
        href_end = content.find('"', found + len(anchor) + 1)
        href = content[found + len(anchor): href_end + 1]
        href = href.replace('"', "")
        if href.startswith("http://") or href.startswith("https://"):
            url_links.add(href.strip("/"))
        found = content.find(anchor, href_end)
    return list(url_links)


def bfs(links):
    """Show links in Breadth-First search."""
    for link in links:
        print(link)


def dfs(links):
    if not links:
        print("Links not found")
    else:
        for link in links:
            if link in checked_sites:
                pass
            content = get_content(link)
            new_links = get_urls_from_content(content)
            if len(new_links) != 0:
                for link in new_links:
                    if link in checked_sites:
                        pass
                    new_content = get_content(link)
                    new_links2 = get_urls_from_content(new_content)
                    checked_sites.append(link)
    return (new_links, new_links2) 
