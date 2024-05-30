from modeller import *
from modeller.scripts import complete_pdb

log.verbose()  
env = environ()
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

# read model file
mdl = complete_pdb(env, 'bace2.13DOPE.pdb')

# Assess all atoms with DOPE:
s = selection(mdl)
s.assess_dope(output='ENERGY_PROFILE NO_REPORT', file='model13.profile',
              normalize_profile=True, smoothing_window=15)
