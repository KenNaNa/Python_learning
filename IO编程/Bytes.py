from io import BytesIO

f = BytesIO()
f.write('中国'.encode('utf-8'))

print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
data = f.read()
print(data)