import pickle

data = {'set': {1,2,3}, 'tuple': (1,2,3)}

with open('files\\data.pkl', 'wb') as file:
    pickle.dump(data, file)

with open('files\\data.pkl', 'rb') as file:
    print(pickle.load(file))


