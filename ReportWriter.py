import json

class ReportWriter:
    """ Classe permettant de créé le rapport d'analyse des buckets.
     
        """

    def __init__(self):
        self.nom_fichier = "rapport.jsonl"
        self.données = {
            'url_bucket' :"",
            'date - heure' : "",
            'lecture' :{},
            'ecriture' :{}
        }

    def write_file(self):
        """Fonction qui écrit les infos d'un bucket dans le fichier rapport.jsonl
        """
        with open(self.nom_fichier , 'a+') as fichier :
            json.dump(self.données, fichier)
            fichier.write('\n')
        self.reset()
        

    def add_infos(self, clé, valeur, section=None):
        """Fonction qui centralise les infos liés à un bucket
        """
        if section == None:
            self.données[clé] = valeur
            return
        self.données[section][clé] = valeur


    def reset(self):
        """Fonction qui reset les données pour analyser un nouveau bucket
        """
        self.données = {
                            'url_bucket' :"",
                            'lecture' :{},
                            'ecriture' :{}
                        }