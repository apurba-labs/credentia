from pathlib import Path

import fitz
import pdfplumber


class AssetParser:
    """
    Parse supported financial documents.
    """

    def parse(self, file_path: str) -> dict:

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        extracted_text = ""

        try:

            with pdfplumber.open(path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        extracted_text += page_text + "\n"

        except Exception:

            document = fitz.open(path)

            for page in document:
                extracted_text += page.get_text()

            document.close()

        return {
            "filename": path.name,
            "text": extracted_text.strip(),
        }