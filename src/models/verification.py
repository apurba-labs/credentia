from datetime import UTC, datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class VerificationRequest(BaseModel):
    """
    Internal verification request passed through the orchestration pipeline.
    """

    id: UUID = Field(default_factory=uuid4)
    document_type: str = Field(..., description="Uploaded document classification.")
    verification_policy: str = Field(..., description="Verification policy to evaluate.")
    user_id: Optional[str] = Field(default=None, description="Optional user reference.")
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

class VerificationResult(BaseModel):
    """
    Result produced by the eligibility agent.
    """

    verified: bool
    reason: str
    confidence: float
    proof_id: Optional[UUID] = None