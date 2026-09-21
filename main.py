from core import config
from network import ping
while True:
    config.menu_disp()
    select_router = int(input("NETRA > "))
    if select_router == 0:
        print("saindo...")
        break
    else:
        ip_router = config.loc_dispositivos(select_router)

    ping.check_host(ip_router)
    input("Pressione ENTER para prosseguir com o ping mais pesado....")
    ping.ping_test(ip_router)