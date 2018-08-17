'''Simple app that searches the web.'''
from flask import Flask, request, render_template
from search_urls import get_content, get_urls_from_content

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])

def index():
    '''Loads the index page.

    POST: handles requests send via POST request.
    GET: handles requests send via GET.'''
    if request.method == 'POST':
        app.logger.info(request.form)
        url_string = request.form.get('term', None)
        if url_string is None:
            return f'You need to supply a search term!'
        else:
            return search_term(url_string)
    else:
        return render_template(template_name_or_list='index.html')

def dfs(links, checked_sites):
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

def search_term(url):
    '''Return a list of URLs with the term.'''
    checked_sites = []
    content = get_content(url)
    checked_sites.append(url)
    Level1_urls = get_urls_from_content(content)
    Level2_urls, Level3_urls = dfs(Level1_urls, checked_sites)
        
    return render_template(
        template_name_or_list='index.html', level0_url=url, Level1_urls=Level1_urls, Level2_urls=Level2_urls, Level3_urls=Level3_urls)