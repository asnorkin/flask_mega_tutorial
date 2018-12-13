import json
import requests as rq
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    if 'YANDEX_TRANSLATE_TOKEN' not in app.config or not app.config['YANDEX_TRANSLATE_TOKEN']:
        return _('Error: the translation service is not configured.')

    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    API_TOKEN = app.config['YANDEX_TRANSLATE_TOKEN']
    translation_pair = '{}-{}'.format(source_language, dest_language)
    resp = rq.post(url, data={'key': API_TOKEN, 'text': text, 'lang': translation_pair})

    if resp.status_code != 200:
        return _('Error: the translation service failed.')

    return json.loads(resp.content)['text'][0]
