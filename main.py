from test_spapi import get_access_token, get_marketplace_participations

print("[🧪] Running SP-API test...")

try:
    token = get_access_token()
    print("[✅] Access token received!")

    result = get_marketplace_participations(token)
    print("[✅] Success! Marketplaces:")
    print(result)

except Exception as e:
    print("[❌] Error during SP-API call:")
    print(e)

# Dummy line to force Railway rebuild
print("Triggering fresh Railway build...")
