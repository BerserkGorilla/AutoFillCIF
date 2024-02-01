import os
from shutil import copyfile
from sys import argv
import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import re

def open_cif():

    """Open a file for editing."""

    global cifpath
    cifpath = fd.askopenfilename(
        filetypes=[("Cif Files", "*.cif"), ("OD Files", "*.cif_od"), ("All Files", "*.*")]
    )
    norm_path = cifpath.split("/")[-1]
    selected_cif.config(text = "CIF selecionado: %s"%(norm_path))

    
def open_od():

    """Open a file for editing."""

    global odpath
    odpath = fd.askopenfilename(

        filetypes=[("OD Files", "*.cif_od"),("Cif Files", "*.cif"), ("All Files", "*.*")]

    )
    norm_path = odpath.split("/")[-1]
    selected_odcif.config(text = "CIF selecionado: %s"%(norm_path))

def start_command():
    global nfname
    nfname = ent_nfname.get()
    if nfname != '':
        nfname += '.cif'
        window.destroy()

def fa_finder(fileaddress):
    file_array = fileaddress.split('/')
    folder_address = ''
    for ad in file_array:
        if ad == file_array[-1]:
            break
        folder_address += ad + '/'
    return folder_address

cifpath = '' 
odpath = ''
nfname = ''
window = tk.Tk()
window.title("AutoCif")
greeting = tk.Label(text="Bem vindo ao AutoCif", fg="#000000",bg = "#FFFFFF")
greeting.pack()
selected_cif = tk.Label(text="CIF selecionado: %s"%(cifpath), fg="#000000",bg = "#FFFFFF")
selected_cif.pack()
btn_opencif = tk.Button(text= "Open Cif File",fg="#000000",bg = "#FFFFFF",relief= "groove",command= open_cif)
btn_opencif.pack()
# label_cif = tk.Label(text=cifpath)
# label_cif.pack()
selected_odcif = tk.Label(text="CIF_OD selecionado: %s"%(odpath), fg="#000000",bg = "#FFFFFF")
selected_odcif.pack()
btn_openod = tk.Button(text= "Open OD File",fg="#000000",bg = "#FFFFFF",relief= "groove" ,command= open_od)
btn_openod.pack()
# label_od = tk.Label(text=odpath)
# label_od.pack()

label = tk.Label(text="Name the new Cif File")
label.pack()
ent_nfname = tk.Entry()
ent_nfname.pack()

btn_start = tk.Button(text= "Start Process",fg="#000000",bg = "#FFFFFF",relief= "groove" ,command= start_command)
btn_start.pack()
window.update
window.update_idletasks
window.mainloop()


line_count = 0
folder_address = fa_finder(cifpath)

Snippets = ['_cell_measurement_reflns_used','_cell_measurement_theta_min','_cell_measurement_theta_max','_exptl_crystal_description','_exptl_crystal_colour','_diffrn_measurement_device_type']

f1 = open(folder_address+nfname,'w')
f2 = open(cifpath,'r')

for line in f2:
    line_count += 1
    line_ns = re.sub(' +','  ',line) 
    if line_ns.split('  ')[0] not in Snippets:
        f1.write(line)
    else:
        f3 = open(odpath,'r')
        for linef3 in f3:
            linef3_ns = re.sub(' +','  ',linef3)
            if linef3_ns.split('  ')[0] == line_ns.split('  ')[0]:
                f1.write(linef3)
        f3.close()
f1.close()
f2.close()