import datetime

def test_func_speed(func):
    start = datetime.datetime.now()

    finish = datetime.datetime.now()
    print finish - start

def count_substring_b(string, sub_string):
    sum = 0
    index = 0
    while(index < len(string)):
        matchIndex = string.find(sub_string, index)
        if matchIndex != -1:
            index = matchIndex + 1
            sum += 1
        else:
            break
    return sum

def count_substring_a(string, substring):
    return sum([ 1 for i in range(len(string)-len(substring)+1) if string[i:i+len(substring)] == substring])

string = """aabsabasdbabbasdbadifjaasdaboibaijdaodiabjabasdibaosidjbaos
        aabsabasdbabbasdbadifjaasdaboibaijdaodiabjabasdibaosidjbaosdibj
        aabsabasdbabbasdbadifjaasdaboibaijdaodiabjabasdibaosidjbaosdibj
        aabsabasdbabbasdbadifjaasdaboibaijdaodiabjabasdibaosidjbaosdibj"""

substring = 'ab'

# print 'a n * 1'
# test_func_speed(count_substring_a(string, substring))
#
# print 'b n * 1'
# test_func_speed(count_substring_b(string, substring))

# print 'a n * 2'
# test_func_speed(count_substring_a(string*2, substring))
#
# print 'b n * 2'
# test_func_speed(count_substring_b(string*2, substring))

print 'a n * 3'
test_func_speed(count_substring_a(string*3, substring))

print 'b n * 3'
test_func_speed(count_substring_b(string*3, substring))
