# Leon Bot Monitor

Este projeto é um bot de monitoramento simples desenvolvido em Python. Ele envia notificações por e-mail a cada hora para informar que o sistema está ativo, além de enviar um alerta assim que o script é iniciado.

O projeto utiliza a biblioteca [Rocketry](https://rocketry.readthedocs.io/) para o agendamento de tarefas e `smtplib` para o envio de e-mails.

## Funcionalidades

- **Notificação de Inicialização**: Envia um e-mail informando o horário em que o bot (e consequentemente o PC) foi iniciado.
- **Monitoramento Horário**: Envia um e-mail a cada 1 hora confirmando que o bot continua em execução.
- **Logging**: Registra atividades e erros no console para fácil depuração.

## Pré-requisitos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)

## Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/Leon_bot.git
   cd Leon_bot
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # No Linux/macOS
   # .venv\Scripts\activate   # No Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuração

1. Renomeie o arquivo `.env.example` para `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edite o arquivo `.env` com suas credenciais de e-mail e servidor SMTP:
   ```ini
   EMAIL_ADDRESS=seu_email@exemplo.com
   EMAIL_PASSWORD=sua_senha_de_app
   EMAIL_SMTP_SERVER=smtp.gmail.com  # Exemplo para Gmail
   EMAIL_SMTP_PORT=587
   EMAIL_TO=destinatario@exemplo.com
   ```

   > **Nota**: Se estiver usando Gmail, você precisará gerar uma "Senha de App" nas configurações de segurança da sua conta Google (se a verificação em duas etapas estiver ativa).

## Como Usar

### Execução Manual
Com o ambiente virtual ativo, execute:
```bash
python bot.py
```

### Execução via Script (Linux/macOS)
Foi disponibilizado um script `run_bot.sh` para facilitar a execução. Certifique-se de dar permissão de execução:

```bash
chmod +x run_bot.sh
./run_bot.sh
```

## Estrutura do Projeto

- `bot.py`: Código principal do bot contendo a lógica de envio de e-mail e agendamento.
- `requirements.txt`: Lista de dependências do projeto.
- `.env`: Arquivo de configuração (não versionado) para credenciais sensíveis.
- `run_bot.sh`: Script shell para automação da execução.
