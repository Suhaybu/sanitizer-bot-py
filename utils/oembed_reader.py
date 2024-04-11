import inspect
import types


class OembedReader:
	def __init__(self):
		caller_frame = inspect.stack()[1]
		frame_module = inspect.getmodule(caller_frame[0])
		if isinstance(frame_module, types.ModuleType):
			self.file_name = frame_module.__name__
		else:
			# Handle the case where frame_module is not a module
			self.file_name = ''
