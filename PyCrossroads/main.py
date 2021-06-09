timeDoingFirstGreenLight = int(input("Введіть час горіння першого зеленого світла на світлофорі:"))
timeDoingSecondGreenLight = int(input("Введіть час горіння другого зеленого світла на світлофорі:"))
roadWidth = 4
numberOfLineAtFirstRoad = int(input("Введіть кількість ліній на першій дорозі:"))
numberOfLineAtSecondRoad = int(input("Введіть кількість ліній на другій дорозі:"))
numberOfCar = ((timeDoingFirstGreenLight*10*roadWidth*numberOfLineAtSecondRoad)/100)+((timeDoingSecondGreenLight*10*roadWidth*numberOfLineAtFirstRoad)/100)
