import inspect
import pprint
import types
from typing import Union

import requests


class OembedReader:
	def __init__(self):
		caller_frame = inspect.stack()[1]
		frame_module = inspect.getmodule(caller_frame[0])

		if isinstance(frame_module, types.ModuleType):
			self.module_name = frame_module.__name__
		else:
			# Handle the case where frame_module is not a module
			self.module_name = None

	def get_module_name(self) -> str:
		return str(self.module_name)

	@staticmethod
	def get_embed_data(url: str) -> str:
		endpoint = f'https://api.embed.rocks/api/oembed?url={url}'
		response = requests.get(endpoint)
		if response.status_code == 200:
			data = response.json()
			pprint.pprint(data)
			return str(data)
		print(f'Failed to fetch oEmbed data. Status code: {response.status_code}')

	@staticmethod
	def get_embed_response() -> Union[str, None]:
		headers = {
			'accept': '*/*',
			'accept-language': 'en-US,en;q=0.9',
			'authorization': 'MTIwNTU2MTY2ODYxMjkxOTQ5Nw.G3OZ4E.3PkkZpV68wB4wv4MVvQ4aTQfjvXIDNSR7DSS-8',
			'content-type': 'application/json',
			'cookie': '__Secure-recent_mfa=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE3MTI4NzQyNzIsIm5iZiI6MTcxMjg3NDI3MiwiZXhwIjoxNzEyODc0NTcyLCJpc3MiOiJ1cm46ZGlzY29yZC1hcGkiLCJhdWQiOiJ1cm46ZGlzY29yZC1tZmEtcmVwcm9tcHQiLCJ1c2VyIjo3MjE0MzA2NTM0NjM0MjkxMjF9.MTNz_xKsjdJ3H6zybvSs7_NIKubzH3gTHP6-9KBMmz7WEW6y-6vCFegcpALNordljNXqufQT3hOxMXTcXbQ7UA; __dcfduid=e3d34dc0cfcf11eeaca5913583765d19; __sdcfduid=e3d34dc1cfcf11eeaca5913583765d19349ddc586680b11449218565ac9f700ff1d1c140dbd224451dca0cd04939c250; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Thu+Apr+11+2024+22%3A44%3A00+GMT%2B0300+(Arabian+Standard+Time)&version=6.33.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; __cfruid=49d519f6907abc0710dd55cf7b5a3ddf300d4cef-1712874186; _cfuvid=QE_gY277E3bqlPMkm93CC8f8sldHshgokN_m8Re.SVk-1712874186079-0.0.1.1-604800000; cf_clearance=TgHeOx420S8gjsK0HRpg3709bs.uT0nRTjhTfQxJZsI-1712874186-1.0.1.1-Hubq_E912k1JQva78NUkkO58FSvwn_iQzweUzhpykwT5Rwpltz4TBQOnXiOCuIb16xvPACwK7d5tygBn8oeckQ',
			'dnt': '1',
			'origin': 'https://discord.com',
			'referer': 'https://discord.com/developers/embeds?url=https%253A%252F%252Ffixupx.com%252Fstatus%252F1774825827873513703',
			'sec-ch-ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"macOS"',
			'sec-fetch-dest': 'empty',
			'sec-fetch-mode': 'cors',
			'sec-fetch-site': 'same-origin',
			'sec-gpc': '1',
			'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
			'x-track': 'eyJvcyI6Ik1hYyBPUyBYIiwiYnJvd3NlciI6IkNocm9tZSIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChNYWNpbnRvc2g7IEludGVsIE1hYyBPUyBYIDEwXzE1XzcpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMjMuMC4wLjAgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEyMy4wLjAuMCIsIm9zX3ZlcnNpb24iOiIxMC4xNS43IiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6Mzg2OTQsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
		}

		data = '{"url":"https://fixupx.com/status/1774825827873513703"}'

		response = requests.post(
			'https://discord.com/api/v9/unfurler/unfurl', headers=headers, data=data
		)
		print(response.text)
		return str(response)

	@staticmethod
	def get_oembed_metadata(metaCdnUrl, format='jsonp', maxwidth=None, maxheight=None):
		url = 'http://www.metacdn.com/api/oembed'
		params = {
			'url': metaCdnUrl,
			'format': format,
			'maxwidth': maxwidth,
			'maxheight': maxheight,
		}
		headers = {'Accept': 'application/json+oembed'}
		response = requests.get(url, params=params, headers=headers)
		return str(response)
		# if response.status_code == 200:
		# 	return response.json()
		# else:
		# 	print('Error:', response.status_code)
		# 	return None
