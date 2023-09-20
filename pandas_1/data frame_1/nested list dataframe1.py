import numpy as np
import pandas as pd
lst=[[101,'arun','k',25,'bigdata',2500],[102,'ashwin','kd',24,'python',1500],[103,'ajmal','pk',26,'mearn',2300],[104,'bilal','bb',28,'java',1500],[105,'anto','r',31,'tablue',1800]]
a=pd.DataFrame(lst,columns=['id','fname','lname','age','prof','salary'])
print(a)
print(a.shape)
print(a.head(3))
print(a.tail(2))
print(a.size)
print(a.columns)
print(a.dtypes)
print(a.describe(include='all'))