import pandas as pd
import numpy as np

from voice import mfcc
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import glob
import pickle
from sklearn.metrics import classification_report

def train_on_test():
    features = []

    for file in glob.glob("data/*.wav"):
        features.append(load_data_from_path(file))

    df = pd.DataFrame(features, columns=['feature', 'class_label'])
    print(df.head())
    train_knn(df)


def load_data_from_path(path):
    data = mfcc.extract_features(path)
    label = "inny"
    if "kacper" in path:
        label = 'kacper'
    if "kuba" in path:
        label = "kuba"

    return [data, label]

def train_knn(df, who):

    X = np.array(df.feature.tolist())
    Y = np.array(df.class_label.tolist())
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=127)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(x_train, y_train)

    filename = 'models/'+who+'.sav'
    pickle.dump(clf, open(filename, 'wb'))

    pred = clf.predict(x_test)
    print(pred)
    print(y_test)
    target_names = [who, 'inny']
    print(classification_report(y_test, pred, target_names=target_names))


def decide(model, who):
    data = mfcc.extract_features('output.wav').reshape(1,-1)

    # loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    result = model.predict(data)

    print(result)
    return result == who
