
def population_calc(num_months, k_constant):
    monthly_population = []
    for i in range(num_months):
        if len(monthly_population) < 2:
            new_pop = 1
        else:
            new_pop = monthly_population[-1] + k_constant*monthly_population[-2]
        monthly_population.append(new_pop)

    return monthly_population[-1]

n = 35
k = 2

print(population_calc(n,k))
