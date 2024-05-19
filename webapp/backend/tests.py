from requests import get
from bs4 import BeautifulSoup
from db_connect import google_engine, google_key

#Testing web scraping for information
headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

response = get('https://www.google.com/search?q=How+much+sun+does+a+Pothos+need', headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.find_all('span'))
div = soup.find("span", {"class": "hgKElc"})
print(div)




#Testing using google api for information

response = get('https://www.googleapis.com/customsearch/v1?key=' + google_key + '&cx=' + google_engine + "&q=" + "How+often+should+I+water+a+succulent")
# print(response.text)