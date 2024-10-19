# hackathon
ML hackathon
TNsziSQCYgK1nKhJRP0Mcg
	I6BkIj4M-6HB9z2ncP_u2XuvfRIwDg
from pprint import pprint
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import praw
user_agent = "Scraper 1.0 by /u/python_engineer"
reddit = praw.Reddit(
    client_id = ""
    client_secret = ""
    user_agent = user_agent
)
headlines = set()
for submission in reddit.subreddit('bangalore').hot(limit = NONE):
    print(submission.title)
headlines.add(submission.title)
print(len(headlines))
df = pd.DataFrame(headlines)
df.head()
