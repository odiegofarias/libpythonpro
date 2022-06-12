import pytest

from spam.db import Conexao


@pytest.fixture(scope='session')
def conexao():
    #  Setup
    conexao_obj = Conexao()
    yield Conexao()
    #  Tear Down
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    #  Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    #  Tear Down
    sessao_obj.roll_back()
    sessao_obj.fechar()