import subprocess
import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
	outcome = yield
	rep = outcome.get_result()
	if rep.failed:
		changed_files = subprocess.check_output(["git", "diff", "--name-only", "HEAD"]).decode().splitlines()
		subprocess.run(["flake8", *changed_files])

def pytest_sessionstart(session):
	if not list(session.items):
		changed_files = [item.fspath for item in session.items if item.rep_call.passed]
		subprocess.run(["black", *changed_files, "-j", "0"])
		subprocess.run(["flake8", *changed_files, "-j", "0"])