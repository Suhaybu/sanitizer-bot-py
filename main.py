import os
import pkgutil

import interactions
from dotenv import load_dotenv
from interactions import ActivityType, Client, Intents, listen
from interactions.api.events import Startup

from utils.extensions_loader import extensions_loader

load_dotenv()


bot = Client(
	token=os.getenv("BOT_TOKEN"),
	status=interactions.Status.ONLINE,
	activity=interactions.Activity(name="with embeds", type=ActivityType.PLAYING),
	sync_interactions=True,
	intents=Intents.DEFAULT | Intents.MESSAGE_CONTENT,
)


@listen(Startup)
async def on_ready():
	print("Sanitizer Bot is Online!")


if __name__ == "__main__":
	try:
		print("Starting bot and loading exts..")
		extensions_names = [
			m.name for m in pkgutil.iter_modules(["exts"], prefix="exts.")
		]
		extensions_loader(extensions_names, bot)
		bot.start()
	except Exception as e:
		print(f"Sanitizer bot could not start.\nError: {e}")
	finally:
		print("\nSanitizer Bot is Offline")


def get_quick_vids_token() -> str | None:
	return os.getenv("QUICKVIDS_TOKEN")
