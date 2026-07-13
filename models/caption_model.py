from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration


class CaptionModel:
    def __init__(self):

        self.device = (
            "mps"
            if torch.backends.mps.is_available()
            else "cpu"
        )

        self.processor = BlipProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

        self.model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        ).to(self.device)

        self.model.eval()

    @torch.no_grad()
    def generate_caption(self, image_path: str) -> str:

        image = Image.open(image_path).convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        ).to(self.device)

        output = self.model.generate(
            **inputs,
            max_new_tokens=30
        )

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return caption