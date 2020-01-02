import json

from botocore.vendored import requests


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