import urllib.request as req

img_url = "http://blogfiles.naver.net/data42/2009/4/29/193/1600cat_12020_nobanaba.jpg"
html_url = "http://google.com"

save_path1 = "test1.jpg"
save_path2 = "index.html"

try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print("Download failed")
    print(e)
else:
    print(header1)
    print(header2)
    print("Filename1 {}".format(file1))
    print("Filename2 {}".format(file2))
    print("Download Succeed")
