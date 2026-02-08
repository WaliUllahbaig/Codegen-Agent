def plan(task: str) -> str:
    return f"""
You are a senior software architect.

Break the task into clear coding steps.

Task:
{task}

Return a numbered plan.
"""
