import pyautogui
import ctypes
import glob
import os
import subprocess
import sys
import time

# terminale yazilacak komut: $env:USERPROFILE kullanildigi icin turkce karakterli
# kullanici adi sorun olmaz, en son indirilen kurulum dosyasi sessiz acilir
KOMUT = ('$f=Get-ChildItem "$env:USERPROFILE\\Downloads" -Recurse -EA 0|'
         'Where-Object {$_.Extension -in ".exe",".msi"}|'
         'Sort-Object LastWriteTime -Desc|Select-Object -First 1;'
         'Start-Process $f.FullName -ArgumentList "/S"')

UAC_BEKLEME = 3
KURULMA_SURESI = 600


def admin_mi():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except Exception:
        return False


def kendini_yonetici_yap():
    # UAC admin olmayan script ile kapatilamaz, tek yol bir kez onaylamak
    if admin_mi() or '-yuksek' in sys.argv:
        return

    argumanlar = ' '.join([f'"{os.path.abspath(__file__)}"'] + sys.argv[1:] + ['-yuksek'])
    sonuc = ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, argumanlar, None, 1)
    if sonuc <= 32:
        print('yonetici yetkisi alinamadi, kurulum iptal')
        time.sleep(5)
    else:
        uac_onayla()
    sys.exit()


def en_son_kurulum_dosyasi():
    indirme_klasoru = os.path.join(os.path.expanduser('~'), 'Downloads')
    dosyalar = glob.glob(os.path.join(indirme_klasoru, '**', '*.exe'), recursive=True)
    dosyalar += glob.glob(os.path.join(indirme_klasoru, '**', '*.msi'), recursive=True)
    dosyalar = [d for d in dosyalar if not d.endswith(('.crdownload', '.part'))]
    if not dosyalar:
        return None
    return max(dosyalar, key=os.path.getmtime)


def surec_calisiyor_mu(isim):
    cikti = subprocess.run(['tasklist', '/FI', f'IMAGENAME eq {isim}', '/NH'],
                           capture_output=True, text=True).stdout
    return isim.lower() in cikti.lower()


def kurulumu_bekle(isim, saniye):
    bitis = time.time() + 30
    while time.time() < bitis:
        if surec_calisiyor_mu(isim):
            break
        time.sleep(1)

    bitis = time.time() + saniye
    while time.time() < bitis:
        if not surec_calisiyor_mu(isim):
            return True
        time.sleep(2)
    return False


def terminal_ac():
    pyautogui.hotkey('win', 'r')
    time.sleep(0.8)
    pyautogui.write('powershell -NoExit', interval=0.03)
    pyautogui.press('enter')
    time.sleep(4)


def uac_onayla():
    # guvenli masaustundeki UAC ekrani ekran goruntusu ile gorunmez,
    # varsayilan buton Evet oldugu icin enter ile onaylanir
    time.sleep(UAC_BEKLEME)
    pyautogui.press('enter')
    time.sleep(2)


kendini_yonetici_yap()

dosya = en_son_kurulum_dosyasi()

if not dosya:
    print('Downloads klasorunde kurulum dosyasi bulunamadi')
else:
    print(f'bulunan dosya: {dosya}')

    if not admin_mi():
        uac_onayla()

    terminal_ac()
    pyautogui.write(KOMUT, interval=0.01)
    pyautogui.press('enter')

    isim = os.path.basename(dosya)
    if kurulumu_bekle(isim, KURULMA_SURESI):
        print('tamamlandi')
    else:
        print(f'sure doldu, {isim} hala calisiyor')

    input('\nkapatmak icin Enter tusuna bas')
