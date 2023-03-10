# # 3. City Population

# The city has a known population p0

# A percentage of population perc is added each year

# Every year a certain number of delta also arrive (or leave)

# We need to know when (if at all) the city will reach a population of p

# Write a function get_city_year (p0, perc, delta, target_p) that returns the years (full) when target_p is reached.

# If target_p cannot be reached, then we return -1

# Example:

# get_city_year(1000,2,50,1200) -> 3

# 1000 + 1000 * 0.02 + 50 => 1070 after the 1st year
# notice that we have an integer (whole number) percentage, so the population after the 1st year is 1070, not 1070.4 or 1070.6

# 1070 + 1070 * 0.02 + 50 => 1141 after the 2nd year

# 1141 + 1141 * 0.02 + 50 => 1213 after the 3rd year

# so the function here returns 3 and is done

# PS. Note that we give perc as a percentage to be converted to a decimal number.

# More test examples:

# get_city_year(1000, 2, -50, 5000) -> -1

# get_city_year(1500, 5, 100, 5000) -> 15

# get_city_year(1500000, 2.5, 10000, 2,000,000) -> 10

# the trickiest case is something like this
# get_city_year(1000, -3, 50, 2000) -> -1 is the correct answer but how to get there?


def get_city_year(p0, perc, delta, target_p):
    target_population_year = 0
    current_population = p0
    while current_population <= target_p:
        current_population = current_population + current_population*perc/100 + delta
        target_population_year += 1
    print(target_population_year)
    return target_population_year


get_city_year(1000, 2, 50, 1200)


# 1. The Big Result

# Write an add_mult function that requires three parameters / arguments

# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest argument value.

# PS Assume that numeric parameters will always be passed to the function, no need to check types

# Various solutions are possible (you are allowed to use other data structures inside function such as list).

# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30

# PSS function should return the result, not print it.


# def add_mult(a, b, c):
#     my_list = [a, b, c]
#     my_list.sort()
#     largest = my_list[-1]
#     smallest = my_list[0]
#     smallest2 = my_list[1]
#     result = (smallest + smallest2)*largest
#     print(result)
#     return result


# add_mult(5, 12, 3)


# 2. Palindrome

# Write the function is_palindrome(text)

# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.

# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and uppercase and lowercase letters.

# is_palindrome ("Alus ari i ra    sula") -> True

# is_palindrome("ABa") -> True

# is_palindrome("nava") -> False

# def is_palindrome("aBa"):
#     is_palindrome_new = is_palindrome.replace(" ", "")
#     if is_palindrome_new == is_palindrome_new[::-1]:
#         print(True)
#     else:
#         print(False)
#     return result


# is_palindrome("aBa")
