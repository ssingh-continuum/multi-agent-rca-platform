import ollama
import time

class RCAAgent:

    def analyze(
        self,
        incident,
        logs,
        metrics,
        history
    ):

        print("Starting RCA analysis...")

        start = time.time()

        prompt = f"""
        Incident:
        {incident}

        Logs:
        {logs}

        Metrics:
        {metrics}

        History:
        {history}

        Provide:
        1. Root Cause
        2. Evidence
        3. Recommendation
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

        print(
            f"RCA completed in {time.time()-start:.2f} seconds"
        )

        return response["message"]["content"]