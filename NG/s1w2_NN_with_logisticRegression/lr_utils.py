import numpy as np
import h5py
    
#plt.imshow(train_set_x_orig[index])
#print ("y = " + str(train_set_y[:, index]) + ", it's a '" + classes[np.squeeze(train_set_y[:, index])].decode("utf-8") +  "' picture.")    
def load_dataset():
    train_dataset = h5py.File('./datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features

    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes

    print("load_dataset(),before reshape, train_set_x_orig.shape : " + str(train_set_x_orig.shape) )   
    print("load_dataset(),before reshape, train_set_y_orig.shape : " + str(train_set_y_orig.shape) )   
    print("load_dataset(),before reshape, train_set_y_orig.shape[0] : " + str(train_set_y_orig.shape[0]) )   
    #print("load_dataset(),before reshape, train_set_y_orig.shape[1] : " + str(train_set_y_orig.shape[1]) )   # IndexError: tuple index out of range

    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    print("load_dataset(),after reshape, train_set_y_orig.shape : " + str(train_set_y_orig.shape) )   
    print("load_dataset(),after reshape, train_set_y_orig.shape[0] : " + str(train_set_y_orig.shape[0]) )   

    print("load_dataset(),before reshape, test_set_y_orig.shape : " + str(test_set_y_orig.shape) )   
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    print("load_dataset(),after reshape, test_set_y_orig.shape : " + str(test_set_y_orig.shape) )   
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes
