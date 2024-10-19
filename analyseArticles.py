from textblob import TextBlob
from newspaper import Article
url = 'https://en.wikipedia.org/wiki/Government'
article = Article(url)
article.download()
article.parse()
article.nlp()
text = article.text
print(article)
blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)
