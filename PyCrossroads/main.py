timeDoingFirstGreenLight = int(input("Введіть час горіння першого зеленого світла на світлофорі:"))
timeDoingSecondGreenLight = int(input("Введіть час горіння другого зеленого світла на світлофорі:"))
roadWidth = 4
numberOfLineAtFirstRoad = int(input("Введіть кількість ліній на першій дорозі(1-2):"))
numberOfLineAtSecondRoad = int(input("Введіть кількість ліній на другій дорозі(1-2):"))
numberOfCar = ((timeDoingFirstGreenLight*10*roadWidth*numberOfLineAtSecondRoad)/100)+((timeDoingSecondGreenLight*10*roadWidth*numberOfLineAtFirstRoad)/100)
if(numberOfLineAtFirstRoad == 1):
    print("      ║  ^  ║")
    print("      ║  ^  ║")
    print("══════╝  ^  ╚══════")
    if(numberOfLineAtSecondRoad == 2):
        print(" > > >       > > >")
    if(numberOfLineAtSecondRoad == 2):
        print(" > > >       > > >")
        print(" > > >       > > >")
    print("══════╗  ^  ╔══════")
    print('      ║  ^  ║')
    print('      ║  ^  ║')
if(numberOfLineAtFirstRoad == 2):
    print("      ║  ^ ^  ║")
    print("      ║  ^ ^  ║")
    print("══════╝  ^ ^  ╚══════")
    if(numberOfLineAtSecondRoad == 1):
        print(" > > >         > > >")
    if(numberOfLineAtSecondRoad == 2):
        print(" > > >         > > >")
        print(" > > >         > > >")
    print("══════╗  ^ ^  ╔══════")
    print('      ║  ^ ^  ║')
    print('      ║  ^ ^  ║')
