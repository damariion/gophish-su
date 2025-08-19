from shared.entry import __handle_entry__, Args
from shared       import env, sep
# from base64       import b64encode

class Program:

    def __init__(self):
        pass

    def __main__(self, args: Args):
        
        with open(sep.join([env["root"], "assets", 
            "pages", "landing", args.map["type"] + '.html'])) as page:
            
            page = page.read()
            
            for holder in ("name", "phone", "email", "logo", "clue"):
                page = page.replace(f"{{{{{holder}}}}}", args.map[holder])

        page = page.replace(r"{{logox}}", args.map["logo"].split('.')[-1])
        page = page.replace(r"{{cluex}}", args.map["clue"].split('.')[-1])

        print(page)

__handle_entry__(
    {__name__: Program},
    (
        "name",  # the name of the client
        "phone", # phone number of the client
        "email", # email of the client
        "logo",  # path to an image of the client's logo
        "clue",  # path to the image of clue(s)
        "type"   # type of landing-page to be generated
    )
)