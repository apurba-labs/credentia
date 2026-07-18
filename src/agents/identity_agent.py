from src.services.verification.rules import VerificationRules


class IdentityAgent:
    """
    Extract structured financial information from parsed documents.
    """

    def extract(self, document: dict) -> dict:

        text = document["text"]

        income = VerificationRules.extract_income(text)
        net_worth = VerificationRules.extract_net_worth(text)

        return {
            "income": income,
            "net_worth": net_worth,
            "document_type": "financial_document",
            "confidence": 0.95,
        }