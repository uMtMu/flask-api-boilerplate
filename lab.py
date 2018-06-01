from flask import Flask, render_template
from flask.views import MethodView
from webargs import fields
from webargs.flaskparser import use_args
import redis
r = redis.Redis(host='localhost')

app = Flask(__name__)

class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            return render_template('users.html', objects=[r.get(k) for k in r.keys('user*')])
        else:
            return render_template('users.html', objects=[r.get('user%s' % user_id)])
    post_args = {
        'id': fields.Int(required=True),
        'name': fields.Str(required=True),
        'age': fields.Int(),
    }
    @use_args(post_args)
    def post(self, args):
        r.set('user%s' % args['id'], args['name'])
        if 'age' in args.keys():
            return 'hi %s %s.' % (args['name'], args['age'])
        else:
            return 'hi %s.' % (args['name'])

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