from fastapi import APIRouter

from src.api.schemas import (
    VerificationRequestSchema,
    VerificationResponseSchema,
)

from src.core.orchestrator import VerificationOrchestrator
from src.models.verification import VerificationRequest

router = APIRouter()

orchestrator = VerificationOrchestrator()


@router.get("/")
async def root():
    return {
        "application": "Credentia",
        "status": "running",
    }


@router.get("/health")
async def health():
    return {
        "status": "healthy",
    }


@router.post("/verify", response_model=VerificationResponseSchema)
async def verify(payload: VerificationRequestSchema):

    request = VerificationRequest(
        document_type="bank_statement",
        verification_policy=payload.verification_policy,
    )

    result, certificate = orchestrator.verify(request)

    return VerificationResponseSchema(
        verified=result.verified,
        reason=result.reason,
        confidence=result.confidence,
        proof_id=result.proof_id,
        certificate_id=certificate.certificate_id,
        status=certificate.status,
        summary=certificate.summary,
    )