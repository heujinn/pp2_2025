string = 'Apple BananA Kwii CherrY'

def count_of_upper_lower(string):
    upper_count = sum(1 for x in string if x.isupper())
    lower_count = sum(1 for x in string if x.islower())

    return upper_count, lower_count

print(count_of_upper_lower(string))