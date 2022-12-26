"""Tribbles are a loveable species of alien pet renowned for their fecundity. Their high rate of reproduction can pose a problem for space stations, however, which rely on a predictable load on their life support systems. Given the information below, write a recursive function breed(t, d) which calculates the total number of tribbles there will be in d days, given an initial number of t tribbles, assuming all t of them breed in the first day.
• Each tribble breeds only once, exactly one day after it was born, as tribbles are born pregnant.
• On even number days, each breedable tribble has exactly four offspring. On odd numbered days, each breedable tribble has exactly three offspring.
• Tribbles do not die of natural causes. They have cellular regeneration abilities which evolved naturally due to the frankly ridiculous hostility of their home planet’s natural environment. This is also why they breed so rapidly.
• Optimal breeding conditions are secured for all tribbles by their overpowering cuteness.
• If the simulation is run for 0 days, assume no tribble reproduction has occured."""

def breed(t,d):
    # on day 0, nobody breeds
    if d == 0:
        return t
    if d == 1:
        return t * 4
    # if the day is even, each new tribble born in the previous day produces 4 offsprings
    if d % 2 == 0:
        return breed(t,d-1) + (breed(t,d-1) - breed(t,d-2)) * 4
    # if the day is odd, each new tribble born in the previous day produces 3 offsprings
    if d % 2 == 1:
        return breed(t, d-1) + (breed(t,d-1) - breed(t,d-2)) * 3
for i in range(5):
    print(breed(100,i))