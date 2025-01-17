import praw

reddit = praw.Reddit(
    client_id='TNsziSQCYgK1nKhJRP0Mcg',
    client_secret='I6BkIj4M-6HB9z2ncP_u2XuvfRIwDg',
    user_agent='YOUR_USER_AGENT')

def extract_post_details(post_url):
    submission = reddit.submission(url=post_url)
    title = submission.title

    submission.comments.replace_more(limit=None)
    comments = [comment.body for comment in submission.comments.list()]
    
    return title, body, comments

post_url = "https://www.reddit.com/r/Python/comments/some_post_id"  # Replace with the Reddit post URL
title, body, comments = extract_post_details(post_url)

print("Title:", title)
print("Body:", body)
print("Comments:")
for comment in comments:
    print("-", comment)
