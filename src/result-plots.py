import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

"""
Graph a confusion matrix for the predicted values y_pred agains the true values y_test
    - y_test: Series/List, True values
    - y_pred: Series/List, Predicted values
    - classes: List of strings, contains the names of the classes
    - normalize: Boolean, whether or not to normalize values
"""
def graphConfusionMatrix(y_test, y_pred, classes,
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




"""
Graph scatter points in a map. Returns plot, so one can keep plotting
    - map_file_path: string, Path to image of the map
    - bBox: Tuple, with shape (Long_min, Long_max, Lat_min, Lat_max)
    - x: Series/List, horizontal axis in map
    - y: Series/List, vertical axis in map
    - color: string/char, color of points
"""
def graphScatterInMap(map_file_path,bBox,x,y,color='r'):
    BBox = (bBox)
    mapa = plt.imread(map_file_path)
    fig, ax = plt.subplots()
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(mapa, zorder=0, extent = BBox,  aspect= 'equal')
    plt.grid(b=True, color='aqua', alpha=0.1, linestyle='-', linewidth=1)
    ax.scatter(df.Pickup_longitude, df.Pickup_latitude, zorder=1, alpha= 0.2, c='b', s=10)
    ax.scatter(df.Dropoff_longitude, df.Dropoff_latitude, zorder=1, alpha= 0.2, c='r', s=10)

    return ax
    
