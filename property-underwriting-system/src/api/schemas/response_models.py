from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class DocumentAnalysisResult(BaseModel):
    document_type: str
    extracted_text: str
    key_entities: Dict[str, Any]
    confidence_score: float

class ImageAnalysisResult(BaseModel):
    image_path: str
    detected_objects: List[Dict[str, Any]]
    damage_assessment: Dict[str, Any]
    hazard_indicators: List[str]
    confidence_score: float

class RiskAssessment(BaseModel):
    overall_risk_level: RiskLevel
    risk_score: float
    risk_factors: List[Dict[str, Any]]
    recommendations: List[str]

class AnalysisResponse(BaseModel):
    analysis_id: str
    status: str
    created_at: datetime
    completed_at: Optional[datetime] = None
    document_analysis: List[DocumentAnalysisResult]
    image_analysis: List[ImageAnalysisResult]
    risk_assessment: RiskAssessment
    compliance_check: Dict[str, Any]
    decision: Optional[str] = None
