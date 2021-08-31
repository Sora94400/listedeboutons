from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class Exemple(BoxLayout):
    def build(self):
        self.orientation = 'vertical'
        self.spacing = 20
        self.Mes_Boutons()


    def Mes_Boutons(self):
        # On cree une liste pour les boutons:
        self.Liste_Boutons = []
        # On fait tourner une boucle pour creer 10 boutons:
        for i in range(0, 10):
            # On ajoute un bouton dans la liste:
            self.Liste_Boutons.append(Button())
            # On lui donne un texte qui depend de i:
            self.Liste_Boutons[i].text = "Bouton " + str(i)
            # On lui donne un identite "id" pour le retrouver hors de la liste:
            self.Liste_Boutons[i].id = "B" + str(i)
            # On lui associe une fonction:
            self.Liste_Boutons[i].bind(on_press=self.Une_Fonction_Bouton)
            # On ajoute le bouton au layout principal:
            self.add_widget(self.Liste_Boutons[i])
        # On ajoute une couleur de fond au dernier bouton:
        self.Liste_Boutons[9].background_color = [0, 1, 0, 1]

    def Une_Fonction_Bouton(self, instance):
# instance correspond au bouton qui vient d'etre active:
# On change la couleur des neuf premiers boutons:
        for i in range(0, 9):
            self.Liste_Boutons[i].background_color = [0.5, 0.5, 0.5, 1]  #En gris
# On change la couleur du bouton active si ce n'est pas le dernier:
        if instance.id != "B9":
            instance.background_color = [1, 0, 0, 1] # En rouge
        instance.text= 'Stage'

class Exemple_De_Liste_BoutonsApp(App):

    def build(self):
        root = Exemple()
        root.build()
        return root
if __name__ == '__main__':
    Exemple_De_Liste_BoutonsApp().run()
