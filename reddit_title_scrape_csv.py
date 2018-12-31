from os import listdir, makedirs
import praw
from requests import get

headers = {'User-Agent': 'PyBot3000',}

#####
    Removed personal data
#####

subreddit = reddit.subreddit('python')
reddit.read_only = True

makedirs(f'{subreddit}/', exist_ok=True)
with open(f'{subreddit}/titles.csv', 'w') as file:
    file.write('author,title,score,url\n')
    for post in subreddit.top(limit=1000):
        title = str(post.title).replace(',', '-')
        print(post.author,post.title,post.score)
        file.write(f'{post.author},{title},{post.score},{post.url}\n')
