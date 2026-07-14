from models.clip_model import CLIPModel
from models.attribute_parser import AttributeParser


class QueryParser:

    def __init__(self):
        self.clip = CLIPModel()
        self.parser = AttributeParser()

    def parse(self, query: str):

        embedding = self.clip.encode_text(query)

        metadata = self.parser.parse(query)

        return {
            "query": query,
            "embedding": embedding,
            "metadata": metadata
        }