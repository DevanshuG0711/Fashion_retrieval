from pathlib import Path
from tqdm import tqdm

from models.clip_model import CLIPModel


class EmbeddingGenerator:

    def __init__(self):
        self.clip = CLIPModel()

    def generate(self):

        with open("data/selected_images.txt") as f:
            image_paths = [
                Path(line.strip())
                for line in f
            ]

        embeddings = {}

        for image_path in tqdm(image_paths):

            embeddings[str(image_path)] = (
                self.clip.encode_image(
                    str(image_path)
                ).tolist()
            )

        return embeddings