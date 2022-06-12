from spam.modelos import Usuario

"""
Scopes:
    Function: Padrão. Faz a conexão várias vezes nos testes
    Session: Executa apenas uma vez em toda a sessão de testes
    Module: Executa apenas uma vez em cada um dos módulos
"""


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Diego')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Diego'),
        Usuario(nome='Mirela')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()

