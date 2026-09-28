import pyautogui
import os
import time
import numpy as np
from PIL import Image

GUVEN = 0.95
BEKLEME_SURESI = 15


#script hangi klasorden calistirilirsa calistirilsin dosya hep bulunsun
resim_yolu = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'indir_butonu.png')

# cv2/imread turkce karakterli yollari okuyamaz, PIL ile okuyup dizi olarak veriyoruz
buton_gorseli = np.array(Image.open(resim_yolu).convert('RGB')) if os.path.exists(resim_yolu) else None


def buton_bul(en_alttaki=False, kaydir=False):
    ekran_yuksekligi = pyautogui.size().height
    baslangic = time.time()

    while time.time() - baslangic < BEKLEME_SURESI:
        try:
            eslesmeler = list(pyautogui.locateAllOnScreen(buton_gorseli, confidence=GUVEN))
        except pyautogui.ImageNotFoundException:
            eslesmeler = []
        except Exception as hata:
            print(f'ekran arama hatasi: {hata}')
            return None

        for sira, kutu in enumerate(eslesmeler, 1):
            print(f'  eslesme {sira}: {kutu}')

        secilen = None
        if eslesmeler:
            kutu = max(eslesmeler, key=lambda k: k.top) if en_alttaki else eslesmeler[0]
            nokta = pyautogui.center(kutu)
            if nokta[1] < ekran_yuksekligi - 10:
                secilen = nokta
            elif kaydir:
                pyautogui.scroll(-5)

        if secilen:
            return secilen

        if kaydir and not eslesmeler:
            pyautogui.scroll(-5)
        time.sleep(0.5)

    return None


#chrome acar
pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2.5)

#linki yaz ve git
pyautogui.hotkey('ctrl', 'l')
time.sleep(0.5)
pyautogui.write('https://www.win-rar.com/start.html?&L=5')
pyautogui.press('enter')
time.sleep(2)

if not os.path.exists(resim_yolu):
    print(f'{resim_yolu} bulunamadi')
else:
    #1. sayfadaki indirme butonu
    buton_konumu = buton_bul()

    if buton_konumu:
        pyautogui.click(buton_konumu)
        print(f"buton bulundu {buton_konumu}")
        time.sleep(3)

        #2. sayfa acilinca alt kisimdaki indirme butonu
        buton_konumu = buton_bul(en_alttaki=True, kaydir=True)

        if buton_konumu:
            pyautogui.click(buton_konumu)
            print(f"2. sayfa butonu bulundu {buton_konumu}")
        else:
            print("2. sayfada buton bulunamadi")
    else:
        print("buton bulunamadi")
