import json
import requests
import uuid
from app import app

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in app.config or \
            not app.config['MS_TRANSLATOR_KEY']:
        return 'Error: the translation service is not configured.'
    auth = {
        'Ocp-Apim-Subscription-Key': app.config['MS_TRANSLATOR_KEY'],
        'Ocp-Apim-Subscription-Region': 'global',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())}
    params = {
        'api-version': '3.0',
        'from': source_language,
        'to': dest_language
    }
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/translate', params=params, headers=auth, json=[{'Text': text}])
    if r.status_code != 200:
        return 'Error: the translation service failed.'
    return r.json()[0]['translations'][0]['text']