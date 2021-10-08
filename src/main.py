import os
import re
import sys
import pkg_list as pl
import inspector as ins
import pkg_analysis as pa

def main_helper(key, foo_di):
    p = os.path.abspath(os.getcwd())
    p += "/pckgs_srcode/mypckgs.txt"
    try:
        f = open(p, "r")
    except:
        f = open(p, "w")

    for line in f:
        wordList = re.sub("[^\w]", " ",  line).split()
        for word in wordList:
            if word in foo_di[key]:
                foo_di[key][word] += 1

    print(foo_di)

    f.close()


def main():
    args = sys.argv[1:]
    li = pl.library_lister()
    mods = ins.pkg_importer(li)
    ins.package_srccode_extractor(mods)
    foo_li = pa.pkg_list(args[0])

    main_helper(args[0], foo_li)
    return None


if __name__ == "__main__":
    main()
