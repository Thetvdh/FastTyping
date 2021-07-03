import sys
import time
import string
import random
import pandas as pd
import matplotlib.pyplot as plt


def trainer(sentences_dict):
    data = {}
    for key, value in sentences_dict.items():
        start_time = time.time()
        input1 = input(value['sentence'] + " ")
        runtime = round((time.time() - start_time), 2)
        if value['sentence'] == input1 and runtime < value['time']:
            data[key] = [True, runtime]
        else:
            data[key] = [False, runtime]
    return data


def generate_sentences(num_sentences):
    data = {}
    for i in range(1, num_sentences+1):
        data["Level"+str(i)] = {"sentence": generate_strings(i), "time": i+1}
    return data


def generate_strings(length):
    letters = string.ascii_letters
    digits = string.digits
    output = ""
    for i in range(1, length+1):
        output += random.choice(letters + digits)
    return output


def format_value(formatter):
    new = {}
    for key, value in formatter.items():
        if value[0]:
            new[key] = ["Correct", value[1]]
        else:
            new[key] = ["Incorrect", value[1]]
    return new


def graph_bar(frame):
    choice = input("\nWould you like to have a bar chart of your results? Y/N ")[0].lower()
    if choice == 'y':
        x = ["correct", "incorrect"]
        num_correct = 0
        num_incorrect = 0
        for key, value in frame.items():
            if value[0]:
                num_correct += 1
            else:
                num_incorrect += 1
        y = [num_correct, num_incorrect]

        plt.bar(x, y)
        plt.show()
        print("Goodbye!!")
        sys.exit()
    else:
        print("Ok goodbye!!")
        sys.exit()


if __name__ == '__main__':
    while True:
        try:
            number_sentences = int(input("How many strings would you like to test yourself against?"))
            sentences = generate_sentences(number_sentences)
            results = trainer(sentences)
            formatted = format_value(results)
            dataframe = pd.DataFrame(formatted, index=["Result", "TimeTaken"])
            print(dataframe)
            graph_bar(results)
        except ValueError:
            print("Please enter a number instead")
