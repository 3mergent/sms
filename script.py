import os
import csv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

client = Client(account_sid, auth_token)

errors = []

def send():

#    numbers_list = 'numbers.csv'
   numbers_list = 'test.csv'
  
   counter_success = 0
   counter_error = 0

   with open(numbers_list, 'r') as csvfile:
      
       numbers = csv.reader(csvfile)
       for number in numbers:
               target = '+' + str(number)
               print(target)
               try:
                   message = client.messages \
                       .create(
                               body="🔥🤖 CREATORS CHOICE 🤖🔥 CYBER MONDAY IS HERE! 50 PERCENT OFF ALMOST EVERYTHING! Use promo code:CYBERMONDAY at checkout to receive discount! creatorschoice.ca",
                               from_='+12565738077',
                               to=target
                           )
                   print(message.sid)
                   counter_success += 1
               except TwilioRestException as e:
                   temp_error = str(e.code) + ': ' + str(number)
                   errors.append(temp_error)
                   print(e)
                   counter_error += 1
          
       print(f"\n------------------\n\nMessages Sent: {counter_success}")
       print(f"Errors: {counter_error}\n\nError List (add to scrubs):\n")

send()

for error in errors:
    print(error)
    print('\n')
