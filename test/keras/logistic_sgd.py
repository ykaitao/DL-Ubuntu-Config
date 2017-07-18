import gzip
import six.moves.cPickle as pickle
import numpy as np

import keras
from keras.models import Model
from keras.layers import Input, Dense


# Load the dataset
def load_data(data_file):
    with gzip.open(data_file, 'rb') as f:
        try:
            train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
        except:
            train_set, valid_set, test_set = pickle.load(f)

    return (train_set, valid_set, test_set)



# LogisticRegression using Keras
def LogisticRegression(input_shape=None, activation='softmax', num_classes=10):
    
    img_input = Input(shape=input_shape)
    x = Dense(units=num_classes, activation=activation, name='logistic_regression')(img_input)
    model = Model(img_input, x, name='logistic_regression')
    return model
    
if __name__ == '__main__':
    # Load data
    data_file = r'../mnist.pkl.gz'
    train_set, valid_set, test_set = load_data(data_file)
    print(train_set[0].shape,train_set[1].shape)
    
    # Set parameters
    batch_size = 6000
    num_classes = 10
    lr = 0.1
    epoch_per_batch = 3
    trainset_size, img_dim = train_set[0].shape
    
    # Build model
    model = LogisticRegression(input_shape=(img_dim,), num_classes=num_classes)
    model.compile(optimizer=keras.optimizers.SGD(lr=lr), # Adadelta, sgd
                  loss= 'sparse_categorical_crossentropy', # sparse_categorical_crossentropy loss_custom 
                  metrics=['sparse_categorical_accuracy'])
    

    
    for batch in range(300000000):
        rand_index_array =  np.random.randint(0, trainset_size-1, size=batch_size)
        X = train_set[0][rand_index_array, :]
        y = train_set[1][rand_index_array]
        
#         Y = keras.utils.to_categorical(y, num_classes=num_classes)
        
        for epoch in range(epoch_per_batch):
            loss = model.train_on_batch(X, y)
        
        if 0==batch%10:
            batch_size_valid = 100
            rand_index_array =  np.random.randint(0, valid_set[0].shape[1]-1, size=batch_size_valid)
            X = valid_set[0][rand_index_array, :]
            y = valid_set[1][rand_index_array]
            
            loss = model.evaluate(X, y, batch_size=batch_size_valid, verbose=0)
            print('batch %d, loss %f, accuracy %f'%(batch, loss[0], loss[1]))
    
