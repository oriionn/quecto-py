from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.unshortUrl('https://s.oriondev.fr/s/189d26f157975')
if r["error"]:
    print("Error: " + r["status"])
else:
    print(r["original"])
