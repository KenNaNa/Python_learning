import requests
import BeautifulSoup
import pdfkit
def parse_url_to_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html5lib")
    body = soup.find_all(class_="x-wiki-content")[0]
    html = str(body)
    with open("a.html", 'wb') as f:
        f.write(html)
parse_url_to_html('http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000')
def get_url_list():
    """
    获取所有URL目录列表
    """
    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html5lib")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("li"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls
get_url_list()
def save_pdf(htmls):
    """
    把所有html文件转换成pdf文件
    """
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmls, file_name, options=options)
save_pdf(htmls)