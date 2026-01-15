# Lösenordsgenererare + hashvärden

I övning nummer 2 so kommer vi jobba med en lösenordgenerarare och hash värden.

Syftet med övningen är att skapa ett script som generarar lösenord med hashvärden. Dessa hashvärden kommer vi sedan att försöka knäcka med hashcat för att se om vi kan få tillbaka lösenordet via hashvärdet.

## Användning

Kör ovning2_script för att generara lösenord med hashvärden

```bash
chmod +x ovning2_script.py
./ovning2_script.py
```
Dessa sparas i ovning2_hashvarden.txt filen

Kör sedan ovning2_hashcat.sh

```bash
chmod +x ovning2_hashcat.sh
./ovning2_hashcat.sh
```
Detta ger tillbaka de orginella lösenorden via hashvärdet.
 
