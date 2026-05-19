import os
import json as PyJson

print("Char's Auto Generating uploads page, generator.")

ignoreURLS:list[str] = [
    "python.svg",
    "tips.jpeg",
    "vscode.svg",
    "namecheap.svg",
    "*.db"
    "desc.json",
    "ignore_*"
]

def convertToSize(sizeInBytes:int) -> str:
    GBCalc = sizeInBytes / ((1024 * 1024) * 1024)
    MBCalc = sizeInBytes / (1024 * 1024)
    KBCalc = sizeInBytes / 1024

    if GBCalc >= 1:
        return f'{GBCalc:.2f} GB'
    if MBCalc >= 1:
        return f'{MBCalc:.2f} MB'
    if KBCalc >= 1:
        return f'{KBCalc:.2f} KB'
    
    return f'{sizeInBytes} B'

searchPaths:list[str] = [
    # "../images",
    # "../archive/imgs",
    # "../css",
    # "../js",
    # "../generators"
]
urls:list[str] = []
descs:list[str] = []

try:
    descFile = open("desc.json", 'r')
    descs = PyJson.loads(descFile.read())["descs"]
except OSError as e:
    print("Could not load descs!" + str(e))


def recursiveAddPath(path2:str):
    for path in path2:
        if not path.endswith("/"): path += "/"

        for file in os.listdir(path):
            if file.endswith("/") or not file.__contains__("."):
                continue
            if not isInIgnoredURLS(file):
                urls.append(path + file)
                print(f"Found File: `{file}`")


def isInIgnoredURLS(url:str)->bool:
    if url.__contains__("index.html"): return True
    for iURL in ignoreURLS:
        if iURL.__contains__("*"):
            iURL = iURL.replace("*", "")
            if url.endswith(iURL): return True
            if url.startswith(iURL): return True
        if url.__contains__(iURL): return True
    return False
for file in os.listdir("./"):
    if not isInIgnoredURLS(file):
        urls.append(file)
        print(f"Found File: `{file}`")

for path in searchPaths:
    curPath = path
    if not path.endswith("/"): path += "/"

    for file in os.listdir(path):
        if file.endswith("/") or not file.__contains__("."):
            searchPaths.append(curPath + '/' + file)
        if not isInIgnoredURLS(file):
            urls.append(path + file)
            print(f"Found File: `{file}`")


rawHTML = '''
<!DOCTYPE html>
<head>
    <title>All files open for the public to download</title>
    <link rel="stylesheet" href="https://vschar-official.com/css/vs-char-style.css">
    <link rel="stylesheet" href="https://vschar-official.com/css/global-style.css">
    <style>
        @font-face {
        font-family: funkin;
        src: url('https://vschar-official.com/fonts/funkin.ttf');
        }
        body {
            background-color: #FF880088;
            font-size: 1vw;
            font-family: funkin;
        }
        .ENDOFLIST {
            color: #884422;
        }
        .title {
          align-items: center;
          font-size: 4vw;
          color: #884422;
        }

        img {
        max-width: 25vw;
        }
    </style>
    <script src="/js/AddFooter.js"></script>
</head>
<body>
    <div class="title">
    <img src="/images/chair_download.png" alt="Char says "Download some cool shit!""><BR>FILES:
    </div><br>(Not everything will have a description yet!)<br><br>\n
'''

sortedFiles:list[str] = sorted(urls, key=lambda x: x[-1])
sortedFiles.reverse()

reachedImages = False
for file in sortedFiles:
    if file.lower().startswith("ignore_"): continue
    if file.endswith("/") or not file.__contains__(".") or file.endswith(".db") or file.endswith(".css") or file == "desc.json": continue
    print(f"Processing: `{file}`")
    if not reachedImages and file.endswith(".png"):
        rawHTML += '    <div class="ENDOFLIST">END OF LIST</div><br><br><br><div class="title">Downloadable Images:</div><br><br><br>\n'
        reachedImages = True

    additiveHTML = f'<a href="{file.replace("../", "")}">{file.replace("%20", " ").replace("../", "")} | {convertToSize(os.path.getsize(file))}</a><br><br>\n'
    try:
        additiveHTML = f'<a href="{file.replace("../", "")}">{file.replace("%20", " ").replace("../", "")} | {descs[file.replace("../", "")]} | {convertToSize(os.path.getsize(file))}</a><br><br>\n'
        if file.endswith(".png"): additiveHTML = f'<a href="{file}">{descs[file]} | {convertToSize(os.path.getsize(file))}</a><br><br>\n'
    except Exception as e: print(e)
    rawHTML += additiveHTML
    

rawHTML += '''
    <div class="ENDOFLIST">
        END OF LIST
    </div>
</body>
<footer id="footer_uploads"></footer>'''

os.remove("index.html")
file = open('index.html', 'w')
file.write(rawHTML)
file.close