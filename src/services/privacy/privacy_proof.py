"""
Privacy Proof Service

Transforms an eligibility verification result into a
privacy-preserving proof commitment.

The generated commitment intentionally contains no sensitive financial
information and can later be backed by a native Midnight
implementation through the adapter layer.
"""

from __future__ import annotations

import hashlib

from src.models.proof import Proof
from src.models.verification import VerificationResult

from src.services.midnight.adapter import MidnightNetworkAdapter


class PrivacyProofService:
    """
    Creates privacy-preserving proof commitments.
    """

    def __init__(self) -> None:
        self.adapter = MidnightNetworkAdapter()

    def generate(
        self,
        verification_result: VerificationResult,
        policy: str,
    ) -> Proof:
        """
        Create a proof commitment from the verification outcome.
        """

        #
        # Build a minimal verification payload.
        #
        # Only verification claims are included.
        # No original financial values are stored.
        #

        payload = "|".join(
            [
                policy,
                "eligible"
                if verification_result.verified
                else "not_eligible",
                f"{verification_result.confidence:.4f}",
            ]
        )

        statement_hash = hashlib.sha256(
            payload.encode("utf-8")
        ).hexdigest()

        return self.adapter.generate_proof_commitment(
            policy=policy,
            statement_hash=statement_hash,
        )