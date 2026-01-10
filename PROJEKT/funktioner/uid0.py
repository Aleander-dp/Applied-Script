def uid0_användare_check():
    uid0_användare = []

    print("||-------------------------------------||")
    print("Påbörjar [UID0] kontroll")
    print("||-------------------------------------||")
    
    try:
        with open("/etc/passwd", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) > 2 and parts[2] == "0":
                    uid0_användare.append(parts[0])


    except Exception:
        return {"error": "Kunde inte läsa /etc/passwd"}

    print("||-------------------------------------||")
    print("Avslutar [UID0] kontroll")
    print("||-------------------------------------||")

    return {
        "users": uid0_användare,
        "secure": uid0_användare == ["root"]
    }