def printdict() :
    Guests = [{"name":"ali", "occupation":"student", "age" : 20,},
            {"name":"hassan", "occupation":"businessman", "age" : 35,},
            {"name":"bilal", "occupation":"student", "age" : 19,},
            {"name":"azhar", "occupation":"teacher", "age" : 47,}]
    for Guest in Guests: 
        print(Guest["name"], end = ", ")
        print(Guest["occupation"], end = ", ")
        print(Guest["age"])
