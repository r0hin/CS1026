"""
  CS1026a 2023
  Assignment 03
  Rohin Arya
  251371185
  rarya4
  Nov 7, 2023
"""

def read_keywords(keyword_file_name):
    word_dictionary = {}

    # Read from keywords.tsv
    try:
        keyword_file = open(keyword_file_name, "r")
        for line in keyword_file:
            words = line.split("\t")
            word_dictionary[words[0]] = int(words[1])
    except IOError:
        print("Could not open the file " + keyword_file_name + "!")
        return {}

    return word_dictionary;

def clean_tweet_text(tweet_text):
    lowercase = tweet_text.lower()
    whitelist = set('abcdefghijklmnopqrstuvwxyz ')
    clean_tweet = ''.join(filter(whitelist.__contains__, lowercase))

    return clean_tweet;

def calc_sentiment(tweet_text, keyword_dict):
    sumSentiment = 0
    words = tweet_text.split(" ")

    for word in words:
        if word in keyword_dict:
            sumSentiment += keyword_dict[word]

    return sumSentiment;

def classify(score):
    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    return "neutral";

def read_tweets(tweet_file_name):
    tweetlist = []

    try:
        tweet_file = open(tweet_file_name, "r")
        for line in tweet_file:
            tweet = {
                "city": line.split(",")[8],
                "country": line.split(",")[6],
                "date": line.split(",")[0],
                "favorite": int(line.split(",")[4]),
                "lang": line.split(",")[5],
                "lat": "NULL",
                "lon": "NULL",
                "retweet": int(line.split(",")[3]),
                "state": line.split(",")[7],
                "text": clean_tweet_text(line.split(",")[1]),
                "user": line.split(",")[2]
            }

            if (line.split(",")[9] != "NULL"):
                tweet["lat"] = line.split(",")[9]
            if (line.split(",")[10] != "NULL"):
                tweet["lon"] = line.split(",")[10].strip("\n")
    
            tweetlist.append(tweet)
    except IOError:
        print("Could not open the file " + tweet_file_name)
        return []
    
    return tweetlist;

def make_report(tweet_list, keyword_dict):
    num_tweets = 0
    num_positive = 0
    num_negative = 0
    num_neutral = 0
    sum_tweet_sentiment = 0
    num_favorite = 0
    sum_favorite_sentiment = 0
    num_retweet = 0
    sum_retweet_sentiment = 0
    countries_average_sentiments = {}

    for tweet in tweet_list:
        num_tweets += 1
        sentiment = calc_sentiment(tweet["text"], keyword_dict)
        sum_tweet_sentiment += sentiment

        if tweet["country"] in countries_average_sentiments and tweet["country"]:
            countries_average_sentiments[tweet["country"]].append(sentiment)
        else:
            countries_average_sentiments[tweet["country"]] = [sentiment]

        if classify(sentiment) == "positive":
            num_positive += 1
        elif classify(sentiment) == "negative":
            num_negative += 1
        else:
            num_neutral += 1

        if tweet["favorite"] > 0:
            num_favorite += 1
            sum_favorite_sentiment += sentiment
        if tweet["retweet"] > 0:
            num_retweet += 1
            sum_retweet_sentiment += sentiment

    avg_sentiment = round(sum_tweet_sentiment / num_tweets, 2)
    avg_favorite = round(sum_favorite_sentiment / num_favorite, 2)
    avg_retweet = round(sum_retweet_sentiment / num_retweet, 2)

    # Get top 5 countries
    top_five = []
    for country in countries_average_sentiments:
        if country == "NULL":
            continue
        top_five.append([country, round(sum(countries_average_sentiments[country]) / len(countries_average_sentiments[country]), 2)])
    top_five.sort(key=lambda x: x[1], reverse=True)
    top_five = top_five[:5]

    # 'top_five': 'United States, United Kingdom, United Arab Emirates, Taiwan, Sweden'
    topFiveString = ", ".join([x[0] for x in top_five])

    report = {
        "avg_favorite": avg_favorite,
        "avg_retweet": avg_retweet,
        "avg_sentiment": avg_sentiment,
        "num_favorite": num_favorite,
        "num_negative": num_negative,
        "num_neutral": num_neutral,
        "num_positive": num_positive,
        "num_retweet": num_retweet,
        "num_tweets": num_tweets,
        "top_five": topFiveString,
    }

    return report;

def write_report(report, output_file):
    writable = open(output_file, "w")
    writable.write("Average sentiment of all tweets: " + str(report["avg_sentiment"]) + "\n")
    writable.write("Total number of tweets: " + str(report["num_tweets"]) + "\n")
    writable.write("Number of positive tweets: " + str(report["num_positive"]) + "\n")
    writable.write("Number of negative tweets: " + str(report["num_negative"]) + "\n")
    writable.write("Number of neutral tweets: " + str(report["num_neutral"]) + "\n")
    writable.write("Number of favorited tweets: " + str(report["num_favorite"]) + "\n")
    writable.write("Average sentiment of favorited tweets: " + str(report["avg_favorite"]) + "\n")
    writable.write("Number of retweeted tweets: " + str(report["num_retweet"]) + "\n")
    writable.write("Average sentiment of retweeted tweets: " + str(report["avg_retweet"]) + "\n")
    writable.write("Top five countries by average sentiment: " + str(report["top_five"]) + "\n")
    writable.close()

    return;
