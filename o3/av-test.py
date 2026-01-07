#!/usr/bin/env python3

import platform
import time

system = platform.system()

if system == "Windows":
    # Fortsätt med Windows-specifik kod
    print("Windows upptäckt. Scriptet fortsätter..")

    eicar_str = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    file_name = "AV_TEST_NOT_DANGEROUS.txt"

    with open(file_name, "w") as f:
        f.write(eicar_str)

    time.sleep(3)


    try:
        with open(file_name, "r") as c:
            fil_innehåll = c.read()
            # Kontrollera om innehållet matchar EICAR-signaturen
            if fil_innehåll == eicar_str:
                print(f"skadligt innehåll har hittats i: {file_name}!")
    except Exception as e:
        # Om ett fel uppstår här pga att filen har tagits bort eller flyttats
        print("[!!!] Filen kunde inte läsas!")
        print("[!!!] AV har tagit bort/karantänat filen.")
        print("[---] Din AV/EDR-lösning är helt fungerande och skyddar mot kända virus-signaturer.")

elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()

elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()

else:
    print(f"Okänt operativsystem ({system}). Detta script är avsett för Windows. Avbryter körning.")
    exit()

