salary = [{'Name':'Alice', 'Job':'Data Scientist', 'Salary':122000},
          {'Name':'Bob', 'Job':'Engineer', 'Salary':77000},
          {'Name':'Carl', 'Job':'Manager', 'Salary':119000}]

import pandas as pd
df = pd.DataFrame(salary)
df.to_csv('my_file.csv', index=False, header=True)

a=pd.read_csv("my_file.csv")
print(a)
