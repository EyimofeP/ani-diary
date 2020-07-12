from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapped_func(request, *args, **kwargs):
		if request.user.is_authenticated:
			return redirect("author:profile")
		else:
			return view_func(request, *args, **kwargs)
	return wrapped_func

def admin_only(view_func):
	def wrapped_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == "author":
			return view_func(request, *args, **kwargs)
		else:
			return redirect("author:login")
	return wrapped_function