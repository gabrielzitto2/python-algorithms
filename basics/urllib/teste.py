import urllib.request

response = urllib.request.urlopen('https://gist.github.com/marcoscastro')
info = response.read()
html = info.decode('UTF-8')

pos = None

while True:

	target_ini = '<span class="description">'

	if pos == None:
		pos_find = html.find(target_ini, 0)
	else:
		pos_find = html.find(target_ini, pos)

	if pos_find == -1:
		break

	pos_ini =  pos_find + len(target_ini)
	pos_fim = html.find('</span>', pos_ini)
	title = html[pos_ini:pos_fim].replace('\n', '').lstrip()

	print(title)
	
	pos = pos_fim + len('</span>')