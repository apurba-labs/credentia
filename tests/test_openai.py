from src.core.ai_client import AIClient
from src.core.config import get_settings
from src.providers.openai import OpenAIProvider
settings = get_settings()
client = AIClient()

assert client.model == settings.openai_model

provider = OpenAIProvider()

assert provider.client is not None
print("Model:", client.model)

print("Provider Model:", provider.client.model)