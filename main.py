import requests

url = "https://opencritic-api.p.rapidapi.com/game/search"

querystring = {"criteria":"the withcer 3"}

headers = {
	"X-RapidAPI-Key": "8a17aff511mshb3a4b5c80fe8483p13d835jsn66a6f2244274",
	"X-RapidAPI-Host": "opencritic-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())