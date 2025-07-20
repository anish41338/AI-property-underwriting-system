import pytesseract
from PIL import Image
import PyPDF2
from pathlib import Path
from typing import Dict, Any
import spacy
from src.api.schemas.response_models import DocumentAnalysisResult

class TextExtractor:
    def __init__(self):
        # Load spaCy model for NER
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except IOError:
            print("Please install spaCy English model: python -m spacy download en_core_web_sm")
            self.nlp = None
    
    async def extract_and_analyze(self, file_path: str) -> DocumentAnalysisResult:
        """Extract text from document and perform analysis"""
        file_path = Path(file_path)
        
        if file_path.suffix.lower() == '.pdf':
            text = self._extract_from_pdf(file_path)
        elif file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.tiff']:
            text = self._extract_from_image(file_path)
        else:
            raise ValueError(f"Unsupported file type: {file_path.suffix}")
        
        # Classify document type
        doc_type = self._classify_document(text)
        
        # Extract key entities
        entities = self._extract_entities(text)
        
        # Calculate confidence score
        confidence = self._calculate_confidence(text, entities)
        
        return DocumentAnalysisResult(
            document_type=doc_type,
            extracted_text=text[:1000],  # Truncate for response
            key_entities=entities,
            confidence_score=confidence
        )
    
    def _extract_from_pdf(self, file_path: Path) -> str:
        """Extract text from PDF file"""
        text = ""
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
        return text
    
    def _extract_from_image(self, file_path: Path) -> str:
        """Extract text from image using OCR"""
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text
    
    def _classify_document(self, text: str) -> str:
        """Classify the type of document based on content"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ['appraisal', 'market value', 'comparable']):
            return 'appraisal_report'
        elif any(word in text_lower for word in ['inspection', 'condition', 'structural']):
            return 'inspection_report'
        elif any(word in text_lower for word in ['insurance', 'policy', 'coverage']):
            return 'insurance_document'
        else:
            return 'unknown'
    
    def _extract_entities(self, text: str) -> Dict[str, Any]:
        """Extract key entities from text using NER"""
        if not self.nlp:
            return {}
        
        doc = self.nlp(text)
        entities = {}
        
        for ent in doc.ents:
            if ent.label_ in ['MONEY', 'DATE', 'PERSON', 'ORG', 'GPE']:
                if ent.label_ not in entities:
                    entities[ent.label_] = []
                entities[ent.label_].append(ent.text)
        
        return entities
    
    def _calculate_confidence(self, text: str, entities: Dict[str, Any]) -> float:
        """Calculate confidence score based on text quality and entities found"""
        base_score = 0.5
        
        # Increase score based on text length
        if len(text) > 100:
            base_score += 0.2
        
        # Increase score based on entities found
        if entities:
            base_score += min(len(entities) * 0.1, 0.3)
        
        return min(base_score, 1.0)
