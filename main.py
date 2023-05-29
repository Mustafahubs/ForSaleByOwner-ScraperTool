# Import class from forSaleByOwner file
from forSaleByOwner import ForSaleByOwner

# Create Class object and calling it's method run to initialize the processing
if __name__ == '__main__':

    # Take user input (search keywords) and pass it to the class constructor
    searchAddress = input('Enter your address: ')
    realEstateTool = ForSaleByOwner(searchAddress)
    realEstateTool.run()
