from prometheus_api_client import PrometheusConnect

class StatusCodeProcessor:

    pc = PrometheusConnect(url="http://localhost:9090", disable_ssl=True)
    def __init__(self):
        print("In Status code init")
    def process_status_code(self, full_file_name: str) -> dict:
        """Extract text from the currently loaded file."""
        return {}
