import platform


system = platform.system()

def main():

    if system != "Linux" :
        print("||---------------------------------------------------||")
        print(f"Operativsystemet {system} har identifierats.")
        print("Script godkänns och körs.")
        print("||---------------------------------------------------||")

    else:
        print("||---------------------------------------------------||")
        print("Du har , Avslutar process.")
        print("||---------------------------------------------------||")

if __name__ == "__main__":
    main()