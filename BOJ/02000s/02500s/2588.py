a = int(input())
b = int(input())

third = a*(b%10)
fourth = a*((b%100)//10)
fifth = a*((b%1000)//100)
print(third)
print(fourth)
print(fifth)
print(third + (fourth*10) + (fifth*100))