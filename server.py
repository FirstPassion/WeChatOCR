from flask import Flask, request, render_template, jsonify
import os
import json
from tools import wechat_ocr

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False  # 禁用 ASCII 编码，支持中文

# 设置上传文件的目录
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# 确保上传目录存在
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    """
    首页路由，返回上传文件的页面
    """
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_file():
    """
    处理文件上传的路由
    """
    # 检查是否有文件被上传
    if "file" not in request.files:
        return jsonify({"error": "没有文件被上传"}), 400

    file = request.files["file"]

    # 检查文件名是否为空
    if file.filename == "":
        return jsonify({"error": "没有选择文件"}), 400

    # 保存上传的文件
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    # 使用 OCR 识别文本
    result = wechat_ocr(file_path)

    # 如果结果是字符串，尝试将其解析为 JSON
    if isinstance(result, str):
        try:
            result = json.loads(result)
        except json.JSONDecodeError:
            return jsonify({"error": "OCR 返回的数据不是有效的 JSON"}), 500

    # 返回 JSON 响应，确保中文不乱码
    response = jsonify(result)
    response.headers.add("Access-Control-Allow-Origin", "*")  # 允许跨域请求
    response.headers["Content-Type"] = "application/json; charset=utf-8"  # 设置编码
    return response


if __name__ == "__main__":
    # 启动 Flask 应用
    app.run(debug=True)
