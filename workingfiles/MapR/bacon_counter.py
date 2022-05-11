# Dependencies
from mrjob.job import MRJob

# Create a class
class Bacon_count(MRJob):
    # Takes each line and searches for the word bacon and yields 'bacon', 1 that many times
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == 'bacon':
                yield 'bacon', 1
    
    # There is a 'shuffle' step that occurs after the mapper function - no code is written here but it happens b/c
    # Bacon_count 'class', 'inherits' from the mrjob library
    # The 'shuffle' step will organize the key-value pairs so that there's only one key for each unique key, and combines the values into a list.

    # Reducer function sums up the values (per unique key) from the 'shuffle' step
    def reducer(self, key, values):
        yield key, sum(values)

# Run the program
if __name__ == "__main__":
    Bacon_count.run()