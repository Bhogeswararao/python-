animal={1:'lion',2:'tiger',3:'horse'}
print(animal)
animal[2]='fox'
print(animal)
animal[4]='tiger'
print(animal)
animal['five'] ='lion'
print(animal)
print(type(animal))
print(animal.keys())
print(animal.values())
animal.pop(3)
print(animal)