
#Add additional mass 
add_object='yes'

while add_object.lower() =='yes': 
    mass= float(input("Enter Object's Mass:"))
    format(mass, '.2f')
       

    #Input Validation
    while mass <= 0:
        mass= float(input("ERROR: Re-enter Mass:"))

    #Calculate Weight
    weight= mass * 9.8
    
    #Print weight
    print("The object's weight is",format(weight,'.2f'))

    #Check Weight
    if weight > 1000:
        print("The object is too heavy.")
    elif weight < 10:
        print("The object is too light.")

    add_object= input("Type 'yes' to enter another mass:")

    

    

    

          
    
    
     
    

