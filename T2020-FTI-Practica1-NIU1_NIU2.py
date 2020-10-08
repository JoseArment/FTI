
# coding: utf-8

# In[ ]:


# IMPORTANT!!!
# [1] Introduïu les dades sobre el vostre grup en el format especificat.
# [2] Desar la pràctica posant els NIUs dels membres del grup
# [3] És imprescindible que el worksheet es pugui avaluar completament (Cell->Run All) sense que es produeixi cap error de sintaxi. 
# [4] Cal lliurar el worksheet ABANS de finalitzar la vostra sessió de pràctiques.
# [5] No s'avaluaran worksheets que no compleixin els requisits anteriors.

GROUP = "a2"

NIU_ESTUDIANT_1 = 1459533
NOM_ESTUDIANT_1 = "Adrian Arnela"

NIU_ESTUDIANT_2 = 1457741
NOM_ESTUDIANT_2 = "Jose Armenteros"


# In[6]:


# EXERCISE 1a: Implement divisibility rule for 9
#
# Function UAB_divisible_by_9.
# * Parameter n: Integer to check (>= 0)
# * Returns: boolean, true if n is divisible by 9, false otherwise.
#

def UAB_divisible_by_9(n):
    
    num_as_string = str(n)
    n_length = len(num_as_string)
    digit_sum = 0
    result = None
    
    for i in range (0, n_length):
        digit_sum = digit_sum + (int)(num_as_string[i])
    
    if (digit_sum % 9 == 0):
        result = true
    
    return result


# In[ ]:


# EXERCISE 1b: Implement divisibility rule for 11
#
# Function UAB_divisible_by 11.
# * Parameter n: Integer to check (>= 0)
# * Returns: boolean, true if n is divisible by 11, false otherwise.
#

def UAB_divisible_by_11(n):
    
    num_as_string = str(n)
    n_length = len(num_as_string)
    digit_sum = 0
    result = None
    
    for i in range (0, n_length):
        digit_sum = digit_sum + (int)(num_as_string[i])
    
    if (digit_sum % 11 == 0):
        result = true
    
    return result


# In[ ]:


# EXERCISE 2a: Compute gcd between two integers using Euclid's Algorithm
#
# Function UAB_gcd_with_euclides.
# * Parameter m: Integer to check (>= 0)
# * Parameter n: Integer to check (>= 0)
# * Returns: gcd between the integers m and n.
#

def UAB_gcd_with_euclides(m, n):
    
    result = None
    
    while True:
        result = m % n
        if result == 0:
            return n
        else:
            m = n
            n = result
    #### IMPLEMENTATION GOES HERE ####
    


    ##################################


# In[ ]:


# EXERCISE 2b: Estimate the probability that two random numbers are coprime
#
# Function UAB_exp_coprime_prob.
# * Parameter N: Upper bound on the integers to evaluate size
# * Parameter M: Sample size
# * Returns: float, experimental probability that two random numbers are 
# coprime when performing M experiments with random numbers <= N
#

def UAB_exp_coprime_prob(N, M):

    result = None
    
    #### IMPLEMENTATION GOES HERE ####



    ##################################    
    
    return result;


# In[ ]:


# EXERCISE 2c:

#### IMPLEMENTATION GOES HERE ####



##################################


# In[ ]:


# EXERCISE 3a: Compute Euler's totient function
#
# Function UAB_euler_phi.
# * Parameter n: Integer (>0)
# * Returns: phi(n), the number of number of positive integers less than n that are coprime to n
#

def UAB_euler_phi(n):
    
    e = 0
    i = 2
    suma_1 = 2
    result = suma_1 + float(1/factorial(2))
    
    while fabs(suma_1 - result) >= n:
        suma_1 = reuslt
        result += float(1/factorial(i))
        i += 1
        
    #### IMPLEMENTATION GOES HERE ####
    


    ##################################
    
    return result


# In[ ]:


# EXERCISE 3b: Implement the square-and-multiply algorithm
#
# Function UAB_square_and_multiply.
# * Parameter a: Integer to check (>= 0)
# * Parameter n: Integer to check (>= 0)
# * Parameter p: Integer to check (>= 0)
# * Returns: a^n mod p
#

def UAB_square_and_multiply(a, n, p):
    
    result = None
    
    #### IMPLEMENTATION GOES HERE ####
    
    
    

    ##################################
    
    return result


# In[ ]:


# EXERCISE 3c: Compute 96^-1 mod 191 using the previous function

#### IMPLEMENTATION GOES HERE ####



##################################


# In[7]:


####################################################################################
# TEST CASES EXERCICE 1a:
####################################################################################

def test_case_1a(name, num_tries, interval):
    
    acc_r = True
    ZZ = IntegerRing()
    for _ in range(num_tries):
         e = ZZ.random_element(interval)
         r = UAB_divisible_by_9(e)
         acc_r &= (r == (mod(e, 9) == 0))

    print "Test", name + ":", acc_r            

test_case_1a("1a.1", 200, 10^2)
test_case_1a("1a.2", 200, 10^4)
test_case_1a("1a.3", 200, 10^6)


####################################################################################
# TEST CASES EXERCICE 1b:
####################################################################################

def test_case_1b(name, num_tries, interval):
    
    acc_r = True
    ZZ = IntegerRing()
    for _ in range(num_tries):
         e = ZZ.random_element(interval)
         r = UAB_divisible_by_11(e)
         acc_r &= (r == (mod(e, 11) == 0))

    print "Test", name + ":", acc_r            

test_case_1b("1b.1", 200, 10^2)
test_case_1b("1b.2", 200, 10^4)
test_case_1b("1b.3", 200, 10^6)

####################################################################################
# TEST CASES EXERCICE 2a:
####################################################################################

def test_case_2a(name, num_tries, interval):
    
    acc_r = True
    ZZ = IntegerRing()
    for _ in range(num_tries):
         a = ZZ.random_element(interval)
         b = ZZ.random_element(interval)
         r = UAB_gcd_with_euclides(a, b)
         acc_r &= (r == gcd(a, b))

    print "Test", name + ":", acc_r            

test_case_2a("2a.1", 200, 10^2)
test_case_2a("2a.2", 200, 10^4)
test_case_2a("2a.3", 200, 10^6)

####################################################################################
# TEST CASES EXERCICE 3a:
####################################################################################

def test_case_3a(name, num_tries, interval):
    
    acc_r = True
    ZZ = IntegerRing()
    for _ in range(num_tries):
         a = ZZ.random_element(interval)
         r = UAB_euler_phi(a)
         acc_r &= (r == euler_phi(a))

    print "Test", name + ":", acc_r            

test_case_3a("3a.1", 200, 10^2)
test_case_3a("3a.2", 200, 10^3)
test_case_3a("3a.3", 200, 10^4)

####################################################################################
# TEST CASES EXERCICE 3b:
####################################################################################

def test_case_3b(name, num_tries, interval):
    
    acc_r = True
    ZZ = IntegerRing()
    for _ in range(num_tries):
         a = ZZ.random_element(interval)
         b = ZZ.random_element(interval)
         p = random_prime(interval)
         r = UAB_square_and_multiply(a, b, p)
         acc_r &= (r == power_mod(a, b, p))

    print "Test", name + ":", acc_r            

test_case_3b("3b.1", 200, 10^2)

