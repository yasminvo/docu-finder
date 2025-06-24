from indexer import InvertedIndex
from text_processor import load_stopwords
from search import SearchEngine

def main():
    stopwords = load_stopwords()
    indexer = InvertedIndex()
    indexer.index_documents("docs", stopwords)

    engine = SearchEngine(indexer.get_index())

    print("Sistema de Busca Textual com Posições")
    while True:
        query = input("\nDigite uma palavra para buscar (ou 'sair'): ").strip()
        if query.lower() == "sair":
            break
        result = engine.search(query)
        if result:
            for doc, positions in result.items():
                print(f"'{query}' encontrado em {doc}, posições: {positions}")
        else:
            print(f"Nenhum documento contém a palavra '{query}'.")


if __name__ == "__main__":
    main()
