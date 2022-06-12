class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise EmailInvalido(f'Email de remetente inválido {remetente}')
        return remetente


#  Criando uma classe de ERROR
class EmailInvalido(Exception):
    pass
