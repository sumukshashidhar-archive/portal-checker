import requests
from dotenv import load_dotenv as ld
import os

# load env vars from the .env file
ld()

# url for the admissions update
url = "https://application.gatech.edu/account/login?r=https%3a%2f%2fapplication.gatech.edu%2fapply%2fupdate"

# post data and posting
data = {"email": os.getenv("USERNAME"), "password": os.getenv("PASSWORD")}
x = requests.post(url, data)

# checking if post contains an update

noupstring = "There is no update to your application status to report"
if x.text.find(noupstring) != -1:
    print("No Update Yet")
else:
    print("Updated!!")
