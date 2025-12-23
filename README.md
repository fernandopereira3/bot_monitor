# 🦁 Leon Bot Monitor

**Leon Bot** é um assistente de monitoramento automatizado desenvolvido em Python. Seu objetivo principal é rastrear o tempo de atividade do computador, enviando notificações por e-mail em tempo real sobre o status da máquina.

Este projeto é ideal para quem precisa monitorar remotamente quando uma máquina é ligada e garantir que ela continua operando corretamente ao longo do dia, servindo como um sistema de "Heartbeat" (batimento cardíaco) para o seu PC.

---

## 🚀 Como funciona

O bot opera com dois comportamentos distintos para garantir cobertura total do monitoramento:

1.  **Notificação de Inicialização (Boot)**:
    Assim que o script é executado (idealmente configurado para iniciar junto com o sistema operacional), ele dispara um e-mail imediato informando: *"O Leon ligou o PC às [HORA]"*. Isso serve como alerta de que a máquina ficou online.

2.  **Monitoramento Contínuo (Heartbeat)**:
    Utilizando o framework **Rocketry**, o bot entra em um ciclo de agendamento inteligente. A cada **1 hora**, ele envia uma notificação de status confirmando que o sistema continua ativo e conectado à internet.

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem base do projeto.
- **[Rocketry](https://rocketry.readthedocs.io/)**: Framework moderno de agendamento de tarefas em Python. Diferente de loops `while True` simples ou da biblioteca `schedule`, o Rocketry oferece uma sintaxe declarativa, melhor gerenciamento de execução e persistência.
- **SMTP (Simple Mail Transfer Protocol)**: Utilizado para o envio seguro de e-mails através do servidor configurado (ex: Gmail).
- **Python-dotenv**: Para segurança, garantindo que credenciais sensíveis sejam carregadas de variáveis de ambiente e não fiquem expostas no código.

## 📋 Funcionalidades

- ✅ **Alerta Instantâneo de Boot**: Saiba o minuto exato em que o computador foi ligado.
- ✅ **Confirmação de Atividade Horária**: Receba atualizações periódicas garantindo que o PC não travou ou desligou.
- ✅ **Logging Detalhado**: Registro de operações e erros no console para fácil diagnóstico.
- ✅ **Segurança de Credenciais**: Separação total entre lógica e configurações sensíveis (`.env`).

## ⚙️ Configuração e Instalação

### 1. Clone o repositório
```bash
git clone https://github.com/fernandopereira3/bot_monitor.git
cd Leon_bot
```

### 2. Prepare o ambiente
Recomendamos o uso de um ambiente virtual para isolar as dependências:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows
```

Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```

### 3. Configure as Credenciais
Crie o arquivo de configuração baseado no exemplo:
```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas informações:
```ini
EMAIL_ADDRESS=seu_email@gmail.com
EMAIL_PASSWORD=sua_senha_de_app      # Gere uma "App Password" na conta Google
EMAIL_SMTP_SERVER=smtp.gmail.com     # Servidor SMTP (ex: Gmail)
EMAIL_SMTP_PORT=587                  # Porta TLS padrão
EMAIL_TO=email_destinatario@gmail.com
```

> **Dica**: Se estiver usando Gmail com verificação em duas etapas, é obrigatório criar uma **Senha de App** nas configurações de segurança da sua conta Google. A senha normal não funcionará.

## ▶️ Como Executar

### Manualmente
Para testar ou rodar em primeiro plano:
```bash
python3 bot.py
```

### Via Script (Linux/Mac)
Para facilitar a automação (ex: adicionar aos aplicativos de inicialização), use o script shell incluído:
```bash
chmod +x run_bot.sh
./run_bot.sh
```

---
*Desenvolvido para monitoramento pessoal de uptime e automação residencial.*
