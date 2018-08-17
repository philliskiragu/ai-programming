import copy
from urllib.request import urlopen
from urllib.error import URLError

checked_sites = []
def get_content(url):
    """
    Get content of a url. LAB 1
    """
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
    """
    Get absolute urls from string content LAB 2
    """
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
    """
    Show links in Breadth-First search
    """
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
            

#def dfs(links, depth=None):
    #"""
   # Show links in Depth-First search LAB 3
    #"""
    #    new_links = set()
    #   if depth is None:
     #      depth = 3
    #
    #   def recursive(urls, depth):
    #      """Recursively search for urls in content."""
    #     new_links.update(urls)
    #    print(f"#### New links at depth {depth} #### \n\n {urls}")
     #   if depth != 0:
      #      for url in urls:
       #         new_content = get_content(url)
        #        if new_content is not None:
         #           recursive(get_urls_from_content(new_content), depth - 1)
          #      else:
           #         break
    #    else:
     #       return new_links

    #recursive(links, depth)

    #return new_links


if __name__ == "__main__":
    url = input("Enter the url you want to get the information from: ")
    #print("#### Content #### \n {0}".format(content))
        #if content is not None:
        #   urls = get_urls_from_content(content)
        # dfs_links = dfs(urls)
        #  print(dfs_links)
    
    content = get_content(url)
    checked_sites.append(url)
    Level1_urls = get_urls_from_content(content)
    Level2_urls, Level3_urls = dfs(Level1_urls)

    print("Level 0")
    print(url)
    print("Level 1")
    print(Level1_urls)
    print("Level 2")
    print(Level2_urls)
    print("Level 3")
    print(Level3_urls)
