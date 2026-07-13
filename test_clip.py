from models.clip_model import CLIPModel

# Load model
clip = CLIPModel()

# Encode a text query
embedding = clip.encode_text("white shirt")

print("Embedding Shape:", embedding.shape)
print("First 10 values:", embedding[:10])