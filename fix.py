import io

try:
    with io.open('index.html', 'r', encoding='utf-8') as f:
        text = f.read()
        
    if text.startswith('\ufeff'):
        text = text[1:]
        
    fixed = text.encode('windows-1252').decode('utf-8')
    with io.open('index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)
    print("Fixed!")
except Exception as e:
    print(e)
