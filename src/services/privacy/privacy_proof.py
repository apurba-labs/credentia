from datetime import UTC, datetime
import hashlib
from uuid import uuid4

from src.models.proof import Proof
from src.models.verification import VerificationResult


class PrivacyProofService:
    """
    Generates a deterministic proof for a verification result.
    """

    def generate(
        self,
        verification_result: VerificationResult,
        policy: str,
    ) -> Proof:

        payload = (
            f"{uuid4()}"
            f"{verification_result.verified}"
            f"{policy}"
            f"{datetime.now(UTC).isoformat()}"
        )

        proof_hash = hashlib.sha256(
            payload.encode("utf-8")
        ).hexdigest()

        return Proof(
            proof_hash=proof_hash,
            policy=policy,
        )