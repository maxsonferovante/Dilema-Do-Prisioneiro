from Environment.environment import Environment


if __name__ == "__main__":
   env = Environment(maxgenerations = 100,
                     size = 1000,
                     optimum=100,
                     crossover_rate=0.84,
                     mutation_rate= 0.20
                     )
   env.run()
