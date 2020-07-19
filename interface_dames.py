# Auteurs: À compléter

from tkinter import Tk, Label, NSEW, Menu, Button, Frame, LEFT, filedialog, colorchooser
from canvas_damier import CanvasDamier
from partie import Partie
from position import Position



class FenetrePartie(Tk):
    """Interface graphique de la partie de dames.

    Attributes:
        partie (Partie): Le gestionnaire de la partie de dame
        canvas_damier (CanvasDamier): Le «widget» gérant l'affichage du damier à l'écran
        messages (Label): Un «widget» affichant des messages textes à l'utilisateur du programme

        TODO: AJOUTER VOS PROPRES ATTRIBUTS ICI!
    """

    def __init__(self):
        """Constructeur de la classe FenetrePartie. On initialise une partie en utilisant la classe Partie du TP3 et
        on dispose les «widgets» dans la fenêtre.
        """




        # Appel du constructeur de la classe de base (Tk)
        super().__init__()

        # La partie
        self.partie = Partie()

        # Création du canvas damier.
        self.canvas_damier = CanvasDamier(self, self.partie.damier, 60)
        self.canvas_damier.grid(sticky=NSEW)
        self.canvas_damier.bind('<Button-1>', self.selectionner)

        # Ajout d'une étiquette d'information.
        self.messages = Label(self)
        self.messages.grid()

        # Nom de la fenêtre («title» est une méthode de la classe de base «Tk»)
        self.title("Jeu de dames")

        # Truc pour le redimensionnement automatique des éléments de la fenêtre.
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.messages['text'] = 'Bonjour'

    def selectionner(self, event):
        """Méthode qui gère le clic de souris sur le damier.

        Args:
            event (tkinter.Event): Objet décrivant l'évènement qui a causé l'appel de la méthode.

        """

        # On trouve le numéro de ligne/colonne en divisant les positions en y/x par le nombre de pixels par case.
        ligne = event.y // self.canvas_damier.n_pixels_par_case
        colonne = event.x // self.canvas_damier.n_pixels_par_case
        position = Position(ligne, colonne)

        # On récupère l'information sur la pièce à l'endroit choisi.
        piece = self.partie.damier.recuperer_piece_a_position(position)

        if piece is None:
            self.messages['foreground'] = 'red'
            self.messages['text'] = 'Erreur: Aucune pièce à cet endroit.'
        else:
            self.messages['foreground'] = 'black'
            self.messages['text'] = 'Pièce sélectionnée à la position {}.'.format( position)

        # TODO: À continuer....

        #Creation du menu
        menu = Menu(self)
        self.config(menu=menu)

        def doNothing():
            self.messages['text'] = 'Nouvelle partie commence'

        def quitter():
            self.quit

        #Fonctions optionelles

        subMenu = Menu(menu)
        subMenuOptions = Menu(menu)

        #Fonctions optionelles
        #1. Option de lire les règlements du jeu
        def lireInstructions():
            instruction = Tk()
            instruction.title("Instructions")



            #Ecrire les instructions sur l'interface
            # Un Frame est utiliser pour mieux organiser la page
            instruction_1 = "-> Le joueur avec les pièces blanches commence en premier"
            instruction_2 = "-> Une pièce de départ est appelée unpion, et peut se déplacer en diagonalevers l’avant " \
                            "\n(vers le haut pour les blancs, vers le bas pour les noirs)."
            instruction_3 = "-> Une case doit être libre pourpouvoir s’y déplacer "
            instruction_4 = "-> Lorsqu’un pion atteint le côté opposé du plateau, il devient une dame."
            instruction_5 = "-> Une dame a la particularité qu’elle peut aussi se déplacer vers l’arrière (toujours en diagonale)"
            instruction_6 ="-> Une prise est l’action de «manger» une pièce adverse. Elle est effectuée en sautant par-dessus " \
                           "\nla pièce adverse, toujours en diagonale,vers l’avant ou l’arrière. "
            instruction_7 = "-> On nepeut sauter par-dessus qu’une pièce adverse à la fois : il faut donc que la case d’arrivéesoit libre"
            instruction_8 = "-> Après une prise, le joueur courant peut effectuer une (ou plusieurs) prise(s) supplé-mentaire(s) " \
                            "\nen utilisant la même pièce"
            instruction_9 = "-> Lors du tour d’un joueur, si celui-ci peut prendre une pièce ennemie, " \
                            "\nil doit absolumentle faire (on ne peut pas déplacer une pièce s’il était possible d’effectuer une prise)"
            instruction_10 = "-> On déduit des deux dernières règles que lorsqu’un joueur commence son tour et prendune pièce adverse, " \
                             "\ns’il peut continuer son tour en continuant de prendre des pièces adverses avec la même pièce, il doit le faire\n"

            instruction_message = instruction_1 + "\n\n" + instruction_2 + "\n\n" \
                                  + instruction_3 + "\n\n" + instruction_4 + "\n\n" + instruction_5 \
                                + "\n\n" + instruction_6 + "\n\n" + instruction_7 +"\n\n" + instruction_8 \
                                + "\n\n" + instruction_9 + "\n\n" +instruction_10

            frame = Frame(instruction)
            frame.pack()
            label_instruction = Label(frame, text=instruction_message, justify=LEFT)

            label_instruction.pack(side="left")

            instruction.mainloop()


        menu.add_cascade(label="Fichier", menu=subMenu)
        subMenu.add_command(label="Nouvelle partie", command=doNothing)
        def sauvegarder():
            filedialog.asksaveasfilename()


        subMenu.add_separator()

        subMenu.add_command(label="Sauvegarder", command=sauvegarder)
        subMenu.add_separator()
        subMenu.add_command(label="Quitter", command=quitter)

        menu.add_cascade(label="Options", menu=subMenuOptions)

        # Permettre de changer le thème (couleurs)
        def changerCouleur():
            color = colorchooser.askcolor()
            color_name = color[1]
            self.configure(background=color_name)

        subMenuOptions.add_command(label="Couleur", command=changerCouleur)
        menu.add_command(label="Instructions", command=lireInstructions)



    def piece_peuvent_se_deplacer_sur_damier(self):
        self.partie.tour().grid(CanvasDamier)

        # TODO: À continuer....
        print(self.partie.damier)
        print(self.liste_position)
        print(self.partie.demander_positions_deplacement())
        self.canvas_damier.actualiser()





if __name__ == '__main__':
    # Point d'entrée principal du TP4.


    fenetre = FenetrePartie()
    fenetre.mainloop()
