from shared.entry import __handle_entry__, Args
from pandas       import read_csv

class Program:

    def __init__(self):     
        
        self.emails = []
        self.syntax = {
            "opened": "Opened",
            "clicked": "Clicked Link",
        }

    def __main__(self, args: Args):
        
        with open(args.map["events"], 'r') as file:
            self.data = read_csv(file)

        for event in self.data.values:
            
            if  event[3] == args.map["type"] \
            and event[1] not in self.emails:
                
                self.emails.append(event[1])
                
        print(*self.emails, sep='\n')


__handle_entry__(
    {__name__: Program},
    (
        "events", # exported raw events (from Gophish)
        "type",   # type of event to filter (clicked, submitted, etc)
    )
) 