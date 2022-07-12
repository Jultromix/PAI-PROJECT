#Email:juliomoreno7217@gmail.com
#Github´s link repository: https://github.com/Jultromix/PAI-PROJECT.git  
#File´s creation date: 07/3/2022

#Properties:
    #nd-array
    #GPU support
    #Computational graph / Backpropagation
    #immutable
    
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"    #surprims extra info/warnings not needed*cls


import tensorflow as tf

#Constant Tensors
x0 =tf.constant(4,shape=(1,1), dtype=tf.float32)        #rank 1 tensor
x1 =tf.constant(2,shape=(1,1), dtype=tf.int32)          #rank 1 tensor
x2 =tf.constant([2,4,6,8,10])                           #rank 1 tensor
x3 =tf.constant([[2,4,6,8,10],[1,2,3,4,5]])             #rank 2 tensor
x4=tf.ones((2,5))                                       #rank 2 tensor
x5=tf.zeros((2,5))                                      #rank 2 tensor

print(x0)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)