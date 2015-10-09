def length(word):
    return len([i for i in word if i!= " "])
    
tot = 0

#"and"
tot += 3 * ((1000-100)-10)

#ten 
tot += 3 * 10

#twenty
tot += 6 * (10 * 10)

#thirty
tot += 6 * (10 * 10)

#forty
tot += 5 * (10 * 10)

#fifty
tot += 5 * (10 * 10)

#sixty
tot += 5 * (10 * 10)

#seventy
tot += 7 * (10 * 10)

#eighty
tot += 6 * (10 * 10)

#ninety
tot += 6 * (10 * 10)

#hundred
tot += 7 * (1000-100)

#one thousand
tot += 11

#teens
tot += len("eleventwelvethirteenfourteenfifteensixteenseventeeneighteennineteen") * 10

#one
tot += 3 * ((10 * 10 + 100) + 1 - 10)

#two
tot += 3 * (10 * 10 + 100 - 10)

#three
tot += 5 * (10 * 10 + 100 - 10)

#four
tot += 4 * (10 * 10 + 100 - 10)

#five
tot += 4 * (10 * 10 + 100 - 10)

#six
tot += 3 * (10 * 10 + 100 - 10)

#seven
tot += 5 * (10 * 10 + 100 - 10)

#eight
tot += 5 * (10 * 10 + 100 - 10)

#nine
tot += 4 * (10 * 10 + 100 - 10)

print tot