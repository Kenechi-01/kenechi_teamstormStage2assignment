def three_five_sum(limit):
    result = 0
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            result+=i
            return result
print (three_five_sum(20))

def three_five_sum(limit):
    result = 0
    for number in range (limit):
        if number %3 == 0:
            result += number
        elif number %5 == 0:
            result += number
        return result
print(three_five_sum(20))