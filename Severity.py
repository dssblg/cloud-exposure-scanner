from enum import Enum
class Severity(Enum):
    """ Classe qui defini si le bucket est vulnerable ou non """

    SAFE = "safe"

    VULNERABLE= "vulnerable"

