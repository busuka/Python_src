import requests
from bs4 import BeautifulSoup
import urllib.request



#武庫川Webサイトにログインする際に入力するデータ
#参考 http://docs.python.jp/3/howto/urllib2.html#introduction
#<input type="text" name="b.studentId" size="18" maxlength="7" value="" id="p01aForm_b_studentId" style="ime-mode:disabled">
#<input type="password" name="b.password" size="18" maxlength="16" id="p01aForm_b_password">

url = "https://www.e-license.jp/el2/?abc=%2FkZZ5Rkdn8k%2BbrGQYS%2B1OA%3D%3D"
payload = {"b.studentID":10380,"b.password":"y19991102"}

data = urllib.parse.urlencode(payload)
data = data.encode('Shift_JIS') # data should be bytes
req = urllib.request.Request(url, data)

with urllib.request.urlopen(req) as response:
   the_page = response.read()




