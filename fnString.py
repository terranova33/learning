

# String Boolean Functions

combo = '1234abcd'
nums = '123456'
letters = 'abcdef'
lowerc = 'good'
upperc = 'BAD'
sentence = 'This is a Sentence'
acronym = 'This Is All Capitalised'
space = "This that"

print(combo, "alnum", (str.isalnum(combo)))

print(letters, "alpha", (str.isalpha(letters)))

print(nums, "digit", (str.isdigit(nums)))

print(lowerc, "lower", (str.islower(lowerc)))
print(upperc, "lower", (str.islower(upperc)))
print(lowerc, "lower to upper", (str.upper(lowerc)))
print(upperc, "upper to lower", (str.lower(upperc)))

print(upperc, "upper", (str.isupper(upperc)))
print(lowerc, "upper", (str.isupper(lowerc)))

print(nums, "numeric", (str.isnumeric(nums)))

print(sentence, "space", (str.isspace(sentence)))

print(sentence, "length", (len(sentence)))

#print(sentence, "count", (str.count('en', 0, 18)))


#print(acronym, "title", (str.istitle(acronym)))
#print(space, "space", (str.isspace(space)))
