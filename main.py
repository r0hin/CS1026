#If either read_keywords or read_tweets returns an empty dictionary or empty list an Exception with the text "Tweet list or keyword dictionary is empty!" should be raised.
from sentiment_analysis import *

def main():
    keyword_name = input("Input keyword filename (.tsv file): ")
    if not keyword_name.endswith(".tsv"):
        raise Exception("Must have tsv file extension!")
    tweet_name = input("Input tweet filename (.csv file): ")
    if not tweet_name.endswith(".csv"):
        raise Exception("Must have csv file extension!")
    report_name = input("Input filename to output report in (.txt file): ")
    if not report_name.endswith(".txt"):
        raise Exception("Must have txt file extension!")
    
    write_report(make_report(read_tweets(tweet_name), read_keywords(keyword_name)), report_name)
	
    print("Wrote report to " + report_name)

main()
