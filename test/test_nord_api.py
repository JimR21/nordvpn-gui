import json

import pytest

from mypkg.nord_api import NordApi


@pytest.fixture
def servers():
    with open('test/test_data.json', 'r') as f:
        return json.load(f)


@pytest.fixture
def api():
    return NordApi()


def test_get_countries(servers, api):
    countries = api.get_country_list(servers)
    assert 'United States' in countries
    assert 'United Kingdom' in countries
    assert 'Sweden' in countries


def test_get_server_by_country(servers, api):
    usa_servers = api.get_servers_by_country(servers, 'United States')
    countries = api.get_country_list(usa_servers)
    assert 'United States' in countries
    assert 'United Kingdom' not in countries
    assert 'Sweden' not in countries
