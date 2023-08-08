from quecto import Quecto

client = Quecto('https://s.oriondev.fr')
r = client.isValidInstance()

if r:
    print("Test 5: Passed")
else:
    print("Test 5: Failed")
