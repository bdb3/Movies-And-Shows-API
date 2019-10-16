import json
import requests

def lambda_handler(event, context):
    showID = event["queryStringParameters"]["id"]
    apiKey = ''
    url = 'https://api.themoviedb.org/3/tv/' + str(showID) + '?api_key='+ apiKey
    r = requests.get(url)
    json_data = r.json() if r and r.status_code == 200 else None
    return {
    'statusCode': "200",
    'body': json.dumps(json_data)
}
