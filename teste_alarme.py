from datetime import datetime


def verificar_alarme(hora_atual, horario_alarme):
    return hora_atual == horario_alarme


# Teste
hora_teste = datetime.now().strftime("%H:%M")

assert verificar_alarme(hora_teste, hora_teste) is True

print("Teste executado com sucesso!")