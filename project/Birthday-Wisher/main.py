import smtplib
import datetime as dt
import pandas as pd
from random import randint
import webbrowser as web

#global consonant
matching = False

try:
    data = pd.read_csv("project/Birthday-Wisher/birthdays.csv")
    date = dt.datetime.now().date()
     
    for index,df in data.iterrows():
        match = dt.datetime.strptime(f"{dt.datetime.today().year}-{df['month']}-{str(df['day']).zfill(2)}","%Y-%m-%d").date()
        if match == date:
            name = df['name']
            path = f"project/Birthday-Wisher/letter_templates/letter_{randint(1,3)}.txt"
            with open(path,mode="r+",encoding="utf-8") as letter:
                text = letter.read()
                replace = text.replace("[NAME]",name)
                print(replace)
                matching = True
        
except FileNotFoundError as error:
    print(error)

else:
    if matching:
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user="rahul1991modi@gmail.com",password="@Rahul123")
        connection.sendmail(from_addr="rahul1991modi@gmail.com",
        to_addrs="sarthakpunjabi04@gmail.com",
        msg=f"Subject:Happy Birthday to you\n\n{replace}"
        )
        ph = "+353"+"89 955 8494"
        web.open("https://web.whatsapp.com/send?="+ph+"&text="+replace)
        connection.close()