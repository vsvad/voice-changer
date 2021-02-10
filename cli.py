import os
def prompt(flt):
	out=f'Select a filter:\n'
	out+='\n'.join([str(i) for i in flt.list])
	return out
def _getflt(flt):
	n=input('Your select: ')
	if not n.isdigit():
		print('Error: isn\'t id')
		return 'no'
	n=int(n)
	o=flt.byid(n)
	if o is None:
		print('Error: not found')
		return 'no'
	return o
def getflt(flt):
	print(prompt(flt))
	z=_getflt(flt)
	while z=='no':
		z=_getflt(flt)
	return z
def _getfile(ext='',mustexist=1):
	f=input('File:')
	if not f.strip():
		print('Error: type any file path')
		return None
	if not os.path.exists(f) and mustexist:
		print('Error: not exist')
		return None
	if os.path.isdir(f):
		print('Error: is a directory')
		return None
	if not f.endswith(ext):
		print('Error: invalid format')
		return None
	return f
def getfile(ext='',mustexist=1):
	u=''
	while not u:
		u=_getfile(ext,mustexist)
	return u