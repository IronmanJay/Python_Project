import urllib.request
import urllib.parse
import urllib.error
url = 'https://blog.csdn.net/sinat_41688684/article/d' \
      'etails/8249436'
try:
    response = urllib.request.urlopen(url)
    print(url)
except urllib.error.HTTPError as e:
    print(e)
    print(e.code)
except urllib.error.URLError as e:
    print(e)