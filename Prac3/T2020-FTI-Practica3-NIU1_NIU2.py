
# coding: utf-8

# In[5]:


# IMPORTANT!!!
# [1] Introduïu les dades sobre el vostre grup en el format especificat.
# [2] Desar la pràctica posant els NIUs dels membres del grup
# [3] És imprescindible que el worksheet es pugui avaluar completament (Cell->Run All) sense que es produeixi cap error de sintaxi. 
# [4] Cal lliurar el worksheet ABANS de finalitzar la vostra sessió de pràctiques.
# [5] No s'avaluaran worksheets que no compleixin els requisits anteriors.

GROUP = None

NIU_ESTUDIANT_1 = None
NOM_ESTUDIANT_1 = None

NIU_ESTUDIANT_2 = None
NOM_ESTUDIANT_2 = None


# In[6]:


# EXERCISE 1a: Implement ElGamal key generation algorithm
#
# Function UAB_generate_ElGamal_keys.
# * Parameter nBits: Length in bits of the prime p
# * Returns: two element list with private and public keys. 
#    The private key is a list of three values: the prime p, the generator alpha, and the secret value d. 
#    The public key is a list of three values: the prime p, the generator alpha, and public value c (alpha^d).
# 

def UAB_generate_ElGamal_keys(nBits):
    
    k_priv = (None, None, None)
    k_pub = (None, None, None)
    
    #### IMPLEMENTATION GOES HERE ####
    p = random_prime(2^nBits,False,2^(nBits-1))
    
    valor=0
    valor2=0
    
    while (valor!=1 and valor2!=1):
        d=randint(2,p-2)
        valor=gcd(d,p-1)
        a=randint(2,p-2)
        valor2=gcd(a,p-1)
        
    
    k_priv=(p,a,d)
    k_pub=(p,a,pow(a,d,p))

    
    ##################################
    
    return [k_priv, k_pub]


# In[7]:


# EXERCISE 1b: Implement ElGamal signature generation algorithm
#
# Function UAB_ElGamal_sign.
# * Parameter k_priv: 3-element list with the private key (as returned by UAB_generate_ElGamal_keys).
# * Parameter m: Integer, message to sign
# * Parameter k: Optional Integer, the random k value (if present, the function must use the supplied k value, otherwise, 
#     it must select k randomly.
# * Returns: two element list with the signature ([r, s]) 
# 

def UAB_ElGamal_sign(k_priv, m, k=None):

    r, s = None, None
    p=k_priv[0]
    a=k_priv[1]
    d = k_priv[2]
    
    #### IMPLEMENTATION GOES HERE ####
    #Para sacar r    
    
 
    if k == None:
        valor=0
        while not (valor==1):
            k=randint(2,p-1)
            valor=gcd(k,p-1)
           
    
        
    r = int(pow(a,k,p))
    
    #Para sacar l
        
    l = inverse_mod(k,p-1)
    s = int(mod(l*(m-d*r),p-1))
    

    
    ##################################
    
    return (r, s)


# In[8]:


# EXERCISE 1c (part 1): Show that v1 == v2
#
#
"""
#### EXPLANATION GOES HERE #######
Obtenint els valors de les funcions realitzades amb anterioritat, podem comprovar utilitzant 
les equacions v1 = (c**r)*(r**s) mod (p) i v2 = alfa**m mod(p) que, si compleix la igualtat la 
asignatura es valida i en cas contrari no. Es rebutja de la mateixa manera en cas de que r no
compleix que 1<=r>=p-1.
##################################
"""

m=40
    
[k_priv, k_pub]=UAB_generate_ElGamal_keys(3)
[r,s]=UAB_ElGamal_sign(k_priv, m, k=None)
p=k_priv[0]
a=k_priv[1]
c = k_pub[2]
valor = 0

if r >= 1 and r <= p-1:
    valor = 1
    
  
v1 = mod(pow(c,r)*pow(r,s),p)
v2 = mod(pow(a, m),p)

if (v1 == v2):
    print "les v son iguals"


# In[17]:


# EXERCISE 1c (part 2): Implement ElGamal signature verification algorithm
#
# Function UAB_ElGamal_verify.
# * Parameter sig: signature to verify (as returned by UAB_ElGamal_sign)
# * Parameter k_pub: 3-element list with the public key (as returned by UAB_generate_ElGamal_keys).
# * Parameter m: Integer, message that was signed
# * Returns: boolean, True iff signature is valid
# 

def UAB_ElGamal_verify(sig, k_pub, m):

    result = None

    #### IMPLEMENTATION GOES HERE ####
    [r,s] = sig
    [p,a,c]=k_pub
    
    if r >= 1 and r <= p-1:

        v11 = pow(c,r,p)
        v12 = pow(r,s,p)    
        v1 = mod(v11*v12,p)
        v2 = pow(a,m,p)
    
        if(v1==v2):
            result=True
        else:
            result = False

    
    ##################################
    
    return result


# In[10]:


# EXERCISE 2a: Describe the procedure followed by the attacker
#
#
"""
#### EXPLANATION GOES HERE #######

Tenim dos casos possibles:
    
1) Per tal de aconseguir k, l'hem aïllat fent que --> s1*k−m1 ≡ s2*k−m2  (mod p)
                                                      (s1−s2)*k ≡ m1−m2  (mod p)
A partir d'aquesta expressió, podem treure k pero només en el cas de que existeixi una inversa de (s1-s2). 
Si existeix: k≡(m1−m2)(s1−s2)−1modp−1

En el cas de que poguem obtenir k, per aconseguir d necesitarem saber si la r te inversa, en cas que ho tingui, 
podrem calcular-la: d≡(m1−k*s1)*(r−1)  (modp−1)
    
2) En el cas que s1-s2 o r no tinguin inversa, tindrem que afrontar el problema d'una altre manera:

Utilitzant expresions on encara no ens faci falta l'us de la inversa i calculant les incognites 
amb solve_mod (Aquestes seran diferents elements per k i diferents per d)

k = solve_mod(x*(s_M1-s_M2) == (m1-m2),p-1)

Llavors per saber quina k es la correcta, ho comprovarem amb --> r == alfa**k

Un cop tenim la k, ara calcularem els possibles elements de d:
    
d=solve_mod([x*r==m1-(k*s_M1)],p-1)

I anirem mirant els diferents valors de d, per veure quin compleix aixó --> c=alfa**d
##################################
"""


# In[11]:


# EXERCISE 2b: Implement the algorithm used by the attacker to recover the private key
#
# Function UAB_extract_private_key.
# * Parameter k_pub: 3-element list with the public key (as returned by UAB_generate_ElGamal_keys).
# * Parameter m1: Integer, a message that was signed
# * Parameter sig1: signature of message m1 (as returned by UAB_ElGamal_sign)
# * Parameter m2: Integer, a message that was signed
# * Parameter sig2: signature of message m2 (as returned by UAB_ElGamal_sign)
# * Returns: a 3-element list with the private key if it was possible to recover it, -1 otherwise
# 

def UAB_extract_private_key(k_pub, m1, sig1, m2, sig2):
    
    k_priv = None
    
    #### IMPLEMENTATION GOES HERE ####
    [p,a,c]=k_pub
    [r1,s_M1]=sig1
    [r2,s_M2]=sig2
    noBuena=0

### Tenim que k i alfa és igual, per això podem dir que r1 i r2 tindran el mateix valor
    so=s_M1-s_M2
    valor=gcd(so,p-1)
    r=r1
    valor2=gcd(r,p-1)
    
    if(r1==r2) and (valor == 1) and (r == 1) :
        k=mod(((m1-m2)/so),p-1)
        
        d=mod((m1-(k*s_M1))/r,p-1)
    
        k_priv=[p,a,d]
        
    else:
        
        k = solve_mod(x*(s_M1-s_M2) == (m1-m2),p-1)
        
        for v in k:
            if(r==pow(a,v)):
                k=v
        
        value2=solve_mod([y*r==m1-(k*s_M1)],p-1)
        
        for i in value2:
            if(c==pow(a,i)):
                d=i
                
        k_priv=[p,a,d]

    
    ##################################
    
    return k_priv


# In[12]:


####################################################################################
# TEST CASES EXERCICE 1a:
####################################################################################

def test_case_1a(name, num_tries, num_bits):
    
    [k_priv, k_pub] = UAB_generate_ElGamal_keys(num_bits)
    
    t1 = len(k_priv) == 3
    t2 = len(k_pub) == 3
    
    t3, t4, t5 = False, False, False
    if t1 & t2:
        t3 = k_pub[0] == k_priv[0]
        t4 = k_pub[1] == k_priv[1]
        t5 = k_pub[2] == power_mod(k_pub[1], k_priv[2], k_pub[0])
        
    print "Test", name + ":", t1 & t2 & t3 & t4 & t5            

test_case_1a("1a.1", 20, 64)
test_case_1a("1a.2", 20, 128)
test_case_1a("1a.3", 1, 256)


# In[13]:


####################################################################################
# TEST CASES EXERCICE 1b:
####################################################################################

def test_case_1b(name, k_priv, h, m, exp_r, exp_s):

    (r, s) = UAB_ElGamal_sign(k_priv, m, h) 
    print "Test", name + ":", (r == exp_r) & (s == exp_s)

k_priv =  (141627058957340093855620484680587497231, 49407674567884478422262585667470127500, 91557801542207645804476483173676169513L)
k_pub =  (141627058957340093855620484680587497231, 49407674567884478422262585667470127500, 136166465183429483437614516541235447540)
h =  6505205550934361491179720631243
exp_r =  16070586247864526048715174304611921161
exp_s =  79906657969558945308772045181673566953
test_case_1b("1b.1", k_priv, h, 42, exp_r, exp_s)

k_priv =  (12992917616897605511470512010377760999, 6497100366721531782651229087612454514, 8184645315919973579263902520077142907L)
k_pub =  (12992917616897605511470512010377760999, 6497100366721531782651229087612454514, 4784536271623967017080018506651914749)
h =  30541127218530291833593754023
exp_r =  370282987414176508036351785758150113
exp_s =  57221387644974029881195998309189883
test_case_1b("1b.2", k_priv, h, 42424242, exp_r, exp_s)

k_priv =  (111095862244100561185773259658903092441, 68715015864842833415840443685753818922, 10688562822627073336062911686899436628L)
k_pub =  (111095862244100561185773259658903092441, 68715015864842833415840443685753818922, 37400235185594015815971136915025528910)
h =  6235123811656012209298405325689
exp_r =  16165481899748746481848784352851142527
exp_s =  98809740663833529553705269007330012337
test_case_1b("1b.3", k_priv, h, 123456789, exp_r, exp_s)

k_priv =  (112847941112170644296267772277509350846555975113583168624796765318122631009049, 8727126823951345831686546296722679628937575768766379507115329576365730863802, 90254950644239289915262816357689053461511329394130471493737946140216700916566L)
k_pub =  (112847941112170644296267772277509350846555975113583168624796765318122631009049, 8727126823951345831686546296722679628937575768766379507115329576365730863802, 2099965966935399988641793851392022051292773481845879860193310339903489213462)
h =  2294742374266784531203391331539988254350495938206389588496594528290435
exp_r =  5243953816691648242050551475605541294498933363835245262768302013908462924792
exp_s =  72567626378663072501746825375182155635676274934487883661122801069515340587487
test_case_1b("1b.4", k_priv, h, 123456789123456789123456789, exp_r, exp_s)


# In[18]:


####################################################################################
# TEST CASES EXERCICE 1c:
####################################################################################

def test_case_1c(name, sig, k_pub, m, exp_result):

    result = UAB_ElGamal_verify(sig, k_pub, m)
    print "Test", name + ":", (result == exp_result)
    
k_pub =  (141627058957340093855620484680587497231, 49407674567884478422262585667470127500, 136166465183429483437614516541235447540)
r =  16070586247864526048715174304611921161
s =  79906657969558945308772045181673566953
test_case_1c("1c.1", (r, s), k_pub, 42, True)

k_pub =  (12992917616897605511470512010377760999, 6497100366721531782651229087612454514, 4784536271623967017080018506651914749)
r =  370282987414176508036351785758150113
s =  57221387644974029881195998309189883
test_case_1c("1c.2", (r, s), k_pub, 42424242, True)

k_pub =  (111095862244100561185773259658903092441, 68715015864842833415840443685753818922, 37400235185594015815971136915025528910)
r =  16165481899748746481848784352851142527
s =  98809740663833529553705269007330012337
test_case_1c("1c.3", (r, s), k_pub, 123456789, True)

k_pub =  (112847941112170644296267772277509350846555975113583168624796765318122631009049, 8727126823951345831686546296722679628937575768766379507115329576365730863802, 2099965966935399988641793851392022051292773481845879860193310339903489213462)
r =  5243953816691648242050551475605541294498933363835245262768302013908462924792
s =  72567626378663072501746825375182155635676274934487883661122801069515340587487
test_case_1c("1c.4", (r, s), k_pub, 123456789123456789123456789, True)

k_pub =  (141627058957340093855620484680587497231, 49407674567884478422262585667470127500, 136166465183429483437614516541235447540)
r =  16070586247864526048715174304611921161
s =  79906657969558945308772045181673566954
test_case_1c("1c.5", (r, s), k_pub, 42, False)

k_pub =  (12992917616897605511470512010377760999, 6497100366721531782651229087612454514, 4784536271623967017080018506651914749)
r =  370282987414176508036351785758150115
s =  57221387644974029881195998309189883
test_case_1c("1c.6", (r, s), k_pub, 42424242, False)

k_pub =  (111095862244100561185773259658903092443, 68715015864842833415840443685753818922, 37400235185594015815971136915025528910)
r =  16165481899748746481848784352851142527
s =  98809740663833529553705269007330012337
test_case_1c("1c.7", (r, s), k_pub, 123456789, False)

k_pub =  (112847941112170644296267772277509350846555975113583168624796765318122631009049, 8727126823951345831686546296722679628937575768766379507115329576365730863803, 2099965966935399988641793851392022051292773481845879860193310339903489213462)
r =  5243953816691648242050551475605541294498933363835245262768302013908462924792
s =  72567626378663072501746825375182155635676274934487883661122801069515340587487
test_case_1c("1c.8", (r, s), k_pub, 123456789123456789123456789, False)


# In[15]:


####################################################################################
# TEST CASES EXERCICE 1(all):
####################################################################################

def test_case_1d(name, num_its, num_bits):

    acc_r = []
    for _ in range(num_its):
        m = randint(2, 2^(num_bits-1)-1)
        
        [k_priv, k_pub] = UAB_generate_ElGamal_keys(num_bits)
        result = UAB_ElGamal_verify(UAB_ElGamal_sign(k_priv, m), k_pub, m)
        acc_r.append(result)
    
    print "Test", name + ":", all(acc_r)

def test_case_1e(name, num_its, num_bits):

    acc_r = []
    for _ in range(num_its):
        m = randint(2, 2^(num_bits-1)-1)
        
        [k_priv, k_pub] = UAB_generate_ElGamal_keys(num_bits)
        result = UAB_ElGamal_verify(UAB_ElGamal_sign(k_priv, m), k_pub, m-1)
        acc_r.append(result)
    
    print "Test", name + ":", not any(acc_r)
        
        
test_case_1d("1d.1", 100, 64)    
test_case_1d("1d.2", 10, 128)  

test_case_1e("1e.1", 10, 64)    
test_case_1e("1e.2", 10, 128)


# In[16]:


####################################################################################
# TEST CASES EXERCICE 2:
####################################################################################

def test_case_2(name, k_pub, m1, sig1, m2, sig2, exp_k_priv):
    
    extracted_k_priv = UAB_extract_private_key(k_pub, m1, sig1, m2, sig2)
    print "Test", name + ":",  exp_k_priv == extracted_k_priv
    
exp_k_priv =  (1736419493, 423105914, 1439798331)
k_pub =  (1736419493, 423105914, 1388681513)
m1, m2 = 4321, 1234
sig1 =  (1670801833L, 813531998L)
sig2 =  (1670801833L, 1514976703L)
test_case_2("2.1", k_pub, m1, sig1, m2, sig2, exp_k_priv)
       	
exp_k_priv =  (3043480277, 949971850, 2984002184L)
k_pub =  (3043480277, 949971850, 450506446)
m1, m2 = 4321, 1234
sig1 =  (652612267, 1904199797)
sig2 =  (652612267, 716941154)
test_case_2("2.2", k_pub, m1, sig1, m2, sig2, exp_k_priv)

exp_k_priv =  (3081644339, 432364326, 231991852)
k_pub =  (3081644339, 432364326, 1072654913)
m1, m2 = 4321, 1234
sig1 =  (2294114827L, 97380409)
sig2 =  (2294114827L, 744220606)
test_case_2("2.3", k_pub, m1, sig1, m2, sig2, exp_k_priv)

exp_k_priv =  (39929, 23050, 17872)
k_pub =  (39929, 23050, 3414)
m1, m2 = 4321, 1234
sig1 =  (39612, 35145)
sig2 =  (39612, 38386)
test_case_2("2.4", k_pub, m1, sig1, m2, sig2, exp_k_priv)

exp_k_priv =  (38783, 10357, 9046)
k_pub =  (38783, 10357, 14443)
m1, m2 = 4321, 1234
sig1 =  (12778, 29913)
sig2 =  (12778, 20620)
test_case_2("2.5", k_pub, m1, sig1, m2, sig2, exp_k_priv)
       	
exp_k_priv =  (6203, 3754, 5115)
k_pub =  (6203, 3754, 540)
m1, m2 = 4321, 1234
sig1 =  (3747, 3790)
sig2 =  (3747, 5435)
test_case_2("2.6", k_pub, m1, sig1, m2, sig2, exp_k_priv)

exp_k_priv =  -1
k_pub =  (1400337509, 1359471971, 45907697)
m1, m2 = 4321, 4321
sig1 =  (639541257L, 1115934695L)
sig2 =  (639541257L, 1115934695L)
test_case_2("2.7", k_pub, m1, sig1, m2, sig2, exp_k_priv)

exp_k_priv =  -1
k_pub =  (2056635443, 830686420, 1880350451)
m1, m2 = 4321, 1234
sig1 =  (1601254651L, 1061368902L)
sig2 =  (1601254651L, 935119992L)
test_case_2("2.8", k_pub, m1, sig1, m2, sig2, exp_k_priv)

exp_k_priv = -1
m1, m2 = 4321, 1234
k_pub =  (460730117, 91503345, 401055661)
sig1 =  (457648992L, 18325781L)
sig2 =  (457648992L, 180721743L)
test_case_2("2.9", k_pub, m1, sig1, m2, sig2, exp_k_priv)


exp_k_priv =  -1
m1, m2 = 4321, 1234
k_pub =  (3342796253, 1046051573, 77303856)
sig1 =  (1629150615, 2477614166L)
sig2 =  (1462514112, 61485630)
test_case_2("2.10", k_pub, m1, sig1, m2, sig2, exp_k_priv)

