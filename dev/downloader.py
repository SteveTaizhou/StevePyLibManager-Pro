import urllib.request

def download(url,filename):
    urllib.request.urlretrieve(url, filename)

if __name__ == "__main__":
    url = "https://github.com/SteveTaizhou/StevePyLibManager-Pro/raw/main/plugins/list.txt"
    urllib.request.urlretrieve(url, "pluginslist.txt")
