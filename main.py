import cli
from eff import flt
import filters
print('Input file')
i=cli.getfile('.wav')
s=filters.wavread(i)
f=cli.getflt(flt)
s=f.feed(s)
print('Output file')
o=cli.getfile('.wav',mustexist=0)
filters.wavwrite(o,s)