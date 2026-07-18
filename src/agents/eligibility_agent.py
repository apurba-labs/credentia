from src.models.verification import VerificationResult
from src.services.verification.rules import VerificationRules


class EligibilityAgent:

    def verify(
        self,
        identity: dict,
        policy: str,
    ) -> VerificationResult:

        if policy != "accredited_investor":
            return VerificationResult(
                verified=False,
                reason=f"Unsupported verification policy: {policy}",
                confidence=1.0,
            )

        verified = VerificationRules.is_accredited(
            income=identity["income"],
            net_worth=identity["net_worth"],
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