worldPopulation = 8_000_000_000
growthRate = 9

print("YEAR     ANTICIPATED-P       NUMERICAL-INCREASE")
for year in range(1, 101):
    numericalIncrease = growthRate / 100 * worldPopulation
    worldPopulation = worldPopulation + numericalIncrease
    print('{0:4d}       {1:.2f}         {2:.2f}'.format(year,     worldPopulation,       numericalIncrease))
