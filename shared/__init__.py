from os import sep

env = {
    "api": {
        "host" : "127.0.0.1",
        "port" : 3333,
        "key"  : open("shared/.key", 'r').read()
    },

    "root" : sep.join(__file__.split(sep)[:-2])
}