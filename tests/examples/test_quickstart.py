"""PS303 example mirror stub: ensure examples/quickstart.py is syntactically valid."""

import subprocess
import sys
from pathlib import Path

EXAMPLE = Path(__file__).resolve().parents[2] / "examples" / "quickstart.py"


def test_quickstart_example_file_exists_on_disk():
    # Arrange
    expected_path = EXAMPLE

    # Act
    exists = expected_path.exists()

    # Assert
    assert exists, f"missing example: {expected_path}"


def test_quickstart_example_compiles_without_syntax_errors():
    # Arrange
    cmd = [sys.executable, "-m", "py_compile", str(EXAMPLE)]

    # Act
    result = subprocess.run(cmd, capture_output=True, text=True)

    # Assert
    assert result.returncode == 0, f"py_compile failed: {result.stderr}"
