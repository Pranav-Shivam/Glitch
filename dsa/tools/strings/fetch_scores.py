"""Download the six per-company CSVs and write scores.json (company-tag scores for the problems in this topic).
Source: github.com/liquidslr/leetcode-company-wise-problems (unofficial; scores are normalised, method undocumented)."""
import csv, json, os, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__))
COMPANIES = ["Google", "Meta", "Amazon", "Microsoft", "Apple", "Uber"]
TITLES = ['Valid Word Abbreviation', 'Longest Palindromic Substring', 'String to Integer (atoi)', 'Roman to Integer', 'Reverse Words in a String',
          'First Unique Character in a String', 'Custom Sort String', 'Group Shifted Strings', 'Add Strings', 'Multiply Strings', 'Zigzag Conversion',
          'Longest Common Prefix', 'String Compression', 'Find the Index of the First Occurrence in a String', 'Merge Strings Alternately', 'Add Binary',
          'Palindromic Substrings', 'Compare Version Numbers', 'Encode and Decode Strings', 'Text Justification', 'Valid Number', 'Valid Palindrome II',
          'Integer to English Words']
os.makedirs(os.path.join(HERE, 'csv'), exist_ok=True)
res = {t: {} for t in TITLES}
for c in COMPANIES:
    path = os.path.join(HERE, 'csv', c + '.csv')
    url = f"https://raw.githubusercontent.com/liquidslr/leetcode-company-wise-problems/main/{c}/5.%20All.csv"
    urllib.request.urlretrieve(url, path)
    for r in csv.DictReader(open(path, encoding='utf8')):
        if r['Title'] in res: res[r['Title']][c] = round(float(r['Frequency']), 1)
json.dump(res, open(os.path.join(HERE, 'scores.json'), 'w'))
print('wrote scores.json')
