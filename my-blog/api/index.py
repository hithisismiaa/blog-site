import os
from flask import Flask, render_template

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "../templates"),
    static_folder=os.path.join(BASE_DIR, "../static")
)

# 샘플 데이터 (DB 없이)
posts = [
    {"id": 1, "title": "첫 글", "content": "Flask + Vercel 블로그 시작!"},
    {"id": 2, "title": "두 번째 글", "content": "배포 성공을 목표로!"}
]

# 홈
@app.route("/")
def index():
    return render_template("index.html", posts=posts)

# 상세 페이지
@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    return render_template("post.html", post=post)
