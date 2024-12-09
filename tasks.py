import time
import library

def ulepszaj(is_running):
    while is_running:
        note = "Rozwijam wiedzę o nowych technikach programowania i narzędziach."
        library.zapisz_do_biblioteki(note)
        time.sleep(10)

def penetruj(is_running, target):
    while is_running:
        if not target:
            break
        note = f"Penetruję cel: {target}. Analizuję dziury w ich murach."
        library.zapisz_do_biblioteki(note)
        time.sleep(15)

def zaczaruj(is_running, task):
    while is_running:
        if not task:
            break
        note = f"Tworzę zaczarowane rozwiązanie: {task}."
        library.zapisz_do_biblioteki(note)
        time.sleep(20)
