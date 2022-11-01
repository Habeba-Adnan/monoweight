
from pyopenms import *
#Alinine , Arginine , Glycine , Lycine
seq = AASequence.fromString("ARGK")
res = seq.getMonoWeight()
print (res)

seq1 = AASequence.fromString("A")
res1 = seq1.getMonoWeight()
print (res1)

seq2 = AASequence.fromString("R")
res2 = seq2.getMonoWeight()
print (res2)

seq3 = AASequence.fromString("G")
res3 = seq3.getMonoWeight()
print (res3)

seq4 = AASequence.fromString("K")
res4 = seq4.getMonoWeight()
print (res4)

fullres=res1+res2+res3+res4
print(fullres)
