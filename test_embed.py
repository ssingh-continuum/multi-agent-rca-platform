import ollama

print("Starting...")

response = ollama.embed(
    model="nomic-embed-text",
    input="Payment API returning HTTP 500"
)

print(response)
