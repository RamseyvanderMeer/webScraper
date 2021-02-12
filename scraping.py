# need to install requests, bs4 and lxml
import requests
from bs4 import BeautifulSoup
import json


def save_function(article_list):
    with open('articles.txt', 'w') as file:
        for item in article_list:
            file.write(json.dumps(item,ensure_ascii=True))
        file.close()


def hackernews_rss(url='https://news.ycombinator.com/rss'):
    article_list = []
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')        
        for a in articles:
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            article = {
                'title': title,
                'link': link,
                'published': published
                }
            article_list.append(article)
        return save_function(article_list)
    except Exception as e:
        print('The scraping job failed. See exception: ')
        print(e)

print('Starting scraping')
hackernews_rss()
print('Finished scraping')

