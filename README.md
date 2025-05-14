# Projeto Cybersegurança

# 💀 SKYCRACKER – Cybersecurity Toolkit (CLI)


> Uma ferramenta de linha de comando para pentesters iniciantes ou entusiastas de segurança ofensiva, que automatiza comandos básicos usando ferramentas como **Nmap**, **Nikto**, **Hydra** e outros.

---

## 🚀 Funcionalidades

- [x] Ping em servidores
- [x] Escaneamento de portas com **Nmap** (modo padrão ou stealth `-sS`)
- [x] Verificação de vulnerabilidades web com **Nikto**
- [x] Ataque de força bruta com **Hydra**
- [x] Visualização de serviços ativos com **Netstat**
- [x] Consulta de DNS com **nslookup**
- [x] Interface CLI interativa com menu

---

## 📦 Requisitos

- Python 3.8+
- Ferramentas externas instaladas:
  - [`nmap`](https://nmap.org/)
  - [`nikto`](https://cirt.net/Nikto2)
  - [`hydra`](https://github.com/vanhauser-thc/thc-hydra)
  - `netstat` (ou `ss` no Linux)
  - `nslookup`

> 💡 As ferramentas devem estar acessíveis via terminal (no PATH).

---

## 🧪 Como usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/skycracker.git
   cd skycracker

