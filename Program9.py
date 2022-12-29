option=0

def menu():
    #menu
    print()
    print('Below is the option menu:')
    print()
    print('1. Convert to kilometers')
    print()
    print('2. Convert to inches')
    print()
    print('3. Convert to feet')
    print()
    print('4. Quit the program')
    print()

def meters():
    #meters stored as distance, passed for validation
     dist=float(input('Please enter a distance in meters:'))
     dist=valid(dist)
     return dist
    
def select():
    #select from menu
    select=int(input('Enter your choice from the menu:'))
    #validate
    while select not in [1,2,3,4]:
        select= int(input('Error: Please choose an option from the menu:'))    
    return select

    #convert to kilometers
def show_kilometers(dist): 
    kilo=(dist)*0.001
    print(dist,'meters equals',kilo,'kilometers.')

    #convert to inches
def show_inches(dist):
    inch=dist*39.37
    print(dist,'meters equals',inch,'inches.')
    
    #convert to feet
def show_feet(dist):
    feet=dist*3.281
    print(dist,'meters equals',feet,'feet.')

    #if option==4, quit program
def end():
    print('Thank you for using this program. Goodbye.')

    #validate distance 
def valid(dist):
    while dist < 0:
        dist= int(input('Error: Please re-enter a positive number:'))
    return dist

def main():
    #collect meters
    dist=meters()
    #display menu
    menu()
    #convert based on selection
    option=int(select())
    while option != 4:
        if option == 1:
            show_kilometers(dist)
        elif option == 2:
            show_inches(dist)
        elif option == 3:
             show_feet(dist)
        print()
        #select again
        option=int(select())
        
    if option ==4:
        end()
       
                
main()    
    
