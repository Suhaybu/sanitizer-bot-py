import requests
from requests.exceptions import RequestException


def get_iframely_data(url):
	try:
		response = requests.get(url)
		response.raise_for_status()  # Raise an exception for HTTP errors
		data = response.json()
		return data
	except RequestException as e:
		print(f'Error fetching Iframely data: {e}')
		return None


# Example usage:
iframely_url = 'https://fixupx.com/status/1776651619083370731'
data = get_iframely_data(iframely_url)
if data:
	print('Iframely Data:')
	print(data)
