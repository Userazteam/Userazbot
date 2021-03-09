<div align="center">
  <img src="https://telegra.ph/file/fb9ddf3b324d40c34c5cf.jpg" width="200" height="200">
  <h1>USER-AZ</h1>
</div>
<p align="center">
    USER-AZ Telegram istifadəsini rahatlaşdıracaq və taməmən pulsuz və açıq qaynaqlıdır
    <br>
        <a href="https://t.me/Userazbot">Telegram Kanalı</a>
    <br>
</p>

----

## Qurulum
### Asan yol
[Youtube](https://www.youtube.com/watch?v=jJlH56saM4A)

**Android:** Termuxu açın ve bu kodu yapışdırın: <br> `bash <(curl -L https://cutt.ly/ezguHNZ)`

**iOS:** iSH açın ve bu kodu yapışdırın: <br> `apk update && apk add bash && apk add curl && curl -L -o useraz_installer.sh https://cutt.ly/ezguHNZ && chmod +x useraz_installer.sh && bash useraz_installer.sh`

**Windows 10:** [Python](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l#activetab=pivot:overviewtab) indirin ardından PowerShell bu kodu yapıştırın: <br> `Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://kutt.it/BqRltH')`


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Userazteam/Userazbot)
### Çətin yol
```python
git clone https://github.com/Userazteam/Userazbot.git
cd Userazbot
pip install -r requirements.txt
# Config.env oluşturun ve düzenleyin. #
python3 main.py
```

## Örnek Plugin
```python
from userbot.events import register
from userbot.cmdhelp import CmdHelp # <-- Bunu əlavə edin.

@register(outgoing=True, pattern="^.test")
async def test(event):
    await event.edit('salam Dünya!')

Help = CmdHelp('test') # Məlumat əlavə edəciyik
Help.add_command('test', # əmr
    None, # Əmr açıxlaması varsa yazın yoxdusa None yazın
    'Salam Dünyalılar!', # Əmir açıqlaması
    'test' # Test İstifadə
    )
Help.add_info('@Samil tərəfindən hazırlandı.') # Məlumat əlavə edin
# Ya da eror --> Help.add_warning('QURMA!')
Help.add() # Və bunu yazağ
```

## Bilgilendirme
Herhansı bir istək & şikayət & təklifiniz varsa [Support Groupuna](https://t.me/Userazsup) yazın.

```
    Userazbot işlədərək məsuliyəti siz daşımış olursuz.
    Userbotu işlədərkən hesabınız banlana bilər
    Bu bir açıq qaynaqlı proyekdir, etdiyiniz hər şeydən siz cavabdehsiniz. Useraz Qurucuları bundan cavbdeh deyil və şikayət qəbul etmir.
```
