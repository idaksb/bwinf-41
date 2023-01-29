
# Definition von Variablen
player1 = [[1]]
player2 = [[2]]
data = open("huepfburg4.txt")  
jumps = [] 
time = 0

# Methode zu Überprüfung, ob die Spieler auf dem selben Feld stehen
def controll():
    for i in player1:
        for j in player2:
            if i[-1] == j[-1]:
                return i,j

# Umwandeln von Data in eine Liste
for line in data:
    jumps = jumps+[line[0:len(line)-1]]

# Nutzen der Ersten Zeile der Liste um eine maxmile Länge der Simulation zu bestimmen
counts = jumps[0].split()
counts = int(counts[0])
often = (counts*counts)/2+counts # often = maximale Länge

status = "main"

# Starten der Simulation
while status == "main":
    time = time +1
    # für jedes Feld auf dem Spieler 1 stehen kann, werden die nächsten möglichen Felder bestimmt
    extra = []
    for i in player1:
        for j in jumps:
            j = j.split()
            first = int(j[0])
            second = int(j[1])
            if first == i[-1]:
                extra = extra+[i+[second]]
    player1 = extra

    # das gleiche für Spieler 2
    extra = []
    for i in player2:
        for j in jumps:
            j = j.split()
            first = int(j[0])
            second = int(j[1])
            if first == i[-1]:
                extra = extra+[i+[second]]
    player2 = extra

    # alle mehrfach auftretenden Zielfelder werden gelöscht
    x = 0
    for i in player1:
        y=0
        x=x+1
        for j in player1:
            y=y+1
            if i[-1] == j[-1] and x != y:
                del player1[y-1]

    # dito für Spieler 2
    x = 0
    for i in player2:
        y=0
        x=x+1
        for j in player2:
            y=y+1
            if i[-1] == j[-1] and x != y:
                del player2[y-1]

    # Überprüfung, ob beide auf dem selben Feld stehen können
    ergebniss = controll()
    if ergebniss != None:
        status = "end"
    # Test, ob die Simulation beendet werden soll    
    if time == counts+1:
        status = "stop"

# Ergebnisausgabe
if status == "stop":
    print("leider gibt es keine möglichkeit")

if status == "end":
    player1_springt = str(ergebniss[0])
    print("Spieler 1 springt " + player1_springt)
    player2_springt = str(ergebniss[1])
    print("Spieler 2 springt " + player2_springt)

