class InformalConnectorInterface:
    def load_data_source(self, path: str, file_name: str) -> str:
        """Load in the file for extracting text."""
        pass

    def connect(self, auth: dict) -> object:
        """Extract text from the currently loaded file."""
        return {}