import platform
from funktioner.suid import suidkoll
from funktioner.kernel import kolla_kernel_version

system = platform.system()

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
            print("Script körs.")
            print("||---------------------------------------------------||")

            suid()

            kernel()

            print("Kontroller utförda... [suid] [kernel]")
            print("Avslutar")
    
    except Exception as e:
        print("Ett fel har uppstått, avslutar.")
        exit()


if __name__ == "__main__":
    main()