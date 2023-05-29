# Import Modules
import sys
import csv
from pyinputplus import inputInt, inputMenu
from prettytable import PrettyTable
from requests.sessions import Session


# Here is the One Class ForSaleByOwner (refrence by website) with 9 methods

class ForSaleByOwner:
    def __init__(self, searchAddress) -> None:
        # Take input from outside the class (from user before the execution)
        self.searchAddress = searchAddress
        # Ths variable to count the number of listings saved into the csv
        # So that we can break the loop on specific condition
        # Let say if we need only 200 properties data out of 300 then this variable will us to break -
        # - when we reach at 200
        self.listingCount = 1

    def makeSession(self) -> object:
        # Initialize the session
        sess = Session()

        # Base Headers for all requests
        headers = {
            'authority': 'directory.forsalebyowner.com',
            'accept': 'application/json, text/plain, */*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.forsalebyowner.com',
            'referer': 'https://www.forsalebyowner.com/',
            'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50',
        }

        # Update session with this headers return sess (session)
        sess.headers.update(headers)
        return sess

    # This function take a search keyword and return a dict of Suggestions (like a Search Engine)
    def getSlugs(self, searchKeyword: str) -> dict:
        # searchKeyword = 'loss Angeles' # Any address
        params = {'searchString': searchKeyword}

        searchResp = self.sess.get(
            'https://directory.forsalebyowner.com/search/autocomplete', params=params)

        # Check if response is 200 (Means Accessed) or not
        if searchResp.status_code == 200:
            jsonSearch = searchResp.json()
            if len(jsonSearch) > 0:
                # Return jsonObject like Dictionary if response is 200 and it not empty
                return jsonSearch

            else:
                # Response is 200 but If there are no any suggestions of a given keywords then
                # show a Info message and warning and stop script execution
                errorMsg = f"[INFO] - The Address *{searchKeyword}* don't have any Suggestions"
                tips = 'There are some tips for search:\n\t1. Make your address short\n\t2. Use City,State or County Name'
                print(errorMsg)
                print(tips)
                sys.exit()  # Stop Script
        else:
            # If Response is not 200 or any other network error then show a warning stop script execution
            errorMsg = f'[ERROR] - Could not find the search :-> {searchResp}'
            print(errorMsg)
            sys.exit()

    def chooseSlug(self, jsonSearch: dict) -> str:

        # This function will be called when the getSlugs() method successfully processes
        # and returns a dictionary of suggestions
        # Here it will display the suggestions and ask the user to Choose one suggestion by index number
        # I used PrettyTable Module to display the suggestions in Tabular format

        table = PrettyTable()  # Initialize the PrettyTable
        # Add some table fields name as Table-Header
        table.field_names = ["Index", "Slugs", "Type"]
        table.align['Slugs'] = 'l'  # Align Slugs column to left
        table.align['Type'] = 'l'   # Align Type column to left

        slugs = []  # Create a Empty list to store suggestions after parsing the given dictionary

        # Loop through the dict suggestions with their index using enumerate methods
        for index, item in enumerate(jsonSearch, start=1):
            slug = item['_source']['slug']
            type = item['_source']['type']
            slugs.append(slug)  # Add the slug to the Empty list above
            table.add_row([index, slug, type])  # Add the row to the table
        print(table)  # show slugs in table

        # Ask to choose one Suggestion by index number
        # I use pyinputplus to ask the user input and validate
        choice = inputInt(
            "Enter the number corresponding to your choice: ", min=1, max=len(slugs))
        selectedOp = slugs[int(choice) - 1]
        print(f"[INFO] - You selected: {selectedOp}")

        # Return select address text after indexing of stored list
        return selectedOp

    # This method will call after chooseSlug method Because it uses the return text of chooseSlug function
    # Here it will take a address text and a page number and return listing info in json like dict formate
    def getPageListings(self, slug: str, page: int) -> dict:

        # Parameters for payload request
        data = {
            'listing_search': {'page': page,
                               'limit': 200,
                               'slug': slug}}
        pageListingResp = self.sess.post(
            'https://directory.forsalebyowner.com/search/listings', json=data)
        if pageListingResp.status_code == 200:
            jsonListing = pageListingResp.json()

            # if everything is good then it will return listing info in json or dict
            return jsonListing
        else:
            errorMsg = f'[ERROR] - Page listing not found -> {pageListingResp}'
            print(errorMsg)

    # This function will take row (list) and save it into csv file
    def saveToCSV(self, row: list) -> None:
        with open('ForsaleByOwner.csv', 'a', encoding='utf-8', newline='') as f:
            csv.writer(f).writerow(row)

    def csvHeader(self) -> None:
        # This function will run only one time at the beginings of the script execution.
        # Here it just for csv header and it will ask delete Old data or not before write the header row
        print('[ALERT] - Deleting or Cleaning CSV Previous Data')
        cleanSheet = inputMenu(['Yes', 'No'], lettered=True)
        print(f'[INFO] - You selected {cleanSheet}')
        if cleanSheet == 'Yes':
            headerRow = ['Name', 'URL', 'Address', 'City', 'Zip',
                         'State', 'Price', 'Bath', 'Bed', 'SquareFt']
            with open('ForsaleByOwner.csv', 'w', encoding='utf-8', newline='') as f:
                csv.writer(f).writerow(headerRow)
        else:
            print('[INFO] - Appending CSV with old data')

    def extractInfo(self, jsonListing: list) -> None:
        # This function extracts information from the output of getPageListings function
        # And save the parsed information into csv file

        listingData = jsonListing['data']['listings']
        for index, item in enumerate(listingData, start=self.listingCount):
            fullName = item.get('fullName', 'None')
            price = item.get('listPrice')
            bathRooms = item.get('bathrooms')
            bedRooms = item.get('bedrooms')
            squareFt = item.get('livingArea')
            propertyId = item.get('id')
            # property URL will auto redirect by filling underscore(_)
            propertyURL = f'https://www.forsalebyowner.com/listing/_/{propertyId}'
            address = item.get('address')
            if address != None:
                fullAddress = address.get('fullStreetAddress')
                city = address.get('city')
                zipCode = address.get('postalCode')
                state = address.get('stateOrProvince')

            # Create row list of all the variables of a property
            row = [fullName, propertyURL, fullAddress, city,
                   zipCode, state, price, bathRooms, bedRooms, squareFt]
            print(f'[{index}][INFO] - ID: {propertyId} :: Property: {fullName}')
            # Send row list to the saveToCsv method to save into csv file
            self.saveToCSV(row)

            # Break the loop when the listings count reaches to listing needs
            if self.listingCount >= self.listingNeeds:
                sys.exit()
            self.listingCount += 1

    def getPagingInfo(self, jsonListing: list) -> int:
        # This function will be called after first execution to get the information about pagination -
        # - so that we can break the loop when pages are finished.
        totalItems = jsonListing['data']['paging']['totalItemCount']
        print(f'[INFO] - Found total listing items -> {totalItems}')
        if totalItems > 0:
            noOfListings = inputInt(
                '[INFO] - How many listings do you want to save?: ', min=1, max=totalItems)
            print(f"[INFO] - You Select {noOfListings} Listings ...")
            # Return the number of listings we found after first execution
            return noOfListings
        else:
            # Stop the loop execution if there is no any listings
            errorMsg = '[ERROR] - No listings are available for this Address'
            print(errorMsg)
            sys.exit()

    def run(self) -> None:
        # This our main funciton to start the execution of all the above functions
        # Here all the functions will run one by one and return the output to save in a variable -
        # - then we will use those varialbes to execut next method and so on so..

        # Call the makeSessions function to create a session
        self.sess = self.makeSession()

        # Save output (suggestions dict) into a variable
        jsonSearch = self.getSlugs(self.searchAddress)

        # Pass the JsonSearch (dict) to chooseSlug Function for Address selection
        slugText = self.chooseSlug(jsonSearch)

        # Create CSV header before saving data fields
        self.csvHeader()

        # Run until self.listingCount variable becomes equal to the self.listingNeeds in extractInfo
        # Once both variables become equal script execution will stop
        page = 1  # Increment variable for page number
        while True:
            jsonListing = self.getPageListings(slug=slugText, page=page)

            if page == 1:
                # As I mention above getPagingInfo method will execute only for one time (for first page)
                self.listingNeeds = self.getPagingInfo(jsonListing)
            self.extractInfo(jsonListing)
            page += 1

