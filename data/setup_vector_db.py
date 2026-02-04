import chromadb

def init_db():
    client = chromadb.PersistentClient(path="./data/sre_knowledge")
    # Delete if exists to start fresh for demo
    try: client.delete_collection("runbooks")
    except: pass
    
    collection = client.create_collection(name="runbooks")

    collection.add(
        documents=[
            "Error: DB_CONN_LIMIT. Action: Call /fix-pool. Root Cause: Unclosed SQL cursors.",
            "Error: AUTH_TIMEOUT. Action: Call /refresh-keys. Root Cause: Vault token expired.",
            "Error: DISK_FULL. Action: Call /clear-logs. Root Cause: Log rotation failure."
        ],
        ids=["id1", "id2", "id3"],
        metadatas=[{"impact": "high"}, {"impact": "medium"}, {"impact": "low"}]
    )
    print("VectorDB Initialized with SRE Runbooks.")

if __name__ == "__main__":
    init_db()