import os
import uuid
import socket
import time
from os.path import expanduser

version = "1.3"
cls = lambda: os.system("cls" if os.name == "nt" else "clear")
os.system("title Verio Screensharing Assistant %s" %version if os.name == "nt" else "pass")
os.system("color 03" if os.name == "nt" else "pass")

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


def menu():
    cls()
    logo()

    print("\n\n")
    print("                                              [ 1 ] Scanner")
    print("                                              [ 2 ] Tools")
    print("                                              [ 3 ] OS Information")
    print("                                              [ C ] Copyright")
    print("                                              [ V ] About\n\n\n\n\n\n")
    choice = input(">> ").lower()
    if not choice:
        menu()

    if choice == "1":
        scanner()

    elif choice == "2":
        tools()

    elif choice == "3":
        info()

    elif choice == "c":
        cc()

    elif choice == "v":
        creds()

    else:
        print("\nPlease make a valid selection.")
        os.system("timeout 2 >nul 2>&1")
        menu()


def scanner():
    cls()
    logo()

    print("\n\n")
    print("                                              [ 1 ] .exe Scanner")
    print("                                              [ 2 ] .jar Scanner")
    print("\n\n\n\n\n\n")
    print("                                                        [ x ]\n")

    choose = input(">> ").lower()
    if not choose:
        scanner()

    if choose == "1":
        cls()
        os.system('powershell -Command "Get-Childitem -path $Directory -Recurse -Include *.exe')
        print("\n")
        os.system("timeout -1 >nul 2>&1")
        scanner()

    elif choose == "2":
        cls()
        os.system('powershell -Command "Get-Childitem -path $Directory -Recurse -Include *.jar')
        print("\n")
        os.system("timeout -1 >nul 2>&1")
        scanner()

    elif choose == "x":
        menu()

    else:
        print("\nPlease make a valid selection.")
        os.system("timeout 2 >nul 2>&1")
        scanner()


def tools():
    cls()
    logo()

    print("\n\n")
    print("                                              [ 1 ] Process Hacker 2")
    print("                                              [ 2 ] Luyten")
    print("                                              [ 3 ] Search Everything")
    print("                                              [ 4 ] UserAssistView")
    print("                                              [ 5 ] Last Activity Viewer")
    print("\n\n\n")
    print("                                                        [ x ]\n")

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
        print("\nPlease make a valid selection.")
        os.system("timeout 2 >nul 2>&1")
        tools()


def info():
    cls()
    logo()

    print("\n\n")
    print("                                              _________________________\n")
    os.system("echo                                                  Windows ^> %OS%")
    os.system("echo                                                  Hostname ^> %username%")
    os.system("echo                                                  Nickname ^> %s" %nickname)
    os.system("echo                                                  HWID ^> %s" %hwid)
    print("                                              _________________________\n\n\n\n")

    os.system("timeout -1 >nul 2>&1")
    menu()


def cc():
    cls()
    logo()

    print("\n\n")
    print("                                              Copyright (C) 2020 Helix.")
    print("                                                 All Rights Reserved.\n\n\n\n\n\n\n\n\n")

    os.system("timeout -1 >nul 2>&1")
    menu()


def creds():
    cls()
    logo()

    print("\n\n")
    print("                                              Made by splars#1252 with <3")
    print("                                                    Credits to Mvk#0349\n")
    print("                                              https://www.youtube.com/splars")
    print("                                              https://namemc.com/profile/Splars")
    print("                                              https://github.com/splarsxd\n\n\n\n\n")

    os.system("timeout -1 >nul 2>&1")
    menu()

menu()
