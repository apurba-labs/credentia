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

        summary = (
            "Verification policy satisfied."
            if verification_result.verified
            else "Verification policy not satisfied."
        )

        return VerificationCertificate(
            status=status,
            proof=proof,
            summary=summary,
        )