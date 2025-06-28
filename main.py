from test_spapi import get_access_token, get_marketplace_participations

print("[🧪] Running SP-API test...")

token = get_access_token()
print("[✅] Access token received!")

result = get_marketplace_participations(token)
print("[✅] Success! Marketplaces:")
print(result)
