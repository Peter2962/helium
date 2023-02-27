from flask_http_middleware import MiddlewareManager, BaseHttpMiddleware

class CheckIfAuthenticated(BaseHttpMiddleware):
	def __init__(self):
		super().__init__()

	def dispatch(self, request, call_next):
		print("Dispatching middleware: CheckIfAuthenticated")
		return call_next(request)