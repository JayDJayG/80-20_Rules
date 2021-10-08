import os
import sys
import pkg_list as pl
import inspector as ins
import pkg_analysis as pa


def main_helper(foo_di):
    p = os.path.abspath(os.getcwd())
    p += "/pckgs_srcode/mypckgs.txt"
    print(foo_di)
    print(p)
    try:
        f = open(p, "r")
    except:
        f = open(p, "w")
    file_content = f.read()
    f.close()


def main():
    args = sys.argv[1:]
    li = pl.library_lister()
    mods = ins.pkg_importer(li)
    ins.package_srccode_extractor(mods)
    foo_li = pa.pkg_list(args[0])

    print(main_helper(foo_li))
    return None


if __name__ == "__main__":
    main()
