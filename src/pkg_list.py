import pkg_resources


def slicer_index(lib_list):
    """
    Keeps only the name of the package, removing the version number
    """
    arr = []
    for lib in lib_list:
        lib_split = lib.split("=")
        arr.append(lib_split[0])

    return arr


def library_lister():
    """
    List all the packages used in this project
    """
    dist = [str(d).replace(" ", "==") for d in pkg_resources.working_set]
    return slicer_index(dist)
