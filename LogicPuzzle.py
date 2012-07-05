"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

import itertools

def logic_puzzle():
    "Return a list of the names of the people, in the order they arrive."
    days = range(2, 7)
    names = ['Wilkes', 'Hamming', 'Minsky', 'Knuth', 'Simon']
    orderings = list(itertools.permutations(days))
    return next([name for (day, name) in sorted(zip((Wilkes, Hamming, Minsky, Knuth, Simon), names))]
                for (Monday, Tuesday, Wednesday, Thursday, Friday) in orderings
                for (Laptop, Droid, Tablet, iPhone, DEVICE) in orderings
                if Wednesday is Laptop and
                Friday is not Tablet and
                Tuesday in set([iPhone, Tablet]) #1,8,12
                for (Wilkes, Hamming, Minsky, Knuth, Simon) in orderings
                if Knuth is Simon + 1 #6
                for (Programmer, Writer, Manager, Designer, PRO) in orderings
                if Programmer is not Wilkes and
                set([Programmer, Droid]) == set([Wilkes, Hamming]) and
                Writer is not Minsky and
                Manager not in set([Knuth, Tablet]) and
                Thursday is not Designer and
                Designer is not Droid and
                Knuth is Manager + 1 and
                set([Laptop, Wilkes]) == set([Monday, Writer]) #2,3,4,5,7,9,10,11
                )

print logic_puzzle()