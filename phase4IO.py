NumTestCase = int(input())
while NumTestCase > 0:
    nm = input()
    splitNM = nm.split(" ")
    N = int(splitNM[0])
    M = int(splitNM[1])
    i = 0
    ListOfTunnels = []
    for i in range(M):
        abc = input()
        ABC = abc.split()
        a = int(ABC[0])
        b = int(ABC[1])
        c = int(ABC[2])
        ListOfTunnels.append((a, b, c))

    numberOfTreasures = int(input())

    TreasureCavesStr = input().split(" ")
    TreasureCavesInt = [int(a) for a in TreasureCavesStr]
    maxDist = int(input())

    # call functions here