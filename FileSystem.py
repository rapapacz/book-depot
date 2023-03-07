class FileSystem:

    def __init__(self):
        self.filepath = input("Enter a file path: ")

    def write(self, data):
        with open(self. filepath, 'w') as file_object:
            file_object.write(data)
        file_object.close()

    def append(self, data):
        with open(self.filepath, 'a') as file_object:
            file_object.write(data)
        file_object.close()

    def read(self):
        with open(self.filepath, 'r') as file_object:
            print(file_object.read())
        file_object.close()
