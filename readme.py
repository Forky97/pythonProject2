class Git_start :

    def __init__(self,name=None):
        self.name = name

    def privet(self):
        print(self.name)


cris = Git_start('cris')
cris.privet()
