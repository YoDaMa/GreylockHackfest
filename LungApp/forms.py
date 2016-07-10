# import flask.ext.login as flask_login

# login_manager = flask_login.LoginManager()

# login_manager.init_app(app)


# class User(UserMixin):
#     # proxy for a database of users
#     user_database = {"JohnDoe": ("JohnDoe", "John"),
#                "JaneDoe": ("JaneDoe", "Jane")}

#     def __init__(self, username, password):
#         self.id = username
#         self.password = password

#     @classmethod
#     def get(cls,id):
#         return cls.user_database.get(id)

# class LoginForm(Form):
#     username = TextField('Username', [validators.Required()])
#     password = PasswordField('Password', [validators.Required()])
#     remember_me = BooleanField('remember_me',default=False)

#     def __init__(self, *args, **kwargs):
#         Form.__init__(self, *args, **kwargs)
#         self.user = None

#     def validate(self):
#         rv = Form.validate(self)
#         if not rv:
#             return False

#         user = User.query.filter_by(
#             username=self.username.data).first()
#         if user is None:
#             self.username.errors.append('Unknown username')
#             return False

#         if not user.check_password(self.password.data):
#             self.password.errors.append('Invalid password')
#             return False

#         self.user = user
#         return True