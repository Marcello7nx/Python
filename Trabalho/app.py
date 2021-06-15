import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox as msb
import sqlite3

root = Tk()
root.title("Sistema de Acompanhamento de Notas")
width = 1100
height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(1, 1)
root.iconbitmap("icons/python.ico")
root.config(bg="#1C1C1C")

# ----------------------- Variaveis -----------------------

nome = StringVar()
matricula = IntVar()
disciplina = StringVar()
professor = StringVar()
av1 = DoubleVar()
av2 = DoubleVar()
av3 = DoubleVar()
avd = DoubleVar()
avds = DoubleVar()
av = DoubleVar()
avs = DoubleVar()
cd = DoubleVar()
cadast = None

# ----------------------- Forma -----------------------

def database():
    conn = sqlite3.connect("Notas.db")
    cursor = conn.cursor()
    query = """ CREATE TABLE IF NOT EXISTS 'cadastro' (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT, matricula INT, disciplina TEXT, professor TEXT, av1 DOUBLE, av2 DOUBLE, av3 DOUBLE, avd DOUBLE, avds DOUBLE, av DOUBLE, avs DOUBLE, cd DOUBLE) """
    cursor.execute(query)
    cursor.execute("SELECT * FROM 'cadastro' ORDER BY nome")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()

def submitData():
    if nome.get() == "" or matricula.get() == "" or disciplina.get() == "" or professor.get() == "" or av1.get() == "" or av2.get() == "" or av3.get() == "" or avd.get() == "" or avds.get() == "" or av.get() == '' or avs.get() == '' or cd.get() == '':
        resultado = tk.showwarning("", "Por favor, informe todos os campos.", icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("Notas.db")
        cursor = conn.cursor()
        query = """INSERT INTO 'cadastro' (nome, matricula, disciplina, professor, av1, av2, av3, avd, avds, av, avs, cd) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
        cursor.execute(query, (str(nome.get()), int(matricula.get()), str(disciplina.get()), str(professor.get()), float(av1.get()), float(av2.get()), float(av3.get()), float(avd.get()), float(avds.get()), float(av.get()), float(avs.get()), float(cd.get())))
        conn.commit()
        cursor.execute("SELECT * FROM 'cadastro' ORDER BY nome")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        nome.set("")
        matricula.set("")
        disciplina.set("")
        professor.set("")
        av1.set("")
        av2.set("")
        av3.set("")
        avd.set("")
        avds.set("")
        av.set("")
        avs.set("")
        cd.set("")
        cadast.destroy()

def addData():
    global cadast
    nome.set("")
    matricula.set("")
    disciplina.set("")
    professor.set("")
    av1.set("")
    av2.set("")
    av3.set("")
    avd.set("")
    avds.set("")
    av.set("")
    avs.set("")
    cd.set("")

# ----------------------- 2º - Pagina -----------------------

    cadast = Toplevel()
    cadast.title("Sistema de Cadastro")
    formTitle = Frame(cadast)
    formTitle.pack(side=TOP)
    formContact = Frame(cadast)
    formContact.pack(side=TOP, pady=10)
    width = 500
    height = 500
    screen_width = cadast.winfo_screenwidth()
    screen_height = cadast.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    cadast.geometry("%dx%d+%d+%d" % (width, height, x, y))
    cadast.resizable(1, 1)
    cadast.iconbitmap("icons/python.ico")

# ----------------------- Tabela - Inicio -----------------------

    lbl_title = Label(formTitle, text="Preencher Todos os Requisitos",
                      font=('Helvética', 15), bg='#00BFFF', width=300, pady=7)
    lbl_title.pack(fill=X)
    lbl_nome = Label(formContact, text='Nome', font=('Helvética', 15))
    lbl_nome.grid(row=0, sticky=W)
    lbl_matricula = Label(formContact, text='Matricula', font=('Helvética', 15))
    lbl_matricula.grid(row=1, sticky=W)
    lbl_disciplina = Label(formContact, text='Disciplina', font=('Helvética', 15))
    lbl_disciplina.grid(row=2, sticky=W)
    lbl_professor = Label(formContact, text='Professor', font=('Helvética', 15))
    lbl_professor.grid(row=3, sticky=W)
    lbl_av1 = Label(formContact, text='AV1', font=('Helvética', 15))
    lbl_av1.grid(row=4, sticky=W)
    lbl_av2 = Label(formContact, text='AV2', font=('Helvética', 15))
    lbl_av2.grid(row=5, sticky=W)
    lbl_av3 = Label(formContact, text='AV3', font=('Helvética', 15))
    lbl_av3.grid(row=6, sticky=W)
    lbl_avd = Label(formContact, text='AVD', font=('Helvética', 15))
    lbl_avd.grid(row=7, sticky=W)
    lbl_avds = Label(formContact, text='AVDS', font=('Helvética', 15))
    lbl_avds.grid(row=8, sticky=W)
    lbl_av = Label(formContact, text='AV', font=('Helvética', 15))
    lbl_av.grid(row=9, sticky=W)
    lbl_avs = Label(formContact, text='AVS', font=('Helvética', 15))
    lbl_avs.grid(row=10, sticky=W)
    lbl_cd = Label(formContact, text='CD', font=('Helvética', 15))
    lbl_cd.grid(row=11, sticky=W)

# ----------------------- Entrar - Fonte -----------------------

    nomeEntry = Entry(formContact, textvariable=nome, font=('Helvética', 12))
    nomeEntry.grid(row=0, column=1)
    matriculaEntry = Entry(formContact, textvariable=matricula, font=('Helvética', 12))
    matriculaEntry.grid(row=1, column=1)
    disciplinaEntry = Entry(formContact, textvariable=disciplina, font=('Helvética', 12))
    disciplinaEntry.grid(row=2, column=1)
    professorEntry = Entry(formContact, textvariable=professor, font=('Helvética', 12))
    professorEntry.grid(row=3, column=1)
    av1Entry = Entry(formContact, textvariable=av1, font=('Helvética', 12))
    av1Entry.grid(row=4, column=1)
    av2Entry = Entry(formContact, textvariable=av2, font=('Helvética', 12))
    av2Entry.grid(row=5, column=1)
    av3Entry = Entry(formContact, textvariable=av3, font=('Helvética', 12))
    av3Entry.grid(row=6, column=1)
    avdEntry = Entry(formContact, textvariable=avd, font=('Helvética', 12))
    avdEntry.grid(row=7, column=1)
    avdsEntry = Entry(formContact, textvariable=avds, font=('Helvética', 12))
    avdsEntry.grid(row=8, column=1)
    avEntry = Entry(formContact, textvariable=av, font=('Helvética', 12))
    avEntry.grid(row=9, column=1)
    avsEntry = Entry(formContact, textvariable=avs, font=('Helvética', 12))
    avsEntry.grid(row=10, column=1)
    cdEntry = Entry(formContact, textvariable=cd, font=('Helvética', 12))
    cdEntry.grid(row=11, column=1)


# ----------------------- Botão - Finalizar -----------------------

    btn_includecom = Button(formContact, text="Finalizar",
                           width=30, bg='#00BFFF', font=('Helvética', 15), command=submitData)
    btn_includecom.grid(row=50, columnspan=5, pady=15)

# ----------------------- Principal -----------------------

top = Frame(root, width=500, bd=1, relief=SOLID)
top.pack(side=TOP)
mid = Frame(root, width=500, bg="#1C1C1C")
mid.pack(side=TOP)
midleft = Frame(mid, width=100)
midleft.pack(side=LEFT, pady=20)
midleftPadding = Frame(mid, width=350, bg="#FF0000")
bottom = Frame(root, width=200)
bottom.pack(side=BOTTOM)
tableMargin = Frame(root, width=500)
tableMargin.pack(side=TOP)

# ----------------------- Titulo Principal -----------------------

lbl_title = Label(top, text="Bem-Vindo Ao Sistema de Cadastro de Matérias", font=('Helvética', 18), bg='#00BFFF', width=100)
lbl_title.pack(fill=X)

# ----------------------- Botão - Cadastrar -----------------------

bttn_add = Button(midleft, text="Cadastrar",
                  bg="#00BFFF", font=('Helvética', 15), width=10, command=addData)
bttn_add.pack()

# ----------------------- Final -----------------------

scrollbarX = Scrollbar(tableMargin, orient=HORIZONTAL)
scrollbarY = Scrollbar(tableMargin, orient=VERTICAL)

tree = ttk.Treeview(tableMargin, columns=("ID", "Nome", "Matricula", "Disciplina", "Professor", "AV1", "AV2", "AV3", "AVD", "AVDS", "AV", "AVS", "CD"), 
                    height=25, selectmode="extended", yscrollcommand=scrollbarY.set, xscrollcommand=scrollbarX.set)
scrollbarX.config(command=tree.xview)
scrollbarX.pack(side=BOTTOM, fill=X)
scrollbarY.config(command=tree.yview)
scrollbarY.pack(side=RIGHT, fill=Y)

tree.heading("ID", text="ID", anchor=W)
tree.heading("Nome", text="Nome", anchor=W)
tree.heading("Matricula", text="Matricula", anchor=W)
tree.heading("Disciplina", text="Disciplina", anchor=W)
tree.heading("Professor", text="Professor", anchor=W)
tree.heading("AV1", text="AV1", anchor=W)
tree.heading("AV2", text="AV2", anchor=W)
tree.heading("AV3", text="AV3", anchor=W)
tree.heading("AVD", text="AVD", anchor=W)
tree.heading("AVDS", text="AVDS", anchor=W)
tree.heading("AV", text="AV", anchor=W)
tree.heading("AVS", text="AVS", anchor=W)
tree.heading("CD", text="CD", anchor=W)

tree.column('#0', stretch=NO, minwidth=0, width=1)
tree.column('#1', stretch=NO, minwidth=0, width=20)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=45)
tree.column('#6', stretch=NO, minwidth=0, width=45)
tree.column('#7', stretch=NO, minwidth=0, width=45)
tree.column('#8', stretch=NO, minwidth=0, width=45)
tree.column('#9', stretch=NO, minwidth=0, width=45)
tree.column('#10', stretch=NO, minwidth=0, width=45)
tree.column('#11', stretch=NO, minwidth=0, width=45)
tree.column('#12', stretch=NO, minwidth=0, width=45)
tree.column('#13', stretch=NO, minwidth=0, width=45)
tree.pack()

if __name__ == '__main__':
    database()
    root.mainloop()