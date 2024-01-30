
import csv
import numpy as np

#input_features=['Age', 'Gender', 'Chest Pain', 'Blood Pr', 'Cholesterol', 'Blood Sugar',
#       'ElectroCardio', 'Max Heart Rate', 'Exercise Induced Angina',
#       'ST depression ind. By exercise', 'Slope of the peak exercise ',
#       '# of vessels', 'defect', 'Result']
# y=[]

with open("test_data.csv","r") as f_input:
    csv_input = csv.DictReader(f_input)
    age =[]
    chestPain =[]
    y_true =[]
    for row in csv_input:
        age.append(int(float(row['Age'])))
        chestPain.append(int(float(row['Chest Pain'])))
        y_true.append(row['Result'])


y_pred=[]

for i in range(len(y_true)):
    if chestPain[i] == 4:
        if age[i] >= 50:
            y_pred.append('yes')
        else:
            y_pred.append('no')
    elif chestPain[i] < 4:
        if age[i] < 50:
            y_pred.append('no')
        else:
            y_pred.append('no')
        #print(chestPain[i])
        #print(age[i])

#print(len(y_true))
#print(len(y_pred))


count=0

for i in range(len(y_true)):
    if(y_true[i]!=y_pred[i]):
        count+=1
print("Incorrect: {}".format(count))
accuracy=((len(y_true)-count)/len(y_true))
print("Accuracy: {}".format(accuracy))
print("The accuracy of the model is {:.2%}".format(accuracy))
