from src.agents.eligibility_agent import EligibilityAgent

def test_accredited_investor():
    agent = EligibilityAgent()

    identity = {
        "income": 300000,
        "net_worth": 2000000,
    }
    result = agent.verify(
        identity=identity,
        policy="accredited_investor",
    )
    assert result.verified is True

def test_rejected_investor():
    agent = EligibilityAgent()
    identity = {
        "income": 40000,
        "net_worth": 80000,
    }

    result = agent.verify(
        identity=identity,
        policy="accredited_investor",
    )
    assert result.verified is False