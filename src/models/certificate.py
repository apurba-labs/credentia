from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from src.models.proof import Proof

class VerificationCertificate(BaseModel):
    """
    Public verification certificate returned after a successful verification.
    """

    certificate_id: UUID = Field(default_factory=uuid4)

    status: str = Field(
        ...,
        description="Certificate status (ISSUED, REJECTED, REVOKED).",
    )

    proof: Proof

    summary: str = Field(
        ...,
        description="Human-readable verification summary.",
    )