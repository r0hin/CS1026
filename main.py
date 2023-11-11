"""
  CS1026a 2023
  Assignment 03
  Rohin Arya
  251371185
  rarya4
  Nov 7, 2023
"""

from sentiment_analysis import *

# This function writes the report to a file
def main():
    # Get filenames
    keyword_name = input("Input keyword filename (.tsv file): ")
    if not keyword_name.endswith(".tsv"):
        raise Exception("Must have tsv file extension!") # Raise an exception if the file does not have the correct extension
    # Get filenames
    tweet_name = input("Input tweet filename (.csv file): ")
    if not tweet_name.endswith(".csv"):
        raise Exception("Must have csv file extension!") # Raise an exception if the file does not have the correct extension
    # Get filenames
    report_name = input("Input filename to output report in (.txt file): ")
    if not report_name.endswith(".txt"):
        raise Exception("Must have txt file extension!") # Raise an exception if the file does not have the correct extension
    
    # Write report
    write_report(make_report(read_tweets(tweet_name), read_keywords(keyword_name)), report_name)
	
    print("Wrote report to " + report_name)

main()
