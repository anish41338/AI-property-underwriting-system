from typing import List, Dict, Any
from src.api.schemas.response_models import RiskAssessment, RiskLevel

class RiskCalculator:
    async def calculate_risk(self, document_results: List, image_results: List, property_info: Any) -> RiskAssessment:
        """Simple risk model based on basic info"""

        score = 0.5

        if document_results:
            score += 0.15
        
        if image_results:
            score += 0.15

        if property_info:
            if property_info.property_type == "old" or (property_info.year_built and property_info.year_built < 1980):
                score += 0.10
        
        score = min(score, 1.0)  # cap max score

        if score < 0.4:
            level = RiskLevel.LOW
        elif score < 0.7:
            level = RiskLevel.MEDIUM
        elif score < 0.9:
            level = RiskLevel.HIGH
        else:
            level = RiskLevel.CRITICAL

        return RiskAssessment(
            overall_risk_level=level,
            risk_score=score,
            risk_factors=[
                {"factor": "DOC_PRESENT", "weight": len(document_results)},
                {"factor": "IMG_PRESENT", "weight": len(image_results)},
            ],
            recommendations=["Review for manual override" if level != RiskLevel.LOW else "Auto-approve"]
        )
