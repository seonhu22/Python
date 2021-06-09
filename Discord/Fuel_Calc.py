import discord
import math

client = discord.Client()

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.content.startswith("!커맨드"):
        await message.channel.send("커맨드 목록\n"
                                   "!도움말\n"
                                   "!기름")
    if message.content.startswith("!도움말"):
        await message.channel.send("기름 커맨드 사용법입니다.\n"
                                   "입력값은 '레이스 시간', '랩 타입', '랩당 기름 소요량' 입니다.\n\n"
                                   "예시\n"
                                   "총 레이스 시간: 30분, 랩 타임: 1분 57초, 랩당 기름 소모량: 1.7L\n"
                                   "!기름 30 1 57 1.7")
    if message.content.startswith("!기름"):
        #await message.channel.send("레이스 시간을 입력해주세요")
        msg_l = message.content.split()
        if msg_l[1:3] is not None:
            fuel = math.ceil((int(msg_l[1]) * 60) / (int(msg_l[2]) * 60 + int(msg_l[3])) * float(msg_l[4]))
        else:
            await message.channel.send("내용을 입력해주세요!")
            return
        await message.channel.send(str(fuel) + "L가 정확하며 안전 권장량은 " + str(int(fuel) + math.ceil(float(msg_l[4]) * 2)) + "L 입니다.")
        #await message.channel.send(str(fuel) + "L가 정확하며 안전 권장량은")

client.run('token')
