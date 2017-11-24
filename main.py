# Name: Assignment Project Part A
# Author: Michael McCormick (15012271)

import csv
import os


def main():
    fileInfo = FileInformation()

    fileInfo.get_file_names()

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

    # Allow access to Root file list and file names
    global fileList
    fileList = os.listdir()
    fileList.remove('.idea')
    fileList.remove('main.py')
    fileList.remove('.git')
    global maleScoresFile
    global femaleScoresFile
    global rankingPointsFile
    global prizeMoneyFile
    global malePlayersFile
    global femalePlayersFile

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

    def get_file_info(self):
        with open('DADSA 17-18 COURSEWORK A RANKING POINTS.csv', "rb") as f:
            reader = csv.reader(f)
        for row in reader:
            print(row)


menu()
if __name__ == "__main__": main()