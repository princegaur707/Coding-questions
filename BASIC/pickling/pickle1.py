import pickle #pickling means preserving and storing(built in module)
#Pickling a python project
cars = ["Audi","BMW","Ferrari","Harryti Tuzuki"]
file = "mycar.pkl"
fileobj= open(file,'wb')
pickle.dump(cars,fileobj)#(object we wanna pack , fileobject)
fileobj.close()


