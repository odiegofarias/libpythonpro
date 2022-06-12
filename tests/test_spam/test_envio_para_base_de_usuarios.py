from unittest.mock import Mock
import pytest
from spam.enviador_de_email import Enviador
from spam.main import EnviadorDeSpam
from spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Diego', email='diego@email.com.br'),
            Usuario(nome='Mirela', email='diego@email.com.br')
        ],
        [
            Usuario(nome='Diego', email='diego@email.com.br'),
        ]
    ]
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'diego@email.com.br',
        'Curso Python Pro',
        'Aprendendo Python com Renzo no Python Pro',
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Diego', email='diego@email.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'Mirela@email.com.br',
        'Curso Python Pro',
        'Aprendendo Python com Renzo no Python Pro',
    )
    enviador.enviar.assert_called_onde_with(
        'Mirela@email.com.br',
        'diego@email.com.br'
        'Curso Python Pro',
        'Aprendendo Python com Renzo no Python Pro',
    )