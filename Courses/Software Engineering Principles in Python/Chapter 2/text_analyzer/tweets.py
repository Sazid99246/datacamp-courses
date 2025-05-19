import text_analyzer
from .scoial_media import SocialMedia

# Define a Tweet class that inherits from SocialMedia


class Tweets(SocialMedia):
    def __init__(self, text):
        super().__init__()
        self.retweets = self._process_retweets()

    def _process_retweets(self):
        retweet_text = filter_lines(self.text, first_chars='RT')
        return SocialMedia(retweet_text)


# Create instance of Tweets
my_tweets = text_analyzer.Tweets(datacamp_tweets)

# Plot the most used hashtags in the retweets
my_tweets.retweets.plot_counts('hashtag_counts')

