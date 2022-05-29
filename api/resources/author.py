from api import Resource, reqparse, db, auth
from api.models.author import AuthorModel
from api.schemas.author import author_schema, authors_schema


# Если запрос приходит по url: /authors/<int:author_id>
class AuthorResource(Resource):
    def get(self, author_id):
        if author_id is None:
            authors = AuthorModel.query.all()
            authors_list = [author.to_dict() for author in authors]
            return authors_list, 200

        author = AuthorModel.query.get(author_id)
        if author is None:
            return f"Author id={author_id} not found", 404
        return author_schema.dump(author), 200

    def put(self, author_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        author_data = parser.parse_args()
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        author.name = author_data["name"]
        db.session.commit()
        return author_schema.dump(author), 200

    def delete(self, author_id):
        author = AuthorModel.query.get(author_id)
        if author is None:
            return {"Error": f"Author id={author_id} not found"}, 404
        db.session.delete(author)
        db.session.commit()
        return author_schema.dump(author)

# Если запрос приходит по url: /authors

class AuthorListResource(Resource):
    def get(self):
        authors = AuthorModel.query.all()
        return authors_schema.dump(authors), 200

    @auth.login_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", required=True)
        author_data = parser.parse_args()
        author = AuthorModel(author_data["name"])
        db.session.add(author)
        db.session.commit()
        return author_schema.dump(author), 201
