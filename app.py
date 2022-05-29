from api import api, app
from api.resources.quote import QuoteResource, QuoteListResource
from api.resources.author import AuthorResource, AuthorListResource
from api.resources.user import UserResource, UsersListResource
from api.resources.auth import TokenResource
from config import Config

app.config['JSON_AS_ASCII'] = False

api.add_resource(QuoteResource,
                 '/authors/<int:author_id>/quotes/<int:quote_id>'
                 )  # <-- requests

api.add_resource(QuoteListResource,
                 '/quotes/',
                 '/authors/<int:author_id>/quotes'
                 )  # <-- requests

api.add_resource(AuthorResource,
                 '/authors/<int:author_id>')

api.add_resource(AuthorListResource,
                 '/authors')  # <-- requests

api.add_resource(UserResource,
                 '/users/<int:user_id>')

api.add_resource(UsersListResource,
                 '/users')  # <-- requests

api.add_resource(TokenResource,
                 '/auth/token')  # <-- requests

if __name__ == '__main__':
    app.run(debug=Config.DEBUG, port=Config.PORT)
