import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_lint_is_installed(host):
    file = host.file("/usr/local/bin/ansible-lint")
    assert file.is_executable

def test_molecule_is_installed(host):
    file = host.file("/usr/local/bin/molecule")
    assert file.is_executable
