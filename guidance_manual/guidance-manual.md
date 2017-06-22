# 使用手册

## 替换 gitbook build
使用以下命令替换`gitbook build`
```shell
python3 my-gitbook-build-p3.py
```

## 插件

### prism
"plugins": ["prism","prism-themes"]

"pluginsConfig": {
    "prism": {
        "css": [
            "prismjs/themes/prism-mma.css"
        ]
    }
}

**JS**
/node_modules/prismjs/components/prism-mathematica.js
/node_modules/prismjs/components/prism-mma.js

**CSS**
/node_modules/prismjs/themes/prism-mma.css
