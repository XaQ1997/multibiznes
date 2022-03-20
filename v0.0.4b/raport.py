class Raport:
    def __init__(self, path):
        self.path=path

    def write(self, description):
        file=open(self.path, 'a+')
        file.write(description)
        file.close()