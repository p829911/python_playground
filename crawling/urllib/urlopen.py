import urllib.request as req
from urllib.error import URLError, HTTPError

path_list = ["test2.jpg", "index2.html"]
target_url = [
    "http://blogfiles.naver.net/data42/2009/4/29/193/1600cat_12020_nobanaba.jpg",
    "http://google.com",
]

for i, url in enumerate(target_url):
    try:
        response = req.urlopen(url)
        contents = response.read()
        print("-------------------------------------")
        print("Header Info-{}: {}".format(i, response.info()))
        print("HTTP Status Code: {}".format(response.getcode()))
        print()
        print("-------------------------------------")

        with open(path_list[i], "wb") as f:
            f.write(contents)

    except HTTPError as e:
        print("Download failed.")
        print("HTTPError Code: ", e.code)

    except URLError as e:
        print("Download failed.")
        print("URLError Reason: ", e.reason)

    else:
        print()
        print("Download Succeed.")
