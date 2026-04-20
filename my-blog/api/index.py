from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# 더미 데이터
posts = [
    {"id": 1, "title": "첫 글", "content": "Flask + Vercel 블로그입니다."},
    {"id": 2, "title": "두번째 글", "content": "서버리스로 배포 중!"}
]

@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)

# Vercel용 핸들러
def handler(request, context):
    return app(request.environ, start_response=lambda status, headers: None)
