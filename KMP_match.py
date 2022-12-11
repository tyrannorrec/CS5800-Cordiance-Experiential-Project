#using openGPT


class string_to_int:

    def __init__(self) -> None:
        pass

    # Function to create the KMP table for a given word
    def create_kmp_table(self, word):
        # Initialize the KMP table with zeros
        table = [0] * len(word)

        # Set the first value in the table to -1
        table[0] = -1

        # Set the values in the table by looping over the word
        for i in range(1, len(word)):
            j = table[i - 1]
            while j >= 0 and word[j] != word[i - 1]:
                j = table[j]
            table[i] = j + 1
        return table

    # Function to match a list of words to a long string using the KMP algorithm
    def match_words_kmp(self, words, string):
        # Initialize the list of matches
        matches = []

        # Create the KMP table for each word
        tables = [self.create_kmp_table(word) for word in words]

        # Loop over the long string, looking for matches
        for i in range(len(string)):
            # Loop over each word in the list
            for j, word in enumerate(words):
                # Initialize the word match index to 0
                k = 0
                # Loop over the word and the string
                while k < len(word) and i + k < len(string) and word[k] == string[i + k]:
                    # Increment the word match index
                    k += 1

                # If the entire word has been matched, add it to the list of matches
                if k == len(word):
                    matches.append((i, i + k - 1, j))

                # Update the word index based on the KMP table
                i += k - tables[j][k]
        return matches

def main():
    ava_words = ['digital', 'goods', 'digital', 'goods', 'generally', 'viewed', 'downloadable', 'items', 'that', 'sold', 'websites', 'that', 'otherwise', 'transferred', 'electronically', 'examples', 'would', 'include', 'computer', 'software', 'artwork', 'photographs', 'music', 'movies', 'files', 'books', 'pdfs', 'more', 'digital', 'goods', 'generally', 'viewed', 'downloadable', 'items', 'that', 'sold', 'websites', 'that', 'otherwise', 'transferred', 'electronically', 'examples', 'would', 'include', 'computer', 'software', 'artwork', 'photographs', 'music', 'movies', 'files', 'books', 'pdfs', 'more']
# UN = "cloudservicessaasserviceagreementdatabaseproductsforbusinessuseonly"
# *set() * is the unpack the list and each element is passed as different parameters.
# set will remove duplicates and using [] merge all the remaining elements to form a new list
ava_words_set = [*set(ava_words)]
UN = "Cloud services - saas - service agreement - database products - for business use only"


if __name__== '__main__':
    main()