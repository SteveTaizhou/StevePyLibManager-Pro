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


if __name__ == "__main__":
    a=SearchList("12","22","33","32")
    print(a.find("2"))

