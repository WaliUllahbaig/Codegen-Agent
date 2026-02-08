import subprocess
import tempfile

def execute_code(code: str):
    with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as f:
        f.write(code.encode())

    result = subprocess.run(
        ["python", "-m", "py_compile", f.name],
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return False, result.stderr

    return True, None
