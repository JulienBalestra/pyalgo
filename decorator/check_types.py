def accepts(*types):
	def check_args(ft_to_decorate):
		if len(types) != ft_to_decorate.func_code.co_argcount:
			raise AttributeError("<%s> have %d *args and <%s> have %d *args" % (
				accepts.__name__, len(types), ft_to_decorate.__name__, ft_to_decorate.func_code.co_argcount))

		def ft_decorated(*args, **kwargs):
			for a, t in zip(args, types):
				if type(a) is not t:
					raise TypeError("arg %r does not match %s" % (a, t))
			return ft_to_decorate(*args, **kwargs)

		ft_decorated.func_name = ft_to_decorate.func_name
		return ft_decorated

	return check_args
