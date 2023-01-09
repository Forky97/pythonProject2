class Git_start :

    def __init__(self,name=None):
        self.name = name

    def privet(self):
        print(self.name)


cris = Git_start('cris')
cris.privet()

########### add 2 objects ##########

edic = Git_start('edic')
vlad = Git_start('vlad')
bily = Git_start('billy') 
edic.privet()
vlad.privet()
billy.privet()

