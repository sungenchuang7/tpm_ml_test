tweet = '@elonmusk thinking of quitting my jobs & becoming an influencer full-time wdyt'

# pre-process tweet and get rid of any @mention and url http
tweet_words = []

for word in tweet.split(' '):
    if word.startswith('@') and len(word) > 1:
        word = '@user'
    
    elif word.startswith('http'):
        word = "http"
    tweet_words.append(word)

print(tweet_words)

tweet_proc = " ".join(tweet_words)
print(tweet_proc)