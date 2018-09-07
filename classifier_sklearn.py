import csv

#read data from .csv
rf = open('result.csv','r')
dataReader = csv.reader(rf)
DataList_1 = []
DataList_2 = []
DataList_3 = []
DataList_4 = []
for rList in dataReader:
    featureIndex = len(rList) - 1
    if rList[featureIndex] == '1':
        DataList_1.append(rList)
    elif rList[featureIndex] == '2':
        DataList_2.append(rList)
    elif rList[featureIndex] == '3':
        DataList_3.append(rList)
    elif rList[featureIndex] == '4':
        DataList_4.append(rList)
rf.close()

print(len(DataList_1))
print(len(DataList_2))
print(len(DataList_3))
print(len(DataList_4))

featureIndex = len(DataList_1[0]) - 1
train_features = []
train_labels = []
test_features = []
test_labels = []

"""
print(len(DataList_1))
print(len(DataList_2))
print(len(DataList_3))
print(len(DataList_4))
"""

#switch proportion
import random
"""
TrainList_1 = random.sample(DataList_1, int(round(len(DataList_1) * 0.174)))
TrainList_2 = random.sample(DataList_2, int(round(len(DataList_2) * 0.381)))
TrainList_3 = random.sample(DataList_3, int(round(len(DataList_3) * 0.765)))
TrainList_4 = random.sample(DataList_4, int(round(len(DataList_4) * 0.1315)))
"""

TrainList_1 = random.sample(DataList_1, int(round(len(DataList_1) * 0.208)))
TrainList_2 = random.sample(DataList_2, int(round(len(DataList_2) * 0.458)))
TrainList_3 = random.sample(DataList_3, int(round(len(DataList_3) * 0.918)))
TrainList_4 = random.sample(DataList_4, int(round(len(DataList_4) * 0.158)))


# 1
for pTrain in TrainList_1:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTrain[i]))
    train_features.append(fList)
    train_labels.append(int(pTrain[featureIndex]))
    DataList_1.remove(pTrain)
for pTest in DataList_1:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTest[i]))
    test_features.append(fList)
    test_labels.append(int(pTest[featureIndex]))

# 2
for pTrain in TrainList_2:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTrain[i]))
    train_features.append(fList)
    train_labels.append(int(pTrain[featureIndex]))
    DataList_2.remove(pTrain)
for pTest in DataList_2:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTest[i]))
    test_features.append(fList)
    test_labels.append(int(pTest[featureIndex]))

#3
for pTrain in TrainList_3:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTrain[i]))
    train_features.append(fList)
    train_labels.append(int(pTrain[featureIndex]))
    DataList_3.remove(pTrain)
for pTest in DataList_3:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTest[i]))
    test_features.append(fList)
    test_labels.append(int(pTest[featureIndex]))

#4
for pTrain in TrainList_4:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTrain[i]))
    train_features.append(fList)
    train_labels.append(int(pTrain[featureIndex]))
    DataList_4.remove(pTrain)
for pTest in DataList_4:
    fList = []
    for i in range(featureIndex - 1):
        fList.append(float(pTest[i]))
    test_features.append(fList)
    test_labels.append(int(pTest[featureIndex]))

print(len(TrainList_1))
print(len(TrainList_2))
print(len(TrainList_3))
print(len(TrainList_4))


#train & predict
from sklearn import svm
modelSVM = svm.SVC(C=128.0, gamma=0.000122070312)
modelSVM.fit(train_features, train_labels)
prediction = modelSVM.predict(test_features)

""""""
#Accuracy
from sklearn.metrics import accuracy_score
from sklearn.metrics import f1_score
print f1_score(test_labels, prediction, average='micro')
print f1_score(test_labels, prediction, average='weighted')
print accuracy_score(test_labels, prediction)
