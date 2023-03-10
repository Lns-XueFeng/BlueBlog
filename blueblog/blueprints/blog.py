from flask import Blueprint
from flask import render_template, request, current_app, abort, make_response

from blueblog.models import Post, Category
from blueblog.utils import redirect_back


blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_POST_PER_PAGE"]
    pagination = Post.query.order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("blog/index.html", pagination=pagination, posts=posts)


@blog_bp.route("/about")
def about():
    return render_template("blog/about.html")


@blog_bp.route("/category/<int:category_id>")
def show_category(category_id):
    category = Category.query.get_or_404(category_id)
    page = request.args.get("page", 1, type=int)
    per_page = current_app.config["BLUELOG_POST_PER_PAGE"]
    pagination = Post.query.with_parent(category).order_by(Post.timestamp.desc()).paginate(page=page, per_page=per_page)
    posts = pagination.items
    return render_template("blog/category.html", category=category, pagination=pagination, posts=posts)


@blog_bp.route("/post/<int:post_id>", methods=["GET", "POST"])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("blog/post.html", post=post)


@blog_bp.route("/change-theme/<theme_name>")
def change_theme(theme_name):
    if theme_name not in current_app.config["BLUELOG_THEMES"].keys():
        abort(404)

    response = make_response(redirect_back())
    response.set_cookie("theme", theme_name, max_age=30 * 24 * 60 * 60)
    return response
