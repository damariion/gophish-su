from shared.entry import __handle_entry__, Args
from shared.api   import API

# for fully featured query (@pd)
import pandas as pd

class Program:

    def __init__(self):
        
        # configuration
        pd.set_option('display.max_rows', None)

        self.api   = API()
        self.cache = {
            key: [] for key in 
            (
                "id", 
                "name", 
                "sent", 
                "opened", 
                "clicked", 
                "submitted", 
                "opened->%", 
                "clicked->%", 
                "submitted->%"
             )
        }

    
    def __ratio(self, a: int, b: int) -> float:

        return f"{a / b * 100:.1f}" if b else 0

    def __main__(self, args: Args):
        
        for campaign in self.api.get("campaigns"):
            
            summary = self.api.get(
                f"campaigns/{campaign['id']}/summary")["stats"]
            
            mapping = {
                
                # meta
                "id"           : campaign["id"],
                "name"         : campaign["name"],
                
                # stats
                "sent"         : summary["sent"],
                "opened"       : summary["opened"],
                "clicked"      : summary["clicked"],
                "submitted"    : summary["submitted_data"],

                # ratios
                "opened->%"    : self.__ratio(
                    summary["opened"], summary["sent"]),
                "clicked->%"   : self.__ratio(
                    summary["clicked"], summary["sent"]),
                "submitted->%" : self.__ratio(
                    summary["submitted_data"], summary["sent"])
            }

            for key, value in mapping.items():
                self.cache[key].append(value)

        data  = pd.DataFrame(self.cache).set_index("id")
        query = args.map["query"]
        
        print(data if query == '*' else data.query(query, engine="python"))

__handle_entry__(
    {__name__: Program}, 
    (
        "query", # pandas query on the DataFrame
    )
)