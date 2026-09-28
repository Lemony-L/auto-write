import pyautogui
import time

pyautogui.FAILSAFE = True
uyglar = {
    'whatsapp':(263,25),
    'google':(400, 25)
}

    


def screen():
    getScreen = pyautogui.size()
    print(f"Ekran Çözünürlüğü: {getScreen}")
    return getScreen

def keyboard():
    # 2 kez dönecek döngü (0 ve 1 değerlerini alır)
    #for i in range(2):
    pyautogui.hotkey('alt', 'tab')


def mouse():
    #move_mouse = pyautogui.moveTo(861,79)
    pos_mouse = pyautogui.position()
    print(pos_mouse)


def click_mouse(x,y):
    click = pyautogui.click(x=x, y=y,clicks=1, interval=1, button='left')


def type_kb(metin):
    #write = pyautogui.typewrite('bu bir testtir ne kadar hizli yazicak deniyorum aaaaaasdadakjsjd akjsdh aksjdh askdjha sdkjh\n', interval=0.3)
    pyautogui.write(metin, interval=0.05)
    pyautogui.press('enter')
    # Eğer ekran boyutu başarıyla alındıysa keyboard() fonksiyonunu çağır

def secim_al():
    print("\nMevcut uygulamalar:", list(uyglar.keys()))
    secim = input("hangi uygulamayi kullanmak istersin: ").strip().lower()

    if secim in uyglar:
        return secim, uyglar[secim]
    else:
        print("gecersiz uygulama")
        return None,None

#ana gidisat

# Ekran bilgisini al
current_screen = screen()

secilen_uyg, kordinat = secim_al()
#kullanicidan yazilcak metni al
if current_screen and kordinat:
    yazilcak_metin = input(f"{secilen_uyg}yazilmasini istedigin metni yaz: " )
    print("islem baslatiliyor...")
    time.sleep(2.5)

    #alt tab olur
    keyboard()
    time.sleep(1)

    #secilen uygulamanin kordinatina tiklar
    click_mouse(kordinat[0], kordinat[1])
    time.sleep(0.5)

    type_kb(yazilcak_metin)
    print("islem okey")



#if current_screen:
#    keyboard() #alt tab atio 
#    time.sleep(2.5) #2.5 saniye bekliyor sonraki islemden once
#    mouse() #mouse pos cord aliyor
#    click_mouse() #istenilen kordinata tikliyor
#    type_kb() #istenilen yaziyi yaziyor
