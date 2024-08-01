from telethon import TelegramClient, events

import logging

# Configurar logging para ajudar na depuração
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


source_channel_username = -1002094462215
target_channel_username = -1002170325171

# api_id = 22065622
# api_hash = "594fa52ca7a512dee8287bcf885d3852"
# TOKEN = "7282540350:AAErCunUDUt0Fd5-61jXGA6FlSEgZjZLUcg"


api_id = 25397054
api_hash = "4e82e1c81cd168c2595c909f6e8aa8d8"
TOKEN = "7190389378:AAGDBeyYWjPc64NbfHbfeOs5zk2KYl27HRg"

# Crie uma instância do cliente
client = TelegramClient("aa_Tips", api_id, api_hash)


# Evento que lida com novas mensagens no canal de origem
@client.on(events.NewMessage(chats=source_channel_username))
async def handler(event):
    try:
        # Obtém a mensagem
        message = event.message
        logger.info(f"Nova mensagem recebida no canal de origem: {message.text}")

        # Envia a mensagem para o canal de destino
        await client.send_message(target_channel_username, message)
        logger.info("Mensagem enviada para o canal de destino.")

    except Exception as e:
        logger.error(f"Erro ao processar mensagem: {e}")


# Inicie o cliente
async def start_bot():
    try:
        await client.start()
        logger.info("Client is running. Listening for messages...")
        await client.run_until_disconnected()

    except Exception as e:
        logger.error(f"Erro ao iniciar o cliente: {e}")


# Executar o bot
if __name__ == "__main__":
    client.loop.run_until_complete(start_bot())
