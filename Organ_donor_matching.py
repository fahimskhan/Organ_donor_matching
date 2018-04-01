import random
pop_size=1000
pop=random.sample(xrange(0,1000),1000) #generates a population of 1000 with frequency number fpr bloodtype
pop2=[]
needs_organ=[]
pair_compatible=[]
pair_not_compatible=[]
cross_pair_matched=[]
donor_pool_matched=[]

i=0
for i in range(0,1000): #assigns bloodtype to population
    if pop[i] < 10:
        pop2.append('AB-')
        i+=1
    elif pop[i] < 40:
        pop2.append('AB+')
        i+=1
    elif pop[i] < 100:
        pop2.append('A-')
        i+=1
    elif pop[i] < 440:
        pop2.append('A+')
        i+=1
    elif pop[i] < 460:
        pop2.append('B-')
        i+=1
    elif pop[i] < 550:
        pop2.append('B+')
        i+=1
    elif pop[i] < 620:
        pop2.append('O-')
        i+=1
    elif pop[i] < 1000:
        pop2.append('O+')
        i+=1

def split(A, n):   #creates arrays of n-dimension
    return [A[i:i+n] for i in range(0, len(A), n)]

B=split(pop2,2)

i=0
while i<50:   #population that need organs
    needs_organ.append(random.choice(B))
    i+=1

print needs_organ, 'needs organ'

recbt={'AB-':['O-','AB-','B-','A-'],
       'AB+':['AB+','O-','A-','B-','O+','AB-','A+','B+'],
       'A-':['A-','O-'],
       'A+':['O-','A-','O+','A+'],
       'B-':['B-','O-'],
       'B+':['B-','B+','O+','O-'],
       'O-':['O-'],
       'O+':['O+','O-']}


def pair_compatibility_match(array):
    donor=array[i][0]
    rec=array[i][1]
    list_recbt=recbt[rec]
    if donor in list_recbt:
        pair_compatible.append(array[i])
    else:
        pair_not_compatible.append(array[i])

i=0
while i<50:
    pair_compatibility_match(needs_organ)
    i+=1

print pair_compatible, 'compatible'

print pair_not_compatible, 'not compatible'


def pair_wise_match(array):   #pair wise comparison
    donor1=array[j][0]
    rec1=array[j][1]
    donor2=array[i+1][0]
    rec2=array[i+1][1]
    list_recbt=recbt[rec1]
    if donor2 in list_recbt:
        list_recbt=recbt[rec2]
        if donor1 in list_recbt:
            cross_pair_matched.extend((array[j],array[i+1]))
            del array[j]
            del array[i]
i=0
j=0
while i<(len(pair_not_compatible)-1) and j<len(pair_not_compatible):
    pair_wise_match(pair_not_compatible)
    i+=1
    if i == (len(pair_not_compatible)-1):
        j+=1
        i=j

cross_pair_matched= split(cross_pair_matched,4)

print cross_pair_matched, 'cross pair matched'

import random
pop3=random.sample(xrange(0,100),10)

donor_pool=[]
i=0
for i in range(0,10):
    if pop3[i] < 1:
        donor_pool.append('AB-')
        i+=1
    elif pop3[i] < 4:
        donor_pool.append('AB+')
        i+=1
    elif pop3[i] < 10:
        donor_pool.append('A-')
        i+=1
    elif pop3[i] < 44:
        donor_pool.append('A+')
        i+=1
    elif pop3[i] < 46:
        donor_pool.append('B-')
        i+=1
    elif pop3[i] < 55:
        donor_pool.append('B+')
        i+=1
    elif pop3[i] < 62:
        donor_pool.append('O-')
        i+=1
    elif pop3[i] < 100:
        donor_pool.append('O+')
        i+=1

print donor_pool, 'Donor pool'

def donor_pool_match(array1, array2):
    donor=array2[j]
    rec=array1[i][1]
    list_recbt=recbt[rec]
    if donor in list_recbt:
        donor_pool_matched.append(array1[i])
        del array2[j]
        del array1[i]

i=0
j=0
while i<(len(pair_not_compatible)) and j<len(donor_pool):
    donor_pool_match(pair_not_compatible, donor_pool)
    j+=1
    if j == (len(donor_pool)):
        i+=1

print (donor_pool_matched, 'donor pool matched')

print (pair_not_compatible,'did not receive organ')

print ('# people who needed organs', len(needs_organ))

print ('# of spouse matches', len(pair_compatible))

print ('# of cross matches', sum(len(x) for x in cross_pair_matched))

print ('# of donors matches', len(donor_pool_matched))

print ('# of people who received no organ', len(pair_not_compatible))








