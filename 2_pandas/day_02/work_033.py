import pandas as pd
datafile=r'C:\Users\KDP-17\EX_PANDAS6'
csvDf=pd.read_csv(datafile,encoding='euc-kr',header=None)
print(csvDf)