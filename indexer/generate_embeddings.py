from pathlib import Path
import json
import random
from tqdm import tqdm

from models.clip_model import CLIPModel


class EmbeddingGenerator:

    def __init__(self):
        self.clip = CLIPModel()

    def generate(self, image_dir, output_file):

        image_dir = Path(image_dir)

        image_paths = sorted(image_dir.glob("*"))

        random.seed(42)
        random.shuffle(image_paths)
        image_paths = image_paths[:800]

        embeddings = []

        for image_path in tqdm(image_paths):

            embedding = self.clip.encode_image(str(image_path))

            embeddings.append({
                "image_path": str(image_path),
                "embedding": embedding.tolist()
            })

            with open(output_file, "w") as f:
                json.dump(embeddings, f)

        print(f"Saved {len(embeddings)} embeddings.")