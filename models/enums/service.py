from enum import Enum


class Service(Enum):
	TIKTOK = "TikTok"
	INSTAGRAM = "Instagram"
	TWITTER = "Twitter"


class ServiceResponse:
	def __init__(self, service: Service, content: str):
		self.service = service
		self.content = content

	def __repr__(self):
		return f"ServiceResponse(service={self.service}, content={self.content})"
