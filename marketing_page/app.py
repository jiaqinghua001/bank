from flask import Flask, render_template

# 创建Flask应用（保持不变）
app = Flask(__name__)

# 1. 首页路由：访问根目录（http://127.0.0.1:5000）时返回index.html
@app.route('/')
def index():
    return render_template('index.html')

# 2. 子页面1：银行简介（对应URL：http://127.0.0.1:5000/intro）
@app.route('/intro')
def intro():
    return render_template('intro.html')  # 对应templates/intro.html

# 3. 子页面2：最热最新产品活动（对应URL：http://127.0.0.1:5000/activity）
@app.route('/activity')
def activity():
    return render_template('activity.html')  # 对应templates/activity.html

# 4. 子页面3：存款产品（对应URL：http://127.0.0.1:5000/deposit）
@app.route('/deposit')
def deposit():
    return render_template('deposit.html')  # 对应templates/deposit.html

# 5. 子页面4：办理收款二维码（对应URL：http://127.0.0.1:5000/qr-code）
@app.route('/qr-code')
def qr_code():
    return render_template('qr-code.html')  # 对应templates/qr-code.html

# 6. 子页面5：办理ETC（对应URL：http://127.0.0.1:5000/etc）
@app.route('/etc')
def etc():
    return render_template('etc.html')  # 对应templates/etc.html

# 7. 子页面6：办理信用卡（对应URL：http://127.0.0.1:5000/credit-card）
@app.route('/credit-card')
def credit_card():
    return render_template('credit-card.html')  # 对应templates/credit-card.html

# 8. 子页面7：开立对公账户资料（对应URL：http://127.0.0.1:5000/corporate-account）
@app.route('/corporate-account')
def corporate_account():
    return render_template('corporate-account.html')  # 对应templates/corporate-account.html

# 9. 子页面8：其他业务咨询（对应URL：http://127.0.0.1:5000/other）
@app.route('/other')
def other():
    return render_template('other.html')  # 对应templates/other.html

# 启动服务（本地调试用，保持不变）
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)