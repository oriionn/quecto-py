from quecto import Quecto

client = Quecto('https://example.com')
r = client.isValidInstance()

if not r:
    print("Test 6: Passed")
else:
    print("Test 6: Failed")
