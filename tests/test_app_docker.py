import pytest
import subprocess

@pytest.fixture()
def run_docker():
    subprocess.check_call(['docker', 'build', '-t', 'imdblk:test', '--build-arg', 'VERSION=test', '.'])
    docker_id = subprocess.check_output(
        ['docker', 'run', '-d', 'imdblk:test']).decode().strip()
    def _run(*args):
        return subprocess.run(["docker", "run", "-it", "imdblk:test"] + list(args))
    yield _run
    subprocess.check_call(['docker', 'rm', '-f', docker_id])


def test_myimage(run_docker):
    result = run_docker("matrix")
    assert result.returncode == 1
