from src.models.verification import VerificationResult

class EligibilityAgent:
    """
    Applies business verification rules.
    """

    def verify(
        self,
        identity: dict,
        policy: str,
    ) -> VerificationResult:

        verified = (
            identity["income"] >= 200000
            or identity["net_worth"] >= 1000000
        )

        return VerificationResult(
            verified=verified,
            reason=(
                "Verification policy satisfied."
                if verified
                else "Verification policy not satisfied."
            ),
            confidence=0.99,
        )