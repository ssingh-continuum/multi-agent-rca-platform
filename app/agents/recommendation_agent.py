import ollama


class RecommendationAgent:

    def generate(self, rca):

        prompt = f"""
        Based on this RCA:

        {rca}

        Create:

        Immediate Actions
        Long Term Fixes
        Risk Level
        """

        response = ollama.chat(
            model="qwen3:8b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
