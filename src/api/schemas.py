from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class VerificationSummarySchema(BaseModel):
    verified: bool
    policy: str
    confidence: float
    reason: str


class CertificateSchema(BaseModel):
    certificate_id: UUID
    proof_id: UUID
    status: str
    issued_at: datetime
    summary: str


class ReportSchema(BaseModel):
    document_type: str
    income: float
    net_worth: float
    evaluation: str

class IntelligenceSchema(BaseModel):
    executive_summary: str
    reasoning: str
    evidence_summary: str
    confidence_explanation: str
    recommendations: list[str]
    limitations: list[str]
    
class VerificationResponseSchema(BaseModel):
    verification: VerificationSummarySchema
    certificate: CertificateSchema
    report: ReportSchema
    intelligence: IntelligenceSchema | None = None