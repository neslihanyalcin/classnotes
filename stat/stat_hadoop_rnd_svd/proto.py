from mrjob.job import MRJob
import re, sys, struct, cStringIO
import cPickle

try:
    import simplejson as json  # preferred because of C speedups
    json  # quiet "redefinition of unused ..." warning from pyflakes
except ImportError:
    import json  # built in to Python 2.6 and later

class StructProtocol(object):

    def read(self, line):
        raw_key, raw_value = line.split('\t', 1)
        return (self._loads(raw_key), self._loads(raw_value))

    def write(self, key, value):
        return '%s\t%s' % (self._dumps(key),self._dumps(value))
    
    def _loads(self, value):
        return cPickle.loads(value.decode('string_escape'))
        #sio = cStringIO.StringIO()

    def _dumps(self, value):
        return cPickle.dumps(value).encode('string_escape')


WORD_RE = re.compile(r"[\w']+")

class MRWordFreqCount(MRJob):
    
    INTERNAL_PROTOCOL = StructProtocol

    def mapper(self, _, line):
        for word in WORD_RE.findall(line):
            yield (word.lower(), 1)

    def reducer(self, word, counts):
        yield (word, sum(counts))

if __name__ == '__main__':
    MRWordFreqCount.run()
    
