import json
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def lambda_handler(event, context):
    URL = 'https://api.chucknorris.io/jokes/random?category=dev'
    response = requests.get(URL)
    #logger.debug(response.json())
    return {
        "statusCode": 200,
        "body": json.dumps({
            "fact": response.json()['value']
        }),
    }
