class SearchEngine:
    def __init__(self, index):
        self.index = index

    def search(self, term):
        term = term.lower()
        return self.index.get(term, {})
