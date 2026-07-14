import json
import uuid

from tqdm import tqdm
from qdrant_client.models import PointStruct

from indexer.generate_embeddings import EmbeddingGenerator
from Vector_db.qdrant import QdrantDB


class IndexBuilder:

    def __init__(self):

        self.db = QdrantDB()
        self.embedding_generator = EmbeddingGenerator()

    def build(self):

        # Load metadata
        with open("data/metadata/metadata.json", "r") as f:
            metadata = json.load(f)

        # Generate embeddings
        embeddings = self.embedding_generator.generate()

        points = []

        for image_path, embedding in tqdm(embeddings.items()):

            item = metadata[image_path]

            payload = {
                "image_path": image_path,
                "caption": item["caption"],
                "metadata": item["metadata"]
            }

            points.append(

                PointStruct(
                    id=str(uuid.uuid4()),
                    vector=embedding,
                    payload=payload
                )

            )

        self.db.create_collection()

        self.db.insert_points(points)

        print(f"\nSuccessfully indexed {len(points)} images.")