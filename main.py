# Name: Assignment Project Part A
# Author: Michael McCormick (15012271)

import csv
import os


def main():
    fileInfo = FileInformation()

    fileInfo.get_file_names()

    fileInfo.store_file_info()



def menu():
    print("Please select an option:\n\n1 - Read players score from file\n2 - Enter players score manually\n:: ")

    userInput = input()

    fileInfo = FileInformation()

    if userInput == '1':
        fileInfo.get_score_files()
        fileInfo.set_difficulty(maleScoresFile) # Set difficulty using file name
        print(tournamentName)
        print(tournamentDifficulty)
    elif userInput == '2':
        fileInfo.get_score_input()
        fileInfo.set_difficulty("")  # Set difficulty using user input
        print(tournamentName)
        print(tournamentDifficulty)
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

    # Allow global access to Root file list, and remove irrelevant files
    global fileList
    fileList = os.listdir()
    fileList.remove('.idea')
    fileList.remove('main.py')
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



    def get_score_files(self):

        # SEARCH STRING FOR WORD,,, TO IDENTIFY DIFFICULTY I.E TAC1, ASK FOR THIS FROM USER INPUT

        # Get MALE SCORE File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing the MALE PLAYERS scores: ")
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
            userInput = input("\nPlease select the file containing the FEMALE PLAYERS scores: ")
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
        #region Retrieve file names from user
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
        #endregion

    def store_file_info(self):
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

        # Store RANKING POINTS FILE information in array
        with open(rankingPointsFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            for row in readCsv:
                rankingPointsInfo.append(row[0])

        # Store PRIZE MONEY FILE information in array
        with open(prizeMoneyFile) as csvFile:
            readCsv = csv.reader(csvFile, delimiter=',')
            found = False
            count = 0
            for row in readCsv:
                if tournamentName in row[0]:
                    found = True
                    print("FOUND")
                if found is True:
                    prizeMoneyInfo.append(row[2])
                    count += 1    # DONT HARD CODE THIS CHAAANNGGEEEE
                    print(prizeMoneyInfo)
                    if count >= 8:
                        break





menu()
if __name__ == "__main__": main()