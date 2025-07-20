from typing import Dict, Any
from src.api.schemas.response_models import RiskAssessment

class RuleEngine:
    async def check_compliance(self, risk_assessment: RiskAssessment, document_results: Any, image_results: Any) -> Dict[str, Any]:
        """
        Mock rule compliance check based on risk level
        """
        compliant = risk_assessment.overall_risk_level in ["low", "medium"]
        return {
            "compliant": compliant,
            "issues": [] if compliant else ["Risk level too high"],
            "recommendations": ["Proceed with caution"] if not compliant else ["Standard underwriting"]
        }

    async def make_decision(self, risk_assessment: RiskAssessment, compliance_check: Dict[str, Any]) -> str:
        """
        Simple decision logic
        """
        if compliance_check["compliant"] and risk_assessment.overall_risk_level == "low":
            return "APPROVED"
        elif risk_assessment.overall_risk_level == "medium":
            return "REVIEW_REQUIRED"
        else:
            return "DECLINED"
