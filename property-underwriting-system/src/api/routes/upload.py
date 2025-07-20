from fastapi import APIRouter, File, UploadFile, HTTPException, Depends
from typing import List
import os
import uuid
from src.core.config import settings
from src.services.analysis_service import AnalysisService

router = APIRouter()

@router.post("/upload")
async def upload_files(
    files: List[UploadFile] = File(...),
    analysis_service: AnalysisService = Depends()
):
    """Upload documents and images for analysis"""
    try:
        uploaded_files = []
        
        # Create upload directory if it doesn't exist
        os.makedirs(settings.upload_dir, exist_ok=True)
        
        for file in files:
            # Validate file size
            if file.size > settings.max_file_size:
                raise HTTPException(
                    status_code=413, 
                    detail=f"File {file.filename} too large"
                )
            
            # Generate unique filename
            file_id = str(uuid.uuid4())
            file_extension = os.path.splitext(file.filename)[1]
            unique_filename = f"{file_id}{file_extension}"
            file_path = os.path.join(settings.upload_dir, unique_filename)
            
            # Save file
            with open(file_path, "wb") as buffer:
                content = await file.read()
                buffer.write(content)
            
            uploaded_files.append({
                "file_id": file_id,
                "original_name": file.filename,
                "file_path": file_path,
                "file_size": len(content),
                "content_type": file.content_type
            })
        
        return {
            "message": "Files uploaded successfully",
            "files": uploaded_files,
            "total_files": len(uploaded_files)
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
