import json
import random
from pathlib import Path
from tqdm import tqdm

from models.caption_model import CaptionModel
from models.attribute_parser import AttributeParser


class MetadataGenerator:

    def __init__(self):

        self.caption_model = CaptionModel()
        self.parser = AttributeParser()

    def generate(self, image_dir, output_file):

        image_dir = Path(image_dir)

        metadata = []

        with open("data/selected_images.txt") as f:
            image_paths = [
                Path(line.strip())
                for line in f
            ]

        for image_path in tqdm(image_paths):

            caption = self.caption_model.generate_caption(
                str(image_path)
            )

            parsed = self.parser.parse(caption)

            metadata.append({

                "image_path": str(image_path),

                "caption": caption,

                "metadata": parsed

            })

        with open(output_file, "w") as f:

            json.dump(metadata, f, indent=4)