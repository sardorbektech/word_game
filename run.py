"""Application Runner."""
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))
    print(f"==================================================")
    print(f"  Adaptive English Sentence Reconstruction Game   ")
    print(f"  Running at: http://{host}:{port}                ")
    print(f"==================================================")
    uvicorn.run("backend.main:app", host=host, port=port, reload=True)
