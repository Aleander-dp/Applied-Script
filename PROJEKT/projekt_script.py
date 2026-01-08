import platform

system = platform.system()

def Hitta_operativsystem():

    if system == "Windows" :
        print("||---------------------------------------------------||")
        print(f"Operativsystemet {system} har identifierats.")
        print("||---------------------------------------------------||")
    elif system == "Linux":
        print(f"")
    elif system == "Darwin":
        print(f"")
    else:
        print("||---------------------------------------------------||")
        print("Kan inte indentifiera operativsystem, Avslutar process.")
        print("||---------------------------------------------------||")

