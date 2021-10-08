import pkg_resources

def slicer_index(lib_list):
    arr = []
    for lib in lib_list:
        lib_split = lib.split("=")
        arr.append(lib_split[0])

    return arr

def library_lister():
    dist = [str(d).replace(" ","==") for d in pkg_resources.working_set]
    return slicer_index(dist)
