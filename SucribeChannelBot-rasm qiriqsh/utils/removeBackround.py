import requests

url = "https://background-removal.p.rapidapi.com/remove"

# payload = { "image_url": "https://objectcut.com/assets/img/raven.jpg" }
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "4ddfe2be95mshb2f8e97f21065b6p1f6045jsn6a197bb72815",
	"X-RapidAPI-Host": "background-removal.p.rapidapi.com"
}

# response = requests.post(url, data=payload, headers=headers)

# print(response.json())
async def remove(img_url):
	payload = f"image_url={img_url}"
	response = requests.request("POST", url, data=payload, headers=headers)
	return response.json()["response"]["image_url"]