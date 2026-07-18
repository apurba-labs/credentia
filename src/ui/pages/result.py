"""
Credentia Result Page
"""

from __future__ import annotations

import streamlit as st

from src.ui.components import (
    certificate_card,
    download_report,
    verification_banner,
)


def render_result(result: dict) -> None:
    """
    Render verification results.
    """

    verification = result["verification"]
    report = result["report"]
    certificate = result["certificate"]

    st.divider()

    # ----------------------------------------------------
    # Success Banner
    # ----------------------------------------------------

    verification_banner(result)

    st.divider()

    # ----------------------------------------------------
    # Verification Summary
    # ----------------------------------------------------

    st.subheader("📊 Verification Summary")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Status",
            "✅ VERIFIED"
            if verification["verified"]
            else "❌ FAILED",
        )

    with c2:

        st.metric(
            "Confidence",
            f"{verification['confidence']:.0%}",
        )

    with c3:

        st.metric(
            "Policy",
            verification["policy"].replace(
                "_",
                " ",
            ).title(),
        )

    st.info(verification["reason"])

    # ----------------------------------------------------
    # Certificate
    # ----------------------------------------------------

    st.divider()

    certificate_card(certificate)

    # ----------------------------------------------------
    # Eligibility Report
    # ----------------------------------------------------

    st.divider()

    st.subheader("📈 Eligibility Report")

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Annual Income",
            f"${report['income']:,.0f}",
        )

    with c2:

        st.metric(
            "Net Worth",
            f"${report['net_worth']:,.0f}",
        )

    c1, c2 = st.columns(2)

    with c1:

        st.metric(
            "Evaluation",
            report["evaluation"],
        )

    with c2:

        st.metric(
            "Document",
            report["document_type"].replace(
                "_",
                " ",
            ).title(),
        )

    st.success(
        """
### 🔒 Selective Disclosure

Only the verification outcome is intended to be shared.

The underlying financial document remains private,
aligning with Midnight's privacy-first philosophy.
"""
    )

    # ----------------------------------------------------
    # Downloads
    # ----------------------------------------------------

    st.divider()

    st.subheader("📥 Export")

    download_report(result)