#developed by Ekin Şuataman
from __future__ import print_function
from simpleai.search import SearchProblem
from simpleai.search.viewers import WebViewer
from simpleai.search.local import genetic, hill_climbing, hill_climbing_random_restarts

import random

list_of_weights= []
list_of_values = []

numberOfItems = int(input("How many items will you enter?"))
knapsack_capacity = int(input("What will be knapsack_capacity(Bag capacity)?"))

for i in range(numberOfItems):
    list_of_weights.append(input("Enter the {}.items's weight : ".format(i+1)))
    list_of_values.append(input("Enter the {}.items's value : ".format(i+1)))

weights = tuple(list_of_weights)
values = tuple(list_of_values)

print('Weights :' , weights , 'Values :' , values)

def Converting(string): 
    lists=[] 
    lists[:0]=string 
    return lists 

def list_to_string(s):
    listToStr = ''.join(map(str, s))
    return listToStr

class Knap_Sack(SearchProblem):

    def generate_random_state(self):

        state = ''
        letter = '0','1'
        for i in range(numberOfItems):
            state = state + random.choice(letter)
        return state

    def actions(self, state):
        listOfAction  = []
        for i in range(len(state)):
            listOfAction.append(i+1)
        a = list_to_string(listOfAction)
        return a

    def value(self, state):
        sum_w = 0
        sum_v =  0
        for i in range(numberOfItems):
            if(state[i] == '1'):
                sum_w = sum_w + int(weights[i])
                sum_v = sum_v + int(values[i])
        if(sum_w <= knapsack_capacity):
            return sum_v
        else:
            return 0

    def result(self, state, action):
        State_list = Converting(state)
        r = int(action)
        if(State_list[r-1] == '0'):
            State_list[r-1] = '1'
            state = list_to_string(State_list)
            return state
        elif(State_list[r-1] == '1'):
            State_list[r-1] = '0'
            state = list_to_string(State_list)
            return state

    def crossover(self, state1, state2):
        part = random.randint(1, numberOfItems - 1)
        
        crossover_f_state1 = state1[:part]

        crossover_s_state2 = state2[part:]

        crossover_newstate = crossover_f_state1 + crossover_s_state2

        return crossover_newstate

    def mutate(self, state):
        mut_number = random.randint(0, numberOfItems - 2)
        if(state[mut_number] == 0):
            state[mut_number] = 1
        elif(state[mut_number] == 1):
            state[mut_number] = 0
        return state
print("Choose to algorithms.")
print("Enter 1 for Hill climbing")
#Requires: actions, result and value.
print("Enter 2 for Hill climbing Random Restarts")
#Requires: actions, result, value, and generate_random_state.
print("Enter 3 for Genetic")
#Requires: generate_random_state, crossover, mutate and value.
#------------------------------------------------------------------------------------------
while True:
    x = int(input("Which one? "))
    if x == 1:
        initial_type = int(input("\nEnter 1 to manually enter the initial state, 2 to randomize: "))
        if(initial_type == 1):
            initial_state = input("Please enter (e.g. 10101)initial state: ")  
            while True:               
                if(numberOfItems == len(initial_state)):
                    initial_state_size = 1                
                    for x in range(numberOfItems):
                        if(initial_state[x] == '0' or initial_state[x] == '1'):
                            continue
                        else:
                            print("Wrong entry")
                            initial_state_size = 0
                            break 
                    if initial_state_size == 1:
                        problem = Knap_Sack(initial_state)
                        result = hill_climbing(problem, viewer = WebViewer())
                        print(result.state)
                        print(result.path())
                        print('Stats : ')
                        print(WebViewer().stats)
                    elif initial_state_size == 0:
                        print("No value other than zero and one is entered.")
                        initial_state = input("Please enter (e.g. 10101)initial state: ")
                        continue
                else:
                    print("You entered wrong")
                    print("The value you entered must be combined.")
                    print("And its size has to be equal to the item number.")
                    initial_state = input("Please enter (e.g. 10101)initial state: ")
                    continue
        elif(initial_type == 2):
            initial_state = ''
            letter = '0' , '1'
            for i in range(numberOfItems):
                initial_state = initial_state + random.choice(letter)
            problem = Knap_Sack(initial_state)
            result = hill_climbing(problem, viewer = WebViewer())
            print(result.state)
            print(result.path())
            print('Stats : ')
            print(WebViewer().stats)
        else:
            print("You entered incorrectly ...")
#------------------------------------------------------------------------------------------
    elif x == 2:
        problem = Knap_Sack(initial_state = None)
        result = hill_climbing_random_restarts(problem, 10, viewer=WebViewer())
        print(result.state)
        print(result.path())
        print('Stats : ')
        print(WebViewer().stats)
#------------------------------------------------------------------------------------------
    elif x == 3:
        problem = Knap_Sack(initial_state=None)
        result = genetic(problem, population_size=100, mutation_chance=0.1, iterations_limit=0, viewer=WebViewer())
        print(result.state)
        print(result.path())
        print('Stats : ')
        print(WebViewer().stats)
#------------------------------------------------------------------------------------------
    if x == 1 or x == 2 or x == 3:
        print("The End") 
        print("Developed by Ekin Şuataman, Mert Dumanlı and Ege Aydınoğlu")
        break
#------------------------------------------------------------------------------------------
    else:
        print("Wrong value entered, please restart again...")