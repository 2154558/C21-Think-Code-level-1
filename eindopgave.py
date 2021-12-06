#je moet gokken of iets goter is dan 100
import random

n = random.randint(0, 200)


print("denk je dat het hoger of lager is dan 100")
print(n)

y = input("hoger of lager: ").lower()


if n < 100 and y =='lager':
    print("juist")

if n < 100 and y =='hoger':
    print("onjuist")

if n > 100 and y =='hoger':
    print("juist")

if n > 100 and y =='lager':
    print("onjuist")