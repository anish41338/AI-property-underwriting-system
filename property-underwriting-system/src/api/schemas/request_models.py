from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime

class FileInfo(BaseModel):
    file_id: str
    file_path: str
    file_type: str  # 'document' or 'image'

class PropertyInfo(BaseModel):
    address: Optional[str] = None
    property_type: Optional[str] = None
    year_built: Optional[int] = None
    square_footage: Optional[float] = None
    lot_size: Optional[float] = None

class AnalysisRequest(BaseModel):
    files: List[FileInfo]
    property_info: Optional[PropertyInfo] = None
    analysis_type: str = Field(default="full", description="Type of analysis to perform")
    priority: str = Field(default="normal", description="Priority level")
    metadata: Optional[Dict[str, Any]] = None
