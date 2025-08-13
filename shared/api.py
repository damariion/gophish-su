from shared   import env
from json     import loads
from requests import get

from contextlib import redirect_stderr

class API:

    def __init__(self):
        
        self.host = env["api"]["host"]
        self.port = env["api"]["port"]
        self.key  = env["api"]["key"]

        self.endp = f"https://{self.host}:{self.port}/api"

    def get(self, path: str) -> ...:
        
        with redirect_stderr(None):
            
            response = get(
                verify  = 0,
                url     = f"{self.endp}/{path}",
                headers = {"Authorization": self.key}, 
            )
        
        return loads(response.text)
    
    @staticmethod
    def serialize_name(name: dict) -> dict:

        client, template, serial = map(str.strip, name.split("::"))
        code, variant, difficulty = serial[:4], serial[-2], serial[-1] 

        return {
            
            "client"   : client,
            "template" : template,
            "code"     : int(code),
            
            "variant": {
                'p': "Plus",
                'b': "Basic",
                'c': "Continu",
            }[variant.lower()],
            
            "difficulty": {
                0: "makkelijk",
                1: "gemiddeld",
                2: "moeilijk",
                3: "zeer moeilijk"
            }[int(difficulty)]

        }
