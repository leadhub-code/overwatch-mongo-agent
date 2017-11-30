from pathlib import Path
from pytest import fixture


@fixture
def tmp_dir(tmpdir):
    return Path(str(tmpdir))
