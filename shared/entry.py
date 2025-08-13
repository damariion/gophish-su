from sys         import argv
from argparse    import ArgumentParser

class Args:

    count  : int = len(argv)
    vector : tuple[str] = argv

    def __init__(self, flags: tuple[str]):
        
        parser = ArgumentParser()
        
        for flag in flags:
            
            parser.add_argument(

                f"-{flag[0]}",
                f"--{flag}",
                
                action   = "store",
                required = 1
            
            )

        self.map = dict(
            parser.parse_args()._get_kwargs())

def __handle_entry__(entry: dict[str: object], flags: tuple[str]) -> None:

    modus = [*entry.keys()][0]
    entry = [*entry.values()][0]

    if modus == "__main__":

        instance = entry()
        instance.__main__(Args(flags))
        del instance