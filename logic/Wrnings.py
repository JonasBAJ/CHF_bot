

class Warnings(object):

    @staticmethod
    def fileNameException():
        return "Strange letters in filename detected!\n" \
               "Please rename the file."

    @staticmethod
    def fileTypeException():
        return "Only MS Word (.docx) and LibreOffice (.odt)\n" \
               "file formats are supported."

    @staticmethod
    def noneFileException():
        return "File not loaded!"
