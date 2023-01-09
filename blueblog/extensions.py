from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_moment import Moment
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
csrf = CSRFProtect()
ckeditor = CKEditor()
bootstrap = Bootstrap()
debug_toolbar = DebugToolbarExtension()
moment = Moment()
login_manager = LoginManager()
migrate = Migrate()
