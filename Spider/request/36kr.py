import re
import requests
import json
from pprint import pprint
url = "https://36kr.com/"
headers = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763',
}
response = requests.get(url=url,headers=headers)
ret = re.findall("<script>var props=(.*?),locationnal",response)[0]
ret = json.loads(ret)
pprint(ret)