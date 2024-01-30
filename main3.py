import pandas as pd


# training_data = pd.read_csv('traindata.csv')
# print(training_data.columns)


# print(row['Age'],#1
#       row['Gender'],#2
#       row['Chest Pain'],#3
#       row['Blood Pr'],#4
#       row['Cholesterol'],#5
#       row['Blood Sugar'],#6
#       row['ElectroCardio'],#7
#       row['Max Heart Rate'],#8
#       row['Exercise Induced Angina'],#9
#       row['ST depression ind. By exercise'],#10
#       row['Slope of the peak exercise '],#11
#       row['# of vessels'],#12
#       row['defect'],#13
#       row['Result'])#14


def predict(arr):
    arr['Prediction'] = ''

    # rules
    for row in arr.itertuples():
        if row[1] <= 55 and (row[13] < 6 or row[3] < 4):  # Defect and Chest Pain and Age
            arr._set_value(row[0], 'Prediction', 'no')
        elif (row[13] == 6 and row[3] > 4 and row[1] > 55):  # Defect and Chest Pain and Age
            arr._set_value(row[0], 'Prediction', 'yes')
        else:
            arr._set_value(row[0], 'Prediction', 'no')
        # if row[2] == 0 and row[13] == 7:  # Gender and Defect
        #     arr._set_value(row[0], 'Prediction', 'yes')
        # elif row[2] == 0 and row[1] >= 59 and row[3] == 4:  # Gender, Age and Chest Pain
        #     arr._set_value(row[0], 'Prediction', 'yes')
        # elif row[2] == 1 and row[3] == 4 and row[13] == 7:  # Gender, Defect
        #         arr._set_value(row[0], 'Prediction', 'yes')
        # else:
        #     arr._set_value(row[0], 'Prediction', 'no')


def get_accuracy_stats(arr, name):
    mismatches = len(arr[arr["Result"] != arr['Prediction']])
    total_cnt = len(arr)
    accuracy_pct = (100 * (total_cnt - mismatches)) / total_cnt

    print(f"""{name} data stats:

    Number of Mismatches: {mismatches}
    Total Count: {total_cnt}
    Accuracy Percent: {accuracy_pct}""")


training_data = pd.read_csv('test_data2.csv')

# test
training_data = training_data.sort_values(by=['Result'])

predict(training_data)

# print(training_data.groupby(by=['Gender', 'Result']).size())
#
# print(training_data.groupby(by=['Gender', 'Result','Chest Pain', 'defect']).agg({'Age': ['min', 'max', 'count']}))
#
# print('\n\n')
get_accuracy_stats(training_data, 'Training')

# print(training_data[['Age', 'Result', 'Prediction']])
test_data = pd.read_csv('test_data2.csv')
predict(test_data)
get_accuracy_stats(test_data, 'Test')
