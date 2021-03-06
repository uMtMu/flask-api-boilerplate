from flask import Flask, render_template
from flask.views import MethodView
from webargs import fields, ValidationError
from webargs.flaskparser import use_kwargs
import redis
r = redis.Redis(host='localhost')

app = Flask(__name__)

class UserAPI(MethodView):
    def name_validator(name):
        if len(name) > 7:
            raise ValidationError('Length of user name must shorter than 7', status_code=500)
        else:
            return True
            
    def get(self, user_id):
        if user_id is None:
            return render_template('users.html', objects=[r.get(k) for k in r.keys('user*')])
        else:
            return render_template('users.html', objects=[r.get('user%s' % user_id)])
    post_args = {
        'id': fields.Int(required=True),
        'name': fields.Str(required=True, validate=name_validator),
        'age': fields.Int(),
    }
    @use_kwargs(post_args, locations=('json', 'form', 'query', 'headers', 'cookies', 'files'))
    def post(self, id, name, age=None):
        r.set('user%s' % id, name)
        if age:
            return 'hi %s %s.' % (name, age)
        else:
            return 'hi %s.' % (name)

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass


user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
app.add_url_rule('/users/<int:user_id>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])


if __name__ == "__main__":
    r.set('user1', 'umt')
    r.set('user2', 'utk')
    r.set('user3', 'cem')
    app.run(debug=True)