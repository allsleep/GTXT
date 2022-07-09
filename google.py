from googletrans import Translator


# 谷歌翻译模块
class Translation:
    def __init__(self):
        self.translator = Translator(service_urls=['translate.google.cn',])# 如果可以上外网，还可添加 'translate.google.com' 等
    
    def get_translen(self, mes):
        trans=self.translator.translate(mes, src='zh-cn', dest='en')
        # print(trans.origin) # 原文
        # print(trans.text)   # 译文
        return len(trans.text)