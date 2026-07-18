"""
Credentia Streamlit UI
"""

from __future__ import annotations

import os
import sys
from urllib.parse import urljoin

import requests
import streamlit as st

sys.path.insert(
    0,
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../..",
        )
    ),
)

from src.core.config import get_settings
from src.ui.components import (
    footer,
    verification_progress,
)
from src.ui.pages.result import render_result
from src.ui.pages.upload import render_upload
from src.ui.theme import (
    configure_page,
    inject_theme,
    render_header,
)

settings = get_settings()

VERIFY_ENDPOINT = urljoin(
    settings.api_url,
    "/verify",
)

session = requests.Session()


# -------------------------------------------------------
# API
# -------------------------------------------------------


def verify_document(file, policy):

    files = {
        "file": (
            getattr(file, "name", "document.pdf"),
            file,
            "application/pdf",
        )
    }

    data = {
        "verification_policy": policy,
    }

    response = session.post(
        VERIFY_ENDPOINT,
        files=files,
        data=data,
        timeout=180,
    )

    response.raise_for_status()

    return response.json()


# -------------------------------------------------------
# Main
# -------------------------------------------------------


def main():

    configure_page()

    inject_theme()

    render_header()

    uploaded_file, policy, verify = render_upload()

    if verify:

        if uploaded_file is None:

            st.warning(
                "Please upload or select a demo document."
            )

            st.stop()

        try:

            verification_progress()

            result = verify_document(
                uploaded_file,
                policy,
            )

            st.session_state["result"] = result

        except requests.HTTPError as exc:

            try:

                detail = exc.response.json()["detail"]

            except Exception:

                detail = str(exc)

            st.error(detail)

            st.stop()

        except Exception as exc:

            st.error(str(exc))

            st.stop()

    # -------------------------------------------------------

    if "result" in st.session_state:

        render_result(
            st.session_state["result"]
        )

    footer()


if __name__ == "__main__":

    main()