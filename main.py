from telethon.sync import TelegramClient, events

# Change these variables with your credentials
api_id = 13356656
api_hash = "304ec89622dc2ede528971d19f14087b"
phone = "+994707909291"

# The channels/groups that you want to get messages from
source_channel_names = ['FRI® VIP', 'Binance Killers® VIP Signals', 'Bitcoin Bullets® VIP', 'Fed. Russian Insiders®', 'Bitcoin Bullets®', 'Binance Killers®','test01']
##
# The channel/group where you want to forward messages
destination_channel_link = -1002145629944

# The channel where you want to forward messages containing the word "profit"
profit_channel_link = -1002074911090  # Replace with the actual channel ID

client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code:'))

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat = await event.get_chat()
    try:
        if chat.title in source_channel_names:
            if "profit" in event.message.text.lower():
                await client.forward_messages(entity=profit_channel_link, messages=event.message)
            else:
                await client.forward_messages(entity=destination_channel_link, messages=event.message)
    except AttributeError:
        pass
    except KeyboardInterrupt:
        exit

client.start()
client.run_until_disconnected()

