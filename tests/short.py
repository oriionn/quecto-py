from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.shortUrl('https://example.com')
if r["error"]:
    print("Error: " + r["status"])
else:
    print(r["shorten"])
