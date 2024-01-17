import requests
import time 


url = "https://visitseattle.org/events/page/1"

# CREATE -> POST
# Read -> GET
# Update -> PUT
# DELETE -> DELETE

# requests.post("https://concert.com/buy")
# requests.put("https://github.com/rgulla")
# requests.delete("https://facebook.com/ravinder.gulla/post/1")

res = requests.get(url)

# 200 -> OK
# 201 -> Created (after POST)
# 301 -> Moved Permanently
# 302
# 400 -> Bad Request (error from user)
# 404 -> Not Found (error from user)
# 500 -> Internal Server Error (error from server)
res.status_code

res.text

open("seattleevents.html", "w").write(res.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text, "html.parser")

selector = "div.search-result-preview> div > h3 > a "
a_eles = soup.select(selector)
a_eles


#[x['href'] for x in a_eles]

#for x in [1,2,3,4]:
#    time.sleep(1)
#    # do some requests.get()... 

#requests.get(url)    



#import requests

#url
#res
#res

#res.text 