from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.api.routes import upload, analysis, results
from src.core.config import Settings
from src.core.logging_config import setup_logging

# Initialize settings and logging
settings = Settings()
setup_logging()

# Create FastAPI app
app = FastAPI(
    title="AI Property Underwriting System",
    description="Automated property risk assessment using AI",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(upload.router, prefix="/api/v1", tags=["Upload"])
app.include_router(analysis.router, prefix="/api/v1", tags=["Analysis"])
app.include_router(results.router, prefix="/api/v1", tags=["Results"])

@app.get("/")
async def root():
    return {"message": "AI Property Underwriting System API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
