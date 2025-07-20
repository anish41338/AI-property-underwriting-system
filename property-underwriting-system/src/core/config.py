from pydantic_settings import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://localhost:5432/underwriting_db"
    
    # Redis - REMOVED
    # redis_url: str = "redis://localhost:6379"
    
    # Security
    secret_key: str = "your-secret-key-change-this"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # File handling
    upload_dir: str = "./uploads"
    max_file_size: int = 50 * 1024 * 1024  # 50MB
    
    # Model paths
    model_path: str = "./data/models/trained_models"
    tesseract_path: Optional[str] = None
    
    # API Keys
    ocr_api_key: Optional[str] = None
    vision_api_key: Optional[str] = None
    
    class Config:
        env_file = ".env"

settings = Settings()
