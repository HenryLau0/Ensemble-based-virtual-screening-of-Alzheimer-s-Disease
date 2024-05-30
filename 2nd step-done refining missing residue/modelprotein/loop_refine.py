from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()

env.io.atom_files_directory = './:../atom_files'


class MyLoop(loopmodel):
    def select_loop_atoms(self): 
        return selection(self.residue_range('125', '145'))

m = MyLoop(env,
           inimodel='##########.pdb',
           sequence='#####',
		   loop_assess_methods=assess.DOPE)          

m.loop.starting_model= 1          
m.loop.ending_model  = 3         
m.loop.md_level = refine.slow


m.make()