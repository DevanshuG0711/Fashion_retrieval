class ReRanker:

    def rerank(self, query_metadata, results):

        reranked = []

        for result in results:

            score = result.score

            metadata = result.payload["metadata"]

            # Scene match
            if (
                query_metadata["scene"]
                and metadata["scene"] == query_metadata["scene"]
            ):
                score += 0.20

            # Style match
            if (
                query_metadata["style"]
                and metadata["style"] == query_metadata["style"]
            ):
                score += 0.10

            # Clothing match
            for query_item in query_metadata["clothing"]:

                for image_item in metadata["clothing"]:

                    # Clothing type match
                    if query_item["type"] == image_item["type"]:
                        score += 0.10

                    # Color match
                    if query_item["color"] == image_item["color"]:
                        score += 0.05

            reranked.append((score, result))

        reranked.sort(
            key=lambda x: x[0],
            reverse=True
        )

        return [r[1] for r in reranked]