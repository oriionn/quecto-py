from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.unshortUrl('https://s.oriondev.fr/s/189d280c1252d', "password")

if r["error"]:
    print("Error: " + r["status"])
    print("Test 4: Failed")
else:
    if r["original"] != "https://example.com":
        print("Test 4: Failed")
    else:
        print("Test 4: Passed")
