import tkinter as tk
from tkinter import ttk
from googlesearch import search
from textblob import TextBlob
from newspaper import Article
import nltk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

redditResults = []
quoraResults = []
newsResults = []

def search_action():
    for widget in result_frame.winfo_children():
        widget.destroy()

    query = search_entry.get()

    l1 = tk.Label(result_frame, text="Reddit Links Referred", width=100, anchor='w')
    l1.pack(anchor='w', pady=5)
    for result in search(query + " reddit", num_results=3):
        redditResults.append(Article(result))
        link_label = tk.Label(result_frame, text=result, fg="blue", width=100, anchor='w')
        link_label.pack(anchor='w', padx=10)
        
    l2 = tk.Label(result_frame, text="Quora Links Referred", width=100, anchor='w')
    l2.pack(anchor='w', pady=5)
    for result in search(query + " quora", num_results=3):
        quoraResults.append(Article(result))
        link_label = tk.Label(result_frame, text=result, fg="blue", width=100, anchor='w')
        link_label.pack(anchor='w', padx=10)

    l3 = tk.Label(result_frame, text="News Channels Links Referred", width=100, anchor='w')
    l3.pack(anchor='w', pady=5)
    for result in search(query + " news articles -pdf", num_results=3):
        newsResults.append(Article(result))
        link_label = tk.Label(result_frame, text=result, fg="blue", width=100, anchor='w')
        link_label.pack(anchor='w', padx=10)

    plot_sentiment()

def plot_sentiment():
    sentiment = 0
    for article in redditResults:
        article.download()
        article.parse()
        article.nlp()
        blob = TextBlob(article.summary)
        sentiment += blob.sentiment.polarity
    redditPerc = ((sentiment / 3 + 1) / 2) * 100

    sentiment = 0
    for article in quoraResults:
        article.download()
        article.parse()
        article.nlp()
        blob = TextBlob(article.summary)
        sentiment += blob.sentiment.polarity
    quoraPerc = ((sentiment / 3 + 1) / 2) * 100

    sentiment = 0
    for article in newsResults:
        article.download()
        article.parse()
        article.nlp()
        blob = TextBlob(article.summary)
        sentiment += blob.sentiment.polarity
    newsPerc = ((sentiment / 3 + 1) / 2) * 100

    x = ['Reddit', 'Quora', 'News Channels']
    y = [redditPerc, quoraPerc, newsPerc]
    colors = ['red', 'green', 'blue']

    fig, ax = plt.subplots()
    ax.bar(x, y, color=colors)
    ax.set_title('Sentiment Analysis of Search Results')
    ax.set_xlabel('Sources')
    ax.set_ylabel('Sentiment Score')
    ax.set_ylim(0, 100) 

    for widget in plot_frame.winfo_children():
        widget.destroy()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

root = tk.Tk()
root.title("Feedback Analysis")
root.geometry("1920x1080")

frame = tk.Frame(root)
frame.pack(pady=20)

search_entry = tk.Entry(frame, width=60)
search_entry.pack(side=tk.LEFT, padx=5)

search_button = tk.Button(frame, text="Search", command=search_action)
search_button.pack(side=tk.LEFT)

result_frame = tk.Frame(root)
result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

plot_frame = tk.Frame(root)
plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

root.mainloop()
