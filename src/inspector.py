import inspect
import pkg_list as pl


def pkg_importer():
    pck_list = pl.library_lister()
    modules = {}
    for x in pck_list:
        try:
            modules[x] = __import__(x)
        except ImportError:
            pass
    return modules


def package_foos():
    mods = pkg_importer()
    d = dict()

    for pkg in mods:
        d[pkg] = inspect.getsource(mods[pkg])

    return d


real = package_foos()
print(real)
# print(real)
# help(pck_list[0])
# source_DF =

# print(source_DF)
