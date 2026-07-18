"""
Verification Orchestrator

Coordinates the complete verification workflow without containing
business logic. Each responsibility is delegated to a dedicated
agent or service.
"""

from src.agents.identity_agent import IdentityAgent
from src.agents.eligibility_agent import EligibilityAgent
from src.agents.certificate_agent import CertificateAgent

from src.services.privacy.privacy_proof import PrivacyProofService

from src.models.verification import (
    VerificationRequest,
    VerificationResult,
)
from src.models.certificate import VerificationCertificate


class VerificationOrchestrator:
    """
    Coordinates the end-to-end verification workflow.
    """

    def __init__(self) -> None:
        self.identity_agent = IdentityAgent()
        self.eligibility_agent = EligibilityAgent()
        self.privacy_service = PrivacyProofService()
        self.certificate_agent = CertificateAgent()

    def verify(self, request: VerificationRequest) -> tuple[VerificationResult, VerificationCertificate]:

        identity = self.identity_agent.extract(request)

        result = self.eligibility_agent.verify(
            identity=identity,
            policy=request.verification_policy,
        )

        proof = self.privacy_service.generate(
            verification_result=result,
            policy=request.verification_policy,
        )

        certificate = self.certificate_agent.issue(
            verification_result=result,
            proof=proof,
        )

        result.proof_id = proof.proof_id

        return result, certificate