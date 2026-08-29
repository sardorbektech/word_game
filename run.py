"""Application Runner optimized for 0.1 CPU & 512MB RAM."""
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
    print(f"  Profile: Light Cloud (0.1 CPU / 512MB RAM)      ")
    print(f"==================================================")
    
    uvicorn.run(
        "backend.main:app",
        host=host,
        port=port,
        reload=is_dev,
        workers=1,
        access_log=is_dev,
        timeout_keep_alive=30,
        limit_concurrency=100
    )
