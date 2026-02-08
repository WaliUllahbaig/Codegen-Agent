import subprocess
from .base import BaseLLM

class OllamaLLM(BaseLLM):

    def __init__(self, model: str):
        self.model = model

    def generate(self, prompt: str) -> str:
        result = subprocess.run(
            ["ollama", "run", self.model],
            input=prompt,
            text=True,
            capture_output=True
        )
        return result.stdout.strip()
