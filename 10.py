import random
import math
from deap import base, creator, tools, algorithms

# Create fitness class (maximize)
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Create individual class (chromosome)
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator: random int between 0 and 100
toolbox.register("attr_int", random.randint, 0, 100)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_int, 2)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Fitness function
def fitness_func(individual):
    x, y = individual

    # Constraint handling
    if x + y > 120:
        return (-1000,),
    
    val = math.sin(x) * math.cos(y)
    return (val,)

toolbox.register("evaluate", fitness_func)
toolbox.register("mate", tools.cxUniform, indpb=0.5)
toolbox.register("mutate", tools.mutUniformInt, low=0, up=100, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)

    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("max", max)
    stats.register("avg", lambda x: sum(x) / len(x))

    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.6, mutpb=0.1, ngen=30, 
                                   stats=stats, halloffame=hof, verbose=True)

    best = hof[0]
    print("\nBest individual:", best)
    print(f"Best fitness: {fitness_func(best)[0]:.6f}")

if __name__ == "__main__":
    main()
