from .settings import THEME

def theme(request):
	return {"theme": THEME}