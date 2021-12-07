def __getattr__(key) :
    mod = __import__(key + "_", globals(), None, [], 1)
    return getattr(mod, key)
