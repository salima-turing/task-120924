import subprocess
import pytest


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed:
        subprocess.run(["flake8", "."])


def pytest_sessionstart(session):
    subprocess.run(["black", "."])
