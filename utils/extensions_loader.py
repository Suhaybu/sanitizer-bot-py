from interactions import Client


def extensions_loader(extensions_names: list[str], bot: Client):
	total = len(extensions_names)
	loaded_extensions: list[str] = []
	failed_extensions: list[str] = []

	for extension in extensions_names:
		try:
			bot.load_extension(extension)
			loaded_extensions.append(extension.split(".")[-1])
		except:
			failed_extensions.append(extension.split(".")[-1])

	if not failed_extensions:
		print("All extensions are loaded!")

	print(
		f"{len(loaded_extensions)}/{total} Successfully loaded: {", ".join(loaded_extensions)}"
	)

	if failed_extensions:
		print(
			f"{len(failed_extensions)}/{total} Failed to load: {", ".join(failed_extensions)}"
		)
