import text_analyzer

datacamp_tweet = 'Basic linear regression example. #DataCamp #DataScience #Python #sklearn'

my_document = text_analyzer.Document(text=datacamp_tweet)

print(my_document.text)


my_doc = text_analyzer.Document(datacamp_tweets)

help(my_doc.plot_counts)

my_doc.plot_counts()
