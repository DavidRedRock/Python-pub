## python version: 3.10.5
python -V

Python 3.10.5

## Install packages:

    .1) pip install --upgrade markdown

    .2) pip install beautifulsoup4


## Use markdon and beautifulsoup4 

### reading in a markdown file and converting it to one text.
  html = markdown.markdown(open("code-test.md").read())
  test_text = ("".join(BeautifulSoup(html, features="html.parser").findAll(text=True)))

### regular expression for the test case inputs.
  input_structure = re.compile(r'(?<=Input\n```)(\s?\n)(.*)(?=\n```)')

### find all the inputs and put into an array by matching the regular expression in the given test file.
  test_case_inputs = re.findall(input_structure, test_text)

## Run and print out all the test cases and add into README.md:

  python .\test-solution.py >> .\README.MD

### Test Case Results:

## Test case 1 output:
   .The Longest length: 3, Longest subsequence: [1, 5, 9]
## Test case 2 output:
   .The Longest length: 6, Longest subsequence: [1710, 2461, 9288, 10195, 10431, 12485]
## Test case 3 output:
   .The Longest length: 8, Longest subsequence: [10298, 10897, 12291, 15037, 18446, 23435, 25333, 27266]
## Test case 4 output:
   .The Longest length: 4, Longest subsequence: [3862, 16353, 22813, 28735]
## Test case 5 output:
   .The Longest length: 4, Longest subsequence: [11084, 11970, 24975, 30922]
## Test case 6 output:
   .The Longest length: 4, Longest subsequence: [3808, 3908, 10386, 19306]
## Test case 7 output:
   .The Longest length: 6, Longest subsequence: [125, 1841, 5882, 18464, 28317, 31497]
## Test case 8 output:
   .The Longest length: 6, Longest subsequence: [9139, 17687, 25106, 26202, 27592, 30937]
## Test case 9 output:
   .The Longest length: 8, Longest subsequence: [918, 1089, 5133, 7725, 18035, 24605, 26716, 27095]
## Test case 10 output:
   .The Longest length: 3, Longest subsequence: [2, 4, 6]
## Test case 11 output:
   .The Longest length: 3, Longest subsequence: [1, 5, 9]

