import requests
from urllib.parse import urlencode, unquote, quote_plus

url = '서비스 URL 주소'
query_params = '?' + urlencode(
   {
       # 요청 변수

       # quote_plus('serviceKey') : 'aa',

       # quote_plus('numOfRows') : 'bb',

       # quote_plus('pageNo') : 'cc',

       # quote_plus('resultType') : 'dd'
   }
)

# a = url + operation[0] + unquote(query_params)
response = requests.get(url + unquote(query_params))
print(response.text)