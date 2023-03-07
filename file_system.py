class FileSystem:

    @staticmethod
    def write(filepath, data):
        with open(filepath, 'w') as file_object:
            file_object.write(data)
        file_object.close()

    @staticmethod
    def append(filepath, data):
        with open(filepath, 'a') as file_object:
            file_object.write(data)
        file_object.close()

    @staticmethod
    def read(filepath):
        with open(filepath, 'r') as file_object:
            file_content = file_object.read()
        file_object.close()
        return file_content
