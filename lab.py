from flask import Flask, render_template, abort
from flask.views import View, MethodView

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

users = [123, 244, 113, 488]

#1 @app.route('/users/')
#1 def show_users():
#1     return render_template('users.html', objects=users)

#1 class ShowUsers(View):
#1     def dispatch_request(self):
#1         return render_template('users.html', objects=users)

#2 class ListView(View):
#2 
#2     def get_template_name(self):
#2         raise NotImplemented()
#2 
#2     def render_template(self, context):
#2         return render_template(self.get_template_name(), **context)
#2 
#2     def dispatch_request(self):
#2         context = {'objects': self.get_objects()}
#2         return self.render_template(context)
#2 
#2 class UserView(ListView):
#2 
#2     def get_template_name(self):
#2         return 'users.html'
#2 
#2     def get_objects(self):
#2         return users

#2 app.add_url_rule('/users/', view_func=UserView.as_view('show_users'))

#3 class UserAPI(MethodView):
#3 
#3     def get(self):
#3         return render_template('users.html', objects=users)
#3 
#3 app.add_url_rule('/users/', view_func=UserAPI.as_view('users'))



#4 user_status = True
#4 def user_required(f):
#4     """Checks whether user is logged in or raises error 401."""
#4     def decorator(*args, **kwargs):
#4         if not user_status:
#4             abort(401)
#4         return f(*args, **kwargs)
#4     return decorator
#4 
#4 
#4 # How to use decorator on views
#4 class UserAPI(MethodView):
#4 
#4     def get(self):
#4         return render_template('users.html', objects=users)
#4 
#4 # How to use decorator on views (Alternative way)
#4 class UserAPI2(MethodView):
#4     decorators = [user_required]
#4     def get(self):
#4         return render_template('users.html', objects=users)
#4 
#4 
#4 
#4 view = user_required(UserAPI.as_view('users'))
#4 app.add_url_rule('/users/', view_func=view)
#4 
#4 app.add_url_rule('/users2/', view_func=UserAPI2.as_view('users'))


# Method Views for APIs
class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            return render_template('users.html', objects=users)
        else:
            return render_template('users.html', objects=[users[user_id]])

    def post(self):
        # create a new user
        pass

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


# Method Views for APIs
## Alternative way to register, for multiple endpoints
class UserAPI2(MethodView):

    def get(self, user_id):
        if user_id is None:
            return render_template('users.html', objects=users)
        else:
            return render_template('users.html', objects=[users[user_id]])

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass


## Alternative way to register, for multiple endpoints
def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])

register_api(UserAPI2, 'user_api2', '/users2/', pk='user_id')


if __name__ == "__main__":
    app.run()