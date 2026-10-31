import chromadb
import ollama
from pathlib import Path

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="incidents"
)

incident_dir = Path("data/incidents")

for file in incident_dir.glob("*.txt"):

    content = file.read_text(
        encoding="utf-8"
    )

    response = ollama.embed(
        model="nomic-embed-text",
        input=content
    )

    embedding = response["embeddings"][0]

    collection.add(
        ids=[file.stem],
        documents=[content],
        embeddings=[embedding]
    )

    print(f"Loaded {file.name}")

print("✅ Ingestion Complete")