# ---------------------------------------------------------------------
# Flask Framework에서 WebServer 구동 파일
# - 파일명 : app.py
# ---------------------------------------------------------------------

## 모듈 로딩 -----------------------------------------------------------
from flask import Flask, render_template


# 사용자 정의함수
def create_app() :

    ## 전역변수 ------------------------------------------------------------
    # Flask Web Server 인스턴스 생성
    APP = Flask(__name__)

    ## 라우팅 기능 함수 -----------------------------------------------------
    #@Flask Web Server 인스턴스.route("URL")
    @APP.route("/")
    def index() :
        # return """<body style='background-color:yellow;'>
        #           <h1>Hello<h1>
        #           </body>
        
        # """
        return render_template("index.html")
    # http://127.0.0.1:5000/info
    # http://127.0.0.1:5000/info/


    # -----------------------------------------------------------------------------------------------------
    @APP.route("/info")
    @APP.route("/info/")
    def info() :
        return """<body style='background-color:green; text-align:center'>
                <h1>INFORMATION<h1>
                </body>
        
        """
    # -----------------------------------------------------------------------------------------------------
    # http://127.0.0.1:5000/info/문자열변수
    # name에 문자열 변수 저장 => name=문자열변수
    @APP.route("/info/<name>")
    def printinfo(name) :
    #     return f"""
    #         <body style='background-color:green; text-align:center'>
    #         <h1>{name}`s INFORMATTION</h1>
    #         HELLO~
    # """
        return render_template("info.html",name=name)


    # -----------------------------------------------------------------------------------------------------
    @APP.route("/info/<int:age>")
    def checkAge(age) :
        return f"""
            <body style='background-color:green; text-align:center'>
            <h1>나이 : {age}</h1>
    """   



    # -----------------------------------------------------------------------------------------------------
    ## 다른 페이지로 넘어가기
    @APP.route("/go")
    def goHOME() :
        return APP.redirect("/info")

    

    return APP
## 조건부 실행 ------------------------------------------------------------
# __name__이 __main__과 같을때 서버 구동
if __name__ == '__main__' :
    app = create_app() 
    app.run()
