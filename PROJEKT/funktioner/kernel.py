import platform

# Senaste kernel
SENASTE_KERNEL = "6.18.4"

def kolla_kernel_version():

    aktuell_kernel = "okänd"
    print("||-------------------------------------||")
    print("Påbörjar [Kernel] kontroll")
    print("||-------------------------------------||")
    
    try:
        print("kontrollera senaste Kernel: versionskontroll")

        aktuell_kernel = platform.release()
        print(f"Aktuell kernel: {aktuell_kernel}")
        print(f"Senast kända kernel: {SENASTE_KERNEL}")

        if aktuell_kernel.startswith(SENASTE_KERNEL):
            print("Kernel är uppdaterad")
        else:
            print("||------------------------------------||")
            print("Varning! Kernel behöver uppdateras.")
            print("||------------------------------------||")
    
    except Exception as e:
        print("Kunde inte utföra kernel versionskontroll")

    return {
        "current": aktuell_kernel,
        "latest": SENASTE_KERNEL,
        "secure": aktuell_kernel.startswith(SENASTE_KERNEL)
    }
