from src.models.report import VerificationReport

class ReportService:

    def build(
        self,
        certificate,
        income,
        net_worth,
        reason,
    ) -> VerificationReport:

        return VerificationReport(
            certificate=certificate,
            extracted_income=income,
            extracted_net_worth=net_worth,
            verification_reason=reason,
        )