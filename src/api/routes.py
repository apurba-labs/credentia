from __future__ import annotations

import os
import tempfile

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from src.api.schemas import VerificationResponseSchema
from src.core.orchestrator import VerificationOrchestrator
from src.models.verification import VerificationRequest
from src.services.parser.asset_parser import AssetParser
from src.models.policy import VerificationPolicy

router = APIRouter(tags=["Verification"])

parser = AssetParser()
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


@router.post(
    "/verify",
    response_model=VerificationResponseSchema,
)
async def verify(
    file: UploadFile = File(...),
    verification_policy: VerificationPolicy = Form(...),
):
    temp_file = None

    try:
        
        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are supported.",
            )
            
        suffix = os.path.splitext(file.filename)[1] or ".pdf"

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=suffix,
        ) as tmp:
            tmp.write(await file.read())
            temp_file = tmp.name

        # Parse uploaded document
        document = parser.parse(temp_file)

        # Build verification request
        request = VerificationRequest(
            verification_policy=verification_policy.value,
        )

        # Execute verification workflow
        result, certificate = orchestrator.verify(
            request=request,
            document=document,
        )

        return VerificationResponseSchema(
            verified=result.verified,
            reason=result.reason,
            confidence=result.confidence,
            proof_id=result.proof_id,
            certificate_id=certificate.certificate_id,
            status=certificate.status,
            summary=certificate.summary,
        )

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"Verification failed: {str(exc)}",
        )

    finally:
        if temp_file and os.path.exists(temp_file):
            os.remove(temp_file)