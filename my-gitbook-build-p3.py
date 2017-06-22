#!/usr/bin/python
# coding=utf-8

import re
import os
current_path = os.path.dirname(os.path.realpath(__file__))


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 1 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 替换 Markdown 中的转义字符
# 主要是为了处理数学公式中的特殊字符
def replace_escaped_characters(path):
    with open(path, 'r', encoding="utf8") as f:
        md_str = f.read()
    # 处理 {% raw %}--{% endraw %} 或 {% math %}--{% endmath %}
    md_str_raws = re.findall(r'\{\%\s*raw\s*\%\}(.+?)\{\%\s*endraw\s*\%\}', md_str, flags=re.I|re.M|re.S)
    k = 1
    for md_str_raw in md_str_raws:
        ii = md_str_raw.strip(' \n\r')
        if ii[0] == '$' or ii[0:2] == r'\[':
            k += 1
            ii = re.sub(r'^\\\[|\\\]$', '$$', ii, flags=re.I)   # 处理 \[--\]
            ns = re.sub(r'(?P<aa>[\_\{\}\\\$])', r'\\\g<aa>', ii, flags=re.I | re.M | re.S)
            md_str = md_str.replace(md_str_raw, ns)
        if k > 10000:
            break
    path_new = re.sub(r'-o\.md$', r'.md', path, flags=re.I)
    with open(path_new, 'w', encoding="utf8") as f:
        f.write(md_str)
        print('Escaped characters done:\t' + path)


my_path = os.path.join(current_path, 'docs')
for (path, sub_paths, file_names) in os.walk(my_path):
    for f in file_names:
        if f[-5:] == '-o.md':
            replace_escaped_characters(os.path.join(path, f))

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 2 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 运行gitbook build
print('gitbook building ...')
os.system('gitbook build')
print('gitbook build done!')


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ 3 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 1. 修改“*.html”中的：http 为 https
# 2. 修改“*.html”中的：国外镜像为国内镜像
# 修改 *.html 中的链接：改为国内 CDN 镜像
def replace_cdn(path):
    with open(path, 'r', encoding='UTF-8') as f:
        fc = f.read()
        fc2 = re.sub(r'https://cdn\.mathjax\.org/mathjax/[^\/]+/MathJax\.js',
            r'//cdn.bootcss.com/mathjax/2.7.0/MathJax.js', fc)
        fc2 = re.sub(r'https://maxcdn\.bootstrapcdn\.com/bootstrap/[^\/]+/js/bootstrap\.min\.js',
            r'//cdn.bootcss.com/bootstrap/3.3.7/js/bootstrap.min.js', fc2)
        fc2 = re.sub(r'https://maxcdn\.bootstrapcdn\.com/bootstrap/[^\/]+/css/bootstrap\.min\.css',
            r'//cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css', fc2)
    with open(path, 'w', encoding='UTF-8') as f:
        f.write(fc2)
    print('https and CDN done:\t' + path)

my_path = os.path.join(current_path, '_book')
for (path, sub_paths, file_names) in os.walk(my_path):
    for f in file_names:
        if f[-5:] == '.html':
            replace_cdn(os.path.join(path, f))


# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 畅言 中的链接：改 http 为 https
my_path = os.path.join(current_path, '_book/gitbook/gitbook-plugin-changyan/changyan.js')
try:
    with open(my_path, 'r', encoding='UTF-8') as f:
        file_content = f.read()
        file_content2 = re.sub(r'http://', r'https://', file_content)
    with open(my_path, 'w', encoding='UTF-8') as f:
        f.write(file_content2)
    print('https done:\t' + 'changyan')
except:
    print('has no changyan!')

# ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
# 修改 MathJax 配置
mathjax_conf = '''
      extensions: ["tex2jax.js"],
      jax: ["input/TeX", "output/HTML-CSS"],
      tex2jax: {
        inlineMath: [
          ['$', '$'],
          ["\\(", "\\)"]
        ],
        displayMath: [
          ['$$', '$$'],
          ["\\[", "\\]"]
        ],
        processEscapes: true
      },
      "HTML-CSS": {
        availableFonts: ["TeX"],
        styles: {
          "#MathJax_Zoom": {
            'background': '#eaeaea',
            '-webkit-box-shadow': '3px 3px 3px rgba(100,100,100,0.2)',
            'box-shadow': '3px 3px 3px rgba(100,100,100,0.2)'
          }
        }
      },
      menuSettings: { zoom: "Click" }
'''

my_path = os.path.join(current_path, '_book/gitbook/gitbook-plugin-mathjax/plugin.js')
try:
    with open(my_path, 'r', encoding='UTF-8') as f:
        file_content = f.read()
        file_content2 = re.sub(r'tex2jax\:\s\{\}', mathjax_conf, file_content)
    with open(my_path, 'w', encoding='UTF-8') as f:
        f.write(file_content2)
    print('MathJax done:\t' + 'MathJax')
except:
    print('has no MathJax')
