anzahlTests = float(input("Wie viele Tests hattest du schon? "))
noteJetzt = float(input("Welche Note hast du jetzt? "))
noteGewollt = float(input("Welche Note möchtest du?"))
noteSumme = noteJetzt * anzahlTests
newAnzahlTests = anzahlTests + 1
noteGesucht = noteGewollt * newAnzahlTests - noteSumme

if noteGesucht <= 6:
    print("Du kannst es noch schaffen!")
    print("Du brauchst noch eine " + str(noteGesucht) + " für eine " + str(noteGewollt))
elif noteGesucht > 6:
    print("Leider schaffst du es nicht mehr :/")
    print("Du bräuchtest eine " + str(noteGesucht) + " für eine " + str(noteGewollt))
