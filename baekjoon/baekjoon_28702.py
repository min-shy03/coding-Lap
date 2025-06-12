# FizzBuzz

lst = [input() for _ in range(3)]

for idx, val in enumerate(lst) :
    if val.isdigit() :
        val = int(val)
        break
        
val += (3 - idx)

if val % 3 == 0 and val % 5 == 0 :
    print("FizzBuzz")
elif val % 3 == 0 :
    print("Fizz")
elif val % 5 == 0 :
    print("Buzz")
else :
    print(val)