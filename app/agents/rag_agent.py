import chromadb
import ollama


class RagAgent:

    def __init__(self):

        client = chromadb.PersistentClient(
            path="./chroma_db"
        )

        self.collection = client.get_collection(
            "incidents"
        )

    def retrieve(self, query):

        response = ollama.embed(
            model="nomic-embed-text",
            input=query
        )

        query_embedding = response["embeddings"][0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=3,
            include=["documents", "distances"]
        )

        print(results["distances"])

        docs = results["documents"][0]

        return "\n\n".join(docs)