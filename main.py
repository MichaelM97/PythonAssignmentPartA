# Name: Assignment Project Part A
# Author: Michael McCormick (15012271)

import csv
import os
import sys


def main():
    fileInfo = FileInformation() # Create object to access class

    fileInfo.get_file_names() # Get file names from user

    while True:  # Loop allows for entry of additional tournaments
        menu(fileInfo)  # User chooses if scores entered manually or via file

        # Store information from selected files
        fileInfo.store_ranking_info()
        fileInfo.store_prize_info()

        # Get file selection from user, and loop through to calculate top 16 players scores
        count = 1
        if scoreChoice == '1':
            while maleRankingPosition > 1 and femaleRankingPosition > 1:  # While they're players remaining
                count += 1
                fileInfo.get_score_files(count)
                with open(maleScoresFile) as csvFile:  # Open the selected file
                    readCsv = csv.reader(csvFile, delimiter=',')
                    if len(list(readCsv)) <= 9:  # Ensures that only top 16 players are processed
                        fileInfo.process_file_scores()

        # Get score input from user, and loop through to calculate top 16 players scores
        elif scoreChoice == '2':
            while maleRankingPosition > 1 and femaleRankingPosition > 1:  # While they're players remaining
                count += 1
                fileInfo.reset_player_names()
                fileInfo.get_score_input(count)
                if len(list(maleUserScores)) <= 9:  # Ensures that only top 16 players are processed
                    fileInfo.process_user_scores()

        # Calculate players winnings and display results
        fileInfo.process_winnings()
        if len(prevMaleRankings) > 0 or len(prevFemaleRankings) > 0:  # Adds previous tournament results (if they exist)
            fileInfo.add_previous_results()
        fileInfo.display_results()

        # Store results in a file (if users chooses to)
        while True:
            print("Would you like to store these results in a file? [Y/N]: ")
            userInput = get_valid_input().upper()
            if userInput == 'Y':
                fileInfo.store_result_file()
                break
            elif userInput == 'N':
                print("Scores will not be saved.")
                break
            else:
                print("Invalid Input!!!\n")

        # Allows user to add more scores for more tournaments
        while True:
            print("Would you like add results for another tournament? [Y/N]: ")
            userInput = get_valid_input().upper()
            if userInput == 'Y':
                fileInfo.store_previous_results()
                # Clear arrays for further use
                global malePlayerRankings
                malePlayerRankings = []
                global femalePlayerRankings
                femalePlayerRankings = []
                global prizeMoneyInfo
                prizeMoneyInfo = []
                extraTournament = True
                break
            elif userInput == 'N':
                print("No further tournament scores will be added.")
                extraTournament = False
                break
            else:
                print("Invalid Input!!!\n")

        if not extraTournament:
            break


# Allows user to choose to enter scores manually or from files
def menu(fileInfo):
    clear_screen()
    global scoreChoice

    #  Get valid user input
    while True:
        print("Please select an option:\n\n1 - Read players score from file\n2 - Enter players score manually\n:: ")
        scoreChoice = get_valid_input()
        if scoreChoice == '1':
            fileInfo.get_score_files(1)
            with open(maleScoresFile) as csvFile:
                readCsv = csv.reader(csvFile, delimiter=',')
                if len(list(readCsv)) <= 9:  # Ensures that only top 16 players are processed
                    fileInfo.process_file_scores()
            fileInfo.set_difficulty(maleScoresFile)  # Set difficulty using file name
            break
        elif scoreChoice == '2':
            fileInfo.store_player_names()  # Stores player names so user can identify who scored what
            fileInfo.get_score_input(1)
            if len(list(maleUserScores)) <= 9:  # Ensures that only top 16 players are processed
                fileInfo.process_user_scores()
            fileInfo.set_difficulty("")  # Set difficulty using user input
            break
        else:
            print("Invalid Input!\n\n")


# Validates a user input against blank entries
def get_valid_input():
    while True:
        try:
            userInput = input("::")
        except SyntaxError:
            userInput = None
        if userInput:
            return userInput
            break
        else:
            print("Invalid input! Please enter again.")


# Clears display screen (checks if Windows or Linux as command differs)
def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# Class holds all information and functions related to storing and manipulating file data
class FileInformation:

    # Degree's of difficulty
    global TAC1_DIFFICULTY
    TAC1_DIFFICULTY = 2.7
    global TAE21_DIFFICULTY
    TAE21_DIFFICULTY = 2.3
    global TAW11_DIFFICULTY
    TAW11_DIFFICULTY = 3.1
    global TBS2_DIFFICULTY
    TBS2_DIFFICULTY = 3.25

    # Allow global access to root directory file list, removes irrelevant files (if they exist)
    global fileList
    fileList = os.listdir()
    if '.idea' in fileList:
        fileList.remove('.idea')
    if 'main.py' in fileList:
        fileList.remove('main.py')
    if '.git' in fileList:
        fileList.remove('.git')

    # Arrays used to store file information
    global maleScoresInfo
    maleScoresInfo = []
    global femaleScoresInfo
    femaleScoresInfo = []
    global rankingPointsInfo
    rankingPointsInfo = []
    global malePlayerNames
    malePlayerNames = []
    global femalePlayerNames
    femalePlayerNames = []
    global prizeMoneyInfo
    prizeMoneyInfo = []
    global malePlayerRankings
    malePlayerRankings = []
    global femalePlayerRankings
    femalePlayerRankings = []
    global prevMaleRankings
    prevMaleRankings = []
    global prevFemaleRankings
    prevFemaleRankings = []
    global malePlayerWinners
    malePlayerWinners = []
    global femalePlayerWinners
    femalePlayerWinners = []
    global maleUserScores
    maleUserScores = []
    global femaleUserScores
    femaleUserScores = []

    # Get names of files containing player scores
    def get_score_files(self, roundNum):
        clear_screen()
        # Get MALE SCORES File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            print("\nPlease select the file containing the MALE PLAYERS scores for round %d: " % roundNum)
            userInput = get_valid_input()
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global maleScoresFile
        maleScoresFile = fileList[int(userInput)]  # Stores male file name globally
        fileList.remove(maleScoresFile)  # Removes file from list so it cannot be selected again

        clear_screen()
        # Get FEMALE SCORES File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
                print("\nPlease select the file containing the FEMALE PLAYERS scores for round %d: " % roundNum)
                userInput = get_valid_input()
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global femaleScoresFile
        femaleScoresFile = fileList[int(userInput)]  # Stores female file name globally
        fileList.remove(femaleScoresFile)  # Removes file from list so it cannot be selected again

    # Allows user to input scores
    def get_score_input(self, roundNum):
        # Get MALE PLAYER scores as input
        global maleUserScores
        maleUserScores = []
        while len(malePlayerNames) > 1:  # While there are still male players left without a score
            clear_screen()
            print("Entering MALE PLAYER scores for round %d: \n" % roundNum)
            row = []
            # User selects first player in match
            for i, name in enumerate(malePlayerNames):  # List all available players
                print(i + 1, "-", name)
            while True:
                print("\nPlease select the first player: ")
                userInput = get_valid_input()
                if int(userInput) < 1 or int(userInput) > len(malePlayerNames):
                    print("Invalid Input!\n")
                else:
                    break
            row.append(malePlayerNames[int(userInput) - 1])
            malePlayerNames.remove(malePlayerNames[int(userInput) - 1])
            # User enters the first players score
            while True:
                print("\nPlease enter the first players score[0-3]: ")
                firstScore = get_valid_input()
                if int(firstScore) < 0 or int(firstScore) > 3:
                    print("Invalid Input!\n")
                else:
                    break
            row.append(firstScore)

            # User selects second player in match
            for i, name in enumerate(malePlayerNames):  # List all available players
                print(i + 1, "-", name)
            while True:
                print("\nPlease select the second player: ")
                userInput = get_valid_input()
                if int(userInput) < 1 or int(userInput) > len(malePlayerNames):
                    print("Invalid Input!\n")
                else:
                    break
            row.append(malePlayerNames[int(userInput) - 1])
            malePlayerNames.remove(malePlayerNames[int(userInput) - 1])
            # User enters the second players score
            while True:
                print("\nPlease enter the second players score[0-3]: ")
                secondScore = get_valid_input()
                if int(secondScore) < 0 or int(secondScore) > 3:
                    print("Invalid Input!\n")
                elif (int(firstScore) + int(secondScore)) > 5:
                    print("Invalid Input! There can only be a total of 5 games per pair.\n")
                elif int(firstScore) != 3 and int(secondScore) != 3:
                    print("Invalid Input! One player must win 3 games, or there is no winner.\n")
                else:
                    break
            row.append(secondScore)
            maleUserScores.append(row)  # Store data entered into global array for later processing

        # Get FEMALE PLAYER scores as input
        global femaleUserScores
        femaleUserScores = []
        while len(femalePlayerNames) > 1:  # While there are still female players left without a score
            clear_screen()
            print("Entering FEMALE PLAYER scores for round %d: \n" % roundNum)
            row = []
            # User selects first player in match
            for i, name in enumerate(femalePlayerNames):  # List all available players
                print(i + 1, "-", name)
            while True:
                print("\nPlease select the first player: ")
                userInput = get_valid_input()
                if int(userInput) < 1 or int(userInput) > len(femalePlayerNames):
                    print("Invalid Input!\n")
                else:
                    break
            row.append(femalePlayerNames[int(userInput) - 1])
            femalePlayerNames.remove(femalePlayerNames[int(userInput) - 1])
            # User enters the first players score
            while True:
                print("\nPlease enter the first players score[0-2]: ")
                firstScore = get_valid_input()
                if int(firstScore) < 0 or int(firstScore) > 2:
                    print("Invalid Input!\n")
                else:
                    break
            row.append(firstScore)
            # User selects second player in match
            for i, name in enumerate(femalePlayerNames):  # List all available players
                print(i + 1, "-", name)
            while True:
                print("\nPlease select the second player: ")
                userInput = get_valid_input()
                if int(userInput) < 1 or int(userInput) > len(femalePlayerNames):
                    print("Invalid Input!\n")
                else:
                    break
            row.append(femalePlayerNames[int(userInput) - 1])
            femalePlayerNames.remove(femalePlayerNames[int(userInput) - 1])
            # User enters the second players score
            while True:
                print("\nPlease enter the second players score[0-2]: ")
                secondScore = get_valid_input()
                if int(secondScore) < 0 or int(secondScore) > 2:
                    print("Invalid Input!\n")
                elif (int(firstScore) + int(secondScore)) > 3:
                    print("Invalid Input! There can only be a total of 3 games per pair.\n")
                elif int(firstScore) != 2 and int(secondScore) != 2:
                    print("Invalid Input! One player must win 2 games, or there is no winner.\n")
                else:
                    break
            row.append(secondScore)
            femaleUserScores.append(row)  # Store data entered into global array for later processing

    # Sets the tournament name and difficulty based on file name, or user input
    def set_difficulty(self, tournament):
        global tournamentName
        global tournamentDifficulty

        if 'TAC1' in tournament:
            tournamentName = 'TAC1'
            tournamentDifficulty = TAC1_DIFFICULTY
        elif 'TAE21' in tournament:
            tournamentName = 'TAE21'
            tournamentDifficulty = TAE21_DIFFICULTY
        elif 'TAW11' in tournament:
            tournamentName = 'TAW11'
            tournamentDifficulty = TAW11_DIFFICULTY
        elif 'TBS2' in tournament:
            tournamentName = 'TBS2'
            tournamentDifficulty = TBS2_DIFFICULTY
        else:
            print("Could not find difficulty, please enter Tournament Name -\nTAC1\nTAE21\nTAW11\nTBS2\n")
            userInput = get_valid_input().upper()
            FileInformation.set_difficulty(self, userInput)

    # Allows user to select files containing required information
    def get_file_names(self):
        clear_screen()
        # Get RANKING POINTS File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            print("\nPlease select the file containing RANKING POINTS information: ")
            userInput = get_valid_input()
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global rankingPointsFile
        rankingPointsFile = fileList[int(userInput)]  # Stores ranking points file name globally
        fileList.remove(rankingPointsFile)  # Removes file from list so it cannot be selected again

        clear_screen()
        # Get PRIZE MONEY File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            print("\nPlease select the file containing PRIZE MONEY information: ")
            userInput = get_valid_input()
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global prizeMoneyFile
        prizeMoneyFile = fileList[int(userInput)]  # Stores prize money file name globally
        fileList.remove(prizeMoneyFile)  # Removes file from list so it cannot be selected again

        clear_screen()
        # Get MALE PLAYERS File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            print("\nPlease select the file containing MALE PLAYERS information: ")
            userInput = get_valid_input()
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global malePlayersFile
        malePlayersFile = fileList[int(userInput)]  # Stores male players file name globally
        fileList.remove(malePlayersFile)  # Removes file from list so it cannot be selected again

        clear_screen()
        # Get FEMALE PLAYERS File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            print("\nPlease select the file containing FEMALE PLAYERS information: ")
            userInput = get_valid_input()
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global femalePlayersFile
        femalePlayersFile = fileList[int(userInput)]  # Stores female players file name globally
        fileList.remove(femalePlayersFile)  # Removes file from list so it cannot be selected again

    # Store player names provided from file
    def store_player_names(self):
        # Store MALE PLAYERS FILE information in array
        with open(malePlayersFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for i, row in enumerate(readCsv):
                malePlayerNames.append(row[0])

        # Store FEMALE PLAYERS FILE information in array
        with open(femalePlayersFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for i, row in enumerate(readCsv):
                femalePlayerNames.append(row[0])

    # Adds back all winners to the player name arrays, allowing further processing of winners
    def reset_player_names(self):
        # Reset MALE PLAYER scores
        for row in maleUserScores:
            if row[1] > row[3]:
                malePlayerNames.append(row[0])  # Adds winner back to list
            elif row[1] < row[3]:
                malePlayerNames.append(row[2])  # Adds winner back to list

        # Reset FEMALE PLAYER scores
        for row in femaleUserScores:
            if row[1] > row[3]:
                femalePlayerNames.append(row[0])  # Adds winner back to list
            elif row[1] < row[3]:
                femalePlayerNames.append(row[2])  # Adds winner back to list

    # Stores required ranking points information from file provided by user
    def store_ranking_info(self):
        # Store RANKING POINTS FILE information in array
        with open(rankingPointsFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for i, row in enumerate(readCsv):
                rankingPointsInfo.append(row[0])
            # Set male and female ranking position counters
            global maleRankingPosition
            maleRankingPosition = i
            global femaleRankingPosition
            femaleRankingPosition = i

    # Stores required prize money information from file provided by user
    def store_prize_info(self):
        # Store PRIZE MONEY FILE information in array
        with open(prizeMoneyFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            found = False
            previous = 0
            for row in readCsv:
                if tournamentName in row[0]:
                    found = True
                if found is True:
                    if int(row[1]) < int(previous):  # Prevents storing other tournament values
                        break
                    else:
                        prizeMoneyInfo.append(row[2])
                        previous = row[1]

    # Stores players in order of their scores given in a file
    def process_file_scores(self):
        global maleRankingPosition
        global femaleRankingPosition

        # Process MALE PLAYER scores
        with open(maleScoresFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            next(readCsv)  # Skip headers in file
            # Calculate ranking points and assign them to losing player
            rankingPoints = int(rankingPointsInfo[maleRankingPosition]) * tournamentDifficulty
            for row in readCsv:
                if row[1] > row[3]:
                    malePlayerRankings.append(row[2] + '-' + str(rankingPoints))
                elif row[1] < row[3]:
                    malePlayerRankings.append(row[0] + '-' + str(rankingPoints))
                else:  # If no winner is found, display error and exit
                    print("\n\nERROR IN SCORE ENTRY!!!\n\n")
                    sys.exit()
                maleRankingPosition += -1
                # If this is the last player, assign them the highest ranking points
                if maleRankingPosition == 1:
                    rankingPoints = int(rankingPointsInfo[maleRankingPosition]) * tournamentDifficulty
                    if row[1] > row[3]:
                        malePlayerRankings.append(row[0] + '-' + str(rankingPoints))
                    elif row[1] < row[3]:
                        malePlayerRankings.append(row[2] + '-' + str(rankingPoints))

        # Process FEMALE PLAYER scores
        with open(femaleScoresFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            next(readCsv)  # Skip headers in file
            # Calculate ranking points and assign them to losing player
            rankingPoints = int(rankingPointsInfo[femaleRankingPosition]) * tournamentDifficulty
            for row in readCsv:
                if row[1] > row[3]:
                    femalePlayerRankings.append(row[2] + '-' + str(rankingPoints))
                elif row[1] < row[3]:
                    femalePlayerRankings.append(row[0] + '-' + str(rankingPoints))
                else:  # If no winner is found, display error and exit
                    print("\n\nERROR IN SCORE ENTRY!!!\n\n")
                    sys.exit()
                femaleRankingPosition += -1
                # If this is the last player, assign them the highest ranking points
                if femaleRankingPosition == 1:
                    rankingPoints = int(rankingPointsInfo[femaleRankingPosition]) * tournamentDifficulty
                    if row[1] > row[3]:
                        femalePlayerRankings.append(row[0] + '-' + str(rankingPoints))
                    elif row[1] < row[3]:
                        femalePlayerRankings.append(row[2] + '-' + str(rankingPoints))

    # Stores players in order of their scores given by the user
    def process_user_scores(self):
        global maleRankingPosition
        global femaleRankingPosition

        # Process MALE PLAYER scores
        # Calculate ranking points and assign them to losing player
        rankingPoints = int(rankingPointsInfo[maleRankingPosition]) * tournamentDifficulty
        for row in maleUserScores:
            if row[1] > row[3]:
                malePlayerRankings.append(row[2] + '-' + str(rankingPoints))
            elif row[1] < row[3]:
                malePlayerRankings.append(row[0] + '-' + str(rankingPoints))
            else:  # If no winner is found, display error and exit
                print("\n\nERROR IN SCORE ENTRY!!!\n\n")
                sys.exit()
            maleRankingPosition += -1
            # If this is the last player, assign them the highest ranking points
            if maleRankingPosition == 1:
                rankingPoints = int(rankingPointsInfo[maleRankingPosition]) * tournamentDifficulty
                if row[1] > row[3]:
                    malePlayerRankings.append(row[0] + '-' + str(rankingPoints))
                elif row[1] < row[3]:
                    malePlayerRankings.append(row[2] + '-' + str(rankingPoints))

        # Process FEMALE PLAYER scores
        # Calculate ranking points and assign them to losing player
        rankingPoints = int(rankingPointsInfo[femaleRankingPosition]) * tournamentDifficulty
        for row in femaleUserScores:
            if row[1] > row[3]:
                femalePlayerRankings.append(row[2] + '-' + str(rankingPoints))
            elif row[1] < row[3]:
                femalePlayerRankings.append(row[0] + '-' + str(rankingPoints))
            else:  # If no winner is found, display error and exit
                print("\n\nERROR IN SCORE ENTRY!!!\n\n")
                sys.exit()
            femaleRankingPosition += -1
            # If this is the last player, assign them the highest ranking points
            if femaleRankingPosition == 1:
                rankingPoints = int(rankingPointsInfo[femaleRankingPosition]) * tournamentDifficulty
                if row[1] > row[3]:
                    femalePlayerRankings.append(row[0] + '-' + str(rankingPoints))
                elif row[1] < row[3]:
                    femalePlayerRankings.append(row[2] + '-' + str(rankingPoints))

    # Assign prize money to top players
    def process_winnings(selfs):
        # Assign MALE PLAYERS winnings
        count = len(malePlayerRankings) - 1
        for prize in prizeMoneyInfo:
            malePlayerRankings[count] += ("-" + prize)
            count += -1

        # Assign FEMALE PLAYERS winnings
        count = len(femalePlayerRankings) - 1
        for prize in prizeMoneyInfo:
            femalePlayerRankings[count] += ("-" + prize)
            count += -1

    # Stores results from previously calculated tournaments
    def store_previous_results(self):
        global prevMaleRankings
        global prevFemaleRankings

        # Save MALE PLAYER data from previous calculation
        for prevPlayer in prevMaleRankings:  # Avoids double entry of players
            if prevPlayer[0] in malePlayerRankings:
                prevMaleRankings.remove(prevPlayer)
        prevMaleRankings.extend(malePlayerRankings)

        # Save FEMALE PLAYER data from previous calculation
        for prevPlayer in prevFemaleRankings:  # Avoids double entry of players
            if prevPlayer[0] in femalePlayerRankings:
                prevFemaleRankings.remove(prevPlayer)
        prevFemaleRankings.extend(femalePlayerRankings)

    # Adds the prize money and rankings points to players (if they were previously awarded any)
    def add_previous_results(self):
        # Add previous MALE PLAYER data
        for i, x in enumerate(malePlayerRankings):
            player = x.split('-')  # Splits current player information
            for y in prevMaleRankings:
                prevPlayer = y.split('-')  # Splits previous player information
                # If player names match then add previous data
                if player[0] in prevPlayer[0]:
                    # Adds previous RANKING POINTS
                    if len(prevPlayer) > 1 and len(player) > 1:  # Adds previous points to current amount
                        player[1] = (float(player[1]) + float(prevPlayer[1]))
                    elif len(prevPlayer) > 1 >= len(player):  # Adds previous points to empty amount
                        malePlayerRankings[i] += ("-" + str(prevPlayer[1]))
                    # Adds previous PRIZE MONEY
                    if len(prevPlayer) > 3 and len(player) > 2:  # Adds previous money to current amount
                        # Removes commas for addition
                        playerMoney = player[2].replace(',', '')
                        prevPlayerMoney = prevPlayer[2].replace(',', '')
                        total = (int(playerMoney) + int(prevPlayerMoney))
                        total = format(total, ",d")  # Adds commas back
                        # Stores updated total in array
                        malePlayerRankings[i] = (player[0] + '-' + str(player[1]) + '-' + total)
                    elif len(prevPlayer) > 3 >= len(player):  # Adds previous money to empty amount
                        malePlayerRankings[i] += ("-" + str(prevPlayer[2]))
                    break  # Ends loop once player is found

        # Add previous FEMALE PLAYER data
        for i, x in enumerate(femalePlayerRankings):
            player = x.split('-')  # Splits current player information
            for y in prevFemaleRankings:
                prevPlayer = y.split('-')  # Splits previous player information
                # If player names match then add previous data
                if player[0] in prevPlayer[0]:
                    # Adds previous RANKING POINTS
                    if len(prevPlayer) > 1 and len(player) > 1:  # Adds previous points to current amount
                        player[1] = (float(player[1]) + float(prevPlayer[1]))
                    elif len(prevPlayer) > 1 >= len(player):  # Adds previous points to empty amount
                        femalePlayerRankings[i] += ("-" + str(prevPlayer[1]))
                    # Adds previous PRIZE MONEY
                    if len(prevPlayer) > 3 and len(player) > 2:  # Adds previous money to current amount
                        # Removes commas for addition
                        playerMoney = player[2].replace(',', '')
                        prevPlayerMoney = prevPlayer[2].replace(',', '')
                        total = (int(playerMoney) + int(prevPlayerMoney))
                        total = format(total, ",d")  # Adds commas back
                        # Stores updated total in array
                        femalePlayerRankings[i] = (player[0] + '-' + str(player[1]) + '-' + total)
                    elif len(prevPlayer) > 3 >= len(player):  # Adds previous money to empty amount
                        femalePlayerRankings[i] += ("-" + str(prevPlayer[2]))

    # Displays results to the user via the prompt
    def display_results(self):
        print("The following results for tournament " + tournamentName + " have been calculated:")
        # Displays the MALE PLAYER results
        print("Male Players:")
        for place, rankings in enumerate(malePlayerRankings[::-1]):  # Loops in descending order
            # Adds players position in tournament to array
            malePlayerRankings[(len(malePlayerRankings) - (place + 1))] += ('-' + str(place + 1))
            result = rankings.split('-')  # Splits player information
            print("Place - " + str(place + 1) + ", Player Name - " + result[0] + ", Ranking Points - " + result[1],
                  end="")
            if len(result) > 2:  # Only displays prize money if player has been awarded any
                print(", Prize Money - $" + result[2])
            else:
                print("")

        # Displays the FEMALE PLAYER results
        print("Female Players:")
        for place, rankings in enumerate(femalePlayerRankings[::-1]):  # Loops in descending order
            # Adds players position in tournament to array
            femalePlayerRankings[(len(femalePlayerRankings) - (place + 1))] += ('-' + str(place + 1))
            result = rankings.split('-')  # Splits player information
            print("Place - " + str(place + 1) + ", Player Name - " + result[0] + ", Ranking Points - " + result[1],
                  end="")
            if len(result) > 2:  # Only displays prize money if player has been awarded any
                print(", Prize Money - $" + result[2])
            else:
                print("")

    # Stores results in files named by the user
    def store_result_file(self):
        directory = str(os.path.dirname(os.path.realpath(__file__)))  # Retrieves directory path
        # Stores MALE PLAYER results in a file
        fileName = input("\nPlease enter the desired file name to store the MALE PLAYER results: ")
        # Creates file using chosen name in root directory
        with open((directory + "\\" + fileName + ".csv"), 'w', newline="\n", encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile, dialect='excel')
            header = ['Place', 'Player Name', 'Ranking Points', 'Prize Money($)']  # Sets file headers
            writer.writerow(header)
            # Writes player information in descending order to file
            for row in malePlayerRankings[::-1]:
                data = row.split('-')  # Splits player information
                if len(data) == 4:
                    line = [str(data[3]), str(data[0]), str(data[1]), str(data[2])]
                    writer.writerow(line)
                else:  # If player does not have prize money
                    line = [str(data[2]), str(data[0]), str(data[1]), 'N/A']
                    writer.writerow(line)

        # Stores FEMALE PLAYER results in a file
        fileName = input("\nPlease enter the desired file name to store the FEMALE PLAYER results: ")
        # Creates file using chosen name in root directory
        with open((directory + "\\" + fileName + ".csv"), 'w', newline="\n", encoding="utf-8") as csvFile:
            writer = csv.writer(csvFile, dialect='excel')
            header = ['Place', 'Player Name', 'Ranking Points', 'Prize Money($)']  # Sets file headers
            writer.writerow(header)
            # Writes player information in descending order to file
            for row in femalePlayerRankings[::-1]:
                data = row.split('-')  # Splits player information
                if len(data) == 4:
                    line = [str(data[3]), str(data[0]), str(data[1]), str(data[2])]
                    writer.writerow(line)
                else:  # If player does not have prize money
                    line = [str(data[2]), str(data[0]), str(data[1]), 'N/A']
                    writer.writerow(line)


if __name__ == "__main__": main()