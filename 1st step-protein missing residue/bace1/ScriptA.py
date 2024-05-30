from modeller import *

env = environ()
aln = alignment(env)
mdl = model(env, file="7myi", model_segment=("FIRST:A","LAST:A"))
aln.append_model(mdl, align_codes="7myi", atom_files="7myi.pdb")
aln.append(file="bace1.ali", align_codes="bace1")
aln.align2d()
aln.write(file="alignment.ali", alignment_format="PIR")
aln.write(file="alignment.pap", alignment_format="PAP")

























