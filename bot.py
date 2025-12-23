import os
import smtplib
import logging
from datetime import datetime
from email.message import EmailMessage
from dotenv import load_dotenv
from rocketry import Rocketry

# Configuração de logging
logging.basicConfig(
    filename='email.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Carregar variáveis de ambiente
load_dotenv()

app = Rocketry()

@app.task("every 1 hour")
def horario():
    """
    Função responsável por enviar o e-mail usando as configurações do .env
    """
    now_str = datetime.now().strftime('%d/%m/%Y %H:%M')
    try:
        email_address = os.getenv('EMAIL_ADDRESS')
        email_password = os.getenv('EMAIL_PASSWORD')
        smtp_server = os.getenv('EMAIL_SMTP_SERVER')
        smtp_port = int(os.getenv('EMAIL_SMTP_PORT', 587))
        email_to = os.getenv('EMAIL_TO')

        if not all([email_address, email_password, smtp_server, email_to]):
            logging.error("Variáveis de ambiente incompletas. Verifique o arquivo .env")
            return

        msg = EmailMessage()
        msg['Subject'] = 'Bot Notification'
        msg['From'] = email_address
        msg['To'] = email_to
        msg.set_content(f'Olá! Este é um aviso automático do Leon Bot. A hora atual é: {now_str}')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(msg)
            
        logging.info(f"Email enviado com sucesso para {email_to}")

    except Exception as e:
        logging.error(f"Erro ao enviar email: {e}")

def start():
    """
    Função para iniciar o bot.
    """
    now_str = datetime.now().strftime('%d/%m/%Y %H:%M')
    logging.info("Bot iniciado com Rocketry. Agendando envio de email a cada 1 hora.")
    try:
        email_address = os.getenv('EMAIL_ADDRESS')
        email_password = os.getenv('EMAIL_PASSWORD')
        smtp_server = os.getenv('EMAIL_SMTP_SERVER')
        smtp_port = int(os.getenv('EMAIL_SMTP_PORT', 587))
        email_to = os.getenv('EMAIL_TO')

        if not all([email_address, email_password, smtp_server, email_to]):
            logging.error("Variáveis de ambiente incompletas. Verifique o arquivo .env")
            return

        msg = EmailMessage()
        msg['Subject'] = 'Bot Notification'
        msg['From'] = email_address
        msg['To'] = email_to
        msg.set_content(f'Olá! O Leon ligou o PC as {now_str}, e a partir de agora, vou irá monitorar o tempo de uso.')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.send_message(msg)


    except Exception as e:
        logging.error(f"Erro ao enviar email: {e}")



if __name__ == "__main__":
    logging.info("Bot iniciado com Rocketry. Agendando envio de email a cada 1 hora.")
    start()
    app.run()
