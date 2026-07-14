from retriever.parse_query import QueryParser

parser = QueryParser()

result = parser.parse(
    "A person wearing a white shirt inside an office"
)

print(result["metadata"])
print(result["embedding"].shape)