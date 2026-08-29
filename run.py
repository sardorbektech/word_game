"""Application Runner."""
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8000"))
    is_dev = os.getenv("ENV", "production").lower() == "development"
    print(f"==================================================")
    print(f"  Adaptive English Sentence Reconstruction Game   ")
    print(f"  Running at: http://{host}:{port}                ")
    print(f"==================================================")
    uvicorn.run("backend.main:app", host=host, port=port, reload=is_dev)
