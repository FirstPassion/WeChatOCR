# WeChatOCR
这是一个采用Python调用微信OCR功能，进行批处理图片OCR的代码。

首先非常感谢swigger，52PJ的FeiyuYip，nulptr以及其他对此做出贡献的朋友。

基于他们的工作，改动如下：
1. 将WeChatOCR.exe做了本地化，不再依赖微信的安装路径。
2. 将图片处理的格式多样化，增加了jpg，jpeg，bmp，tif格式的处理，只需要将文件放入scr文件夹中的即可。
3. 将OCR的处理结果将以docx格式保存到docx文件夹中。

关于源文件的问题：
我感觉wenchatocr对png格式的处理能力比较好，所以建议将图片格式转换为png以后再做OCR处理。

## 我修改的内容
* 给OCR.py加上了详细的中文注释
* 抽取了wechat_ocr函数到tools.py中,并且加上详细的使用例子
* 增加了server.py文件，用于提供OCR网页识别服务

## 使用

### 1.创建虚拟环境
```bash
python -m venv .venv
```

### 2. 激活虚拟环境
因为pyd文件是windows的，所以需要只能在windows下运行
```bash
.venv\Scripts\activate
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 运行server.py
```bash
python server.py
```