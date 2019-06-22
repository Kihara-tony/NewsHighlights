import urllib.request,json
from .models import Source,Articles
api_key = None
base_url = None
base_url_articles = None
def configure_request(app):
    global api_key,base_url,base_url_articles
    api_key = app.config['NEWSHIGHLIGHT_API_KEY']
    base_url = app.config['NEWSHIGHLIGHT_API_BASE_URL']
    base_url_articles = app.config['NEWSHIGHLIGHT_API_ARTICLE_URL']
def get_sources():
    '''
    Function that get the json request
    '''
    get_sources_url = base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
    return sources_results
def process_results(source_list):
    '''
    Function that get sources result and transform them to list
    Args:
        source_results:A list of sources objects
    Returns:
        source_results:A list of sources objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        source_object = Source('id,name,description')
        source_results.append(source_object)
    return source_results
