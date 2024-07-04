'''REAL-WORLD EXAMPLE: Multithreading for I/O-bound Task
   SCENARIO: Web Scraping
            web scrapping often involves making numerous network request to fetch web pages. 
            These task are I/O-bound because they spend a lot of time waiting for responses 
            from servers. Multithreading can significantly improve the performance by allowing 
            multiple web pages to be fetched concurrently'''

'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/tutorials/

https://python.langchain.com/v0.2/docs/concepts/
'''


import threading
import requests
from bs4 import BeautifulSoup


urls= [
    'https://python.langchain.com/v0.2/docs/introduction/',

    'https://python.langchain.com/v0.2/docs/tutorials/',

    'https://python.langchain.com/v0.2/docs/concepts/',
  
      ]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


print("All web pages fetched")
    