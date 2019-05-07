import random

'''
kan fortfarande göra conektions bakåt, detta är probelm!!
'''

class Node:
    def __init__(self):
        self.constant = 0
        self.value = 0
        self.generationLife = 0
        self.conections = []

class Conection:
    def __init__(self):
        self.toNode = None
        self.multValue = 0


inputLayer = []
hiddenLayer = []
outputLayer = []

def mutateAddConection(inputLayer, hiddenLayer, outputLayer):
    newConectionFrom = random.randrange(0, len(inputLayer) + len(hiddenLayer) - 1, 1)
    newConectionTo = random.randrange(0, len(hiddenLayer) + len(outputLayer) - 1, 1)
    newMultValue = random.randrange(-1, 1, 0.1)
    nodeToConectTo = None
    if newConectionTo < len(hiddenLayer):
        nodeToConectTo = hiddenLayer[newConectionTo]

    else:
        nodeToConectTo = outputLayer[newConectionTo - len(hiddenLayer)]

    newConection = Conection()
    newConection.toNode = nodeToConectTo
    newConection.multValue = newMultValue

    if newConectionFrom < len(inputLayer):
        inputLayer[newConectionFrom].conections.append(newConection)

    else:
        hiddenLayer[newConectionFrom - len(inputLayer)].conections.append(newConection)


#Ej klar fungerar ej
'''
def mutateAddNode(inputLayer, hiddenLayer, outputLayer):
    newNode = Node()
    newNode.constant = random.randrange(-2, 2, 0.1)
    newConectionFrom = random.randrange(0, len(inputLayer) + len(hiddenLayer) - 1, 1)
'''

def mutateNode(inputLayer, hiddenLayer):
    nodeToMutate = random.randrange(0, len(inputLayer) + len(hiddenLayer) - 1, 1)
    if nodeToMutate < len(inputLayer):
        node = inputLayer[nodeToMutate]
        node.constant = node.constant * random.randrange(-2, 2, 0.1)
        inputLayer[nodeToMutate] = node

    else:
        node = hiddenLayer[nodeToMutate - len(inputLayer)]
        node.constant = node.constant * random.randrange(-2, 2, 0.1)
        hiddenLayer[nodeToMutate] = node

def mutateConection(inputLayer, hiddenLayer):
    nodeToMutate = random.randrange(0, len(inputLayer) + len(hiddenLayer) - 1, 1)
    if nodeToMutate < len(inputLayer):
        node = inputLayer[nodeToMutate]
        conections = node.conections
        indexForConectionToMutate = random.randrange(0, len(conections) - 1, 1)
        conectionToMutate = conections[indexForConectionToMutate]
        conectionToMutate.multValue = conectionToMutate.multValue * random.randrange(-2, 2, 0.1)
        conections[indexForConectionToMutate] = conectionToMutate
        node.conections = conections
        inputLayer[nodeToMutate] = node

    else:
        node = hiddenLayer[nodeToMutate - len(inputLayer)]
        conections = node.conections
        indexForConectionToMutate = random.randrange(0, len(conections) - 1, 1)
        conectionToMutate = conections[indexForConectionToMutate]
        conectionToMutate.multValue = conectionToMutate.multValue * random.randrange(-2, 2, 0.1)
        conections[indexForConectionToMutate] = conectionToMutate
        node.conections = conections
        hiddenLayer[nodeToMutate] = node
