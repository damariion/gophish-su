from shared.entry import __handle_entry__, Args
from shared.api   import API
from pandas       import DataFrame

class Program:

    def __init__(self):
        
        self.api   = API()
        self.cache = \
            {
                "id"        : [],
                "name"      : [],
                "sender"    : [],
                "sent"      : [],
                "opened"    : [],
                "clicked"   : [],
                "submitted" : [],
            }
    
    def __ratio(self, a: int, b: int) -> float:

        return f"{a / b * 100:.1f}" if b else 0

    def __main__(self, args: Args):
        
        for campaign in self.api.get("campaigns"):
            
            summary = self.api.get(
                f"campaigns/{campaign['id']}/summary")["stats"]
            
            mapping = {
                "id"        : campaign["id"],
                "name"      : campaign["name"],
                "sender"    : campaign["smtp"]["from_address"],
                "sent"      : summary["sent"],
                "opened"    : f"{summary["opened"]} "
                f"({self.__ratio(summary["opened"], summary["sent"])}%)",
                "clicked"   : f"{summary["clicked"]} "
                f"({self.__ratio(summary["clicked"], summary["sent"])}%)",
                "submitted" : f"{summary["submitted_data"]} "
                f"({self.__ratio(summary["submitted_data"], summary["sent"])}%)"
            }

            for key, value in mapping.items():
                self.cache[key].append(value)

        data  = DataFrame(self.cache).set_index("id")
        query = args.map["query"]
        
        print(data if query == '*' else data.query(query))

__handle_entry__(
    {__name__: Program}, 
    (
        "query", # pandas query on the DataFrame
    )
)