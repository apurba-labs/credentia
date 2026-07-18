import re

class VerificationRules:
    """
    Business rules for financial document verification.
    """

    @staticmethod
    def _parse_amount(value: str) -> float:
        try:
            return float(value.replace(",", "").replace("$", "").strip())
        except ValueError:
            return 0.0

    @classmethod
    def extract_income(cls, text: str) -> float:
        patterns = [
            r"annual\s+income[:\s]*\$?\s*([\d,]+)",
            r"income[:\s]*\$?\s*([\d,]+)",
            r"salary[:\s]*\$?\s*([\d,]+)",
        ]

        text = text.lower()

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return cls._parse_amount(match.group(1))

        return 0.0

    @classmethod
    def extract_net_worth(cls, text: str) -> float:
        patterns = [
            r"net\s+worth[:\s]*\$?\s*([\d,]+)",
            r"total\s+assets[:\s]*\$?\s*([\d,]+)",
        ]

        text = text.lower()

        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return cls._parse_amount(match.group(1))

        return 0.0

    @staticmethod
    def is_accredited(
        income: float,
        net_worth: float,
    ) -> bool:
        return (
            income >= 200000
            or net_worth >= 1000000
        )