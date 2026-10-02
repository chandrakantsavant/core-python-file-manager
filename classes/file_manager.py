from pathlib import Path

class FileManager:
    basePath = "./file_manager/files/"
    def __init__(self):
        self.showPrompt()
        pass

    def showPrompt(self):
        print("********** File Manager ***********")
        print("1. Create File")
        print("2. Edit File")
        print("3. Rename File")
        print("4. Delete File")
        print("5. Terminate Program")
        print("-------------------------------------")
        userInput = int(input("Provide your input:- "))
        self.decideTaskUponInput(userInput)

    def decideTaskUponInput(self, input):
        
        if input == 1:
            self.createFile()
        elif input == 2:
            self.editFile()
        elif input == 3:
            self.renameFile()
        # elif input == 4:
        #     self.deleteFile()
        elif input == 5:
            print("Terminating the program....")
            pass
        else:
            print("Your input is invalid please check below options and provide valid input...")
            self.showPrompt()


    def showAllFiles(self):
        dirPath = Path('./file_manager/files')
        if not dirPath.exists():
            dirPath.mkdir(parents=True, exist_ok=True)
        files = [f.name for f in dirPath.iterdir() if f.is_file()]

        if not files:
            print("No files in the directory")
        else:
            print("--------------- Following are the list of files ---------------")
            for i in range(len(files)):
                print(f"{i+1}. {files[i]}")
            print("--------------- Files list ends here --------------------------")

    def createFile(self):
        self.showAllFiles()
        fileName = input("Enter a file name to Create:- ")
        filePath = Path(f"./file_manager/files/{fileName}")
        # Create a file here
        try:
            with open(filePath, "w") as file:
                content = input("Enter content to add in a file:- ")
                file.write(content)
                file.close()
        except Exception as err:
            print("Something went wrong, please try again....")
            self.showPrompt()

        print(f"Your file is created successfully ")
        self.showPrompt()

    def editFile(self):
        self.showAllFiles()
        print("In this mode you can enter a existing file name and append the new data into it")
        fileName = input("Enter File name:- ")
        filePath = Path(self.basePath+fileName)

        print(filePath)

        try:
            with open(filePath, "a") as file:
                print("Here is the existing file content:--")
                print("-------------------------------------------")
                fileContent = self.getFileContent(filePath)
                print(fileContent)
                print("-------------------------------------------")
                userInput = input("Enter new content to be append in a file:- ")
                file.write(f"\n# {userInput}")
                print("-------------Data writing is done---------------")
                print("Your content is appended to the file")
        except Exception as err:
            print(f"Something went wrong with error {err}")
            self.showPrompt()

        print("Your file is edited successfully with provided content")
        self.showPrompt()

    def renameFile(self):
        print('Following is the list of existing file....')
        self.showAllFiles()
        print("------------------------------------------")
        getFileName = input("Enter file name to rename:- ")
        filePath = Path(self.basePath+getFileName)
        

        try:
            newName = str(input("Enter New file name:- "))
            newNameWithPath = filePath.with_name(newName)
            filePath.rename(newNameWithPath)
            print("File renamed successfully")
            self.showPrompt()
        except Exception as err:
            print(f"Something went wrong and error is {err}, Please try from start")
            self.showPrompt()
    




    def getFileContent(self, filePath):
        try:
            getFile = open(filePath, 'r')
            return getFile.read()
        except Exception as err:
            print("Error in reading a file")



    
