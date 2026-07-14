from retriever.search import SearchEngine


def print_results(query, results):

    print("\n" + "=" * 100)
    print(f"QUERY: {query}")
    print("=" * 100)

    for rank, result in enumerate(results, start=1):

        print(f"\nRank {rank}")
        print(f"Similarity Score : {result.score:.4f}")
        print(f"Image Path       : {result.payload['image_path']}")
        print(f"Caption          : {result.payload['caption']}")
        print(f"Metadata         : {result.payload['metadata']}")


def main():

    engine = SearchEngine()

    queries = [
        "A person in a bright yellow raincoat.",
        "Professional business attire inside a modern office.",
        "Someone wearing a blue shirt sitting on a park bench.",
        "Casual weekend outfit for a city walk.",
        "A red tie and a white shirt in a formal setting."
    ]

    for query in queries:

        _, results = engine.search(
            query=query,
            limit=5
        )

        print_results(query, results)


if __name__ == "__main__":
    main()