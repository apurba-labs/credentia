from src.agents.identity_agent import IdentityAgent

def test_extract_identity():
    agent = IdentityAgent()
    document = {
        "text": """
        Annual Income: $285,000
        Net Worth: $1,850,000
        """
    }
    identity = agent.extract(document)
    assert identity["income"] == 285000
    assert identity["net_worth"] == 1850000

def test_document_type():
    agent = IdentityAgent()
    identity = agent.extract({"text": "Income: 285000 Net Worth: 1850000"})
    assert identity["document_type"] == "financial_document"