import inspect
import os


def pkg_importer(li):
    """
    Import all the packages found within the environment
    """
    modules = {}
    for x in li:
        try:
            modules[x] = __import__(x)
        except ImportError:
            pass
    return modules


def package_srccode_extractor(mods):
    """
    Writes all the source code to a file
    """
    p = os.path.abspath(os.getcwd())
    p += "/pckgs_srcode/mypckgs.txt"

    try:
        f = open(p, "x")
    except:
        f = open(p, "w")

    for pkg in mods:
        f.write(inspect.getsource(mods[pkg]))

    f.close()


def pckgs_to_dict(mods):
    d = dict()
    for pck in mods:
        pass
