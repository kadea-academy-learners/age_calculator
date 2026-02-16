import re
import subprocess
import sys

def run_age_program(birth_year: int) -> str:
    user_input = f"{birth_year}\n"
    proc = subprocess.run(
        [sys.executable, "age_calculator.py"],
        input=user_input,
        text=True,
        capture_output=True
    )
    assert proc.returncode == 0, (
        "Le programme a crash.\n"
        f"STDERR:\n{proc.stderr}\n"
        f"STDOUT:\n{proc.stdout}"
    )
    return proc.stdout

def extract_current_year(output: str) -> int:
    m = re.search(r"Current\s*Year\s*:\s*(\d{4})", output, flags=re.IGNORECASE)
    assert m, f"Ligne 'Current Year:' introuvable.\nOUTPUT:\n{output}"
    return int(m.group(1))

def extract_age(output: str) -> int:
    m = re.search(r"approximately\s+(\d+)\s+years\s+old", output, flags=re.IGNORECASE)
    assert m, f"Phrase d'âge introuvable (\"approximately ... years old\").\nOUTPUT:\n{output}"
    return int(m.group(1))

def assert_minimum_format(output: str) -> None:
    assert "Enter your birth year:" in output, f"Prompt 'Enter your birth year:' manquant.\nOUTPUT:\n{output}"
    assert "Current Year:" in output, f"Ligne 'Current Year:' manquante.\nOUTPUT:\n{output}"
    assert "You are approximately" in output, f"Ligne 'You are approximately' manquante.\nOUTPUT:\n{output}"
