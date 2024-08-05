# custom_exceptions.py
class APIError(Exception):
	def __init__(self, status_code: int, response_text: str):
		self.status_code = status_code
		self.response_text = response_text
		super().__init__(
			f"Error creating short URL: Status Code {status_code}, Message: {response_text}"
		)


class NoAPIResponseError(RuntimeError):
	pass
