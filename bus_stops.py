station1, station2, station3, station4 = list(map(int, input().split()))
stations_bus1 = set(range(min(station1, station2),
                          max(station1, station2) + 1))
stations_bus2 = set(range(min(station4, station3),
                          max(station4, station3) + 1))
print(len(stations_bus1 & stations_bus2))
