
from urllib import urlopen
my_url = "https://www.douban.com/"
urldoc = urlopen(my_url)
print urldoc.read()

