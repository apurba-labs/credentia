from enum import Enum


class VerificationPolicy(str, Enum):
    """
    Supported verification policies.
    """

    ACCREDITED_INVESTOR = "accredited_investor"

    # Future policies
    KYC = "kyc"
    AML = "aml"
    QUALIFIED_PURCHASER = "qualified_purchaser"