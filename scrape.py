import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/')
soup = BeautifulSoup(res.text, 'html.parser')

# These classes are specific to Hacker News
links = soup.select('.storylink')
subtext = soup.select('.subtext')

# Sorts from highest to lowest points
def sortByVotes(HackerNewsList):
    return sorted(HackerNewsList, key = lambda k: k['votes'], reverse = True)

# Custom way to build a list of dictionaries containing title, link and votes.
def customHackerNews(links, subtext):
    HackerNews = []
    for i, any in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                HackerNews.append({'title': title, 'link': href, 'votes': points})
    return sortByVotes(HackerNews)

# Prints more nicely
pprint.pprint(customHackerNews(links, subtext))