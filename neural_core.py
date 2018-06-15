import tensorflow as tf



def getNeuralNetwork(numInputs):
    input_layer = tf.placeholder(tf.float32, shape=[None, numInputs])
    
    #units is number of neurons
    dense = tf.layers.dense(inputs=input_layer, units=100, activation=tf.nn.relu)
    dense2 = tf.layers.dense(inputs=dense, units=100, activation=tf.nn.relu)
    
    logits = tf.layers.dense(inputs=dense2, units=4)#l,r,straight, reverse
    
    predictions = {
      # Generate commands
      "classes": tf.argmax(input=logits, axis=1),
    }

    return tf.estimator.EstimatorSpec(predictions=predictions)


