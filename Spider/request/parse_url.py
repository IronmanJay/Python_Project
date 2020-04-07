import requests
from retrying import retry

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',}

@retry(stop_max_attempt_number=3)
def parse(url):
    print("*"*20)
    response = requests.get(url,headers=headers,verify=False)
    response.status_code == 200
    return response.content.decode()

def parse_url(url):
    try:
        html_str = parse(url)
    except:
        html_str = None
    return html_str

if __name__ == '__main__':
    url = "www.123.com"
    print(parse_url(url))