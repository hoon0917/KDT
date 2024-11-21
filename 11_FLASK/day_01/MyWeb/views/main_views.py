# ---------------------------------------------------------------------
# Flask Framework에서 '/'URL에 대한 라우팅 처리 파일
# - 파일명 : main_views.py
# ---------------------------------------------------------------------

## 모듈 로딩 -----------------------------------------------------------
from flask import Blueprint, render_template

# Blueprint 인스턴스 생성
main_bp = Blueprint('main', __name__, url_prefix='/',template_folder='tempaltes')

# 라우팅 기능 함수 정의 -------------------------------------------------
@main_bp.route('/', endpoint='hello')
def index() :
    return render_template('index.html')