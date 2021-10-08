def pkg_list(pkg):
    """
    Return dict() filled with name of function and initialized at 0 ready for count
    """
    d = dict()
    d[pkg] = {}

    for foo in dir(__import__(pkg)):
        if foo.startswith("_"):
            pass
        else:
            d[pkg][foo] = 0

    return d
