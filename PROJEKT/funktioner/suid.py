import subprocess
import time


def suidkoll():

    suid_files = []
    print("||-------------------------------------||")
    print("Påbörjar [SUID] kontroll")
    print("||-------------------------------------||")
    
    try:
        i = 3
        result = subprocess.run(
            ["find", "/", "-perm", "-4000", "-type", "f"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True
        )
        
        
        suid_files = result.stdout.strip().split("\n")

        if suid_files and suid_files[0] != "":
            print("[!] Följande filer har SUID-bit satt:")
            for file in suid_files:
                print(f"    {file}")
        
        else:
            print("||--------------------------------------||")
            print("Hittade inga SUID filer")
            print("fortsätter om 3 sekunder")
            print("||-------------------------------------||")
            while i >= 0:
                time.sleep(1)
                i = i - 1
                print(f"...{i} sekund(er)")               
                if i == 0:
                    break    
        return [f for f in suid_files if f] 
    
    except Exception as e:
        
        print("||-------------------------------------||")
        print("[[Error]]")
        print("Kunde inte utföra SUID kontroll.")
        print("||-------------------------------------||")
        return []
    

        

