from PIL import Image
import torch
import open_clip


class CLIPModel:

    def __init__(
        self,

        model_name: str = "ViT-B-32",
        pretrained: str = "laion2b_s34b_b79k",
    ):
        self.device = (
            "mps"
            if torch.backends.mps.is_available()
            else "cpu"
        )
        self.model, _, self.preprocess = open_clip.create_model_and_transforms(
            model_name=model_name,
            pretrained=pretrained,
            device=self.device,
        )
        self.tokenizer = open_clip.get_tokenizer(model_name)
        self.model.eval()

    @torch.no_grad()
    def encode_image(self, image_path: str):
        image = self.preprocess(Image.open(image_path)).unsqueeze(0)
        image = image.to(self.device)
        embedding = self.model.encode_image(image)
        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        return embedding.squeeze().cpu().numpy()

    @torch.no_grad()
    def encode_text(self, text: str):
        tokens = self.tokenizer([text]).to(self.device)
        embedding = self.model.encode_text(tokens)
        embedding = embedding / embedding.norm(dim=-1, keepdim=True)
        return embedding.squeeze().cpu().numpy()