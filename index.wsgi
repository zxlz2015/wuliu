import sae
from logistics import wsgi

application = sae.create_wsgi_app(wsgi.application)