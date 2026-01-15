#!/usr/bin/env python3
# FEEDBACK - Code Review:
# 
# Bra jobbat! Koden är välstrukturerad och lätt att följa.
# 
# Förbättringsförslag:
# 1. Shebang (#!/usr/bin/env python3) är nu tillagd längst upp så scriptet kan 
#    köras direkt med ./projekt_script.py (kräver chmod +x projekt_script.py)
# 
# 2. README.md kan utökas med: Syfte/Mål, Funktion, Systemkrav och Instruktioner

import platform
import os
import sys
from datetime import datetime, date
from funktioner.suid import suidkoll
from funktioner.kernel import kolla_kernel_version
from funktioner.uid0 import uid0_användare_check

# relevanta veriabler för att scriptet ska fungera
system = platform.system()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FIL = os.path.join(BASE_DIR, "logs", "scan.log")
os.makedirs(os.path.join(BASE_DIR, "logs"), exist_ok=True)

# skapar log fil om den inte finns i mappen "logs".
if not os.path.exists(LOG_FIL):
    open(LOG_FIL, "a", encoding="utf-8").close()

#Funktion för hur information ska loggas in i log filen.
def log(msg):
    with open(LOG_FIL, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

#Funktion för start och slutmeddelandet i logfilen.
def logger(msg):
    with open(LOG_FIL, "a", encoding="utf-8") as f:
        f.write(msg)

#variabler för logmeddelanden.
datum = date.today()
start_msg = "|------------------------------------|\nLoggning startad "
slut_msg = "Loggning avslutas.\n|------------------------------------|"

def skriv_hjalp():
    print("Användning: python scan.py [alternativ]")
    print()
    print("Alternativ:")
    print("  -h        Visa denna hjälptext")
    print("  -v        Visa information om scriptet")
    print()
    print("Scriptet kontrollerar:")
    print("  - SUID-filer")
    print("  - Kernelversion och om den är uppdaterad")
    print("  - Användare med UID 0")

def skriv_info():
    print("Informationsläge (-v):")
    print("Detta script loggar säkerhetsrelaterad information till logs/scan.log")
    print("Kontroller som görs: SUID, kernelversion, UID 0-användare.")

#main funktion
def main():
    
    # hanterar flaggor
    args = [a.lower() for a in sys.argv[1:]]
    
    if "-h" in args or "-help" in args:
            skriv_hjalp()
            sys.exit(0)
    if "-v" in args or "-version" in args:
            skriv_info()
            sys.exit(0)
    
    try:
        #kollar operativsystem. Om inte "Linux", exit.
        if system != "Linux" :
            print("||---------------------------------------------------||")
            print(f"Operativsystemet {system} har identifierats.")
            print("Script nekas. Linux krävs för detta script.")
            print("||---------------------------------------------------||")
            exit()
    
        else:
            print("||---------------------------------------------------||")
            print(f"Du har operativsystemet {system}.")
            print("Script tillåts & körs.")
            print("||---------------------------------------------------||")

        #Kollar användar id.
        if os.geteuid() != 0:
            print(f"UID =  {os.geteuid()}")
            print("||---------------------------------------------------||")
            print("Du är inte en root användare. Vill du fortsätta ändå?")
            while True:
                # FEEDBACK: Lägg till .lower() för att hantera både "J" och "j"
                val = input("[J]/[N]\n")
                if val in ["j", "ja"]:
                    break
                elif val in ["nej", "n", "ne"]:
                    print("Avslutar")
                    exit()
                else:
                    print("Ogiltigt svar")

        
        #Loggar startmeddelandet + skannar datorn efter SUID-filer, loggar resultatet.
        try: 
            logger(f"\n{start_msg}" + f"{datum}" + "\n")
            suid_files = suidkoll()
            log(f"SUID-filer hittade: {len(suid_files)}")
            for f in suid_files:
                log(f"SUID: {f}")
        except Exception as e:
            log(f"Fel vid SUID-kontroll: {e}")
            print("Ett fel uppstod vid SUID-kontroll, se loggfilen för fel-information")

        #Kollar systemet efter kernel version och meddelar om den behöver uppdateras.
        try:
            kernel = kolla_kernel_version()
            log(f"Kernel: {kernel['current']} | Senaste: {kernel['latest']}")
            if not kernel["secure"]:
                log("VARNING: Kernel ej uppdaterad")
        except Exception as e:
            log(f"Fel vid Kernel-kontroll: {e}")
            print("Ett fel uppsod vid Kernel-kontroll, se loggfil för fel-information")

        #Kollar alla UID0 användare på enheten (borde bara vara en, UID0).
        try:
            uid0 = uid0_användare_check()
            if "error" in uid0:
                log(uid0["error"])
            else:
                log(f"UID 0-användare: {', '.join(uid0['users'])}")
                if not uid0["secure"]:
                    log("VARNING: Fler än root har UID 0")
        except Exception as e:
            log(f"Fel vid UID0-kontroll: {e}")
            print("Ett fel uppstod vid uid0-kontroll, se loggfil för fel-information")
        #loggar slutmeddelandet, avslutar scriptet.
        logger(slut_msg)
        print("Kontroller utförda... [suid] [kernel] [uid0]")
        print("Avslutar")
        exit()
    
    #Om fel har uppstått, printar fel till terminal.
    except Exception as e:
        print("Ett fel har uppstått:" , e)
        exit()


if __name__ == "__main__":
    main()
