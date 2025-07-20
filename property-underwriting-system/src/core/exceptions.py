class UnderwritingException(Exception):
    """Base exception for underwriting system"""
    pass

class DocumentProcessingError(UnderwritingException):
    """Raised when document processing fails"""
    pass

class ImageAnalysisError(UnderwritingException):
    """Raised when image analysis fails"""
    pass

class RiskAssessmentError(UnderwritingException):
    """Raised when risk assessment fails"""
    pass

class RuleEngineError(UnderwritingException):
    """Raised when rule engine encounters errors"""
    pass

class ValidationError(UnderwritingException):
    """Raised when data validation fails"""
    pass
