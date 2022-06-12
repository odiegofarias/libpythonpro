from spam.enviador_de_email import Enviador
from spam.enviador_de_email import EmailInvalido
import pytest


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

#  Parametrizando varios destinatarios no mesmo teste


@pytest.mark.parametrize(
    'remetente',
    ['foo@bar.com.br', 'diego@email.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'diego1@email.com.br',
        'Curso Python Pro',
        'Primeira turma Guido Van Rossum aberta'
    )
    assert remetente in resultado


#  Verificando se o email é válido, usando WITH E RAISES
@pytest.mark.parametrize(
    'remetente',
    ['', 'diego']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        resultado = enviador.enviar(
            remetente,
            'diego1@email.com.br',
            'Curso Python Pro',
            'Primeira turna Guido Van Rossum aberta'
        )
