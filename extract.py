from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re
with open('./data/txt/CREC-2019-01-03.txt', 'r', encoding='utf8', errors='ignore') as inflie:
    text = ""
    for line in inflie:
        text += line
text = text.replace("\n", "")
regex1 = re.compile(r'(Mr\.\s[A-Z]+)(.*?)(?=(?!Mr\.\sPresident)(Mr.\s[A-Z]+))')
matches = re.findall(regex1, text)
print(len(matches))

analyzer = SentimentIntensityAnalyzer()
def analyze_score(match):
    return analyzer.polarity_scores(match)
print(matches[:5])

scores=[]
for match in matches:
    match = match[1]
    scores.append(analyze_score(match))

print (scores[:5])