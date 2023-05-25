import molotov
import json

@molotov.scenario(10)
async def test_json_response(session):
    async with session.get('http://example.com/api') as response: # we use the link of an api online
        if response.status == 200:
            data = await response.json()
            if isinstance(data, dict):
                assert 'key' in data, "Key is missing in the JSON response"
                print("JSON response test passed!")
            else:
                print("JSON response test failed!")
        else:
            print("HTTP status is not 200!")

if __name__ == '__main__':
    molotov.run(
        debug=True,
        print_stats=True,
    )

