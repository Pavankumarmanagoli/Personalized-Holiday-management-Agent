from dotenv import load_dotenv
import os

load_dotenv()

def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"{name} environment variable is required")
    return value


GROQ_API_KEY = _required_env("GROQ_API_KEY")
MODEL_NAME = _required_env("MODEL_NAME")
