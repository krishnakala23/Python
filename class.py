class car:
    '''car task'''
    def __init__(c1,make,model,year):
        c1.make=make
        c1.model=model
        c1.year=year
    def start(c1):
        print("car is starting....")
    def stop(c1):
        print("car is stoping....")    
car1=car("make1","model x",1985)
print(car1.make,car1.model,car1.year)
car1.start()
car1.stop()
