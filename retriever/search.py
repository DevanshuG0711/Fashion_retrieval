from retriever.parse_query import QueryParser
from Vector_db.qdrant import QdrantDB
from retriever.rerank import ReRanker



class SearchEngine:

    def __init__(self):

        self.query_parser = QueryParser()
        self.db = QdrantDB()
        self.reranker = ReRanker()

    def search(self, query: str, limit: int = 10):

        parsed = self.query_parser.parse(query)

        results = self.db.search(
            query_vector=parsed["embedding"].tolist(),
            limit=limit
        )

        results = self.reranker.rerank(
            parsed["metadata"],
            results
        )
        return parsed, results
    
    