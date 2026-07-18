from datetime import UTC, datetime
from uuid import uuid4
from src.models.certificate import VerificationCertificate
from src.models.proof import Proof
from src.models.verification import VerificationResult

class CertificateAgent:
    """
    Issues a verification certificate.
    """
    def issue(
        self,
        verification_result: VerificationResult,
        proof: Proof,
    ) -> VerificationCertificate:

        status = "ISSUED" if verification_result.verified else "REJECTED"

        summary = summary = verification_result.reason

        return VerificationCertificate(
            certificate_id=uuid4(),
            proof_id=proof.proof_id,
            policy=proof.policy,
            verified=verification_result.verified,
            status=status,
            confidence=verification_result.confidence,
            summary=summary,
            issued_at=datetime.now(UTC),
        )