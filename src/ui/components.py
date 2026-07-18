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

def how_it_works() -> None:
    """
    Explain the AI verification workflow and Midnight privacy model.
    """

    st.divider()

    st.markdown("## 🌙 How Credentia Works")

    st.caption(
        "Credentia combines AI-powered document understanding with Midnight's "
        "privacy-first philosophy to verify eligibility while minimizing "
        "disclosure of sensitive financial information."
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.info(
            """
### 📄 Document

Upload a

• Bank Statement

• Brokerage Statement

• Tax Return
"""
        )

    with c2:
        st.info(
            """
### 🤖 AI Agents

• Identity Extraction

• Eligibility Analysis

• Certificate Generation
"""
        )

    with c3:
        st.info(
            """
### 🌙 Privacy

• Selective Disclosure

• Minimal Data Sharing

• Privacy by Design
"""
        )

    with c4:
        st.success(
            """
### 📜 Result

Privacy-Preserving

Verification

Certificate
"""
        )

    st.success(
        """
### 🔐 Powered by Midnight

Instead of sharing an entire financial document, Credentia verifies eligibility
and produces a privacy-preserving verification certificate.

Organizations receive the verification outcome while sensitive financial
information remains protected.
"""
    )

    st.markdown("### 🤖 AI Verification Pipeline")

    a1, a2, a3 = st.columns(3)

    with a1:
        st.metric(
            "Identity Agent",
            "Extract",
            "Claims",
        )

    with a2:
        st.metric(
            "Eligibility Agent",
            "Verify",
            "Policy",
        )

    with a3:
        st.metric(
            "Certificate Agent",
            "Issue",
            "Proof",
        )

    st.caption(
        "Each specialized AI agent performs a single responsibility before "
        "issuing a privacy-preserving verification certificate."
    )

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