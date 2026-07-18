from src.models.verification import VerificationRequest

class IdentityAgent:
    """
    Mock identity extraction.

    Later this will consume parsed PDF data.
    """

    def extract(self, request: VerificationRequest) -> dict:

        return {
            "document_type": request.document_type,
            "income": 250000,
            "net_worth": 1500000,
            "currency": "USD",
            "owner": "Demo User",
        }