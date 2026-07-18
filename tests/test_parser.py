from src.services.parser.asset_parser import AssetParser

def test_parser_extracts_text():
    parser = AssetParser()

    document = parser.parse(
        "samples/accredited_sample.pdf"
    )

    assert len(document["text"]) > 0