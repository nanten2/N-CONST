import sys
import subprocess
from pathlib import Path

import pytest


project_root = Path(__file__).parent.parent.parent
python_version = tuple(sys.version_info)[:2]


@pytest.fixture(scope="module")
def tmp_project_dir(tmp_path_factory) -> Path:
    return tmp_path_factory.mktemp("n_const")


@pytest.mark.skipif(
    python_version < (3, 9),
    reason="No need to support that wide versions for documentation building",
)
def test_create_stub(tmp_project_dir: Path):
    _ = subprocess.run(
        ["cp", "-rv", ".", str(tmp_project_dir)],
        cwd=project_root,
    )
    assert (tmp_project_dir / "docs" / "conf.py").exists()

    result = subprocess.run(
        [
            "poetry",
            "run",
            "sphinx-apidoc",
            "-efTM",
            "-t",
            f"{str(tmp_project_dir)}/docs/_templates/apidoc",
            "-o",
            f"{str(tmp_project_dir)}/docs/_source",
            "neclib",
        ],
        capture_output=True,
    )
    assert result.returncode == 0
    assert result.stderr == b""


@pytest.mark.skipif(
    python_version < (3, 9),
    reason="No need to support that wide versions for documentation building",
)
def test_build(tmp_project_dir: Path):
    assert (tmp_project_dir / "docs" / "conf.py").exists()
    result = subprocess.run(
        [
            "poetry",
            "run",
            "sphinx-build",
            "-W",
            "-a",
            f"{str(tmp_project_dir)}/docs",
            f"{str(tmp_project_dir)}/docs/_build",
        ],
        capture_output=True,
    )
    print(result.stderr, result.stdout)
    assert result.returncode == 0
    assert result.stderr == b""
