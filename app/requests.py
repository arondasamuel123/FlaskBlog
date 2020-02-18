import urllib.request,json


def get_quotes():
    quote_url='http://quotes.stormconsultancy.co.uk/random.json'
    print(quote_url)
    
    with urllib.request.urlopen(quote_url) as url:
        data =url.read()
        response_data =json.loads(data)
        
        return response_data
            