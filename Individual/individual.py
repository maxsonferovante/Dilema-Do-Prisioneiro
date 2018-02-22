import random



class Individual(object):
    def __init__(self,chromosome= []):
        self.__score = 0.0
        self.__chromosome = chromosome or self.__makeChromosome()

    def getLength(self):
        return len(self.__chromosome)

    def getScore(self):
        return self.__score

    def getChromosome(self):
        return self.__chromosome

    def setScore(self, score):
        if score > 0:
            self.__score = score
        else:
            raise "Not acceptable negative score"

    def setChromosome(self, chromosome):
        if chromosome:
            self.__chromosome = chromosome
        else:
            raise "Empty Chromosome Not Acceptable"

    chromosome = property(fget=getChromosome, fset=setChromosome)

    def __makeChromosome(self):
        chromosome_synthetized = [random.choice( [0,1]) for gene in range(67)]
        return chromosome_synthetized

    def evaluate(self):
        """
        Cada cromossomo jogará a estratégia dele contra "sempre denunciar"
        ao longo de 100 rodadas.
        """
        punctuation_1, punctuation_2  = 0,0
        for rodada in range(100):
            if rodada < 3:
                choice = self.chromosome[(len(self.chromosome)-rodada)-1]
            else:
                choice = random.choice(self.chromosome[:64])

            if choice == 1:
                punctuation_1 += 1
                punctuation_2 += 1
            else:
                ##Nesse caso o Individuo não deve recompensa por coperar, logo foi o "enganado".
                punctuation_2 += 5

        self.__score = punctuation_1

    def crossover(self,mate):
        return self.__twopoint(mate)

    def mutate(self,gene):
        self.__pick(gene)

    def __twopoint(self, other):
        cut_one = self.__pickPivots()
        cut_two = self.__pickPivots()
        while cut_one > cut_two:
            cut_two = self.__pickPivots()
        def mate(c1,c2):

            child = c1.__class__(
                c1.__chromosome [:cut_one]+c2.__chromosome [cut_one:cut_two] + c1.chromosome[cut_two:]
            )
            return  child
        return mate(self, other), mate(other, self)

    def __pick(self,point):
        cut = self.__pickPivots()
        self.__chromosome[cut] = int (not self.__chromosome[cut])

    def __pickPivots(self):
        return random.choice(
            [i for i in range(67)]
        )
        # Returns string representation of itself

    def __repr__(self):
        return "score %s Pts" % self.__score

        # The comparison method with other individual
        # @param other: The other individual that will be compared.

    def __eq__(self, other):
        return (self.getScore() == other.getScore())

    def __ne__(self, other):
        return (self.getScore() != other.getScore())

    def __lt__(self, other):
        return (self.getScore() < other.getScore())

    def __le__(self, other):
        return (self.getScore() <= other.getScore())

    def __gt__(self, other):
        return (self.getScore() > other.getScore())

    def __ge__(self, other):
        return (self.getScore() >= other.getScore())

        # Creates a replicate of itself.

    def copy(self):
        clone = Individual(self.chromosome)
        clone.score = self.getScore()
        return clone
