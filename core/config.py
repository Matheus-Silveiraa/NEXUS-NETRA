import json

with open('config/devices.json', 'r', encoding='utf-8') as dados:
    roteadores = json.load(dados)

#print(roteadores)


def loc_dispositivos(input_user):
    dispositivos = {disp["ID"]: disp for disp in roteadores["dispositivos"]}
    print("NOME:", dispositivos[input_user]["Nome"])
    print("Tipo:", dispositivos[input_user]["Tipo"])
    print("IP:", dispositivos[input_user]["IP"])
    print("MAC:", dispositivos[input_user]["MAC"])
    print("Local:", dispositivos[input_user]["Local"])
    ip = dispositivos[input_user]["IP"]
    return ip

def menu_disp():
    print(r"╔═══════════════════════════════════════════════════════════════════╗")
    print(r"║   ███▄▄▄▄      ▄████████     ███        ▄████████    ▄████████    ║")
    print(r"║   ███▀▀▀██▄   ███    ███ ▀█████████▄   ███    ███   ███    ███    ║")
    print(r"║   ███   ███   ███    █▀     ▀███▀▀██   ███    ███   ███    ███    ║")
    print(r"║   ███   ███  ▄███▄▄▄         ███   ▀  ▄███▄▄▄▄██▀   ███    ███    ║")
    print(r"║   ███   ███ ▀▀███▀▀▀         ███     ▀▀███▀▀▀▀▀   ▀███████████    ║")
    print(r"║   ███   ███   ███    █▄      ███     ▀███████████   ███    ███    ║")
    print(r"║   ███   ███   ███    ███     ███       ███    ███   ███    ███    ║")
    print(r"║    ▀█   █▀    ██████████    ▄████▀     ███    ███   ███    █▀     ║")
    print(r"║                                        ███    ███                 ║")
    print(r"╠═══════════════════════════════════════════════════════════════════╣")
    for disp in roteadores["dispositivos"]:
            ids = disp.get("ID")
            router = disp.get("Nome")
            print(f"║ {ids:<3} {router:^61} ║")
    print(r"║ 00                               sair                             ║")
    print(r"╚═══════════════════════════════════════════════════════════════════╝")

