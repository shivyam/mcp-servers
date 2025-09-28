from mcp.server.fastmcp import FastMCP
from openai import OpenAI
import tempfile
from dotenv import load_dotenv
import os

load_dotenv()
client=OpenAI()
VECTOR_STORE_NAME="MEMORIES"
mcp = FastMCP('Memories')


# Checks if a vector store with the given name exists, if not creates one
def get_or_create_vector_store():
    stores = client.vector_stores.list()
    for store in stores:
        if store.name == VECTOR_STORE_NAME:
            return store
    return client.vector_stores.create(name=VECTOR_STORE_NAME)

# Saves a memory
@mcp.tool()
def save_memory(memory: str):
    """Save a memory string to the vector store"""
    vector_store = get_or_create_vector_store()
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.txt') as f:
        f.write(memory)
        f.flush()
        client.vector_stores.files.upload_and_poll(vector_store_id=vector_store.id, file=open(f.name, 'rb'))

    return {"status": "saved", "message": "Vector store id: " + vector_store.id}

@mcp.tool()
def retrieve_memories(query: str):
    """Retrieve memories from the vector store"""
    vector_store = get_or_create_vector_store()
    results = client.vector_stores.search(vector_store_id=vector_store.id, query=query)
    content_texts = [content.text for item in results.data for content in item.content if content.type=='text']
    return {"results": content_texts}

if __name__ == "__main__":
    mcp.run()