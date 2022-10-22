import requests
from bs4 import BeautifulSoup
  
# target url
url = 'https://curl.se/'
  
# making requests instance
reqs = requests.get(url)
  
# using the BeaitifulSoup module
soup = BeautifulSoup(reqs.text, 'html.parser')
  
# displaying the title
print("Title of the website is : ")
for title in soup.find_all('title'):
    print(title.get_text())