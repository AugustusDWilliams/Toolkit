import requests
import os


def download_image(url, dir):
    if url.endswith((".jpg", ".jpeg", ".png", ".gif")):
        img = requests.get(url).content
        file_name = os.path.basename(url)
        with open(f"{dir}{file_name}", "wb") as f:
            f.write(img)


download_image("https://impshum.co.uk/red.png", "./")

