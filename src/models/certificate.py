from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class VerificationCertificate(BaseModel):
    certificate_id: UUID
    proof_id: UUID
    policy: str
    verified: bool
    status: str
    confidence: float
    summary: str
    issued_at: datetime