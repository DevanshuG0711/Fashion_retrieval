from indexer.generate_metadata import MetadataGenerator

generator = MetadataGenerator()

generator.generate(
    image_dir="data/images",
    output_file="data/metadata/metadata.json"
)