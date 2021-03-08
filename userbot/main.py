import importlib
from importlib import import_module
from sqlite3 import connect
import os
import requests
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from telethon.tl.functions.channels import GetMessagesRequest
from . import BRAIN_CHECKER, LOGS, bot, PLUGIN_CHANNEL_ID, CMD_HELP, LANGUAGE, USERAZ_VERSION, PATTERNS
from .modules import ALL_MODULES
import userbot.modules.sql_helper.mesaj_sql as MSJ_SQL
import userbot.modules.sql_helper.galeri_sql as GALERI_SQL
from pySmartDL import SmartDL
from telethon.tl import functions

from random import choice
import chromedriver_autoinstaller
from json import loads, JSONDecodeError
import re
import userbot.cmdhelp

DIZCILIK_STR = [
    "Stikeri Fırladıram...",
    "Yaşasın fırlatmaq...",
    "Bu stikeri öz paketimə dəvət edirəm...",
    "Bunu fırlatmalıyam...",
    "Hey bu gözəl bir stikerdi!\nBir an öncə fırladıram..",
    "Stikerinizi fırladırəm\nhahaha.",
    "Hey bura bax. (☉｡☉)!→\nMən bunu fırladıram...",
    "Güllər qırmızı bənövşələr mavi, bu stikeri paketimə əlavə edərək dava dəbdəbəli olacağam...",
    "Stiker saxlanılır...",
    "Bu stikeri uje sahipləndim... ",
]

AFKSTR = [
    "Mən indi tələsirəm, daha sonra bir mesaj göndərə bilməzsən? Onsuz da yenə gələcəm.",
    "Yazdığınız şəxs hal-hazırda mesajınıza cavab vermir.\nXaiş edirik biraz sonra mesaj yazın!",
    "Bir neçə dəqiqədən sonra gələcəm. Ancaq gəlməsəm ...\ndaha çox gözləyin.",
    "Mən indi burada deyiləm, yəqin ki, başqa bir yerdəyəm.\n{last_second}saniyə əvvəl burda idi",
    "Getsən gedirsənsə sevgili yar amma unutma.\nBirazdan gələcəm",
    "Bəzən həyatda ən yaxşı şeylər gözləməyə dəyər…\nSəndə mənim gəlməyimi gözlə.",
    "Dərsə gedən bir uşaq yıxıldı buz üstə. Sonrada durub yoluna davam elədi.\nSahibim burda deyil amma istəsən biz səninlə söhbət edə bilərik.",
    "Hələdə burda olmadığımı anlamadın?\nSənidə qınamıram eşşəy nə bilir zəfəran nədi?😂.\nBirazdan gələrəm😏\n\n",
    "A kişi saa dedim yazma!\nBurda deyiləmdə aaaa...",
    "Sahibim burda yoxdu mənə dediki sevgilisinnən bezib və yeni bir sevgili tapmağa gedir",
    "Mən hazırda klaviaturadan uzağam, ancaq ekranda kifayət qədər yüksək səslə qışqırırsan, səni eşidərəm.",
    "Jizni varam {mention}\nQapıya gedən yol ---->\n gözlə birazdan gələcəm:)",
    "Sahibim axırıncı dəfə bu tərəf getdi\n<----\nSəndə arxasıyca qaç bəlkə çata bildin.",
    "Xahiş edirəm bir mesaj saxlayın və o mesaj məni indi olduğumdan daha dəyərli hiss etdirsin.",
    "Sahibim burada deyil səndə mənə yazmağı dayandır.",
    "Burda olsaydım,\nSizə harada olduğumu deyərdim.\n\nAmma mən deyiləm,\nqayıdanda məndən soruş...",
    "Mən uzaqdayam!\nNə vaxt qayıdacağımıda bilmirəm !\nÜmid varam bir neçə dəqiqəyə.",
    "Bağışlayın, sahibim burada deyil.\nO gələnə qədər mənimlə danışa bilərsən.\nSahibim sonra sizə qayıdacaq.",
    "Güman edirəm ki, bir mesaj gözləyirdiniz!",
    "Həyat çox qısadır, edilə bilinəcək çox şey var...\nOnlardan birini edirəm...",
    "Bu qədər zəhlə tökən olduğunu bilmirdim\nSAHİBİM\nBURDA\nDEYİL!!!",
]

UNAPPROVED_MSG = ("`Hey,` {mention}`! Mən sahibimin botuyam. Narahat olma.\n\n`"
                  "`Sahibim sənə PM-ə yazma icazə vermədi. `"
                  "`Xahiş edirəm sahibimin aktiv olmasını gözləyin, ümumiyyətlə PM-ləri təsdiqləyir.\n\n`"
                  "`Gözləməyi seçdiyiniz üçün təşəkkürlər🤍.`")

DB = connect("learning-data-root.check")
CURSOR = DB.cursor()
CURSOR.execute("""SELECT * FROM BRAIN1""")
ALL_ROWS = CURSOR.fetchall()
INVALID_PH = '\nHATA: Girilen telefon numarası geçersiz' \
             '\n  Ipucu: Ülke kodunu kullanarak numaranı gir' \
             '\n       Telefon numaranızı tekrar kontrol edin'

for i in ALL_ROWS:
    BRAIN_CHECKER.append(i[0])
connect("learning-data-root.check").close()

def extractCommands(file):
    FileRead = open(file, 'r').read()
    
    if '/' in file:
        file = file.split('/')[-1]

    Pattern = re.findall(r"@register\(.*pattern=(r|)\"(.*)\".*\)", FileRead)
    Komutlar = []


    if re.search(r'CmdHelp\(.*\)', FileRead):
        pass
    else:
        dosyaAdi = file.replace('.py', '')
        CmdHelp = userbot.cmdhelp.CmdHelp(dosyaAdi, False)

        # Komutları Alıyoruz #
        for Command in Pattern:
            Command = Command[1]
            if Command == '' or len(Command) <= 1:
                continue
            Komut = re.findall("(^.*[a-zA-Z0-9şğüöçı]\w)", Command)
            if (len(Komut) >= 1) and (not Komut[0] == ''):
                Komut = Komut[0]
                if Komut[0] == '^':
                    KomutStr = Komut[1:]
                    if KomutStr[0] == '.':
                        KomutStr = KomutStr[1:]
                    Komutlar.append(KomutStr)
                else:
                    if Command[0] == '^':
                        KomutStr = Command[1:]
                        if KomutStr[0] == '.':
                            KomutStr = KomutStr[1:]
                        else:
                            KomutStr = Command
                        Komutlar.append(KomutStr)
             #Useraz
            Userazpy = re.search('\"\"\"USERAZPY(.*)\"\"\"', FileRead, re.DOTALL)
            if not Userazpy == None:
                Userazpy = Userazpy.group(0)
                for Satir in Userazpy.splitlines():
                    if (not '"""' in Satir) and (':' in Satir):
                        Satir = Satir.split(':')
                        Isim = Satir[0]
                        Deger = Satir[1][1:]
                                
                        if Isim == 'INFO':
                            CmdHelp.add_info(Deger)
                        elif Isim == 'WARN':
                            CmdHelp.add_warning(Deger)
                        else:
                            CmdHelp.set_file_info(Isim, Deger)
            for Komut in Komutlar:
                # if re.search('\[(\w*)\]', Komut):
                    # Komut = re.sub('(?<=\[.)[A-Za-z0-9_]*\]', '', Komut).replace('[', '')
                CmdHelp.add_command(Komut, None, 'Bu plugin kənardan yüklənmişdir. Hərhansısa bir açıqlama tapılmadı.')
            CmdHelp.add()

try:
    bot.start()
    idim = bot.get_me().id
    userazbl = requests.get('https://gitlab.com/Quiec/asen/-/raw/master/asen.json').json()
    if idim in userazbl:
        bot.disconnect()

    # ChromeDriver'ı Ayarlayalım #
    try:
        chromedriver_autoinstaller.install()
    except:
        pass
    
    # Galeri için değerler
    GALERI = {}

    # PLUGIN MESAJLARI AYARLIYORUZ
    PLUGIN_MESAJLAR = {}
    ORJ_PLUGIN_MESAJLAR = {"alive": "` USER-AZ super işləyir⚡`", "afk": f"`{str(choice(AFKSTR))}`", "kickme": "`Özünüzdən muğayat olun mən gedirəm🤠", "pm": UNAPPROVED_MSG, "dızcı": str(choice(DIZCILIK_STR)), "ban": "{mention}`, qadağan edildi!`", "mute": "{mention}`, səssizə alındı`", "approve": "{mention}`, mənə mesaj göndərə bilərsən!`", "disapprove": "{mention}`, Bundan sonra mənə mesaj göndərə bilməzsən!`", "block": "{mention}`, əngəlləndin!`"}

    PLUGIN_MESAJLAR_TURLER = ["alive", "afk", "kickme", "pm", "dızcı", "ban", "mute", "approve", "disapprove", "block"]
    for mesaj in PLUGIN_MESAJLAR_TURLER:
        dmsj = MSJ_SQL.getir_mesaj(mesaj)
        if dmsj == False:
            PLUGIN_MESAJLAR[mesaj] = ORJ_PLUGIN_MESAJLAR[mesaj]
        else:
            if dmsj.startswith("MEDYA_"):
                medya = int(dmsj.split("MEDYA_")[1])
                medya = bot.get_messages(PLUGIN_CHANNEL_ID, ids=medya)

                PLUGIN_MESAJLAR[mesaj] = medya
            else:
                PLUGIN_MESAJLAR[mesaj] = dmsj
    if not PLUGIN_CHANNEL_ID == None:
        LOGS.info("Pluginlər Yüklənir")
        try:
            KanalId = bot.get_entity(PLUGIN_CHANNEL_ID)
        except:
            KanalId = "me"

        for plugin in bot.iter_messages(KanalId, filter=InputMessagesFilterDocument):
            if plugin.file.name and (len(plugin.file.name.split('.')) > 1) \
                and plugin.file.name.split('.')[-1] == 'py':
                Split = plugin.file.name.split('.')

                if not os.path.exists("./userbot/modules/" + plugin.file.name):
                    dosya = bot.download_media(plugin, "./userbot/modules/")
                else:
                    LOGS.info("Bu Plugin Onsuz Yüklənib" + plugin.file.name)
                    extractCommands('./userbot/modules/' + plugin.file.name)
                    dosya = plugin.file.name
                    continue 
                
                try:
                    spec = importlib.util.spec_from_file_location("userbot.modules." + Split[0], dosya)
                    mod = importlib.util.module_from_spec(spec)

                    spec.loader.exec_module(mod)
                except Exception as e:
                    LOGS.info(f"`Yükləmə uğursuz oldu! Plugin xətalıdır.\n\nXəta: {e}`")

                    try:
                        plugin.delete()
                    except:
                        pass

                    if os.path.exists("./userbot/modules/" + plugin.file.name):
                        os.remove("./userbot/modules/" + plugin.file.name)
                    continue
                extractCommands('./userbot/modules/' + plugin.file.name)
    else:
        bot.send_message("me", f"`Xaiş edirik, pluginlərin qalıcı olması üçün PLUGIN_CHANNEL_ID'i yerləşdirin.`")
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

async def FotoDegistir (foto):
    FOTOURL = GALERI_SQL.TUM_GALERI[foto].foto
    r = requests.get(FOTOURL)

    with open(str(foto) + ".jpg", 'wb') as f:
        f.write(r.content)    
    file = await bot.upload_file(str(foto) + ".jpg")
    try:
        await bot(functions.photos.UploadProfilePhotoRequest(
            file
        ))
        return True
    except:
        return False

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info("Botunuz problemsiz şəkildə işləyir! hər-hansısa bir söhbətə .alive yazaraq yoxlaya bilərsiniz."
          "Köməyə ehtiyacınız varsa, Dəstək qrupumuza gəlin t.me/UserazSup")
LOGS.info(f"Bot versıyanız: USER-AZ {USERAZ_VERSION}")

"""
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
"""
bot.run_until_disconnected()
