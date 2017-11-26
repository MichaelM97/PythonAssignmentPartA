# Name: Assignment Project Part A
# Author: Michael McCormick (15012271)

import csv
import os
import sys


def main():
    fileInfo = FileInformation() # Create object to access class

    fileInfo.get_file_names()

    menu()

    fileInfo.store_file_info()

    count = 1
    if scoreChoice == '1':
        while maleRankingPosition > 1 and femaleRankingPosition > 1:
            count += 1
            fileInfo.get_score_files(count)
            with open(maleScoresFile) as csvFile:
                readCsv = csv.reader(csvFile, delimiter=',')
                if len(list(readCsv)) <= 9: # Ensures that only top 16 players are processed
                    fileInfo.process_scores()


    print("\nFinished with a total of %d rounds..." % count)

def menu():
    print("Please select an option:\n\n1 - Read players score from file\n2 - Enter players score manually\n:: ")

    global scoreChoice
    scoreChoice = input()

    fileInfo = FileInformation()

    if scoreChoice == '1':
        fileInfo.get_score_files(1)
        fileInfo.set_difficulty(maleScoresFile) # Set difficulty using file name            CHANGE MENU TO ONLY BE CALLED IN MAIN AND RETURN scoreChoice, DO THIS STUFF IN MAIN
    elif scoreChoice == '2':
        fileInfo.get_score_input(1)
        fileInfo.set_difficulty("")  # Set difficulty using user input
    else:
        print("Invalid Input!\n\n")
        menu()


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

    # Allow global access to Root file list, and remove irrelevant files (if they exist)
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
    global malePlayersInfo
    malePlayersInfo = []
    global femalePlayersInfo
    femalePlayersInfo = []
    global prizeMoneyInfo
    prizeMoneyInfo = []
    global malePlayerRankings
    malePlayerRankings = []
    global femalePlayerRankings
    femalePlayerRankings = []

    def get_score_files(self, roundNum):
        # Get MALE SCORE File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing the MALE PLAYERS scores for round %d: " % roundNum)
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global maleScoresFile
        maleScoresFile = fileList[int(userInput)]
        fileList.remove(maleScoresFile)

        # Get FEMALE SCORE File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing the FEMALE PLAYERS scores for round %d: " % roundNum)
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global femaleScoresFile
        femaleScoresFile = fileList[int(userInput)]
        fileList.remove(femaleScoresFile)

    def get_score_input(self):
        print("Get score from user input")
        # USES LIST OF PLAYER NAMES TO ALLOW SELECTION OF WHO PLAYED WHO, AND WHO SCORED WHAT, KEEP THE SAME LAYOUT AS FILES

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
            userInput = input("Could not find difficulty, please enter Tournament Name:")
            FileInformation.set_difficulty(self, userInput)

    def get_file_names(self):
        # Get RANKING POINTS File Name
        while True:
            for f, fileName in enumerate(fileList):
             print(f, "-", fileName)
            userInput = input("\nPlease select the file containing RANKING POINTS information: ")
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global rankingPointsFile
        rankingPointsFile = fileList[int(userInput)]
        fileList.remove(rankingPointsFile)

        # Get PRIZE MONEY File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing PRIZE MONEY information: ")
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global prizeMoneyFile
        prizeMoneyFile = fileList[int(userInput)]
        fileList.remove(prizeMoneyFile)

        # Get MALE PLAYERS File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing MALE PLAYERS information: ")
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global malePlayersFile
        malePlayersFile = fileList[int(userInput)]
        fileList.remove(malePlayersFile)

        # Get FEMALE PLAYERS File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing FEMALE PLAYERS information: ")
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
        global femalePlayersFile
        femalePlayersFile = fileList[int(userInput)]
        fileList.remove(femalePlayersFile)

    def store_file_info(self):   # SEPERATE PLAYER NAMES, ONLY STORE THOSE FILES IF USER ENTERS SCORES MANUALLY
        # Store MALE PLAYERS FILE information in array
        with open(malePlayersFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for i, row in enumerate(readCsv):
                malePlayersInfo.append(row[0])
            global malePlayerCount
            malePlayerCount = i + 1

        # Store MALE PLAYERS FILE information in array
        with open(femalePlayersFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for i, row in enumerate(readCsv):
                femalePlayersInfo.append(row[0])
            global femalePlayerCount
            femalePlayerCount = i + 1

        # Store RANKING POINTS FILE information in array, and set male & female ranking position counters
        with open(rankingPointsFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for i, row in enumerate(readCsv):
                rankingPointsInfo.append(row[0])
            global maleRankingPosition
            maleRankingPosition = i
            global femaleRankingPosition
            femaleRankingPosition = i

        # Store PRIZE MONEY FILE information in array
        with open(prizeMoneyFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            found = False
            count = 0
            for row in readCsv:
                if tournamentName in row[0]:
                    found = True
                if found is True:
                    prizeMoneyInfo.append(row[2])
                    count += 1    # DONT HARD CODE THIS CHAAANNGGEEEE
                    if count >= 8:
                        break

    def process_scores(self):
        global maleRankingPosition
        global femaleRankingPosition

        with open(maleScoresFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            next(readCsv)
            rankingPoints = int(rankingPointsInfo[maleRankingPosition]) * tournamentDifficulty
            for row in readCsv:
                if row[1] > row[3]:
                    malePlayerRankings.append(row[2] + ',' + str(rankingPoints))
                elif row[1] < row[3]:
                    malePlayerRankings.append(row[0] + ',' + str(rankingPoints))
                else:
                    print("\n\nERROR IN FILE!\n\n")
                    sys.exit()
                maleRankingPosition += -1
                if maleRankingPosition == 1:
                    rankingPoints = int(rankingPointsInfo[maleRankingPosition]) * tournamentDifficulty
                    if row[1] > row[3]:
                        malePlayerRankings.append(row[0] + ',' + str(rankingPoints))
                    elif row[1] < row[3]:
                        malePlayerRankings.append(row[2] + ',' + str(rankingPoints))
            print("MALE RANKINGS")
            print(malePlayerRankings)

        with open(femaleScoresFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            next(readCsv)
            rankingPoints = int(rankingPointsInfo[femaleRankingPosition]) * tournamentDifficulty
            for row in readCsv:
                if row[1] > row[3]:
                    femalePlayerRankings.append(row[2] + ',' + str(rankingPoints))
                elif row[1] < row[3]:
                    femalePlayerRankings.append(row[0] + ',' + str(rankingPoints))
                else:
                    print("\n\nERROR IN FILE!\n\n")
                    sys.exit()
                femaleRankingPosition += -1
                if femaleRankingPosition == 1:
                    rankingPoints = int(rankingPointsInfo[femaleRankingPosition]) * tournamentDifficulty
                    if row[1] > row[3]:
                        femalePlayerRankings.append(row[0] + ',' + str(rankingPoints))
                    elif row[1] < row[3]:
                        femalePlayerRankings.append(row[2] + ',' + str(rankingPoints))
            print("FEMALE RANKINGS")
            print(femalePlayerRankings)



if __name__ == "__main__": main()