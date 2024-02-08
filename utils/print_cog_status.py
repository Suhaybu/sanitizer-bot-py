# Handles console message for cog load status
def print_cog_status(loaded_cogs, faulty_cogs):
	total_cogs = len(loaded_cogs) + len(faulty_cogs)

	if total_cogs == 0:
		print('No cogs were loaded')
	else:
		state = 'All' if len(faulty_cogs) == 0 else f'{len(loaded_cogs)}/{total_cogs}'
		print(f'Loaded {state} cogs:', ', '.join(loaded_cogs))

	if faulty_cogs:
		print('Error loading:', ', '.join(faulty_cogs))
