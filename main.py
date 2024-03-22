import pandas as pd
import numpy as np


def getting_file_input():
    file_name = input('put the file name here ')
    file_content = ''

    try:
        if file_name.find('.json') != -1:
            file_content = pd.read_json(file_name)

        elif file_name.find('.xlsx') != -1 or file_name.find('.xls') != -1:
            file_content = pd.read_excel(file_name)

        elif file_name.find('.csv') != -1:
            file_content = pd.read_csv(file_name)

        else:
            print("make sure if the file name is corrct")
        return file_content
    except:
        print("something went wrong")

file_input = getting_file_input()

def Basic_Statistics():
    print("Basic Statistics:")
    print(f"Mean:\n{file_input.mean(numeric_only=True, skipna=True)}\n")
    print(f"Median:\n{file_input.median(numeric_only=True)}\n")
    print(f"Standard Deviation:\n{file_input.std(numeric_only=True)}\n")

def removed_missing_values():
    global file_input
    while True:
        axis = input("Do you want to remove rows or columns? Type 'row' for rows or 'column' for columns: ").lower()

        if axis == 'row':
            print(file_input.dropna())
            break
        elif axis == 'column':
            print(file_input.dropna(axis=1))
            break
        else:
            print("Invalid axis. No changes made.")

def imputed_missing_values():
    global file_input
    while True:
        print("warning u need full numric file to use mean and median using non numric full will case an error")
        imputation_kind = input("Choose the imputation kind (mean/median/mode): ").lower()

        if imputation_kind == "mean":
            file_input = file_input.fillna(file_input.mean())
            print(file_input)
            print("Missing values imputed using mean.")
            break
        elif imputation_kind == 'median':
            file_input = file_input.fillna(file_input.median())
            print(file_input)
            print("Missing values imputed using median.")
            break
        elif imputation_kind == 'mode':
            file_input = file_input.fillna(file_input.mode().iloc[0])
            print(file_input)
            print("Missing values imputed using mode.")
            break
        else:
            print("Invalid imputation strategy. Please choose a valid strategy.")

def one_hot_encode_column(data, column_name):
    unique_values = data[column_name].unique()
    for value in unique_values:
        new_column_name = f"{column_name}_{value}"
        data[new_column_name] = (data[column_name] == value).astype(int)
    data = data.drop(column_name, axis=1)
    return data

def one_hot_encode_categorical_columns(data):
    categorical_columns = data.select_dtypes(include=['object']).columns
    for column in categorical_columns:
        data = one_hot_encode_column(data, column)
    return data
file = file_input

def starting():
    while True:
        choices = print("Write 1 to see the full data\nWrite 2 to see the removed Missing Values\nWrite 3 to see the Basic Statistics for the data\nWrite 4 to perform One-Hot Encoding for categorical columns\nWrite 'QUIT' to stop")
        choice = input("Choose a number: ").lower()

        if choice == "1":
            print(file)
            starting()
            break

        elif choice == "2":
            removed_missing_values()
            starting()
            break


        elif choice == "3":
            Basic_Statistics()
            starting()
            break

        elif choice == "4":
            file_input = one_hot_encode_categorical_columns(file)
            print("One-Hot Encoding applied to categorical columns.")
            print(file_input)
            starting()
            break

        elif choice == "quit":
            break
        else:
            print("Invalid input. Please input one of the numbers.")
starting()