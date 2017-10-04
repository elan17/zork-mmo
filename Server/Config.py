import glob
from logging import warning, info


class Languages:

    def __init__(self, root="./Langs/*"):
        self.languages = {}
        files = glob.glob(root)
        for x in files:
            idioma = x.split("/")[-1]
            info("Cargando idioma: " + idioma)
            self.languages[idioma] = Archivo(x)

    def get_option(self, option, language, advise_non_availability=True):
        try:
            return self.languages[language].get_option(option)
        except KeyError:
            if advise_non_availability:
                warning("El token de idioma \""+option+"\" no esta traducido para el idioma \""+language+"\"")
            return "UNTRANSLATED_TOKEN "+option

    def get_languages(self):
        lista = list(self.languages.keys())
        returneo = []
        for x in lista:
            if "HIDDEN" not in x:
                returneo.append(x)
        return returneo


class Archivo:

    def __init__(self, entrada):
        self.data = {}
        with open(entrada, "r") as f:
            arch = f.readlines()
            working = ""
            for linea in arch:
                if linea == "\n" or linea[0] == "#":
                    continue
                if "=" in linea:
                    tmp = linea.split("=")
                    working = tmp[0].split(" ")[0]
                    if working in self.data:
                        raise ValueError("Corrupted file. Key " + working + " repeated")
                    self.data[working] = tmp[1].split("\n")[0]
                else:
                    self.data[working] += "\n" + linea.split("\n")[0]

    def get_option(self, option):
        return self.data[option]


if __name__ == "__main__":
    idiomas = Languages()
    print(idiomas.get_option("descripcion", "es_ES"))
