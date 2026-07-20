"""
Verification Orchestrator

Coordinates the complete verification workflow without containing
business logic. Each responsibility is delegated to a dedicated
agent or service.
"""

from src.agents.identity_agent import IdentityAgent
from src.agents.eligibility_agent import EligibilityAgent
from src.agents.certificate_agent import CertificateAgent
from src.agents.verification_intelligence_agent import VerificationIntelligenceAgent

from src.services.privacy.privacy_proof import PrivacyProofService

from src.models.verification import (
    VerificationRequest,
    VerificationResponse,
)

class VerificationOrchestrator:
    """
    Coordinates the end-to-end verification workflow.
    """

    def __init__(self) -> None:
        self.identity_agent = IdentityAgent()
        self.eligibility_agent = EligibilityAgent()
        self.privacy_service = PrivacyProofService()
        self.certificate_agent = CertificateAgent()
        self.intelligence_agent = VerificationIntelligenceAgent()

    def verify(
        self,
        request: VerificationRequest,
        document: dict,
    ) -> VerificationResponse:

        # Extract financial information from parsed document
        identity = self.identity_agent.extract(document)

        # Evaluate eligibility
        result = self.eligibility_agent.verify(
            identity=identity,
            policy=request.verification_policy,
        )

        # Generate privacy proof
        proof = self.privacy_service.generate(
            verification_result=result,
            policy=request.verification_policy,
        )

        # Issue certificate
        certificate = self.certificate_agent.issue(
            verification_result=result,
            proof=proof,
        )
        
        payload = {
            "verification_result": result.model_dump(),
            "identity": identity,
            "certificate": certificate.model_dump(),
            "proof": proof.model_dump(),
        }
        
        try:
            intelligence = self.intelligence_agent.generate(payload)
        except Exception:
            intelligence = None
            
        result.proof_id = proof.proof_id

        return VerificationResponse(
            result=result,
            certificate=certificate,
            identity=identity,
            intelligence=intelligence,
        )