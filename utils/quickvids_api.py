import requests


def create_short_url(input_text, detailed=False):
	url = 'https://api.quickvids.win/v1/shorturl/create'
	headers = {'Content-Type': 'application/json'}
	data = {'input_text': input_text, 'detailed': detailed}
	response = requests.post(url, json=data, headers=headers)
	if response.status_code == 200:
		return response.json()  # Includes quickvids_url and possibly details
	else:
		return response.json()  # Error handling
