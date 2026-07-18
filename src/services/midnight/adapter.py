"""
Midnight Privacy Adapter

This adapter encapsulates the privacy proof generation layer used by
Credentia.

For the hackathon submission, it produces a deterministic proof
commitment that represents the output of a privacy-preserving
verification workflow.

The adapter is intentionally isolated so it can later be replaced by
a native Midnight implementation without changing application logic.
"""

from __future__ import annotations

import hashlib
from datetime import datetime, timezone

from src.models.proof import Proof


class MidnightNetworkAdapter:
    """
    Adapter responsible for generating a deterministic proof commitment.

    Current implementation:
        • Demonstration / Simulation

    Future implementation:
        • Native Midnight proof generation
    """

    def __init__(self) -> None:
        self.provider = "MIDNIGHT_SIMULATION"

    def generate_proof_commitment(
        self,
        *,
        policy: str,
        statement_hash: str,
    ) -> Proof:
        """
        Generate a deterministic proof commitment.

        Args:
            policy:
                Verification policy identifier.

            statement_hash:
                SHA-256 fingerprint of the verification payload.

        Returns:
            Proof model.
        """

        payload = f"{policy}:{statement_hash}"

        proof_hash = (
            "0x"
            + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]
        )

        return Proof(
            proof_hash=proof_hash,
            policy=policy,
            issued_at=datetime.now(timezone.utc),
        )