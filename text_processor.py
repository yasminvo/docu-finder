import re

def load_stopwords(filepath="stopwords.txt"):
    with open(filepath, "r", encoding="utf-8") as f:
        return set(f.read().split())

def tokenize(text):
    text = text.lower()
    words = re.findall(r'\b[a-zá-úà-ü]+\b', text)
    return words

def remove_stopwords(words, stopwords):
    return [word for word in words if word not in stopwords]
