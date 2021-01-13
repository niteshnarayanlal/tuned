import tuned.logs
from . import base

class get_netdev_name(base.Function):
	"""
	Checks whether the user has specified any interface name. If
        not, return "all".
	"""
	def __init__(self):
		# 1 argument
		super(get_netdev_name, self).__init__("get_netdev_name", 1, 1)

	def execute(self, args):
		if not super(get_netdev_name, self).execute(args):
			return None
		if "netdev_name" in args[0]:
			return "all"
		return args[0]
