def fix_code(llm, code: str, error: str) -> str:
    prompt = f"""
The following code has an error:

{code}

Error:
{error}

Fix the code. Return ONLY the corrected code.
"""
    return llm.generate(prompt)
