import os
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(r"""
      ██████████████████████████████████████████████████
      ███▄─▄███─▄▄─█─▄▄─█▄─▄▄▀█▄─█─▄█─▄▄─█▄─▄▄─█▄─▄▄▀███
      ████─██▀█─██─█─██─██─▄─▄██─▄▀██─██─██─▄█▀██─▄─▄███
      ██▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀██
              
              SKYCRACKER - Cybersecurity Toolkit
    """)
    print("""
    [1] Ping um servidor
    [2] Escanear portas (Nmap)
    [3] Verificar vulnerabilidades (Nikto)
    [4] Brute Force com Hydra
    [5] Exibir serviços ativos (Netstat)
    [6] Checagem de DNS (nslookup)
    [0] Sair
    """)

def ping():
    host = input("Digite o endereço do servidor: ")
    subprocess.run(["ping", host])

def nmap_scan():
    target = input("Digite o IP ou domínio do alvo: ")
    print("\n[1] Varredura padrão")
    print("[2] Varredura stealth (TCP SYN Scan - nmap -sS)")
    tipo = input("Escolha o tipo de varredura: ")
    if tipo == "2":
        subprocess.run(["nmap", "-sS", target])
    else:
        subprocess.run(["nmap", target])

def nikto_scan():
    target = input("Digite o endereço do servidor web (ex: http://exemplo.com): ")
    subprocess.run(["nikto", "-h", target])

def hydra_attack():
    service = input("Digite o serviço (ex: ssh, http): ")
    target = input("Digite o IP ou domínio do alvo: ")
    user = input("Digite o nome de usuário: ")
    wordlist = input("Digite o caminho da wordlist: ")
    subprocess.run(["hydra", "-l", user, "-P", wordlist, target, service])

def netstat():
    command = "netstat -an" if os.name == 'nt' else "ss -tunap"
    subprocess.run(command, shell=True)

def dns_lookup():
    domain = input("Digite o domínio: ")
    subprocess.run(["nslookup", domain])

def main():
    while True:
        clear()
        banner()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ping()
        elif opcao == "2":
            nmap_scan()
        elif opcao == "3":
            nikto_scan()
        elif opcao == "4":
            hydra_attack()
        elif opcao == "5":
            netstat()
        elif opcao == "6":
            dns_lookup()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
