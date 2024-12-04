def xpath_change(kind, text):
    # 组建xpath路径
    xpath_path = f'//{kind}[contains(text(),"{text}")]'
    return 'xpath', xpath_path