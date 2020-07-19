import os
import uuid
from os.path import expanduser

version = "1.2"
os.system("title Verio Screensharing Assistant %s" %version)
os.system("color 0f")

nickname = socket.gethostname()
hwid = str(uuid.uuid1(uuid.getnode(), 0))[24:]
userfiles = expanduser("~")
os.chdir(userfiles)


def logo():
    print()
    print("                                              __     __        _                                                   ")
    print("                                              \ \   / /__ _ __(_) ___                                              ")
    print("                                               \ \ / / _ \ '__| |/ _ \                                             ")
    print("                                                \ V /  __/ |  | | (_) |                                            ")
    print("                                                 \_/ \___|_|  |_|\___/                                             ")
    print("                                                                                                                   ")


def cls():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    cls()
    logo()

    print("")
    print("")
    print("")
    print("                                              [ 1 ] Scanner")
    print("                                              [ 2 ] Tools")
    print("                                              [ 3 ] OS Information")
    print("                                              [ C ] Copyright")
    print("                                              [ V ] About")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    choose = input(">> ").lower()
    if not choose:
        menu()

    if choose == "1":
        scanner()

    elif choose == "2":
        tools()

    elif choose == "3":
        info()

    elif choose == "c":
        cc()

    elif choose == "v":
        creds()

    else:
        print("")
        print("Please make a valid selection.")
        os.system("timeout 2 >nul 2>&1")
        menu()


def scanner():
    cls()
    logo()

    print("")
    print("")
    print("")
    print("                                              [ 1 ] .exe Scanner")
    print("                                              [ 2 ] .jar Scanner")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("                                                        [ x ]")
    print("")

    choose = input(">> ").lower()
    if not choose:
        scanner()

    if choose == "1":
        cls()
        os.system('powershell -Command "Get-Childitem -path $Directory -Recurse -Include *.exe')
        print("")
        print("")
        os.system("timeout -1 >nul 2>&1")
        scanner()

    elif choose == "2":
        cls()
        os.system('powershell -Command "Get-Childitem -path $Directory -Recurse -Include *.jar')
        print("")
        print("")
        os.system("timeout -1 >nul 2>&1")
        scanner()

    elif choose == "x":
        menu()

    else:
        print("")
        print("Please make a valid selection.")
        os.system("timeout 2 >nul 2>&1")
        scanner()


def tools():
    cls()
    logo()

    print("")
    print("")
    print("")
    print("                                              [ 1 ] Process Hacker 2")
    print("                                              [ 2 ] Luyten")
    print("                                              [ 3 ] Search Everything")
    print("                                              [ 4 ] UserAssistView")
    print("                                              [ 5 ] Last Activity Viewer")
    print("")
    print("")
    print("")
    print("")
    print("                                                        [ x ]")
    print("")

    choose = input(">> ").lower()
    if not choose:
        tools()

    if choose == "1":
        os.system("start https://processhacker.sourceforge.io/downloads.php")
        tools()

    elif choose == "2":
        os.system("start https://github.com/deathmarine/Luyten/releases/tag/v0.5.4_Rebuilt_with_Latest_depenencies")
        tools()

    elif choose == "3":
        os.system("start https://www.voidtools.com")
        tools()

    elif choose == "4":
        os.system("start https://www.nirsoft.net/utils/userassist_view.html")
        tools()

    elif choose == "5":
        os.system("start https://www.nirsoft.net/utils/computer_activity_view.html")
        tools()

    elif choose == "x":
        menu()

    else:
        print("")
        print("Please make a valid selection.")
        os.system("timeout 2 >nul 2>&1")
        tools()


def info():
    cls()
    logo()

    print("")
    print("")
    print("")
    print("                                              _________________________")
    print("")
    os.system("echo                                                  Windows ^> %OS%")
    os.system("echo                                                  Hostname ^> %username%")
    os.system("echo                                                  Nickname ^> %s" %nickname)
    os.system("echo                                                  HWID ^> %s" %hwid)
    print("                                              _________________________")
    print("")
    print("")
    print("")
    print("")

    os.system("timeout -1 >nul 2>&1")
    menu()


def cc():
    cls()
    logo()

    print("")
    print("")
    print("")
    print("                                              Copyright (C) 2020 Helix.")
    print("                                                 All Rights Reserved.")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")

    os.system("timeout -1 >nul 2>&1")
    menu()


def creds():
    cls()
    logo()

    print("")
    print("")
    print("")
    print("                                              Made by splars#1252 with <3")
    print("                                                    Credits to Joey")
    print("")
    print("                                              https://www.youtube.com/splars")
    print("                                              https://namemc.com/profile/Splars")
    print("                                              https://github.com/splarsxd")
    print("")
    print("")
    print("")
    print("")
    print("")

    os.system("timeout -1 >nul 2>&1")
    menu()

menu()
