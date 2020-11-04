import json

def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(config=None)
def get_config():
    if get_config.config is None:
        get_config.config = json.load(open("config.json", 'r'))
    return get_config.config
    