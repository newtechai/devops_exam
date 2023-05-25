import pytest
from testinfra import get_host


@pytest.fixture(scope="module")
def host(request):

    remote_host = get_host("192.168.43.82")
    yield remote_host


def test_nginx_installed(host):
    assert host.package("nginx").is_installed


def test_nginx_running_with_systemd(host):
    assert host.service("nginx").is_running
    assert host.service("nginx").is_enabled


def test_nginx_listening_on_port_80(host):
    assert host.socket("tcp://192.168.43.82:80").is_listening


def test_nginx_binding_to_different_port(host):
    # the port we want to test
    assert host.socket("tcp://192.168.43.82:8080").is_listening
# run this to test pytest sec1_ques7.py
