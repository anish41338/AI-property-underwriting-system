from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Optional
from src.services.underwriting_service import UnderwritingService
from src.api.schemas.request_models import AnalysisRequest
from src.api.schemas.response_models import AnalysisResponse

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_property(
    request: AnalysisRequest,
    underwriting_service: UnderwritingService = Depends()
):
    """Analyze uploaded documents and images for risk assessment"""
    try:
        result = await underwriting_service.process_analysis(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/analysis/{analysis_id}")
async def get_analysis_status(
    analysis_id: str,
    underwriting_service: UnderwritingService = Depends()
):
    """Get the status of an ongoing analysis"""
    try:
        status = await underwriting_service.get_analysis_status(analysis_id)
        if not status:
            raise HTTPException(status_code=404, detail="Analysis not found")
        return status
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
