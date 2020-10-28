
# coding: utf-8

# In[1]:


# IMPORTANT!!!
# [1] Introduïu les dades sobre el vostre grup en el format especificat.
# [2] Desar la pràctica posant els NIUs dels membres del grup
# [3] És imprescindible que el worksheet es pugui avaluar completament (Cell->Run All) sense que es produeixi cap error de sintaxi. 
# [4] Cal lliurar el worksheet ABANS de finalitzar la vostra sessió de pràctiques.
# [5] No s'avaluaran worksheets que no compleixin els requisits anteriors.

# El format del grup hauria de ser una lletra en majúscules seguida d'un número, per exemple, "E5"
GROUP = "" 

NIU_ESTUDIANT_1 = None
NOM_ESTUDIANT_1 = ""

NIU_ESTUDIANT_2 = None
NOM_ESTUDIANT_2 = ""


# In[1]:


# EXERCISE 1: Introduction to codes in sage

# Necessitem definir un cos base: 
F2 = GF(2)
print "F2:"
print F2

# Es pot definir una paraula-codi com un vector: 
v = vector(GF(2),[1, 0, 1, 1])
print "v:"
print v

# I convertir un vector a una llista: 
print "v.list():"
print v.list()

# Podem definir una matriu,
G = matrix(F2, [(0,1,0,1,0),(0,1,1,1,0),(0,0,1,0,1),(0,1,0,0,1)])
print "G:"
print G

# I el codi lineal amb aquesta matriu generadora: 
C = LinearCode(G)
print "C:"
print C

# Construcció de l’anell de polinomis sobre GF(2): 
Z2X.<x> = PolynomialRing(F2)
print "Z2X:"
print Z2X

# Definir un polinomi amb coeficients a GF(2): 
pX = Z2X(1+x^2+x^4+x^5)
print "pX:"
print pX

# Alternativament:
pX = Z2X([1,0,1,1])
print "pX:"
print pX

# Desplaçament dels coeficients d’un polinomi (multiplicar per x^2): 
print "pX.shift(2):"
print pX.shift(2)

# També en l’altre sentit (dividir per x), 
print "pX.shift(-1):"
print pX.shift(-1)

# Operar amb polinomis: 
qX = pX*(x+1)
print "qX:"
print qX

# Comprovar si un polinomi és irreductible: 
print pX.is_irreducible()
print "qX.is_irreducible():"
print qX.is_irreducible()

# I si no ho és, descomposar-lo en factors: 
print "qX.factor():"
print qX.factor()

# Construir un codi cíclic de longitud 3 i polinomi generador x+1: 
C = codes.CyclicCode(x+1, 3)
print "C:"
print C

# Conjunt amb les paraules d'un codi cíclic
S = set(C.list())
print "S:"
print S


# In[14]:


# EXERCISE 2a: Implement a right cyclic shift

# Function UAB_right_shift.
# * Parameter n: Integer, number of places to shift (>= 0)
# * Parameter L: List, list with values to shift
# * Returns: shifted list
#
def UAB_right_shift(n, L):
    
    result = None
    
    #### IMPLEMENTATION GOES HERE ####
    if n>=0:
        if n==0:
            result = L
            return result
        else:
            L[:] = L[-1:] + L[:-1]
            UAB_right_shift(n-1, L)
        
    result = L
    ##################################
    
    return result


# In[3]:


# EXERCISE 2b: Generate the two codes and check they are equivalent. Show length, dimension and minimum distance of the generated code

#### IMPLEMENTATION GOES HERE ####



##################################


# In[4]:


# EXERCISE 3: Check code existence

#### IMPLEMENTATION GOES HERE ####



################################


# In[5]:


# EXERCISE 4: How many cíclic binary codes with length 15 exist?

#### IMPLEMENTATION GOES HERE ####


################################


# In[6]:


# EXERCISE 5: Which is the smallest ciclic code of length 15 that contains the given code-word?

#### IMPLEMENTATION GOES HERE ####


################################


# In[7]:


# EXERCISE 6: Compute h(x), h*(x)

#### IMPLEMENTATION GOES HERE ####


################################


# In[8]:


# EXERCISE 7a: Compute the generator matrix

# Function UAB_gen_matrix.
# * Parameter g: generator polynomial
# * Parameter n: Integer, length of the code
# * Returns: generator matrix
#

def UAB_gen_matrix(g, n):
    
    G = None
    
    #### IMPLEMENTATION GOES HERE ####

    
    ##################################
    
    return G


# In[9]:


# EXERCISE 7b: Compute the generator matrix of the given polynomials

#### IMPLEMENTATION GOES HERE ####


##################################


# In[10]:


# EXERCISE 8a: Compute the control matrix

# Function UAB_con_matrix.
# * Parameter g: generator polynomial
# * Parameter n: Integer, length of the code
# * Returns: control matrix
#

def UAB_con_matrix(g, n):
    
    H = None
    
    #### IMPLEMENTATION GOES HERE ####
    

    
    ##################################
    
    return H


# In[11]:


# EXERCISE 8b: Compute the control matrix of the given polynomials

#### IMPLEMENTATION GOES HERE ####


##################################


# In[15]:


####################################################################################
# TEST CASES EXERCICE 2a
####################################################################################

def test_case_2a(name, n, L, exp_output):    
    r = UAB_right_shift(n, L)
    print "Test", name + ":", exp_output == r


test_case_2a("2a.1", 1, [1,1,1,1,1,1,0], [0,1,1,1,1,1,1]) 
test_case_2a("2a.2", 2, [1,1,1,1,1,1,0], [1,0,1,1,1,1,1]) 
test_case_2a("2a.3", 3, [1,1,1,1,1,1,0], [1,1,0,1,1,1,1]) 
test_case_2a("2a.4", 4, [1,1,1,1,1,1,0], [1,1,1,0,1,1,1]) 
test_case_2a("2a.5", 5, [1,1,1,1,1,1,0], [1,1,1,1,0,1,1]) 
test_case_2a("2a.6", 6, [1,1,1,1,1,1,0], [1,1,1,1,1,0,1]) 
test_case_2a("2a.7", 7, [1,1,1,1,1,1,0], [1,1,1,1,1,1,0]) 
test_case_2a("2a.8", 5, [1,0,1,0,0,1,0,0,0], [0, 1, 0, 0, 0, 1, 0, 1, 0]) 
test_case_2a("2a.9", 3, [1,0,1,0,0,1,0,0,0], [0, 0, 0, 1, 0, 1, 0, 0, 1]) 
test_case_2a("2a.10", 0, [1,0,1,0,0,1,0,0,0], [1, 0, 1, 0, 0, 1, 0, 0, 0]) 
test_case_2a("2a.11", 9, [1,0,1,0,0,1,0,0,0], [1, 0, 1, 0, 0, 1, 0, 0, 0]) 
test_case_2a("2a.12", 10, [1,0,1,0,0,1,0,0,0,1,1,1,1,1,0,0,0,1], [0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0])


# In[13]:


####################################################################################
# TEST CASES EXERCICE 7a
####################################################################################

def test_case_7a(name, g, n, exp_output):    
    r = UAB_gen_matrix(g, n)
    print "Test", name + ":", exp_output == r

exp = matrix(GF(2), [[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]])
test_case_7a("7a.1", Z2X(x+1), 15, exp) 

exp = matrix(GF(2), [[1,1,0,0,1,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,1,0,0,1,0,0,0,0,0,0,0],[0,0,0,0,1,1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,1,1,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,1,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,1,0,0,0],[0,0,0,0,0,0,0,0,1,1,0,0,1,0,0],[0,0,0,0,0,0,0,0,0,1,1,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,1,1,0,0,1]])
test_case_7a("7a.2", Z2X(x^4 + x + 1), 15, exp)

exp = matrix(GF(2), [[1,0,0,1,1,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,1,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,1,0,0,0,0,0,0,0],[0,0,0,0,1,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,1,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,1,1,0,0,0,0],[0,0,0,0,0,0,0,1,0,0,1,1,0,0,0],[0,0,0,0,0,0,0,0,1,0,0,1,1,0,0],[0,0,0,0,0,0,0,0,0,1,0,0,1,1,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,1,1]])
test_case_7a("7a.3", Z2X(x^4 + x^3 + 1), 15, exp) 

exp = matrix(GF(2), [[1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,1,1,1]])
test_case_7a("7a.4", Z2X(x^6 + x^5 + x^4 + x^2 + 1), 21, exp)


# In[ ]:


####################################################################################
# TEST CASES EXERCICE 8a
####################################################################################

def test_case_8a(name, g, n, exp_output):    
    r = UAB_con_matrix(g, n)
    print "Test", name + ":", exp_output == r

exp = matrix(GF(2), [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
test_case_8a("8a.1", Z2X(x+1), 15, exp) 

exp = matrix(GF(2), [[1,0,0,1,1,0,1,0,1,1,1,1,0,0,0],[0,1,0,0,1,1,0,1,0,1,1,1,1,0,0],[0,0,1,0,0,1,1,0,1,0,1,1,1,1,0],[0,0,0,1,0,0,1,1,0,1,0,1,1,1,1]])
test_case_8a("8a.2", Z2X(x^4 + x + 1), 15, exp)

exp = matrix(GF(2), [[1,1,1,1,0,1,0,1,1,0,0,1,0,0,0],[0,1,1,1,1,0,1,0,1,1,0,0,1,0,0],[0,0,1,1,1,1,0,1,0,1,1,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,1]])
test_case_8a("8a.3", Z2X(x^4 + x^3 + 1), 15, exp) 

exp = matrix(GF(2), [[1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0,0],[0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0,0],[0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0,0],[0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0,0],[0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1,0],[0,0,0,0,0,1,1,0,1,0,0,1,1,0,0,1,0,0,1,0,1]])
test_case_8a("8a.4", Z2X(x^6 + x^5 + x^4 + x^2 + 1), 21, exp)

