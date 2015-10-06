from fixer import valuta

amount=10

r = valuta("SEK", "EUR", amount)

if r is not None:
    print (r * amount)