import platform

# Senaste kernel
SENASTE_KERNEL = "6.18.4"

def kolla_kernel_version():
    
    
    try:
        print("kontrollera senaste Kernel: versionskontroll")

        current_kernel = platform.release()
        print(f"Aktuell kernel: {current_kernel}")
        print(f"Senast kända kernel: {SENASTE_KERNEL}")

        if current_kernel.startswith(SENASTE_KERNEL):
            print("Kernel är uppdaterad")
        else:
            print("||------------------------------------||")
            print("Varning! Kernel behöver uppdateras.")
            print("||------------------------------------||")
    
    except Exception as e:
        print("Kunde inte utföra kernel versionskontroll")

kolla_kernel_version()