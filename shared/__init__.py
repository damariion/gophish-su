from os import sep

env = {
    
    "api": {
        "host" : "gophish.lbvd.nl",
        "port" : 3333,
        "key"  : open("shared/.key", 'r').read()
    },

    "root" : sep.join(__file__.split(sep)[:-2])
}