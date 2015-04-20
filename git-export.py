#!/usr/bin/env python

import sys
import subprocess
import os
import shutil
import StringIO
# Reference: http://docs.python.org/library/optparse.html
from optparse import OptionParser

parser = OptionParser();
parser.add_option("-f", "--from-revision", dest="start", default="", type="string", help="Starting revision/commit")
parser.add_option("-t", "--to-revision", dest="end", default="", type="string", help="Last revision/commit that you want to export (optional)")
parser.add_option("-n", "--num-of-revisions", dest="count", default=0, type="int", help="The number of revisions start from the last revision (this will take priority than --from-revision)")

parser.add_option("-o", "--output", dest="destination", default=".", help="Output dir where you want to export")

(options, args) = parser.parse_args(sys.argv)

def cp(src, dst):
    assert not os.path.isabs(src)
    if not os.path.exists(r'' + src):
        print "File '%s' not exists, skip..." % src
        return
    dstdir = os.path.join(dst, os.path.dirname(src))
    if not os.path.exists(dstdir):
        os.makedirs(dstdir)
    dstfile = os.path.join(dst, src)
    shutil.copyfile(src, dstfile)
    print "Copied: "+src+" -> "+dstfile

def main():
    try:
        if options.count > 0:
            p = subprocess.Popen(['git', 'diff', '--name-only', 'HEAD~%d' % options.count], stdout=subprocess.PIPE)
        elif options.end == "":
            p = subprocess.Popen(['git', 'diff', '--name-only', options.start], stdout=subprocess.PIPE)
        else:
            p = subprocess.Popen(['git', 'diff', '--name-only', options.start, options.end], stdout=subprocess.PIPE)

        out, err = p.communicate()
        files = StringIO.StringIO(out)
        for f in files:
            cp(f.rstrip(), options.destination.rstrip('/') + '/git-export')
    except Exception, e:
        print "Couldn't do it: %s" % e
        #parser.print_help()
    sys.exit(0)

if __name__ == "__main__":
    main()
