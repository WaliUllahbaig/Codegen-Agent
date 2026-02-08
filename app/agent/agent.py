from app.agent.executor import execute_code
from app.agent.fixer import fix_code

class CodeAgent:

    def __init__(self, llm, retriever):
        self.llm = llm
        self.retriever = retriever

    def run(self, task: str):
        context = self.retriever.retrieve(task)

        prompt = f"""
You are a senior engineer.

Relevant code:
{context}

Task:
{task}

Write correct, production-quality code.
"""
        code = self.llm.generate(prompt)

        success, error = execute_code(code)

        if not success:
            code = fix_code(self.llm, code, error)

        return code
