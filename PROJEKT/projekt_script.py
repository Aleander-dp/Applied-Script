import platform


system = platform.system()

def main():

    if system != "Linux" :
        print("||---------------------------------------------------||")
        print(f"Operativsystemet {system} har identifierats.")
        print("Script nekas. Linux krävs för detta script.")
        print("||---------------------------------------------------||")

    else:
        print("||---------------------------------------------------||")
        print(f"Du har operativsystemet {system}.")
        print("Script körs.")
        print("||---------------------------------------------------||")

if __name__ == "__main__":
    main()
