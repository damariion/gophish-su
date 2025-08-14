from shared.entry import __handle_entry__, Args
from pandas       import read_csv

class Program:

    def __init__(self):     
        
        ...

    def __main__(self, args: Args):
        
        with open(args.map["events"], 'r') as file:
            self.data = read_csv(file)

        print(self.data)

__handle_entry__(
    {__name__: Program},
    (
        "events", # exported raw events (from Gophish)
    )
) 