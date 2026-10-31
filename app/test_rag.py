from agents.rag_agent import RagAgent

rag = RagAgent()

result = rag.retrieve(
    "Payment API returning HTTP 500 after deployment"
)

print(result)
