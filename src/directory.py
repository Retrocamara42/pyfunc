import os, shutil
import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix


"""
Move all files from folder1 to folder2
    - folder1: string, path of soure folder
    - folder2: string, path of destination folder
"""
def moveBetweenFolders(folder1, folder2):
    for root, subdirs, files in os.walk(folder1):
        for file in files:
            path = os.path.join(root, file)
            shutil.move(path, os.path.join(folder2, os.path.relpath(path, folder1)))


"""
TODO: A function that shows all uniques values in columns for categorical data
and min max range for numeric data (as well as mean and variance) in a very
orderly way
"""



"""
Graph a confusion matrix for the predicted values y_pred agains the true values y_test
    - y_test: Series/List, True values
    - y_pred: Series/List, Predicted values
    - classes: List of strings, contains the names of the classes
    - normalize: Boolean, whether or not to normalize values
"""
def graficarMatrizConfusion(y_test, y_pred, classes,
                          normalize=True,
                          title='Confusion matrix'):
    #cnf_matrix = confusion_matrix(y_test.argmax(axis=1), y_pred.argmax(axis=1))
    cnf_matrix = confusion_matrix(y_test, y_pred, labels=classes)
    np.set_printoptions(precision=2)
    cmap=plt.cm.Blues
    if normalize:
        cnf_matrix = cnf_matrix.astype('float') / cnf_matrix.sum(axis=1)[:, np.newaxis]
    else:
        pass

    plt.figure()
    plt.imshow(cnf_matrix, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cnf_matrix.max() / 2.
    for i, j in itertools.product(range(cnf_matrix.shape[0]), range(cnf_matrix.shape[1])):
        plt.text(j, i, format(cnf_matrix[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cnf_matrix[i, j] > thresh else "black")
    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.show()
