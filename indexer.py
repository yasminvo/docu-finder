import os
from text_processor import tokenize, remove_stopwords

class InvertedIndex:
    def __init__(self):
        self.index = {}  # { termo: {arquivo: [posicoes]} }

    def index_documents(self, directory, stopwords):
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                path = os.path.join(directory, filename)
                with open(path, "r", encoding="utf-8") as file:
                    text = file.read()
                    words = tokenize(text)
                    words = remove_stopwords(words, stopwords)

                    for pos, word in enumerate(words):
                        if word not in self.index:
                            self.index[word] = {}
                        if filename not in self.index[word]:
                            self.index[word][filename] = []
                        self.index[word][filename].append(pos)

    def get_index(self):
        return self.index
