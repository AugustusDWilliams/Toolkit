import requests
import os


def download_mp4(url, dir):
    mp4 = requests.get(url)
    file_name = os.path.basename(url)
    with open(f"{dir}{file_name}", "wb") as f:
        for chunk in mp4.iter_content(chunk_size=255):
            if chunk:
                f.write(chunk)


download_mp4("https://archive.org/download/user-mp4-test/ac3.mp4", "./")

