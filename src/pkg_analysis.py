import pkg_list as pl


def pkf_list(pkg):
    return dir(pkg)


print(pkf_list("pandas"))
