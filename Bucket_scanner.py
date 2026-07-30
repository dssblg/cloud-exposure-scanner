import requests
import ReportWriter
import json
from Severity import Severity
from datetime import datetime

class BucketScanner:
    """ Classe de l'outils qui va scanner les buckets

        Args :
        nom_bucket(string) : le nom du bucket que l'on veut analyser
        nom_fichier(string) : le nom du fichier lier au bucket que l'on veut analyser
        ecriture (boolean) : si l'on souhaite essayer d'ecrire ou juste essayer de lire
 
    """

    def __init__(self, bucket_name,file_name = ""):
        self.bucket_name= bucket_name
        self.file_name =file_name
        self.reporter = ReportWriter.ReportWriter()
        self.url = self.create_url()
        self.reporter.add_infos('url_bucket', self.url)
        self.reporter.add_infos('date - heure', datetime.now().strftime('%d/%m/%Y - %H:%M:%S'))
        
        

    def create_url(self):
        """Fonction qui créé le lien URL a la base de la recherche
        """
        url = "https://"+ self.bucket_name +".s3.eu-central-1.amazonaws.com/" + self.file_name 
        return url

    def check_read(self):
        """ Fonction qui essayer de lire sur le bucket
        """
        try:
            reponse = requests.get(self.url, timeout=5)
        except requests.RequestException as e:
            print(e)
            return
        self.reporter.add_infos('status', reponse.status_code, 'lecture')
        if (reponse.status_code == 403 ):
            res = "Le bucket est sécurisé on ne peut pas le lire."
            self.reporter.add_infos('securité', Severity.SAFE.value, 'lecture')
        elif (reponse.status_code == 404 ):
            res = "Le bucket n'existe pas."
            self.reporter.add_infos('securité', Severity.SAFE.value, 'lecture')
        elif (reponse.status_code == 200 ):
            res = "Le bucket est lisible facilement."
            self.reporter.add_infos('securité', Severity.VULNERABLE.value, 'lecture')
        else:
            res = "Le status retourné est innatendu " + str(reponse.status_code)
            self.reporter.add_infos('securité', Severity.SAFE.value, 'lecture')
        self.reporter.add_infos('test_lecture', res, 'lecture')
        

    def check_write(self):
        """ Fonction qui essayer d'écrire sur le bucket
        """
        try:
            reponse = requests.put(self.url, "Essai d'ecriture dans le bucket!", timeout=5)
        except requests.RequestException as e:
            print(e)
            return
        self.reporter.add_infos('status', reponse.status_code, 'ecriture')
        if (reponse.status_code == 200 ) or (reponse.status_code == 204 ) :
            res = "Le bucket n'est pas sécurisé on peut ecrire dessus!"
            self.reporter.add_infos('securité', Severity.VULNERABLE.value, 'ecriture')
        elif (reponse.status_code == 404 ):
            res = "Le bucket n'existe pas."
            self.reporter.add_infos('securité', Severity.SAFE.value, 'ecriture')
        elif (reponse.status_code == 403 ):
            res = "Le bucket est sécurisé on ne peut pas ecrire dessus."
            self.reporter.add_infos('securité', Severity.SAFE.value, 'ecriture')
        else:
            res = "Le status retourné est innatendu " + str(reponse.status_code)
            self.reporter.add_infos('securité', Severity.SAFE.value, 'ecriture')
        self.reporter.add_infos('test_ecriture', res, 'ecriture')

    def scanne(self):
        """En fonction de si l'tilisateur veut lire ou écrire la fonction scanne le bucket et ecrit l'annalyse dans le fichier rapport.jsonl
        """
        self.check_write()
        self.check_read()
        self.reporter.write_file()

def main():
    with open("test_buckets.json", "r") as fichier:
        buckets = json.load(fichier)

    for bucket in buckets:
        print(f"Scan bucket : {bucket['bucket']}")
        scanner = BucketScanner( bucket["bucket"], bucket["file"])
        scanner.scanne()


if __name__ == "__main__":
    main()