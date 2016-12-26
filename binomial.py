import math

def binomial_tree(u, d, S0, n):
    result = []
    for element in range(1, n + 2):
        temparray = []
        for number in range(element - 1, -1, -1):
            u_power = number
            d_power = element - 1 - number
            temparray.append(u ** u_power * d ** d_power * S0)
        result.append(temparray)
    return result

def ncr(n, r):
    return math.factorial(n)/math.factorial(r)/math.factorial(n-r)

#def price_tree(btree, n, strike):
#    result = []


voltly = 0.3
T = 0.25
n = 15
u = math.exp(voltly*math.sqrt(T/n))
d = 1.0/u
S0 = 100
r = 0.02
c = 0.01
Rn = math.exp(r*T/n)
strike = 110

p = (math.exp((r-c)*T/n) - d) / (u - d)

q = 1 - p

binomial_arr = binomial_tree(u, d, S0, n)

l = [max(binomial_arr[n][i] - strike, 0) for i in range(0, n+1)]

coeff = [ncr(n, number) for number in range(0, n+1)]

price = 0
for number in range(0, n+1):
    price = price + coeff[number]*l[number]*p**(n-number)*q**(number)

price = price/(Rn**n)


print("price of call option", price)





