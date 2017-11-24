# Name: Assignment Project Part A
# Author: Michael McCormick (15012271)

import csv
import os


def main():
    fileInfo = FileInformation()

    fileInfo.store_file_info()

    #fileInfo.get_file_names()

def menu():
    print("Please select an option:\n\n1 - Read players score from file\n2 - Enter players score manually\n:: ")

    userInput = input()

    fileInfo = FileInformation()

    if userInput == '1':
        fileInfo.get_score_files()
    elif userInput == '2':
        fileInfo.get_score_input()
    else:
        print("Invalid Input!\n\n")
        menu()


class FileInformation:

    # Degree's of difficulty
    TAC1_DIFFICULTY = 2.7
    TAE21_DIFFICULTY = 2.3
    TAW11_DIFFICULTY = 3.1
    TBS2_DIFFICULTY = 3.25

    # Allow global access to Root file list, and remove irrelevant files
    global fileList
    fileList = os.listdir()
    fileList.remove('.idea')
    fileList.remove('main.py')
    fileList.remove('.git')

    # Allow global access to file names
    global maleScoresFile
    global femaleScoresFile
    global rankingPointsFile
    global prizeMoneyFile
    global malePlayersFile
    global femalePlayersFile

    # Arrays used to store file information
    global maleScoresInfo
    global femaleScoresInfo
    global rankingPointsInfo
    global prizeMoneyInfo
    global malePlayersInfo
    global femalePlayersInfo


    def get_score_files(self):
        # Get MALE SCORE File Name
        while True:
            for f, fileName in enumerate(fileList):
                print(f, "-", fileName)
            userInput = input("\nPlease select the file containing the MALE PLAYERS scores: ")
            if (int(userInput) < 0) or (int(userInput) > len(fileList)):
                print("Invalid Input!!!\n")
            else:
                break
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
        femaleScoresFile = fileList[int(userInput)]
        fileList.remove(femaleScoresFile)

    def get_score_input(self):
        #global scoresFile
        #scoresFile = 'null'
        print("Get score from user input")

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
        femalePlayersFile = fileList[int(userInput)]
        fileList.remove(femalePlayersFile)
        #endregion

    def store_file_info(self):
        #Store RANKING FILE information in array
        with open(rankingPointsFile) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)


#menu()
if __name__ == "__main__": main()