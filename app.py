from api import api, app
from api.resources.quote import QuoteResource
from api.resources.author import AuthorResource, AuthorListResource
from config import Config

api.add_resource(QuoteResource,
                 '/authors/<int:author_id>/quotes/<int:quote_id>',
                 '/authors/<int:author_id>/quotes',
                 '/quotes'
                 )  # <-- requests

api.add_resource(AuthorResource,
                 '/authors/<int:author_id>')

api.add_resource(AuthorListResource,
                 '/authors')  # <-- requests

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
