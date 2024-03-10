# -*- coding: utf-8 -*-
"""
Dataframe workshop
task 1 : to use dataframe you need to import pandas and it is recommened to use the standard alias as pd
"""
##solution
#%%
import pandas as pd
import numpy as np

df=pd.read_csv("AN6100-Data-3.csv")
print(df)

'''
task 1 : create a dataframe df1 from single list salesList [1254,2654,2514,1425] to represent sales of first quarter in
         current year
expected output :
      0
0  1254
1  2654
2  2514
3  1425
'''

##solution
#%%

import pandas as pd
import numpy as np
df=pd.DataFrame([1254,2654,2514,1425])
print(df)


'''
task 2: the dataframe is using a auto-assigned number as index
        print the sales index by 2 using iloc
sample output :
data row with index 2 is 0    2514
Name: 2, dtype: int64
data with index 2 is 2514
'''

##solution
#%%
import pandas as pd
import numpy as np
df=pd.DataFrame([1254,2654,2514,1425])
sales=df.iloc[2,0]
##sales=df.loc[2,0]
print(f"data with index 2 is {sales}")


'''
task 3: insert a index column for df1
sample output:
        0
Jan  1254
Feb  2654
Mar  2514
Apr  1425    
'''

##solution
#%%

import pandas as pd
import numpy as np
df=pd.DataFrame([1254,2654,2514,1425],index= ['Jan', 'Feb', 'Mar','Apr'])
print(df)

'''
task 4: now get the sales from 'Feb' using loc
sales for Feb is 2654
'''

##solution
#%%
#0 is not treating as integer, it's the name of the column(str)

sales_for_feb=df.loc['Feb',0]
print(f"sales for Feb is {sales_for_feb}")




'''
task 5 : we can change the column name to "sales"
sample output :
     sales
Jan   1254
Feb   2654
Mar   2514
Apr   1425
'''

#solution
#%%
import pandas as pd
import numpy as np
df=pd.DataFrame([1254,2654,2514,1425],index= ['Jan', 'Feb', 'Mar','Apr']) ##columns=['sales'])
df=df.rename(columns={0:"sales"})
print(df)


##Inplace=true should be add to the code when 
##line100 doesn't have "df=", truly amazing



'''
task 6 : add in a new column to df1 with number of transactions [30,52,50,28]
sample output:
     sales  nos
Jan   1254   30
Feb   2654   52
Mar   2514   50
Apr   1425   28
'''

#solution
#%%
nos=['30','52','50','28']
df['nos']=nos
print(df)

#or by using df.insert
# df.insert(2, "Age", [21, 23, 24, 21], True)
# 2=place you want to put, Age means name

'''
task 7 : derive a new column 'avg' that represent the average sales per transaction 
sample output:
     sales  nos        avg
Jan   1254   30  41.800000
Feb   2654   52  51.038462
Mar   2514   50  50.280000
Apr   1425   28  50.892857    
'''

#solution
#%%

import pandas as pd
import numpy as np
df=pd.DataFrame([1254,2654,2514,1425],index= ['Jan', 'Feb', 'Mar','Apr'],columns=['sales'])
nos=[30,52,50,28]
df['nos']=nos
df['avg']=df['sales']/df['nos']
print(df)



'''
task 8 : extract any month's sales with average more than 50 
sample output:
     sales  nos        avg
Feb   2654   52  51.038462
Mar   2514   50  50.280000
Apr   1425   28  50.892857
'''
#solution
#%%

import pandas as pd
import numpy as np
df=pd.DataFrame([1254,2654,2514,1425],index= ['Jan', 'Feb', 'Mar','Apr'],columns=['sales'])
nos=[30,52,50,28]
df['nos']=nos
df['avg']=df['sales']/df['nos']

above=df.loc[df['avg']>50]
print(above)
#%%



'''
Task 9:
reassign the dataframe index and columns to mList, sList, nList and aList respectively
 
'''

import pandas as pd
import numpy as np
df=pd.DataFrame({'sales':[1254,2654,2514,1425],
                 'nos':[30,53,50,28]}
                 ,index= ['Jan', 'Feb', 'Mar','Apr'])

df['avg']=df['sales']/df['nos']
##df.index.name='month'
##df.reset_index(inplace=True)
##df.rename(columns={'month':'mlist','sales':'slist', 'nos':'nlist', 'avg':'alist'}, inplace=True)


mList=list(df.index)
print(mList)
sList=list(df['sales'])
print(sList)
nList=list(df['nos'])
print(nList)
aList=list(df['avg'])
print(aList)

#%%


'''
Task 10 :
    code the following and observe what you get
        df2=pd.DataFrame([mList,sList,nList,aList])
        print(df2)
sample output :
      0        1      2        3
0   Jan      Feb    Mar      Apr
1  1254     2654   2514     1425
2    30       52     50       28
3  41.8  51.0385  50.28  50.8929
'''
#solution
#%%


df2=pd.DataFrame([mList,sList,nList,aList])
print(df2)

#%%


'''
Task 11 :
    create another dataframe df3 with the content from mList, sList, nList and aList, index auto-assign
sample output:
   mth  sales  nos        avg
0  Jan   1254   30  41.800000
1  Feb   2654   52  51.038462
2  Mar   2514   50  50.280000
3  Apr   1425   28  50.892857
'''


df3=pd.DataFrame({'mth':mList,
                  'sales':sList,
                  'nos':nList,
                  'avg':aList})
print(df3)







'''
Task 12 :
    reset the column mth as the index of df3 with the following codes 
        df3.set_index('mth')
        df3
    observe what happen to df3
sample output:
task 12
   mth  sales  nos        avg
0  Jan   1254   30  41.800000
1  Feb   2654   52  51.038462
2  Mar   2514   50  50.280000
3  Apr   1425   28  50.892857
'''



df3.set_index('mth')
df3


'''
Task 13 :
    reset the column mth as the index of df3 again with the following codes 
        df3.set_index('mth',inplace=True)
        print(df3)
    observe what happen to df3
sample output:
task 13
     sales  nos        avg
mth                       
Jan   1254   30  41.800000
Feb   2654   52  51.038462
Mar   2514   50  50.280000
Apr   1425   28  50.892857
'''

##solution
df3.set_index('mth',inplace=True)
print(df3)




#%%
'''
Task 14 :
    create another dataframe df4 with the content from  sList, nList and aList, index column is mList
sample output:
     sales  nos        avg
Jan   1254   30  41.800000
Feb   2654   52  51.038462
Mar   2514   50  50.280000
Apr   1425   28  50.892857
'''

df4=pd.DataFrame({'sales':sList,
                  'nos':nList,
                  'avg':aList}, index=mList)
print(df4)
                  







