from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap4
from flask_debugtoolbar import DebugToolbarExtension
from flask_moment import Moment
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
csrf = CSRFProtect()
ckeditor = CKEditor()
bootstrap4 = Bootstrap4()
debug_toolbar = DebugToolbarExtension()
moment = Moment()
login_manager = LoginManager()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    from blueblog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
# login_manager.login_message = 'Your custom message'
login_manager.login_message_category = 'warning'
