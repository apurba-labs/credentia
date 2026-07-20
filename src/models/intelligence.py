from pydantic import BaseModel, Field

class VerificationIntelligence(BaseModel):
    executive_summary: str = Field(...)
    reasoning: str = Field(...)
    evidence_summary: str = Field(...)
    confidence_explanation: str = Field(...)

    recommendations: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)