import json
import requests
from urllib.parse import quote

def lambda_handler(event, context):
    searchQueryString = event["queryStringParameters"]["query"]
    pageNum = event["queryStringParameters"]["page"]
    apiKey = ''
    
    url = 'https://api.themoviedb.org/3/search/multi' + '?api_key='+ apiKey + '&page='+str(pageNum) + '&query=' + quote(searchQueryString)
    r = requests.get(url)
    json_data = r.json() if r and r.status_code == 200 else None
    return {
    'statusCode': 200,
    'body': json.dumps(json_data)
    }
  