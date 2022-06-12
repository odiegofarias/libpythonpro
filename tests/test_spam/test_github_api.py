from unittest.mock import Mock

import pytest

import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/12721428?v=4'
    resp_mock.json.return_value = {
        "login": "odiegofarias", "id": 12721428,
        "avatar_url": url
    }
    #  Sempre que o teste depende de uma biblioteca: Data, funções aleatória
    #  Passa o caminho do Tear Down para isolar o Mock nos testes. Restaura a LIB original quando o teste rodar
    get_mock = mocker.patch('github_api.requests.get')
    get_mock.return_value = resp_mock

    #  Acessando a "BIBLIOTECA GITHUB_API com a biblioteca REQUESTS e método GET e transformando em MOCK"
    github_api.requests.get = Mock(return_value=resp_mock)
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('odiegofarias')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
