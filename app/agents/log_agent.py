class LogAgent:

    def analyze(self, incident: str):

        incident = incident.lower()

        if "500" in incident:
            return """
            Error detected:
            HTTP 500 Internal Server Error
            """

        return """
        No known error signature found.
        """
