import tensorflow as tf

#defining tensors

a=tf.constant(7)
b=tf.constant(10)
c = tf.add(a,b)

#A simple graph adding two constants

simple_session = tf.compat.v1.Session() # Creating a session to run our graph, (for version 2.0)
value_of_c = simple_session.run(c)
print(value_of_c)   
simple_session.close()
