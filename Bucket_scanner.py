import requests

class BucketScanner:
    """ Classe de l'outils qui va scanner les buckets

        Args :
        nom_bucket(string) : le nom du bucket que l'on veut analyser
        nom_fichier(string) : le nom du fichier lier au bucket que l'on veut analyser
        ecriture (boolean) : si l'on souhaite essayer d'ecrire ou juste essayer de lire
 
    """

    def __init__(self, nom_bucket,nom_fichier = "",ecriture = False):
        self.nom_bucket= nom_bucket
        self.nom_fichier =nom_fichier
        self.ecriture = ecriture
        self.url = self.creer_url()
        
        

    def creer_url(self):
        """Fonction qui créé le lien URL a la base de la recherche
        """
        url = "https://"+ self.nom_bucket +".s3.eu-central-1.amazonaws.com/" + self.nom_fichier 
        return url

    def check_lecture(self):
        """ Fonction qui essayer de lire sur le bucket
        """
        if(not self.ecriture):
            reponse = requests.get(self.url)
            if (reponse.status_code == 403 ):
                return"Le fichier est sécurisé on ne peut pas le lire."
            elif (reponse.status_code == 404 ):
                return"Le fichier n'existe pas."
            elif (reponse.status_code == 200 ):
                return"Le fichier est lisible facilement."
            else:
                return"Le status retourné est innatendu."

    def check_ecriture(self):
        """ Fonction qui essayer d'écrire sur le bucket
                """
        if(self.ecriture):
            reponse = requests.put(self.url, "Essai d'ecriture dans le fichier!")
            if (reponse.status_code == 200 ) or (reponse.status_code == 204 ) :
                return "Le fichier n'est pas sécurisé on peut ecrire dessus!"
            elif (reponse.status_code == 404 ):
                return"Le fichier n'existe pas."
            elif (reponse.status_code == 403 ):
                return"Le fichier est sécurisé on ne peut pas ecrire dessus."
            else:
                return"Le status retourné est innatendu." + str(reponse.status_code)

    def scanne(self):
        """En fonction de si l'tilisateur veut lire ou écrire la fonction scanne le bucket
        """
        if(self.ecriture):
            return self.check_ecriture()
        else:
            return self.check_lecture()

def main():
    scanner = BucketScanner("[REMOVED]","lecture.pdf")
    print ('test1 lecture du fichier lecture.pdf')
    print(scanner.scanne())

    scanner = BucketScanner("[REMOVED]", "ecriture.txt", True)
    print ('test2 ecriture du fichier')
    print(scanner.scanne())

    scanner = BucketScanner("[REMOVED]" )
    print ('test3 lecture de rien')
    print(scanner.scanne())


if __name__ == "__main__":
    main()