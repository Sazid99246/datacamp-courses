tweet_time = df['created_at']

tweet_clock_time = [entry[11:19]
                    for entry in tweet_time if entry[17:19] == '19']

print(tweet_clock_time)
