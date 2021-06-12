class SearchList():
    def  __init__(self,*values):
        self.values=values
    def find(self,text):
        values=self.values
        output=[]
        a=""
        for a in values:
            n=a.find(text)
            if n != -1:
                output.append(a)
        return output


a=SearchList("以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：","执行脚本后，在循环到 Runoob时会跳出循环体：","Python for 循环可以遍历任何可迭代对象，如一")
print(a.find("for"))

