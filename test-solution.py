import markdown
from bs4 import BeautifulSoup
import re

# reading in a markdown file and converting it to one text.
html = markdown.markdown(open("code-test.md").read())
test_text = ("".join(BeautifulSoup(html, features="html.parser").findAll(text=True)))

# regular expression for the test case inputs.
input_structure = re.compile(r'(?<=Input\n```)(\s?\n)(.*)(?=\n```)')

# find all the inputs and put into an array by matching the regular expression in the given test file.
test_case_inputs = re.findall(input_structure, test_text)

# Remove the matches extra spaces.
n = 1
test_case_inputs = [x[n] for x in test_case_inputs]

def find_longest_subsequence(input):
    max_len = 0
    longest_sub = [input[0]]
    current_sub = [input[0]]

    for i in range(1,len(input)):
        #print('i: ' + str(input[i]) + ' i-1: ' + str(input[i-1]) + ' max: ' + str(max))
        # check if next int is bigger than the previous int
        if(input[i]>input[i-1]):
            current_sub.append(input[i])
            #print(current_sub)
            # Check the last digit of the input.
            if (i == len(input) - 1) and (len(current_sub) > len(longest_sub)):
                    longest_sub = current_sub
                    max_len = len(current_sub)
                    # reinitialise
                    current_sub = [input[i]]
        else:
            # update longest subsequence if current subsequence is longer
            if(len(current_sub) > len(longest_sub)):
                longest_sub = current_sub
                max_len = len(current_sub)
                # reinitialise
                current_sub = [input[i]]
            # if current subsequence is not longer than previous longest subsequence, then reinitialise
            else:
                # reinitialise
                current_sub = [input[i]]
    print("Longest length: " + str(max_len) + ", Longest subsequence: " + str(longest_sub))

# Run and print out all the test case outputs.
for i in range(0, len(test_case_inputs)):
    input = list(map(int,test_case_inputs[i].split(' ')))
    print("Test case " + str(i+1) + " output")
    find_longest_subsequence(input)