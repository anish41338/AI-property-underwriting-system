import asyncio
from typing import List, Dict, Any
import uuid
from datetime import datetime
from src.api.schemas.request_models import AnalysisRequest
from src.api.schemas.response_models import AnalysisResponse
from src.models.document_analysis.text_extractor import TextExtractor
from src.models.computer_vision.property_detector import PropertyDetector
from src.models.risk_assessment.risk_calculator import RiskCalculator
from src.rules.rule_engine import RuleEngine
from src.utils.cache import memory_cache  # Use our simple cache

class UnderwritingService:
    def __init__(self):
        self.text_extractor = TextExtractor()
        self.property_detector = PropertyDetector()
        self.risk_calculator = RiskCalculator()
        self.rule_engine = RuleEngine()
        # No need for Redis client - using memory cache instead
    
    async def process_analysis(self, request: AnalysisRequest) -> AnalysisResponse:
        """Process complete underwriting analysis"""
        analysis_id = str(uuid.uuid4())
        
        try:
            # Store analysis status in memory cache
            memory_cache.set(f"analysis_{analysis_id}", {
                "status": "processing",
                "created_at": datetime.now().isoformat()
            })
            
            # ... rest of your analysis code remains the same ...
            
            # Process documents
            document_results = []
            for file_info in request.files:
                if file_info.file_type == "document":
                    doc_result = await self.text_extractor.extract_and_analyze(
                        file_info.file_path
                    )
                    document_results.append(doc_result)
            
            # Process images
            image_results = []
            for file_info in request.files:
                if file_info.file_type == "image":
                    img_result = await self.property_detector.analyze_image(
                        file_info.file_path
                    )
                    image_results.append(img_result)
            
            # Calculate risk assessment
            risk_assessment = await self.risk_calculator.calculate_risk(
                document_results, image_results, request.property_info
            )
            
            # Apply business rules
            compliance_check = await self.rule_engine.check_compliance(
                risk_assessment, document_results, image_results
            )
            
            # Generate final decision
            decision = await self.rule_engine.make_decision(
                risk_assessment, compliance_check
            )
            
            # Create response
            response = AnalysisResponse(
                analysis_id=analysis_id,
                status="completed",
                created_at=datetime.fromisoformat(memory_cache.get(f"analysis_{analysis_id}")["created_at"]),
                completed_at=datetime.now(),
                document_analysis=document_results,
                image_analysis=image_results,
                risk_assessment=risk_assessment,
                compliance_check=compliance_check,
                decision=decision
            )
            
            # Update cache with completed status
            memory_cache.set(f"analysis_{analysis_id}", {
                "status": "completed",
                "created_at": memory_cache.get(f"analysis_{analysis_id}")["created_at"],
                "completed_at": datetime.now().isoformat(),
                "result": response.dict()
            })
            
            return response
            
        except Exception as e:
            # Update cache with error status
            memory_cache.set(f"analysis_{analysis_id}", {
                "status": "failed",
                "error": str(e),
                "created_at": memory_cache.get(f"analysis_{analysis_id}")["created_at"]
            })
            raise e
    
    async def get_analysis_status(self, analysis_id: str) -> Dict[str, Any]:
        """Get the current status of an analysis"""
        analysis_data = memory_cache.get(f"analysis_{analysis_id}")
        
        if not analysis_data:
            return None
        
        return {
            "analysis_id": analysis_id,
            "status": analysis_data["status"],
            "created_at": analysis_data["created_at"]
        }
