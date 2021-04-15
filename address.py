def address_book():

    address_book = {}
    
    while True:

        name = input('What is your name?')   

        if name.lower() == 'quit':
            
            break

        else:

            address = input('What is your address?')

            if address.lower() == 'quit':
                
                break
                
            else:
                
                address_book[name] = address
            
    print(address_book)

address_book()