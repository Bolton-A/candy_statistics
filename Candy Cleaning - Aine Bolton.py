'''
Candy Cleaning - Current Version 1.3 (Updated 09/20/2022)
Developer: Aine Bolton
Started: September 15th, 2022
Purpose: This program was created to practice data-cleaning CSV (Excel) files through Python.

Function: Gathers data from candyhierarchy2017 CSV file. Uses the junkfoodblog alphabetical candy
list in order to filter what is actually a candy against unnecessary entries within 
the candyhierarchy2017 list, therefore eliminating extraneous entries.

After organizing the column titles and filtering only candy, allows the user to select which
statistics they would like to view before displaying the results.

README: Please access the README file for more information on this program and updates planned for the future.

'''

# Modules for scraping CSV file.
import csv
import pandas

# Modules for scraping and formatting data from website.
import requests
from bs4 import BeautifulSoup
import re

# Modules for fuzzy string comparison.
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# Modules for formatting terminal.
import keyboard
import os
import time

#####################################################
# Section One: Data accessing & parsing.
#####################################################

def main():

    # Access URL and build parser.
    URL = "https://junkfoodblog.com/alphabetical-candy-list/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    # Find main page element.
    results = soup.find(id="content")

    # Locate divs containing candies.
    candy_elements = results.find_all("div", class_="nv-content-wrap entry-content")

    # Loop through and assign all within a string.
    for candy_element in candy_elements:
        title = candy_element.find_all("li")
        title = re.sub(r'<.*?>', '', str(title))

    # Use pandas to open CSV file.
    candy = pandas.read_csv(r'C:\Users\bolto\Desktop\Candy\candyhierarchy2017.csv', encoding = "ISO-8859-1")

    #####################################################
    # Section Two: Data cleaning and comparing.
    #####################################################

    # Remove unnecessary leading substrings.
    candy.columns = candy.columns.str.lstrip("Q6 | ")
    candy.columns = candy.columns.str.lstrip("Q2: ")
    candy.columns = candy.columns.str.lstrip("Q3: ")

    # ----- Candys to be implemented in a later version.
    # (These candies all had problems with browsing accented letters and certain punctuation.)
    # Bonkers, Cadburry Creme Eggs, Chick-o-Sticks, Good N' Plenty, 
    # HersheyÕs Milk Chocolate, Jolly Ranchers, M&Ms, Kinder, Licorice, Mint Kisses
    # Mint Juleps, Now & Laters, Reese’s Pieces, Reggie Jackson Bar, Sweetums, Three Musketeers

    # Renames column titles that are different between candyhierarchy2017 and the website candy list.
    candy.rename(columns = {'100 Grand Bar':'Grand'}, inplace = True)
    candy.rename(columns = {'Anonymous brown globs that come in black and orange wrappers	(a.k.a. Mary Janes)':'Mary Jane'}, inplace = True)
    candy.rename(columns = {'Black Jacks':'Blackjack'}, inplace = True)
    candy.rename(columns = {'Caramellos':'Caramello'}, inplace = True)
    candy.rename(columns = {'Chiclets':'Chicklets'}, inplace = True)
    candy.rename(columns = {'Dove Bars':'Dove'}, inplace = True)
    candy.rename(columns = {'Goo Goo Clusters':'Goo Goo'}, inplace = True)
    candy.rename(columns = {'Gummy Bears straight up':'Gummy Bears'}, inplace = True)
    candy.rename(columns = {"Hershey's Dark Chocolate":"Hershey’s Special Dark"}, inplace = True)
    candy.rename(columns = {"Hershey's Kisses":"Hershey’s Kisses"}, inplace = True)
    candy.rename(columns = {'LaffyTaffy':'Laffy Taffy'}, inplace = True)
    candy.rename(columns = {'Lindt Truffle':'Lindor Truffles'}, inplace = True)
    candy.rename(columns = {"Mr. Goodbar":"Goodbar"}, inplace = True)
    candy.rename(columns = {'Nestle Crunch':'Crunch'}, inplace = True)
    candy.rename(columns = {"Now'n'Laters":"Now and Later"}, inplace = True)
    candy.rename(columns = {'ReeseÕs Peanut Butter Cups':"Reese’s Peanut Butter Cups"}, inplace = True)
    candy.rename(columns = {"Rolos":"Rolo"}, inplace = True)
    candy.rename(columns = {"Smarties (American)":"Smarties"}, inplace = True)
    candy.rename(columns = {"Sourpatch Kids (i.e. abominations of nature)":"Sour Patch Kids"}, inplace = True)
    candy.rename(columns = {"Sweet Tarts":"Sweetarts"}, inplace = True)
    candy.rename(columns = {"Tolberone something or other":"Toblerone"}, inplace = True)
    candy.rename(columns = {"Whatchamacallit Bars":"Whatchamacallit"}, inplace = True)
    candy.rename(columns = {"York Peppermint Patties":"York Peppermint Pattie"}, inplace = True)

    # Sets all column titles to lowercase.
    candy = candy.rename(columns = str.lower)

    # Drops columns that do not match the website's list.
    for column in candy.columns:
        if not (column in title.lower()) and (column != "gender") and (column != "age"):
            candy = candy.drop(column, axis = 1)

    # Sets all ages that are not null or junk to integers.
    candy = candy[~candy['age'].isnull()]
    candy = candy[candy['age'].str.isnumeric()]
    candy['age'] = candy['age'].astype(int)

    #####################################################
    # Section Three: Statistics generation.
    #####################################################
    
    while(True):

        # Clears terminal each time.
        os.system('cls')

        # Used to check if a match has been found.
        matches = 0

        # Prompts user to enter the candy they want to search for. Sets it to lowercase to reduce errors and improve fuzz ratio.
        searchCandy = input("Please type the candy that you would like to search for: ").lower()

        if ((searchCandy == "stop") or (searchCandy == "exit") or (searchCandy == "escape")):
            print("Goodbye!")
            time.sleep(2)
            exit()

        # Goes through each column and checks for any that are close matches. (75 fuzz ratio.)
        for column in candy.columns:
            if (fuzz.ratio(searchCandy, column)) > 75:
                matches = matches + 1
                print("**************************************************")
                print(column, "Statistics")
                currentlySearch = column
        
        # User inputs value that is not recognized.
        if matches == 0:
            print("No matches. Try again.")
            input("Press Enter to continue...")
            continue

        ##### Enjoy/indifferent/dislike/non-answer.

        # Total people who enjoy the candy.
        joyVal = candy[currentlySearch].str.contains('JOY').sum()

        # Total people who are indifferent to the candy.
        mehVal = candy[currentlySearch].str.contains('MEH').sum()

        # Total people who dislike the candy.
        despairVal = candy[currentlySearch].str.contains('DESPAIR').sum()

        # Total of people who responded.
        totalVal = joyVal + mehVal + despairVal

        # Display # and % of people who responded for each (like/indifferent/dislike).
        print("# of People Who Enjoy Them:", joyVal, "\nPercentage:", round((joyVal/totalVal), 2), "%")
        print("# of People who are Indifferent To Them:", mehVal, "\nPercentage:", round((mehVal/totalVal), 2), "%")
        print("# of People who Despise Them:", despairVal, "\nPercentage:", round((despairVal/totalVal), 2), "%")
        print()

        ##### Gender breakdown of enjoy/indifferent/dislike/non-answer.

        # Calculate how many women (like/indifferent/dislike) the candy.
        femaleJoy = len(candy[(candy['gender'] == 'Female') & (candy[currentlySearch] == 'JOY')])
        femaleMeh = len(candy[(candy['gender'] == 'Female') & (candy[currentlySearch] == 'MEH')])
        femaleDespair = len(candy[(candy['gender'] == 'Female') & (candy[currentlySearch] == 'DESPAIR')])

        # Used to filter out women who did not answer for the candy.
        femaleTotal = femaleJoy + femaleMeh + femaleDespair

        # Calculate how many women (like/indifferent/dislike) the candy.
        maleJoy = len(candy[(candy['gender'] == 'Male') & (candy[currentlySearch] == 'JOY')])
        maleMeh = len(candy[(candy['gender'] == 'Male') & (candy[currentlySearch] == 'MEH')])
        maleDespair = len(candy[(candy['gender'] == 'Male') & (candy[currentlySearch] == 'DESPAIR')])

        # Used to filter out men who did not answer for the candy.
        maleTotal = maleJoy + maleMeh + maleDespair

        # Display # and % of women who responded for each (like/indifferent/dislike).
        print("# of Women who Enjoy Them:", femaleJoy, "\nPercentage:", round((femaleJoy/femaleTotal), 2), "%")
        print("# of Women who are Indifferent To Them:", femaleMeh, "\nPercentage:", round((femaleMeh/femaleTotal), 2), "%")
        print("# of Women who Despise Them:", femaleDespair, "\nPercentage:", round((femaleDespair/femaleTotal), 2), "%")
        print()

        # Display # and % of men who responded for each (like/indifferent/dislike).
        print("# of Men who Enjoy Them:", maleJoy, "\nPercentage:", round((maleJoy/maleTotal), 2), "%")
        print("# of Men who are Indifferent To Them:", maleMeh, "\nPercentage:", round((maleMeh/maleTotal), 2), "%")
        print("# of Men who Despise Them:", maleDespair, "\nPercentage:", round((maleDespair/maleTotal), 2), "%")
        print()

        ##### Age breakdown of enjoying candy type.

        ### Child
        numChild = len(candy[(candy['age'] > 0) & (candy['age'] <= 14)])
        childJoy = len(candy[((candy['age'] > 0) & (candy['age'] <= 14)) & (candy[currentlySearch] == 'JOY')])
        print("# of Children (1 to 14) who Enjoy Them:", childJoy, "\nPercentage:", round((childJoy/numChild), 2), "%")

        ### Youth
        numYouth = len(candy[(candy['age'] >= 15) & (candy['age'] <= 24)])
        youthJoy = len(candy[((candy['age'] >= 15) & (candy['age'] <= 24)) & (candy[currentlySearch] == 'JOY')])
        print("# of Youths (15 to 24) who Enjoy Them:", youthJoy, "\nPercentage:", round((youthJoy/numYouth), 2), "%")

        ### Adult
        numAdult = len(candy[(candy['age'] >= 25) & (candy['age'] <= 64)])
        adultJoy = len(candy[((candy['age'] >= 25) & (candy['age'] <= 64)) & (candy[currentlySearch] == 'JOY')])
        print("# of Adults (25 to 64) who Enjoy Them:", adultJoy, "\nPercentage:", round((adultJoy/numAdult), 2), "%")

        ### Senior
        numSenior = len(candy[candy['age'] >= 65])
        seniorJoy = len(candy[(candy['age'] >= 65) & (candy[currentlySearch] == 'JOY')])
        print("# of Seniors (65+) who Enjoy Them:", seniorJoy, "\nPercentage:", round((seniorJoy/numSenior), 2), "%")

        # Used to allow user to read presented information before repeating.
        input("Press Enter to continue...")

main()
