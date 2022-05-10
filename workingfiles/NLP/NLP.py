# installed on PythonData:
# pip install nltk
# python -m nltk.downloader popular

# dependencies
import nltk # Natural Language Toolkit Library
from nltk import word_tokenize


text = word_tokenize("My name is Justin and I love video games.")
output = nltk.pos_tag(text)
print(output)