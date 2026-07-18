from datetime import UTC, datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class Proof(BaseModel):
    """
    Privacy-preserving verification proof.

    This model represents the cryptographic proof generated after
    a successful verification. In the MVP it is a SHA-256 hash.
    Later it can be replaced with a real Midnight proof.
    """

    proof_id: UUID = Field(
        default_factory=uuid4,
        description="Unique proof identifier.",
    )

    proof_hash: str = Field(
        ...,
        description="Cryptographic proof hash.",
    )

    policy: str = Field(
        ...,
        description="Verification policy used to generate the proof.",
    )

    issued_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC),
        description="Proof creation timestamp.",
    )