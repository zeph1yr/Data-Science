#Tensorflow 2.0 goes away from session and switches to eager execution.
#You can still run your code using session if you refer to tf.compat library and disable eager execution

import tensorflow as tf

x = tf.Variable(3, name = 'x')
y = tf.Variable(4, name= 'y')
f = x + y


tf.compat.v1.disable_eager_execution()

init = tf.compat.v1.global_variables_initializer()
with tf.compat.v1.Session() as sess:
    init.run()  
    result = f.eval()
    print(result)
