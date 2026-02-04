import requests
import chromadb
from langchain_core.tools import tool

@tool
def search_runbook(error_code: str):
    """Searches the VectorDB for specific remediation steps for an error code."""
    client = chromadb.PersistentClient(path="./data/sre_knowledge")
    collection = client.get_collection(name="runbooks")
    results = collection.query(query_texts=[error_code], n_results=1)
    return results['documents'][0][0] if results['documents'] else "No runbook found."

@tool
def execute_remediation(action_path: str):
    """Executes a fix by calling the specific microservice endpoint."""
    # Logic to map action to the correct service port (Simple for demo)
    url = f"http://localhost:5001{action_path}"
    try:
        response = requests.get(url)
        return f"Remediation Result: {response.text}"
    except Exception as e:
        return f"Failed to execute fix: {str(e)}"