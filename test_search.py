from retriever.search import SearchEngine

engine = SearchEngine()

parsed, results = engine.search(
    "A person wearing a white shirt in an office",
    limit=5
)

print("\nParsed Metadata:")
print(parsed["metadata"])

print("\nTop Results:")

for i, result in enumerate(results, start=1):

    print(f"\nRank {i}")

    print("Score:", result.score)

    print(result.payload["image_path"])

    print(result.payload["caption"])