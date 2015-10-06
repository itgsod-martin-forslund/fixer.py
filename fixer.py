import requests

def valuta(from_currency, to_currency, amount) :
 response = requests.get("http://api.fixer.io/latest?base=" + from_currency)
 data = response.json()


 if from_currency == to_currency:
  print amount
 elif not to_currency in  data ["rates"]:
  print "error"
 else:
  return data ["rates"][to_currency]






 # if to_currency is not exeisting it will breake the code




