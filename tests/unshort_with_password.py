from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.unshortUrl('https://s.oriondev.fr/s/189d2707f3f9d', "password")
if r["error"]:
    print("Error: " + r["status"])
else:
    print(r["original"])
