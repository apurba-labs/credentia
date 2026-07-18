"""
Credentia UI Components
"""

from __future__ import annotations

from datetime import datetime
import json

import streamlit as st


# -----------------------------------------------------
# Progress Animation
# -----------------------------------------------------


def verification_progress() -> None:
    """
    Display an animated verification workflow.
    """

    progress = st.progress(0)
    status = st.empty()

    steps = [
        ("🔍 Reading financial document...", 20),
        ("🧠 Extracting eligibility claims...", 40),
        ("⚖ Evaluating verification policy...", 60),
        ("🔒 Creating privacy-preserving proof...", 80),
        ("📜 Issuing verification certificate...", 100),
    ]

    for message, value in steps:
        status.info(message)
        progress.progress(value)

    status.success("✅ Verification completed successfully.")


# -----------------------------------------------------
# Status Badge
# -----------------------------------------------------


def verification_banner(result: dict) -> None:

    verification = result["verification"]

    if verification["verified"]:

        st.success(
            """
### ✅ Eligibility Successfully Verified

A privacy-preserving verification certificate has been generated.

Only the verification result is intended to be shared.

Sensitive financial information remains protected.
"""
        )

    else:

        st.error(
            """
### ❌ Verification Failed

The supplied document does not satisfy the selected policy.
"""
        )


# -----------------------------------------------------
# Certificate Card
# -----------------------------------------------------


def certificate_card(certificate: dict) -> None:

    st.subheader("📜 Verification Certificate")

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "Status",
            certificate["status"],
        )

    with c2:
        st.metric(
            "Issued",
            certificate["issued_at"][:10],
        )

    st.markdown("##### Certificate ID")

    st.code(
        certificate["certificate_id"],
        language="text",
    )

    st.markdown("##### Proof ID")

    st.code(
        certificate["proof_id"],
        language="text",
    )

    st.info(certificate["summary"])


# -----------------------------------------------------
# Report Download
# -----------------------------------------------------


def download_report(result: dict) -> None:

    verification = result["verification"]
    certificate = result["certificate"]
    report = result["report"]

    text = f"""
Credentia Verification Report

Generated:
{datetime.utcnow().isoformat()} UTC

--------------------------------------------

Verification

Status:
{"VERIFIED" if verification["verified"] else "FAILED"}

Policy:
{verification["policy"]}

Confidence:
{verification["confidence"]:.2%}

--------------------------------------------

Eligibility Report

Document Type:
{report["document_type"]}

Annual Income:
${report["income"]:,.0f}

Net Worth:
${report["net_worth"]:,.0f}

Evaluation:
{report["evaluation"]}

--------------------------------------------

Certificate

Certificate ID:
{certificate["certificate_id"]}

Proof ID:
{certificate["proof_id"]}

Status:
{certificate["status"]}

--------------------------------------------

Built for the Midnight Network Hackathon

Privacy-Preserving Eligibility Verification

AI-assisted verification using Qwen

Open Source by Gotihub
"""

    st.download_button(
        "⬇ Download Verification Report",
        data=text,
        file_name="credentia_verification_report.txt",
        mime="text/plain",
        use_container_width=True,
    )

    st.download_button(
        "⬇ Download JSON",
        data=json.dumps(result, indent=2),
        file_name="credentia_verification.json",
        mime="application/json",
        use_container_width=True,
    )


# -----------------------------------------------------
# Footer
# -----------------------------------------------------


def footer() -> None:

    st.divider()

    st.markdown(
        """
<div style="
text-align:center;
padding:20px;
color:#6b7280;
font-size:14px;
line-height:1.8;
">

<b>🛡 Credentia v1.0</b><br>

Privacy-Preserving Eligibility Verification<br><br>

Built for the <b>Midnight Network Hackathon</b><br>

AI-assisted verification using <b>Qwen</b><br>

Open Source by <b>Gotihub</b><br><br>

© 2026 Gotihub

</div>
""",
        unsafe_allow_html=True,
    )


# -----------------------------------------------------
# API Error
# -----------------------------------------------------


def api_error(message: str) -> None:

    st.error(message)