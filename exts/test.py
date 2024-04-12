from interactions import Extension, SlashContext, slash_command

from utils.oembed_reader import OembedReader


class Test(Extension):
	def __init__(self, bot) -> None:
		self.o_embed = OembedReader()

	@slash_command(name='test', description='Test')
	async def test(self, ctx: SlashContext):
		url: str = 'https://fixupx.com/status/1776651619083370731'

		bot_response: str = 'module name: '
		bot_response += '\nOembed data for url:\n'
		# bot_response += str(self.o_embed.get_embed_response())
		bot_response += str(self.o_embed.get_oembed_metadata(metaCdnUrl=url))

		await ctx.respond(bot_response, ephemeral=True)
