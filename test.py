
from tkinter import Tk, Label, Button, Frame, N, S, E, W, FLAT, RAISED, SUNKEN, GROOVE, RIDGE, Entry, DISABLED, NORMAL, Canvas, messagebox, filedialog, colorchooser, LabelFrame


class MonApplication(Tk):
    def __init__(self):
        super().__init__()
        mon_frame = LabelFrame(self, borderwidth=3, relief=RIDGE, text="Contrôles reliés")
        mon_frame.grid(row=1, column=0)

        self.title("Mon application")

        self.mon_label = Label(mon_frame, text="Ceci est une étiquette de texte", padx=10, pady=20)
        self.mon_label.grid()

        self.mon_entree = Entry(mon_frame, show='*')
        self.mon_entree.grid()

        self.autre_bouton = Button(mon_frame, text="Autre bouton", command=self.ecrire_dans_etiquette)
        self.autre_bouton.grid()

        # Insérer les widgets ici...
        self.mon_bouton = Button(self, text="Bouton!", command=self.afficher_message)
        self.mon_bouton.grid(row=0, column=0, sticky=W+E)

        mon_deuxieme_bouton = Button(self, text="Bouton2!", command=self.changer_texte_du_bouton)
        mon_deuxieme_bouton.grid(row=1, column=1, sticky=S)

        self.entree_canevas = Entry(self)
        self.entree_canevas.grid(columnspan=2)

        self.canevas = Canvas(self, width=400, height=400, background="light grey")
        self.canevas.grid(columnspan=2)
        self.canevas.bind("<Button-1>", self.dessiner_ovale)
        self.canevas.bind("<B1-Motion>", self.dessiner_ovale)

        self.canevas.bind("<Button-3>", self.afficher_texte)

    def changer_texte_du_bouton(self):
        self.mon_entree["state"] = NORMAL
        self.autre_bouton["state"] = NORMAL

    def afficher_message(self):
        # resultat = messagebox.askyesno("Message!", "Ceci est un message!")
        # print(resultat)
        resultat = filedialog.askopenfilename(title="Ouvrir...", filetypes=[("Fichiers Python", "*.py")])
        if resultat != "":
            f = open(resultat)
            for ligne in f.readlines():
                print(ligne)
            f.close()

    def ecrire_dans_etiquette(self):
        self.mon_label["text"] = self.mon_entree.get()
        self.mon_entree["state"] = DISABLED
        self.autre_bouton["state"] = DISABLED

    def dessiner_ovale(self, evenement):
        self.canevas.create_oval(evenement.x - 5, evenement.y - 5, evenement.x + 5, evenement.y + 5, width=2, fill='red')

    def afficher_texte(self, evenement):
        self.canevas.create_text(evenement.x, evenement.y, text=self.entree_canevas.get(), font=("DejaVu Sans", 16))



if __name__ == '__main__':
    app = MonApplication()
    app.mainloop()