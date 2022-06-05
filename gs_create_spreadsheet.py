import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Connect to Google Sheets
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]   

credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)   # import credentials (not included)
client = gspread.authorize(credentials)                                                        # authorize 

#sheet = client.create("FirstSheet") # create the spreadsheet and name it something .. 
#sheet.share("Yourprivate_email@gmail.com" , perm_type='user' , role= 'writer')

sheet =  client.open("FirstSheet").sheet1  # open this sheet. 

df = pd.read_csv('data.csv')  # read data 

# df.colums.values.to_list()  this is the top line 
# df.values.tolist()   the data itself

sheet.update([df.columns.values.tolist()] + df.values.tolist())

print(" The End ")