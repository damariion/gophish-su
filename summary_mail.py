from datetime     import datetime, timedelta
from shared.entry import __handle_entry__, Args
from shared.api   import API

TEMPLATES = {
    
    "start": (
        "De PhishLink {variant}-simulatie van {month} zal zoals gepland {date} van start gaan. Hierbij de details:\n"
        "\n"
        "- Om 09:00 uur wordt er om de 4 seconden een e-mail gestuurd. Dat betekent dat rond {last} uur de laatste e-mail verzonden moet zijn. In totaal zijn het namelijk {total} e-mails.\n"
        "- Morgen zal ik een update geven over hoeveel personen er geklikt hebben na de eerste werkdag;\n"
        "- Het onderwerp van de mail is '{subject}' en de afzender is '{sender}';\n"
        "- De simulatie bevat een inlogpagina.\n"
        "\n"
        "Ik hoop jullie hiermee voldoende geïnformeerd te hebben en als er nog vragen zijn dan hoor ik het uiteraard graag."
    ),

    "update": (
        "Hierbij wil ik een update geven over de statistieken van de phishing e-mail na de eerste werkdag:\n"
        "\n"
        "- Er zijn in totaal {sent} e-mails succesvol verzonden.\n"
        "- In totaal hebben er {clicked} medewerkers ({clicked->%}%) op de link in de phishing e-mail geklikt.\n"
        "- Tot slot zijn er {submitted} inloggegevens ingevuld ({submitted->%}%).\n"
        "\n"
        "{review}"
    ),

    "end": (
        "Zojuist heb ik de phishing campagne stopgezet, verdere clicks op de phishing link zullen niet meer geregistreerd worden. "
        "De eindstand van de simulatie is als volgt:\n"
        "\n"
        "- Er zijn in totaal {sent} e-mails succesvol verzonden;\n"
        "- In totaal hebben {clicked} medewerkers ({clicked->%}%) op de link in de phishing e-mail geklikt;\n"
        "- Van de klikkende medewerkers hebben {submitted} medewerkers ({clicksubbed->%}%) inloggegevens ingevuld . Dit is {submitted->%}% van het totaal.\n"
        "\n"
        "De herkenningspunten heb ik verder bijgevoegd in de bijlagen."
    )
}

class Program:

    def __init__(self):
        
        self.api = API()

    def __ratio(self, a: int, b: int) -> float: 
        
        return f"{a / b:.1f}" if b else 0

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
        message  = TEMPLATES[args.map["variant"]]
        
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