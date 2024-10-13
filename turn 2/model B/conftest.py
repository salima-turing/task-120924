import subprocess
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        modified_files = [f.strpath for f in item.fspath.dirpath().glob("**/*.py")]
        subprocess.run(["flake8"] + modified_files)
