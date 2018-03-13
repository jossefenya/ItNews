from flask import Blueprint
from flask import render_template
from models import Post
from app import db
from flask import request
from flask import url_for, redirect
from .forms import PostForm

posts = Blueprint('posts', __name__, template_folder='templates')


@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


@posts.route('/<slug>')
def news_detail(slug):
    post = Post.query.filter(Post.slug == slug).first()
    return render_template('posts/news_detail.html', post=post)


@posts.route('/create', methods=['POST', 'GET'])
def create_post():

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        try:
            post = Post(title=title, body=body)
            db.session.add(post)
            db.session.commit()
        except:
            print('Error')
        return redirect(url_for('posts.index'))

    form = PostForm()
    return render_template('posts/create_post.html', form=form)