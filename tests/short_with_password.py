from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.shortUrl('https://example.com', "password")
if r["error"]:
    print("Error: " + r["status"])
    print("Test 2: Failed")
else:
    print("Test 2: Passed")
