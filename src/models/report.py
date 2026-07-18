from pydantic import BaseModel
from .certificate import VerificationCertificate

class VerificationReport(BaseModel):
    certificate: VerificationCertificate
    extracted_income: float
    extracted_net_worth: float
    verification_reason: str