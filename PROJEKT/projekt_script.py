import platform
from datetime import datetime
from funktioner.suid import suidkoll
from funktioner.kernel import kolla_kernel_version
from funktioner.uid0 import uid0_användare_check

system = platform.system()

LOG_FIL = "log/scan.log"

def log(msg):
    with open(LOG_FIL, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.now()}] {msg}\n")

def main():
    try:
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

            suidkoll()
            suid_files = suidkoll()
            log(f"SUID-filer hittade: {len(suid_files)}")
            for f in suid_files:
                log(f"SUID: {f}")

            kolla_kernel_version()
            kernel = kolla_kernel_version()
            log(f"Kernel: {kernel['current']} | Senaste: {kernel['latest']}")
            if not kernel["secure"]:
                log("VARNING: Kernel ej uppdaterad")

            uid0_användare_check()
            uid0 = check_uid0_users()
            if "error" in uid0:
                 log(uid0["error"])
            else:
                log(f"UID 0-användare: {', '.join(uid0['users'])}")
                if not uid0["secure"]:
                    log("VARNING: Fler än root har UID 0")

            print("Kontroller utförda... [suid] [kernel] [uid0]")
            print("Avslutar")
    
    except Exception as e:
        print("Ett fel har uppstått, avslutar.")
        exit()


if __name__ == "__main__":
    main()