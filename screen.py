import pyautogui
import time

pyautogui.FAILSAFE = True
uyglar = {
    'whatsapp':(263,25),
    'google':(632,68)
}

    


def screen():
    getScreen = pyautogui.size()
    print(f"Ekran Çözünürlüğü: {getScreen}")
    return getScreen

def keyboard():
    # 2 kez dönecek döngü (0 ve 1 değerlerini alır)
    #for i in range(2):
    pyautogui.hotkey('alt', 'tab')


# Ekran bilgisini al
#current_screen = screen()


def mouse():
    #move_mouse = pyautogui.moveTo(861,79)
    pos_mouse = pyautogui.position()
    print(pos_mouse)


def click_mouse(x,y):
    click = pyautogui.click(x=263, y=25, clicks=1, interval=1, button='left')


def type_kb():
    write = pyautogui.typewrite('bu bir testtir ne kadar hizli yazicak deniyorum aaaaaasdadakjsjd akjsdh aksjdh askdjha sdkjh\n', interval=0.3)
# Eğer ekran boyutu başarıyla alındıysa keyboard() fonksiyonunu çağır





sec()

if current_screen:
    keyboard() #alt tab atio 
    time.sleep(2.5) #2.5 saniye bekliyor sonraki islemden once
    mouse() #mouse pos cord aliyor
    click_mouse() #istenilen kordinata tikliyor
    type_kb() #istenilen yaziyi yaziyor
