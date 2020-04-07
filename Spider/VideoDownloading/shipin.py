import requests
url = 'http://v3-default.ixigua.com/dd48e529360eaf527c9a929e8622e8d8/5d4d0a65/video/m/220c097cb8f27af496eaddb07c5d42edc601162e796e0000acb22a2eb570/?rc=M2psOGZoZ3NrbzMzZTczM0ApdSk6OjUzNTg0NDgzNTw7PDNAKTk8OTU8OzY8PDdnODM6NzNnKXUpQGczdSlAZjN1KTk0ZHIwajItcnIuMF8tLTQtMHNzOmkvNDIvNS0yLS0tMi4tLS4vaS1gY2BgLzFjYl8zLjQyMDA6YzpiMHAjOmEtcCM6YDU0Og%3D%3D'
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
r = requests.get(url=url,headers=headers)
with open('1.mp4','wb') as fp:
    fp.write(r.content)