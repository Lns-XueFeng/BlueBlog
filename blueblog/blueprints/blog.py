from flask import Blueprint
from flask import render_template


blog_bp = Blueprint('blog', __name__)


@blog_bp.route("/")
def index():
    return render_template("blog/index.html")


@blog_bp.route("/post")
def post():
    return render_template("blog/post.html")


@blog_bp.route("/about.html")
def about():
    return render_template("blog/about.html")
