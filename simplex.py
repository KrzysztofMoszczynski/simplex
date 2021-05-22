import numpy as np 

## wygeneruj tablicę , która spełnia warunki
def gen_matrix(var,cons):    
    tab = np.zeros((cons+1, var+cons+2))    
    return tab

## Next, we’ll check to see if 1+ pivots are required due to a negative 
# element in the furthest right column, excluding the bottom value, of course.
def next_round_r(table):    
    m = min(table[:-1,-1])    
    if m>= 0:        
        return False    
    else:        
        return True

#Similarly, we’ll check to see if 1+ pivots are required due to a negative 
# element in the bottom row, excluding the final value.
#
def next_round(table):    
    lr = len(table[:,0])   
    m = min(table[lr-1,:-1])    
    if m>=0:
        return False
    else:
        return True

#And now that we’ve created functions that return booleans, whether or not additional pivots are required, 
# we need to determine 
# where these elements are located. We’ll start with finding negative elements in the furthest right column.

def find_neg_r(table):
    lc = len(table[0,:])
    m = min(table[:-1,lc-1])
    if m<=0:        
        n = np.where(table[:-1,lc-1] == m)[0][0]
    else:
        n = None
    return n

#Similarly, we need to locate negative elements in the bottom row

def find_neg(table):
    lr = len(table[:,0])
    m = min(table[lr-1,:-1])
    if m<=0:
        n = np.where(table[lr-1,:-1] == m)[0][0]
    else:
        n = None
    return n

#Quick recap, we’ve identified the column and row indexes, respectively, 
#for negative elements in the last column, last row. But we need to take 
#it one step further and find the pivot element corresponding to these values.

def loc_piv_r(table):
    total = []        
    r = find_neg_r(table)
    row = table[r,:-1]
    m = min(row)
    c = np.where(row == m)[0][0]
    col = table[:-1,c]
    for i, b in zip(col,table[:-1,-1]):
        if i**2>0 and b/i>0:
            total.append(b/i)
        else:                
            total.append(10000)
    index = total.index(min(total))
    return [index,c]

def loc_piv(table):
    total = []
    n = find_neg(table)
    for i,b in zip(table[:-1,n],table[:-1,-1]):
        if b/i >0 and i**2>0:
            total.append(b/i)
        else:
            total.append(10000)
    index = total.index(min(total))
    return [index,n]
    
def pivot(row,col,table):
    lr = len(table[:,0])
    lc = len(table[0,:])
    t = np.zeros((lr,lc))
    pr = table[row,:]
    if table[row,col]**2>0:
        e = 1/table[row,col]
        r = pr*e
        for i in range(len(table[:,col])):
            k = table[i,:]
            c = table[i,col]
            if list(k) == list(pr):
                continue
            else:
                t[i,:] = list(k-r*c)
        t[row,:] = list(r)
        print(t)
        return t
    else:
        print('Cannot pivot on this element.')
    
def convert(eq):
    eq = eq.split(',')
    if 'G' in eq:
        g = eq.index('G')
        del eq[g]
        eq = [float(i)*-1 for i in eq]
        return eq
    if 'L' in eq:
        l = eq.index('L')
        del eq[l]
        eq = [float(i) for i in eq]
        return eq

def convert_min(table):
    table[-1,:-2] = [-1*i for i in table[-1,:-2]]
    table[-1,-1] = -1*table[-1,-1]
    print(table)
    return table

def gen_var(table):
    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    v = []
    for i in range(var):
        v.append('x'+str(i+1))
    return v

def add_cons(table):
    lr = len(table[:,0])
    empty = []
    for i in range(lr):
        total = 0
        for j in table[i,:]:                       
            total += j**2
        if total == 0: 
            empty.append(total)
    if len(empty)>1:
        return True
    else:
        return False

def constrain(table,eq):
    if add_cons(table) == True:
        lc = len(table[0,:])
        lr = len(table[:,0])
        var = lc - lr -1      
        j = 0
        while j < lr:            
            row_check = table[j,:]
            total = 0
            for i in row_check:
                total += float(i**2)
            if total == 0:                
                row = row_check
                break
            j +=1
        eq = convert(eq)
        i = 0
        while i<len(eq)-1:
            row[i] = eq[i]
            i +=1        
        row[-1] = eq[-1]
        row[var+j] = 1
    else:
        print('Cannot add another constraint.')

def add_obj(table):
    lr = len(table[:,0])
    empty = []
    for i in range(lr):
        total = 0        
        for j in table[i,:]:
            total += j**2
        if total == 0:
            empty.append(total)    
    if len(empty)==1:
        return True
    else:
        return False

def obj(table,eq):
    if add_obj(table)==True:
        eq = [float(i) for i in eq.split(',')]
        lr = len(table[:,0])
        row = table[lr-1,:]
        i = 0        
        while i<len(eq)-1:
            row[i] = eq[i]*-1
            i +=1
        row[-2] = 1
        row[-1] = eq[-1]
        print(table)
    else:
        print('You must finish adding constraints before the objective function can be added.')


def maxz(table):
    while next_round_r(table)==True:
        piv_val_r = loc_piv_r(table)
        table = pivot(piv_val_r[0],piv_val_r[1],table)
    while next_round(table)==True:
        piv_val = loc_piv(table)
        table = pivot(piv_val[0],piv_val[1],table)
    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]            
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0
    val['max'] = table[-1,-1]
    return val


def minz(table):
    table = convert_min(table)
    while next_round_r(table)==True:
        table = pivot(loc_piv_r(table)[0],loc_piv_r(table)[1],table)    
    while next_round(table)==True:
        table = pivot(loc_piv(table)[0],loc_piv(table)[1],table)       
    lc = len(table[0,:])
    lr = len(table[:,0])
    var = lc - lr -1
    i = 0
    val = {}
    for i in range(var):
        col = table[:,i]
        s = sum(col)
        m = max(col)
        if float(s) == float(m):
            loc = np.where(col == m)[0][0]             
            val[gen_var(table)[i]] = table[loc,-1]
        else:
            val[gen_var(table)[i]] = 0 
    val['min'] = table[-1,-1]*-1
    return val


########RUN THIS FUNCTION ###########







