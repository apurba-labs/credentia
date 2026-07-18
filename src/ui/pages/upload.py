"""
Credentia Upload Page
"""

from __future__ import annotations

from pathlib import Path
from typing import BinaryIO

import streamlit as st


# ----------------------------------------------------
# Demo Documents
# ----------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

SAMPLES = ROOT / "samples"

MAX_FILE_SIZE = 25 * 1024 * 1024  # 25 MB


#POLICIES = {
#    "🏦 Accredited Investor": "accredited_investor",
#    "🪪 Identity Verification": "identity_verification",
#    "🏢 Employment Verification": "employment_verification",
#    "💰 Proof of Funds": "proof_of_funds",
#    "🌍 Residency Verification": "residency_verification",
#}

POLICIES = {
    "🏦 Accredited Investor": "accredited_investor",
}


# ----------------------------------------------------
# Helpers
# ----------------------------------------------------


def _load_demo(filename: str):

    file = SAMPLES / filename

    if file.exists():

        st.session_state["demo_file"] = file


# ----------------------------------------------------
# Upload UI
# ----------------------------------------------------


def render_upload() -> tuple[BinaryIO | None, str | None, bool]:

    st.subheader("📂 Financial Document")

    st.caption(
        "Upload a financial statement or use one of the built-in demo documents."
    )

    uploaded = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        help="Supported format: PDF",
    )

    if uploaded is not None:

        if uploaded.size > MAX_FILE_SIZE:

            st.error("Maximum file size is 25 MB.")

            st.stop()

        st.success(
            f"Loaded **{uploaded.name}** "
            f"({uploaded.size / 1024:.1f} KB)"
        )

    st.markdown("### OR")

    # ----------------------------------------------------
    # Demo Documents
    # ----------------------------------------------------

    st.markdown("### 🧪 Demo Financial Documents")
    st.write(
        "Explore common document types used for accredited investor verification.\n\n"
        "Each sample demonstrates how eligibility can be verified while minimizing "
        "disclosure of sensitive financial information."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("### 🏦 Bank Statement")
        st.caption("High Income Example")

        if st.button(
            "Use Demo",
            key="bank_demo",
            use_container_width=True,
        ):
            _load_demo("accredited_sample.pdf")
            st.success("✅ Bank Statement demo loaded.")
            
    with c2:
        st.markdown("### 📈 Brokerage Statement")
        st.caption("Investment Portfolio Example")

        if st.button(
            "Use Demo",
            key="brokerage_demo",
            use_container_width=True,
        ):
            _load_demo("accredited_sample.pdf")
            st.success("✅ Brokerage Statement demo loaded.")

    with c3:
        st.markdown("### 🧾 Tax Return")
        st.caption("Standard Income Filing")

        if st.button(
            "Use Demo",
            key="tax_demo",
            use_container_width=True,
        ):
            _load_demo("rejected_sample.pdf")
            st.success("✅ Tax Return demo loaded.")

    if "demo_file" in st.session_state:

        demo = st.session_state["demo_file"]

        st.success(f"Selected demo: **{demo.name}**")

        with open(demo, "rb") as fp:

            st.download_button(
                "⬇ Download Selected Demo",
                fp.read(),
                file_name=demo.name,
                mime="application/pdf",
                use_container_width=True,
            )

    st.divider()

    # ----------------------------------------------------
    # Policy
    # ----------------------------------------------------

    st.subheader("📋 Verification Policy")

    policy_name = st.selectbox(
        "Choose Verification Policy",
        options=list(POLICIES.keys()),
    )

    st.info("""
### 🚀 Platform Vision

Credentia is designed as a configurable privacy-preserving verification platform.

**Current Demo**
- 🏦 Accredited Investor Verification

**Future Verification Policies**
- 🪪 Identity Verification
- 🏢 Employment Verification
- 💰 Proof of Funds
- 🌍 Residency Verification
- 🎓 Education Verification
- 💼 Professional Certification

Each verification policy uses the same selective disclosure engine while protecting sensitive personal information.
""")

    st.divider()

    # ----------------------------------------------------
    # Verify
    # ----------------------------------------------------

    verify = st.button(
        "🛡 Verify Eligibility",
        type="primary",
        use_container_width=True,
    )

    # ----------------------------------------------------
    # Return Uploaded or Demo
    # ----------------------------------------------------

    if uploaded is not None:

        return (
            uploaded,
            POLICIES[policy_name],
            verify,
        )

    if "demo_file" in st.session_state:

        return (
            open(st.session_state["demo_file"], "rb"),
            POLICIES[policy_name],
            verify,
        )

    return (
        None,
        POLICIES[policy_name],
        verify,
    )