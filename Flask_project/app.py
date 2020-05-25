from flask import Flask
import pymysql
from flask import Flask, render_template, url_for, request,redirect,make_response,session
from flask import jsonify
import time
app = Flask(__name__)


@app.route('/')
# def hello_world():
#     return  render_template('/UI.html',  name="World！")
def hello_world():
    return  render_template('/index.html',  name="World！")

@app.route('/index_paihang',methods=['GET','POST'])
def index_paihang():
    id = int(time.time())%120
    #print(id)

    # 连接database
    conn = pymysql.connect(host="121.36.167.129", user="ncov", password="123", database="ncov", charset="utf8")
    # 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
    sql = "SELECT * from hotItem where id = %d;" % (id)
    # 执行SQL语句
    cursor.execute(sql)
    results = cursor.fetchall()

    conn.commit()
    # 关闭光标对象
    cursor.close()
    # 关闭数据库连接
    conn.close()
    res = {}

    item=0
    if results:
        for result in results:
            #print(result)
            res['time']=result[1]
            res["id1"] = result[2]
            res["count1"] = result[3]
            res["id2"] = result[4]
            res["count2"] = result[5]
            res["id3"] = result[6]
            res["count3"] = result[7]
            item+=1

    rst = make_response(jsonify(res))
    rst.headers['Access-Control-Allow-Origin'] = '*'
    rst.headers['Access-Control-Allow-Methods'] = 'POST'  # 响应POST

    return rst


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888,debug=True)
