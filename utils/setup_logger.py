import logging
import sys


def setup_logger():
	# Initializing logger
	logger = logging.getLogger('discord')
	logger.setLevel(logging.INFO)

	# File handler
	handler = logging.FileHandler(
		filename='logs/discord.log', encoding='utf-8', mode='w'
	)
	handler.setFormatter(
		logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
	)
	logger.addHandler(handler)

	# Console handler
	console_handler = logging.StreamHandler(sys.stdout)
	console_handler.setFormatter(
		logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
	)
	logger.addHandler(console_handler)

	return logger
