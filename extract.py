import spacy
# from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re
with open('./data/CREC-2019-01-03.pdf', 'r', encoding='utf-8') as inflie:
    text = ""
    for line in inflie:
        text += line
text = text.replace("\n", "")
print(text)
# regex1 = re.compile(r'(Mr\.\s[A-Z]+)(.*?)(?=(?!Mr\.\sPresident)(Mr.\s[A-Z]+))')
# matches = re.findall(regex1, text)
# print(len(matches))