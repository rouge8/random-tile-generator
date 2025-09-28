from pathlib import Path

from click.testing import CliRunner
import pytest


@pytest.fixture
def data_dir() -> Path:
    return Path(__file__).parent / "data"


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()
