import subprocess
import re
import time
import signal
import sys
from tqdm import tqdm
import queue
import threading

def check_host(host):
    #executa o comando ping no host desejado
    comando = ["ping", host, "-n", "4"]
    print("pingando no ip {}".format(host))

    #escreve output no arquivo de texto para analise
    with open("network/output.txt", "w", encoding="utf-8") as arquivo:
        subprocess.run(comando, stdout=arquivo, text=True)

    #verifica no output qual foi a saida, se o ping foi bem sucedido ou não
    dispositivo = 0
    with open("network/output.txt", "r", encoding="cp850") as arquivo:
        conteudo = arquivo.read()

        if "inacessível".lower() in conteudo.lower():
            dispositivo = dispositivo + 1
            print("HOST DOWN")
        elif "Esgotado".lower() in conteudo.lower():
            dispositivo = dispositivo + 1
            print("HOST DOWN")
        else:
            dispositivo = 0
            print("HOST UP")

    #testa a latencia do host
    latencia = "Mínimo"
    tempo_latencia = None
    with open("network/output.txt", "r", encoding="cp850") as pingt:
        for linha in pingt:
            if latencia.lower() in linha.lower():
                tempo_latencia = linha.strip()
                break
    if tempo_latencia:
        print(tempo_latencia)

    # exibe os pacotes quantos foram enviados, quantos foram recebidos, e quantos foram perdidos
    with open("network/output.txt", "r", encoding="cp850") as pingp:
        conteudo = pingp.read()
        resultado = re.search(r'(Pacotes:.*?\))', conteudo, re.DOTALL)
        if resultado:
            texto_capturado = resultado.group(1)
    if texto_capturado:
        texto_limpo = " ".join(texto_capturado.split())
        print(texto_limpo)

def ping_test(host):
    minutos = float(input("quantos minutos deseja que o ping seja executado?: "))
    tempo_limite_segundos = int(minutos * 60)
    
    with open("network/ping_test_output.txt", "w", encoding="utf-8") as arquivo:
        processo = subprocess.Popen(
            ["ping", host, "/t"],
            stdout=arquivo,
            stderr=subprocess.STDOUT,
            text=True
        )

        time.sleep(tempo_limite_segundos)
        print("parando o ping...")
        try:
            subprocess.run(
                ["taskkill", "/F", "/PID", str(processo.pid)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except Exception as e:
            print(f"erro {e}")

        processo.kill()
    print("cabo")

    print("analisando o ping....")
    with open("network/ping_test_output.txt", "r", encoding="cp850") as arquivo:
        linhas = arquivo.readlines()

    enviados = 0
    recebidos = 0
    tempos = []
    regex_tempo = r"(?:tempo|time)[:=]\s*(\d+)ms"
    for linha in linhas:
        if "Resposta de" in linha or "Reply from" in linha:
            enviados += 1
            recebidos += 1
            match = re.search(regex_tempo, linha)
            if match:
                tempos.append(int(match.group(1)))
        elif "Esgotado o tempo limite" in linha or "Request timed out" in linha:
            enviados += 1

    perdidos = enviados - recebidos

    if enviados > 0:
        print(f"Enviados: {enviados}")
        print(f"Recebidos: {recebidos}")
        print(f"Perdidos: {perdidos}")
        if tempos:
            print(f"Latencia Maxima {max(tempos)}ms")
            print(f"Latencia min {min(tempos)}ms")
            print(f"Latencia media {int(sum(tempos) / len(tempos))}ms")
        else:
            print("Nenhum pacote obteve resposta")
    else:
        print("Nenhum ping foi registrado no arquivo")

    input("pressione ENTER para prosseguir....")

