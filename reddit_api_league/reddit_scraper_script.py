#!/opt/anaconda3/bin/python

# run
# pip install praw
# pip install fuzzywuzzy
# pip install python-Levenshtein
# before running the script

from os.path import isfile
from constants_dictionaries import champion_counter_dictionary
from constants_dictionaries import champion_name_dictionary
import praw
import pprint as pp
import pandas as pd
from time import sleep
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import re
import csv

reddit = praw.Reddit()
subreddit = reddit.subreddit('leagueoflegends')

selftext_list = []
prep_comment_list = []

for submission in subreddit.top(limit=100):
    initial_comment_tree = submission.comments
    initial_selftext = submission.selftext
    selftext_list.append(initial_selftext)
    prep_comment_list.append(initial_comment_tree.list())

# pp.pprint(prep_comment_list)

comment_list = []

for comment_tree in prep_comment_list:
    for element in comment_tree:
        if isinstance(element, praw.models.reddit.comment.Comment):
            comment_list.append(element)

# pp.pprint(comment_list)

comment_body_list = []

for element in comment_list:
    comment_body_list.append(element.body)

for element in selftext_list:
    comment_body_list.append(element)

split_filtered_list = []

for element in comment_body_list:
    split_filtered_list.append(re.split(r'\W+', element))

split_filtered_list = list(filter(None, split_filtered_list))

split_filtered_list = [item for sublist in split_filtered_list for item in sublist]

for word in split_filtered_list:
    for champ_name_sublist_key in champion_name_dictionary:
        for name in champion_name_dictionary[champ_name_sublist_key]:
            if fuzz.ratio(word, name) > 90:
                champion_counter_dictionary[champ_name_sublist_key][0] += 1

print(type(champion_counter_dictionary["karma"][0]))

champion_counter_dictionary["karma"][0] = round(float(champion_counter_dictionary["karma"][0]) * 0.01)

print(sorted(champion_counter_dictionary.items(), key = lambda x: x[1], reverse = True))

with open('champion_counter_dictionary.csv', 'w') as f:
    for key in champion_counter_dictionary.keys():
        f.write("%s,%s\n"%(key,champion_counter_dictionary[key]))
