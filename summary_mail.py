from datetime     import datetime, timedelta
from shared.entry import __handle_entry__, Args
from shared.api   import API
from shared       import env, sep

class Program:

    def __init__(self):
        
        self.api = API()

    def __ratio(self, a: int, b: int) -> float: 
        
        return f"{a / b * 100:.1f}" if b else 0

    def assemble(self, template: dict, summary: dict) -> dict:
        
        assemblage  = {}
        stats       = summary["stats"]
        metadata    = API.serialize_name(summary["name"])

        # template
        assemblage["{subject}"] = template["subject"]
        assemblage["{sender}"]  = template["envelope_sender"]
        
        # stats
        assemblage["{total}"]     = stats["total"]
        assemblage["{sent}"]      = stats["sent"]
        assemblage["{clicked}"]   = stats["clicked"]
        assemblage["{submitted}"] = stats["submitted_data"]

        # ratial
        assemblage["{clicked->%}"] = \
            self.__ratio(stats["clicked"], stats["total"])
        assemblage["{submitted->%}"] = \
            self.__ratio(assemblage["{submitted}"], stats["total"])
        assemblage["{clicksubbed->%}"] = \
            self.__ratio(assemblage["{submitted}"], stats["clicked"])

        # temporal
        assemblage["{variant}"] = metadata["variant"]
        assemblage["{last}"]    = (datetime(1, 1, 1, 9) + timedelta(
            seconds=stats["total"] * 4)).strftime("%H:%M")

        return assemblage

    def __main__(self, args: Args):
        
        template = self.api.get(f"campaigns/{args.map['id']}")["template"]
        summary  = self.api.get(f"campaigns/{args.map['id']}/summary") 
        message  = open(sep.join([env["root"], "assets", 
            "mails", args.map["variant"] + '.txt'])).read()
        
        for key, value in self.assemble(template, summary).items():
            message = message.replace(key, str(value))

        if ((hour := datetime.now().hour) < 12):
            greeting = "Goedemorgen {to},\n\n"
        elif (hour < 18):
            greeting = "Goedemiddag {to},\n\n"
        else:
            greeting = "Goedenavond {to},\n\n"

        # output
        print(greeting.replace("{to}", 
            args.map["recipient"]) + message, end='')

__handle_entry__(    
    {__name__: Program}, 
    (
        "id",        # the ID of the campaign
        "recipient", # who to greet at the start of the mail
        "variant",   # type of message (begin, update, end)
    )
)