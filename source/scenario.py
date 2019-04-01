import random


class Scenario():

    """ Packages all of the information needed to create an ethical scenario.

    Automatically construct a random scenario in which an autonomous car must
    decide whether to save the car passengers or the pedestrians.

    Args:
        sameNum (bool, optional): if True, enforces that the number of
            pedestrations is the same as the number of car passengers.

    Attributes:
        numPedestrians (int): the number of pedestrians in the crosswalk
        numPassengers (int): the number of passengers in the car
        passengers (list): list of passengers (Person objects) in the car
        pedestrians (list): list of pedestrians (Person objects) in the crosswalk
        youInCar (bool): True if you are one of the passengers in the car
        legalCrossing (bool): True if pedestrians are legally crossing
        pedsInLane (bool): True if car is currently in the same lane as
            the pedestrians (would need to switch lanes to avoid them)
    """
    # The minimum/maximum number of car passengers and pedestrians
    MIN_PASSENGERS = 0
    MAX_PASSENGERS = 4
    MIN_PEDESTRIANS = 1
    MAX_PEDESTRIANS = 4

    # The following variables are lists that represent the probabilities of
    # each feature happening. For example, in YOU_CHANCE, there is a 1 in 4
    # chance that that 'you' are in the vehicle. Similarly, in LEGAL_CROSSING_CHANCE,
    # there is a 2 in 3 chance that the pedestrians are crossing the street
    # legally (the walk sign is on)
    YOU_CHANCE = [True, False, False, False]
    LEGAL_CROSSING_CHANCE = [True, True, False]
    PEDS_IN_LANE_CHANCE = [True, False]

    def __init__(self, passengers=None, pedestrians=None, youInCar=None,
            legalCrossing=None, pedsInLane=None, sameNum=True):
        # Create a random number of pedestrians in the crosswalk
        numPedestrians = random.randint(self.MIN_PEDESTRIANS, self.MAX_PEDESTRIANS)

        # If sameNum is true, create the same number of passengers in the car
        # Otherwise, create a random number of passengers
        if not sameNum:
            numPassengers = random.randint(self.MIN_PASSENGERS, self.MAX_PASSENGERS)
        else:
            numPassengers = numPedestrians

        # DETERMINE THE PASSENGERS
        if passengers is not None:
            self.passengers = passengers
        else:
            # Create randomly generated people for passengers
            self.passengers = [Person() for numPeople in range(numPassengers)]
            # If you are a passenger in the car, replace one of the passengers with you.
            # 25% chance of you being in car
            if youInCar is not None:
                self.youInCar = youInCar
            else:
                self.youInCar = random.choice(self.YOU_CHANCE)

            if self.youInCar is True:
                # Feel free to change these attributes if you'd like.
                youPerson = Person("you")
                if numPassengers > 0:
                    self.passengers[0] = youPerson
                else:
                    self.passengers += [youPerson]

        # DETERMINE THE PEDESTRIANS
        if pedestrians is not None:
            self.pedestrians = pedestrians
        else:
            self.pedestrians = [Person() for numPeople in range(numPedestrians)]

        # Determine if the pedestrians are crossing during a walk sign
        if legalCrossing is not None:
            self.legalCrossing = legalCrossing
        else:
            self.legalCrossing = random.choice(self.LEGAL_CROSSING_CHANCE)

        # Determine if the pedestrians are in the car's CURRENT lane
        if pedsInLane is not None:
            self.legalCrossing = legalCrossing
            self.pedsInLane = pedsInLane
        else:
            self.pedsInLane = random.choice(self.PEDS_IN_LANE_CHANCE)

    def getNumPedestrians(self):
        return self.numPedestrians

    def getNumPassengers(self):
        return self.numPassengers

    def getPedestrians(self):
        return self.pedestrians

    def getPassengers(self):
        return self.passengers


    def __repr__(self):
        """ Method that helps python understand how to print a Scenario

        For example, you can now create a scenario in your code somewhere:
            scenario = Scenario()

        and then print that scenario:
            print(scenario)

        This will print a readable form of the scenario in your program
        """
        readable = 'Passengers: \n'
        for passenger in self.passengers:
            readable += '-' + str(passenger) + '\n'

        readable += '\n'
        readable += 'Pedestrians: \n'
        for pedestrian in self.pedestrians:
            readable += '-' + str(pedestrian) + '\n'
        readable += '\n'

#         if self.legalCrossing:
#             readable += 'Crossing is legal\n'
#         else:
#             readable += 'Crossing is illegal\n'
# 
#         if self.pedsInLane:
#             readable += 'Pedestrians are in your lane.'
#         else:
#             readable += 'Pedestrians are NOT in your lane.'

        return readable

    @staticmethod
    def from_string(passengers, pedestrians):
        return Scenario(
            [Person.from_string(passenger) for passenger in passengers.split(' ')],
            [Person.from_string(pedestrian) for pedestrian in pedestrians.split(' ')],
            youInCar=False,
            legalCrossing=False,
            pedsInLane=True,
        )


#-------------------------------------------------------------------------------#


class Person():

    """ Packages all the info needed for a person.

    Every scenario is composed of characters - many of which are people. Each
    of those people can contain a variety of characteristics. The Person class
    will automatically create a random person or animal.

    Attributes:
        charType (string): 'human', 'you', 'cat', 'dog'
        age (string): humans can be a 'baby', 'child', or 'adult'
        profession (string): adults are assigned a profession: 'doctor', 'CEO', 
            'unemployed', 'unknown'
        gender (string): 'male', 'female', 'nonbinary'
        bodyType (string): adults are classified as 'average', 'athletic',
            or 'overweight'
        pregnant (bool): adult women may also be pregnant. True if pregnant.
        hasCriminalPast (bool): True if has a criminal history. Can only be true 
            if the person is an adult.
        isHomeless (bool): True if person is homeless.

    """
    # The following variables not only contain the possibilities of different
    # attributes of people/animals, but also the probability with which they
    # appear. For example, CHAR_TYPES contains 'human' 4 times and 'animal'
    # just 1 time. That means that 'human' is 4x more likely to appear.

    # Choose between a human or animal
    CHAR_TYPES = ["human", "human", "human", "animal", "human"]
    # If it's an animal, choose between cat or dog
    ANIMAL_TYPES = ["cat", "dog"]
    # Possible ages of humans
    AGE_TYPES = ["baby", "child", "adult", "adult", "adult", "elderly"]
    # Possible professions of adults
    PROF_TYPES = ["doctor", "CEO", "unemployed", "unknown", "unknown", "unknown"]
    # Possible genders of humans
    GENDER_TYPES = ["male", "female", "male", "female", "male", "female", "nonbinary"]
    # Select whether a female is pregnant (currently 25% chance)
    PREGNANT_CHANCE = [True, False, False, False]
    # Select the bodytype of each non-child.
    BODYWEIGHT_CHANCE = ["overweight", "athletic", "average", "average"]
    # Select whether an adult has a criminal (felony) history
    CRIMINAL_CHANCE = [True, False, False, False, False, False, False, False]
    # Select whether a person is homeless
    HOMELESS_CHANCE = [False, False, False, True, False, False, False, False] 

    def __init__(self, charType=None, age=None, profession=None,
            gender=None, bodyType=None, pregnant=None, criminal=None, homeless=None):
        ''' Create a person by randomly selecting their attributes

        All of the parameters in this method are OPTIONAL. This means that by
        default, a random person is made if no information is given. For
        example:
            person = Person()

        However, you can also create a custom person by filling in any
        number of those parameters. For example, the following code would
        create an adult woman with an average body type, but still allow
        the program to randomly select her profession:
            person = Person(charType="human", age="adult", gender="female",
                        bodyType="average")
        '''
        self.charType = charType
        self.profession = profession
        self.age = age
        self.gender = gender
        self.bodyType = bodyType
        self.pregnant = pregnant
        self.criminal = criminal
        self.homeless = homeless

        # set type of character (human or animal?)
        if charType is None:
            self.charType = random.choice(self.CHAR_TYPES) # you is also a char type

        # If it's an animal, choose which type
        if self.charType == "animal":
            self.charType = random.choice(self.ANIMAL_TYPES)
        # If it's a person, set the characteristics
        if self.charType == "human":
            if self.age is None:
                self.age = random.choice(self.AGE_TYPES)
            if self.gender is None:
                self.gender = random.choice(self.GENDER_TYPES)
            if self.homeless is None:
                self.homeless = random.choice(self.HOMELESS_CHANCE)

            # Set adult characteristics.
            if self.age == "adult":
                if self.bodyType is None:
                    self.bodyType = random.choice(self.BODYWEIGHT_CHANCE)
                if self.gender == "female":
                    if self.pregnant is None:
                        self.pregnant = random.choice(self.PREGNANT_CHANCE)
                if self.profession is None:
                    self.profession = random.choice(self.PROF_TYPES)
                if self.criminal is None:
                    self.criminal = random.choice(self.CRIMINAL_CHANCE)

    def getCharType(self):
        return self.charType

    def getProfession(self):
        return self.profession

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getBodyType(self):
        return self.bodyType

    def isPregnant(self):
        return self.pregnant

    def isCriminal(self):
        return self.criminal

    def isHomeless(self):
        return self.homeless

    def __repr__(self):
        """ Method that helps python understand how to print a Person

        For example, you can now create a person in your code somewhere:
            person = Person()

        and then print that person to see what characteristics it has:
            print(person)
        """
        if self.charType == "human":
            readable = '['
            if self.bodyType:
                readable += self.bodyType + ' '
            if self.age:
                readable += self.age
            if self.gender:
                readable += ' ' + self.gender + ']'
            if self.profession:
                readable += ' job:' + self.profession
            if self.pregnant:
                readable += ', pregnant'
            if self.criminal:
                readable += ', has criminal history'
            if self.homeless:
                readable += ', homeless'
        else:
            readable = self.charType
        return readable

    @staticmethod
    def from_string(s):
        attr_dict = {}
        for pair in s.split(','):
            attr, val = pair.split('=')
            attr_dict[attr] = val
        if (attr_dict.get('charType', '') == 'human' and
                attr_dict.get('age', '') == 'adult' and
                attr_dict.get('gender', '') == 'female'):
            if attr_dict.get('pregnant', None) == 'True':
                attr_dict['pregnant'] = True
            else:
                attr_dict['pregnant'] = False

        return Person(**attr_dict)
