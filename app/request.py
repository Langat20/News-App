import urllib.request, json 
from .models import Article, Category, Source, Headlines 

#getting the api_key, source url and category url  

api_key=None
source_url=None
cat_url=None

#method to configure the required api keys and url  
def configure_request(app):
    global api_key, source_url, cat_url
    api_key = app.config['NEWS_API_KEY']
    source_url= app.config['NEWS_API_SOURCE_URL']
    cat_url=app.config['CAT_API_URL']

