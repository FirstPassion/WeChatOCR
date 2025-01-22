import wcocr  # wcocr.pyd 要放在tools.py的同级目录下
import os


def wechat_ocr(
    image_path: str,
    wechat_path: str = "path",
    wechatocr_path: str = "path/WeChatOCR/WeChatOCR.exe",
):
    """
    微信OCR识别函数
    :param image_path: 要识别的图片路径
    :param wechat_path: WeChat路径(当前目录下的 path,保存了其他识别所需要的文件)
    :param wechatocr_path: WeChatOCR路径(当前目录下的 path/WeChatOCR/WeChatOCR.exe)
    :return: 识别结果
    """
    # 要检查的依赖路径
    paths = {"wechat_path": wechat_path, "wechatocr_path": wechatocr_path}
    # 检查路径是否存在
    for path_name, path in paths.items():
        if not path or not os.path.exists(path):
            print(f"{path} {'文件夹' if 'path' in path_name else '文件'}不存在")
            return []  # 返回空结果

    # 初始化 WeChatOCR
    wcocr.init(wechatocr_path, wechat_path)
    # 执行 OCR 识别
    return wcocr.ocr(image_path)


if __name__ == "__main__":
    # 使用wechat_ocr函数进行OCR识别
    result = wechat_ocr("1.png")
    # 打印识别结果
    print(f"imgpath: {result['imgpath']}")
    print(f"errcode: {result['errcode']}")
    print(f"width: {result['width']}")
    print(f"height: {result['height']}")
    # 打印OCR识别结果
    # {'text': '文字内容', 'left': 左上角x坐标, 'top': 左上角y坐标, 'right': 右下角x坐标, 'bottom': 右下角y坐标, 'rate': 置信度}
    print(f"ocr_response: {result['ocr_response']}")
