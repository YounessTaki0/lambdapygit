from pathlib import Path

file = Path("./Es file_sorter/log.txt")

class EstensioneErrata(Exception):
    def __init__(self):
        super().__init__("Estensione non supportata, non è possibile decidere la cartella di destinazione.")
class Sorter():
    def __init__(self):
        self.lista_log = []

    def cartella_estensione(self, path):
        controllo = False
        documenti = ['txt', 'docx', 'pdf', 'doc']
        immagini = ['png', 'jpeg', 'jpg', 'gif', 'bmp']
        video = ['mp4', 'mkv', 'mov', 'avi']
        audio = ['mp3', 'aac', 'wav', 'flac', 'm4a']
        file = Path(path)
        nome = file.name
        path_cartella = path.replace(nome, "")
        estensione = file.suffix.replace(".", "")

        if(estensione in documenti):
            path_cartella += "Documenti"
            controllo = True
        if(estensione in immagini):
            path_cartella += "Immagini"
            controllo = True
        if(estensione in video):
            path_cartella += "Video"
            controllo = True
        if(estensione in audio):
            path_cartella += "Audio"
            controllo = True

        cartella = Path(path_cartella)
        
        if(controllo):
            cartella.mkdir(exist_ok=True)
        
        if(nome == "main.py"):
            return path_cartella, True
        else:
            return path_cartella, controllo
    
    def ordina(self, path):
        cartella = Path(path)
        for file in cartella.iterdir():
            file_path = f"{path}/{file.name}"
            path_cartella, controllo = self.cartella_estensione((file_path))
            c = Path(path_cartella)
            if(not controllo):
                print(f"ERRORE {file.name} --> Estensione non supportata")
                self.lista_log.append(f"ERRORE {file.name} --> Estensione non supportata")
            elif(file.name != "main.py" and file.name != "log.txt"):
                file.rename(c / file.name)
                print(f"SUCCESS {file.name} --> {path_cartella}")
                self.lista_log.append(f"SUCCESS {file.name} --> {path_cartella}")
    
    def to_log(self):
        return self.lista_log
    
sorter = Sorter()
#sorter.cartella_estensione("./Es file_sorter/sium.txt")
sorter.ordina("./Es file_sorter")

with file.open("w", encoding="utf-8") as file_log:
    lista_log = (sorter.to_log())
    for i in lista_log:
        file_log.write(f"{i}\n")