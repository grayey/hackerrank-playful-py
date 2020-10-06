
# FAIILED 11 test cases

def stringAnagram(dictionary, query):
    # Write your code here
    results = list()
    for i, string_value in enumerate(query): # so you can access the index  i
        no_of_anagrams = 0
        for word in dictionary:
            if (sorted(word) == sorted(string_value)):
                no_of_anagrams+=1
        results.append(no_of_anagrams)
    return results 