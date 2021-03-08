from userbot.events import register
from eksipy import Baslik, Giri, Eksi
from datetime import datetime
import urllib.parse
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.başlıq(\d*) ?(.*)")
async def baslik(event):
    sayfa = event.pattern_match.group(1)
    if sayfa == '':
        sayfa = 1
    else:
        sayfa = int(sayfa)

    baslik = event.pattern_match.group(2)
    try:
        baslik = Baslik(baslik, sayfa)
    except:
        return await event.edit('`Belə bir başlıq yoxdur.`')
    
    topic = başlıq.get_topic()
    entrys = başlıq.get_entrys()
    Result = f'**Başlıq: **`{topic.title}`\n`{topic.current_page}/{topic.max_page}`\n\n'
    
    for entry in entrys:
        if len(entry.text().strip()) < 450:
            Result += f'`{entry.text().strip()}`\n__[{datetime.utcfromtimestamp(entry.date).strftime("%d/%m/%Y")}](https://eksisozluk.com/entry/{entry.id}) [{entry.author}](https://eksisozluk.com/biri/{urllib.parse.quote(entry.author)})__\n\n'
        else:
            Result += f'**Bu çox uzun görünür.** `.entry {entry.id}` ilə istifadə edə bilərsiniz.\n\n'
    return await event.edit(Result)

@register(outgoing=True, pattern="^.entry ?(\d*)")
async def entry(event):
    Entry = int(event.pattern_match.group(1))
    try:
        Entry = Giri(Entry).get_entry()
    except:
        return await event.edit('`Belə bir başlıq yoxdur.`')
    
    Result = f'**Başlık: **`{Entry.topic.title}`\n\n'
    Result += f'`{Entry.text().strip()}`\n __[{datetime.utcfromtimestamp(Entry.date).strftime("%d/%m/%Y")}](https://eksisozluk.com/entry/{Entry.id}) [{Entry.author}](https://eksisozluk.com/biri/{urllib.parse.quote(Entry.author)})__\n\n'
    return await event.edit(Result)

@register(outgoing=True, pattern="^.gündəm ?(\d*)$")
async def gundem(event):
    if event.pattern_match.group(1) == '':
        Sayfa = 1
    else:
        Sayfa = int(event.pattern_match.group(1))

    try:
        Gundem = Eksi().gundem(Sayfa)
    except:
        return await event.edit('`Bir xəta yarandı.`')
    
    Result = ""
    i = 1
    for Baslik in Gundem:
        Result += f'`{i}-)` [{Baslik.title}]({Baslik.url()}) __{Baslik.giri}__\n'
    return await event.edit(Result)

CmdHelp('eksi').add_command(
    'başlıq', '<səhifə> <başlıq>', 'Əks başlığı lüğətdə gətirir.', 'baslik2 php'
).add_command(
    'entry', '<id>', 'Entry gətirir.', 'entry 1'
).add_command(
    'gündəm', '<sayfa>', 'Gündəm gətirir.', 'gündəm 1'
).add()
