from uuid import UUID

from pydantic import BaseModel, Field


class VerificationRequestSchema(BaseModel):
    """
    API request payload for a verification operation.
    The uploaded document is handled separately by FastAPI UploadFile.
    """

    verification_policy: str = Field(
        ...,
        description="Verification policy to evaluate (e.g. accredited_investor)",
    )


class VerificationResponseSchema(BaseModel):
    """
    API response returned after verification completes.
    """

    verified: bool = Field(..., description="Verification outcome")
    reason: str = Field(..., description="Explanation of the verification decision")
    confidence: float = Field(..., description="Verification confidence score")

    proof_id: UUID = Field(..., description="Generated proof identifier")
    certificate_id: UUID = Field(..., description="Generated certificate identifier")

    status: str = Field(..., description="Certificate status")
    summary: str = Field(..., description="Human-readable verification summary")