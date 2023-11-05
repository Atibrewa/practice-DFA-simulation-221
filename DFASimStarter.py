"""
File: DFASimulator.py
Author: Susan Fox
Date: Fall 2022
Implements a bare-bones DFA simulator that can read a simple representation from a file and print the information
in the DFA, or simulate a string on it.
"""


class DFASim(object):
    """Simple DFA simulator. Does not allow for missing transitions, so you have to add "dead" states if needed."""

    def __init__(self, filename):
        """Takes in a string filename, and reads the data from the file to create the instance variables. See
        examples for what is expected."""
        fil = open(filename, 'r')
        line0 = fil.readline()
        parts = line0.split()
        self.numStates = int(parts[1])
        line1 = fil.readline()
        parts = line1.split()
        self.startState = int(parts[1])
        line2 = fil.readline()
        parts = line2.split()
        self.acceptStates = [int(s) for s in parts[1:]]
        line3 = fil.readline()
        labels = line3.split()
        self.alphabet = labels[1:]
        self.table = [[]] * self.numStates
        for line in fil:
            parts = [int(s) for s in line.split()]
            state = parts[0]
            transitions = parts[1:]
            self.table[state] = transitions
        fil.close()

    def printDFA(self):
        """Prints the information about the DFA, including the transition table."""
        print("Num states =", self.numStates)
        print("Start state =", self.startState)
        print("Accept states =", self.acceptStates)
        print()
        topLine = "Q  "
        for sym in self.alphabet:
            topLine += " " + sym + " "
        print(topLine)
        for s in range(self.numStates):
            row = str(s) + "->"
            for trans in self.table[s]:
                row += " " + str(trans) + " "
            print(row)

    def simulate(self, inputStr):
        """Given an input string, this simulates the DFA. Remarkably easier than it might seem initially!"""
        state = self.startState
        for c in range(len(inputStr)):
            index = self.alphabet.index(inputStr[c])
            state = self.table[state][index]
        if state in self.acceptStates:
            return True
        else:
            return False
        
if __name__ == "__main__":
    dfa = DFASim("dfa1.txt")
    dfa.printDFA()
    print("aa", dfa.simulate("aa"))
    print("abbbabbbabaaa", dfa.simulate("abbbbbbabaaa"))
    print("-----------")

    dfa2 = DFASim("dfa2.txt")
    dfa2.printDFA()
    print("ab", dfa2.simulate("ab"))
    print("bbb", dfa2.simulate("bbb"))
    print("ababa", dfa2.simulate("ababa"))
    print("aaabbb", dfa2.simulate("aaabbb"))
    print("-----------")

    dfa3 = DFASim("dfa3.txt")
    dfa3.printDFA()
    print("aa", dfa3.simulate("aa"))
    print("abba", dfa3.simulate("abba"))