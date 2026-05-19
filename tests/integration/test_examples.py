"""Smoke test: every example script under examples/ runs to completion."""

import subprocess
import sys
from pathlib import Path

import pytest

EXAMPLES = sorted(Path(__file__).resolve().parents[2].joinpath("examples").glob("*.py"))


def test_examples_directory_contains_at_least_one_script():
    # Arrange
    discovered = EXAMPLES

    # Act
    count = len(discovered)

    # Assert
    assert count > 0, "No example scripts found under examples/"


@pytest.mark.parametrize("example_path", EXAMPLES, ids=lambda p: p.name)
def test_example_script_runs_to_completion_successfully(example_path, tmp_path):
    # Arrange
    cmd = [sys.executable, str(example_path)]

    # Act
    result = subprocess.run(
        cmd,
        cwd=tmp_path,
        capture_output=True,
        text=True,
        timeout=120,
    )

    # Assert
    assert result.returncode == 0, (
        f"{example_path.name} failed:\n"
        f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    )
