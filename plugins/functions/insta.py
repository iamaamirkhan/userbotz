import time
import datetime

def time_format(seconds: int) -> str:
    result = str(datetime.timedelta(seconds=seconds))
    result = result.split(".")[0]
    return result


import requests
def instadownload(url):
    x = 'https://instagram-media-downloader.p.rapidapi.com/rapid/post.php'
    headers = {
	"X-RapidAPI-Key": "a2f4f654f4mshde45095b7f5749cp1cfa31jsncf2f8ad752d8",
	"X-RapidAPI-Host": "instagram-media-downloader.p.rapidapi.com"
}
    response = requests.request("GET", x, headers=headers, params={"url": url})
    # download the video
    video_url = response.json()['video']
    return video_url
