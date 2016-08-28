import urllib

for i in range(100):
    urllib.urlretrieve(r"https://www.irctc.co.in/eticketing/captchaImage","%d.png"%i)
