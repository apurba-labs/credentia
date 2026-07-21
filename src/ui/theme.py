"""
Credentia UI Theme
"""

from __future__ import annotations

import streamlit as st


def configure_page() -> None:

    st.set_page_config(
        page_title="Credentia",
        page_icon="🛡️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def inject_theme() -> None:

    st.markdown(
        """
<style>

/* ------------------------------------------------ */
/* Layout */
/* ------------------------------------------------ */

.block-container{

    max-width:1180px;

    padding-top:1.5rem;

    padding-bottom:2rem;

}

.main{

    padding-top:0rem;

}

/* ------------------------------------------------ */
/* Hide Streamlit */
/* ------------------------------------------------ */



footer{

    visibility:hidden;

}




/* ------------------------------------------------ */
/* Buttons */
/* ------------------------------------------------ */

.stButton > button{

    width:100%;

    height:48px;

    border-radius:12px;

    font-weight:600;

    border:none;

    transition:.25s;

}

.stButton > button:hover{

    transform:translateY(-2px);

    box-shadow:0 8px 18px rgba(0,0,0,.15);

}

/* ------------------------------------------------ */
/* Download */
/* ------------------------------------------------ */

.stDownloadButton > button{

    width:100%;

    height:46px;

    border-radius:12px;

    font-weight:600;

}

/* ------------------------------------------------ */
/* File uploader */
/* ------------------------------------------------ */

[data-testid="stFileUploader"]{

    border:2px dashed #d1d5db;

    border-radius:14px;

    padding:1rem;

}

/* ------------------------------------------------ */
/* Metrics */
/* ------------------------------------------------ */

div[data-testid="stMetric"]{

    border:1px solid #e5e7eb;

    border-radius:14px;

    padding:20px;

    background:white;

    box-shadow:0 2px 8px rgba(0,0,0,.05);

}

/* ------------------------------------------------ */
/* Code */
/* ------------------------------------------------ */

.stCodeBlock{

    border-radius:12px;

}

/* ------------------------------------------------ */
/* Alerts */
/* ------------------------------------------------ */

[data-testid="stAlert"]{

    border-radius:12px;

}

/* ------------------------------------------------ */
/* Divider */
/* ------------------------------------------------ */

hr{

    margin-top:2rem;

    margin-bottom:2rem;

}

/* ------------------------------------------------ */
/* Mobile */
/* ------------------------------------------------ */

@media (max-width:768px){

.block-container{

padding-left:1rem;

padding-right:1rem;

}

}

</style>
""",
        unsafe_allow_html=True,
    )


def render_header() -> None:

    st.title("🛡 Credentia")

    st.caption(
        "Privacy-Preserving Eligibility Verification"
    )

    st.markdown(
        """
Built for the **OpenAI Build Week 2026**

Powered by **OpenAI GPT-5.6**

"""
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.success("🤖 AI Agents")

    with c2:
        st.info("🌙 Midnight Network")

    with c3:
        st.warning("🔐 Selective Disclosure")

    st.info(
        """
### 🚀 Try Credentia in under 30 seconds

- Upload your financial document

- Or use one of the demo documents

- Verify eligibility

- Receive a privacy-preserving verification certificate

Only the verification result is intended to be shared. Sensitive financial information remains protected.
"""
    )

    st.divider()