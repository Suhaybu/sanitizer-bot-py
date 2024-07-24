from interactions import Embed, Extension, SlashContext, slash_command


class Credits(Extension):
	@slash_command(name="credits", description="Roll the credits! 🎺")
	async def credits(self, ctx: SlashContext):
		with open(file="credits.md", mode="r", encoding="utf-8") as file:
			bot_response = file.read()
		await ctx.send(embed=Embed(description=bot_response), ephemeral=True)
