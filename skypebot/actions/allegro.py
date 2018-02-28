import io

import requests
from decouple import config


FACEBOOK_APP_ID = config('FACEBOOK_APP_ID')
FACEBOOK_APP_SECRET = config('FACEBOOK_APP_SECRET')

FACEBOOK_TOKEN = '{}|{}'.format(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
FACEBOOK_URL = 'https://graph.facebook.com/v2.12/'
PARAMS = {'access_token': FACEBOOK_TOKEN}
ALLEGRO_PHOTOS_URL = FACEBOOK_URL + '1555033107877321/photos/'


def get_menu_image_url():
    photos = requests.get(ALLEGRO_PHOTOS_URL, params=PARAMS).json()
    last_photo_id = photos['data'][0]['id']
    last_photo_url = FACEBOOK_URL + '{}?fields=images'.format(last_photo_id)

    images = requests.get(last_photo_url, params=PARAMS).json()
    last_image_url = images['images'][0]['source']
    return last_image_url


def get_menu_image_content():
    image_url = get_menu_image_url()
    response = requests.get(image_url)
    return io.BytesIO(response.content)
