import os
import random

import pandas as pd
import numpy as np

from voice import mfcc
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import glob
import pickle
from sklearn.metrics import classification_report

def train_for_classname(who):
    features = []

    for file in glob.glob("../train_voice/data/*.wav"):
        features.append(load_data_from_path(file, who))

    # ramka której 1. kolumna to wektory cech, a druga to nazwa klasy dla pliku audio
    df = pd.DataFrame(features, columns=['feature', 'class_label'])
    print(df.head())
    train_knn(df, who)


def load_data_from_path(path, who):
    #załaduj dane z pliku i dokonaj pre-processingu i ekstrakcji cech melowych
    data = mfcc.extract_features(path)
    #dopasuj etykietę dla pliku ('kuba', 'kacper', 'inny')
    label = "inny"
    if who in path:
        label = who

    return [data, label]

def train_knn(df, who):
    # przypisanie X tablicy wektorów cech
    X = np.array(df.feature.tolist())
    # przypisanie y tablicy klas dla wektorów
    Y = np.array(df.class_label.tolist())
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.1, random_state=127,)

    clf = KNeighborsClassifier(n_neighbors=3)
    clf.fit(x_train, y_train)

    filename = '../train_voice/models/'+who+'.sav'
    pickle.dump(clf, open(filename, 'wb'))

    # uruchomienie klasyfikacji dla zbiorów testowych
    pred = clf.predict(x_test)
    print(pred)
    print(y_test)
    target_names = [who, 'inny']
    # raport klasyfikacji na zbiorze testowym
    print(classification_report(y_test, pred, target_names=target_names))


def decide(model, who):
    data = mfcc.extract_features('../output.wav').reshape(1,-1)
    # result to wynik klasyfikacji ze zbioru [who, 'inny'], gdzie who to nazwa użytkowanika, którego modelu używamy ('kacper', 'kuba')
    result = model.predict(data)

    print(result)
    return result == who

def decide_for_test(model, who):
    data = mfcc.extract_features(random.choice(os.listdir("../train_voice/data")))
    print(data)
    result = model.predict(data)

    print(result)
    return result == who
