import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


def run_cli(stdin_text: str) -> str:
    result = subprocess.run(
        [sys.executable, "-m", "tetris_engine"],
        input=stdin_text,
        capture_output=True,
        text=True,
        cwd=REPO_ROOT,
        env={"PYTHONPATH": str(REPO_ROOT / "src")},
        check=True,
    )
    return result.stdout


def test_cli_reads_stdin_and_writes_stdout():
    output = run_cli("Q0\nI0,I4,Q8\n")
    assert output == "2\n1\n"


def test_cli_skips_blank_lines():
    output = run_cli("Q0\n\nQ0,Q1\n")
    assert output == "2\n4\n"
