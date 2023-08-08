from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.unshortUrl('https://s.oriondev.fr/s/189d2817c5c3d')
if r["error"]:
    print("Error: " + r["status"])
    print("Test 4: Failed")
else:
    if r["original"] != "https://example.com":
        print("Test 3: Failed")
    else:
        print("Test 3: Passed")
