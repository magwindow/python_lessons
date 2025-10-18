import shutil
import requests

def download_image(url):
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(url.split('/')[-1], 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)

download_image('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png')