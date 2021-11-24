from ftplib import FTP
import pandas as pd

ftp = FTP('10.98.138.4','ftpperformance','Womchile2021#!')
file1 = 'DIM_BSC6910UMTS_Board.csv'
ftp.cwd('/export/home/sysm/opt/oss/server/var/fileint/cm/InvtTimerExport')
ftp.retrlines('LIST')
with open('DIM_BSC6910UMTS_Board.csv', 'wb') as fp:
    ftp.retrbinary('RETR DIM_BSC6910UMTS_Board.csv',fp.write)
df = pd.read_csv('DIM_BSC6910UMTS_Board.csv')
print(df)
