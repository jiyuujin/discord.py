import discord
import time
from dhooks import Webhook, Embed

# discord webhook url
webhook_url = 'https://discordapp.com/api/webhooks/587871998273650728/-OBg63t8bEk9lkOHtgCcm-adDOqw3YS3c2sQ8VcVcViU06xzJR29JuOAHTh-o93_e4qW'

hook = Webhook('url')

embed = Embed(
    description = 'This is the **description** of the embed! :smiley:',
    color = 0x1e0f3,
    timestamp = 'now'
)

client = discord.Client()

# 起動時のデコレータをイベントループに登録
@client.event
async def on_ready():
    # ログインを通知する
    print('ログインしました')
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='18:00:00':
            # チャンネル名を設定する
            channel = client.get_channel('qiita')
            # discordに送信する
            webhook = DiscordWebhook(webhook_url)
            title = ''
            description = ''
            color = '007acc'
            embed = DiscordEmbed(title, description, color)
            webhook.add_embed(embed)
            webhook.execute()

# メッセージ受信時のデコレータをイベントループに登録
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言した場合は「にゃーん」を返す
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # 「/qiita_ts」と発言した場合は「関連する投稿一覧」を返す
    if message.content == '/qiita_ts':
        await message.channel.send('')

# 新メンバージョイン時のデコレータをイベントループに登録
@client.event
async def on_member_join():
    return

client.run(TOKEN)
