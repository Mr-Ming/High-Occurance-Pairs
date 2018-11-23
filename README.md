# High-Occurance-Pairs

Using Python, given an input TXT file `Artist_lists_small.txt`, 
1. find pairs that appear at least 50x most frequent
2. sort it by frequency
3. then output it to `outputFile.csv`

The application can be modified:
1. minimum appearance can be changed here: `https://github.com/Mr-Ming/High-Occurance-Pairs/blob/master/find_high_occurance_pairs.py#L8`
2. input file name can be changed here: `https://github.com/Mr-Ming/High-Occurance-Pairs/blob/master/find_high_occurance_pairs.py#L6`
3. output file name can be changed here: `https://github.com/Mr-Ming/High-Occurance-Pairs/blob/master/find_high_occurance_pairs.py#L7`

## To Run The Program
1. Follow the setup instruction to install `python` and cloning the repo
2. cd into the root of the program directory `cd High-Occurance-Pairs`
3. run `find_high_occurance_pairs`

## To Run The Unit Test (IMPORTANT! TEST NEED TO BE RUN FROM ROOT)
1. Follow the setup instruction to install python and cloning the repo
2. cd into the root of the program directory `cd High-Occurance-Pairs`
3. run `python password_validator_test.py`

.............
----------------------------------------------------------------------
Ran 10 tests in 0.001s

OK


![screen shot 2018-11-22 at 12 58 04 am](https://user-images.githubusercontent.com/2894340/48884340-1382ae00-edf2-11e8-9bc5-68efcb3301b3.png)


## Setup Instructions
1. Let install <a href="https://brew.sh/">`homebrew`</a>, a package manager that will help us install python

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

2. Install Python through brew

```
brew install python
```

3. Clone the Repo

```
git clone https://github.com/Mr-Ming/High-Occurance-Pairs.git
```
## Optimization / Choice of Language
Originally I was going to write this script using PHP that does the following
- Read the Input File, then iterate through everything, then generates the pairs through a double for-loop
- Save each pair as an `index` of an array and the `value` of the array would be its # of occurance
- Finally Save the result to the output file while occurance >= 50

But then using that method has a complexity of O(n^3) due to 3 nested-loops (1st-reading from input, 2nd & 3rd is generating the pair)

So I though this would be a better time to explore python and read more about it, because python is very good for performing complex computation as its widely use in Machine Learning

My research led me to 2 things
- itertool.combination (https://docs.python.org/2/library/itertools.html)
-- Which is a very powerful python package that lets you quickly generate permutation of result in various length you like 
- collections.defaultdict(int) (https://docs.python.org/2/library/collections.html#collections.defaultdict)
-- Which is the best data structure to store exactly this specific type of data because I wanted a data structure type that allows me to 
--- (1) Store both the pair and # of occurance as 1 array
--- (2) Have O(1) constant time for searching


## Screenshots
1. input

![screen shot 2018-11-22 at 1 00 46 am](https://user-images.githubusercontent.com/2894340/48884339-1382ae00-edf2-11e8-98ed-458d357af2bc.png)
2. output

![screen shot 2018-11-22 at 1 00 36 am](https://user-images.githubusercontent.com/2894340/48884338-1382ae00-edf2-11e8-9876-a34120f72c26.png)

