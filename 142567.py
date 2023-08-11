def converter_tempo_segundos(p_horas,p_minutos, p_segundos):
    p_total_segundos = p_horas * 3600 + p_minutos * 60 * p_segundos
    return p_total_segundos

horas = int(input('Digite o valor das horas: '))
minutos = int(input('Digite o valor dos minutos: '))
segundos = int(input('Digite o valor dos segundos: '))
total_segundos = converter_tempo_segundos(horas, minutos, segundos)
print('O tempo total em segundos é:', total_segundos)
