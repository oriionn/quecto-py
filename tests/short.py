from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.shortUrl('https://example.com')
if r["error"]:
    print("Error: " + r["status"])
    print("Test 1: Failed")
else:
    print("Test 1: Passed")
