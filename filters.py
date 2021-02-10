import sys
import scipy.io.wavfile as _wav
class _Filter:
	def __init__(self,func):
		self.feed=func
		self.id=0
		self.name=''
	def __repr__(self):
		return f'{self.id}. {self.name}'
def Filter(id,name=''):
	def new_f(func):
		flt=_Filter(func)
		flt.id=id
		flt.name=name
		return flt
	return new_f
class CollectionOfFilters:
	def __init__(self,flt):
		self.__flt=flt[0]
	@property
	def list(self):
		return self.__flt
	def byid(self,id):
		for f in self.list:
			if f.id==id:
				return f
		return None
class Music:
	def __init__(self,rate,data):
		self.rate=rate
		self.data=data
	def copy(self):
		return Music(self.rate,self.data)
def wavread(fname):
	return Music(*_wav.read(fname))
def wavwrite(fout,mus):
	_wav.write(fout,mus.rate,mus.data)
def export(*filters):
	return CollectionOfFilters(list(filters))