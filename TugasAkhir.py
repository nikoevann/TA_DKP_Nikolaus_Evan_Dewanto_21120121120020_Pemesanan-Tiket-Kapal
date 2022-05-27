import tkinter as tk
from tkinter import *
import re
from tkinter import messagebox


class JayaAbadi(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (FirstPage, PageTwo, PageThree):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame


            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("FirstPage")

    def show_frame(self, page_name):

        frame = self.frames[page_name]
        frame.tkraise()


class FirstPage(tk.Frame):

    def __init__(self, parent, controller):

        def check():
            txtdisplay1.configure(state='normal')
            for k, v in ship_Number.items():
                v = 120 - v
                ship = str(k) + ' Available: ' + str(v)
                txtdisplay1.insert(tk.END, '\n' + ship)
            txtdisplay1.configure(state='disabled')

        def clear1():
            txtdisplay1.configure(state='normal')
            txtdisplay1.delete('1.0', tk.END)
            txtdisplay1.configure(state='disabled')

        def Validation():

            valid = False

            if len(entry_ND.get()) == 0:
                messagebox.showinfo("Error","Please enter Nama Depan")
            elif entry_ND.get().isalpha() == False:
                messagebox.showinfo("Error","Nama Depan can only contain Alphabets")

            if len(entry_NB.get()) == 0:
                messagebox.showinfo("Error","Please enter Nama Belakang")
            elif entry_NB.get().isalpha() == False:
                messagebox.showinfo("Error","Nama Belakang can only contain Alphabets")

            if re.search("[@]", entry_Email.get()):
                if re.search("[.]", entry_Email.get()):
                    valid = True
                else:
                    messagebox.showinfo("Error","Please enter an valid Email address")
            else:
                messagebox.showinfo("Error", "Please enter an valid Email address")

            if len(shipvar.get()) == 0:
                messagebox.showinfo("Error","Please Choose ship")

            if len(penumpangvar.get()) == 0:
                messagebox.showinfo("Error", "Pilih Jumlah Penumpang")

            if len(penumpangvar.get()) != 0 and len(shipvar.get()) != 0:
                if (ship_Number[shipvar.get()]) + int( penumpangvar.get()) > 120:
                    messagebox.showinfo("Error", "Tiket Tidak Tersedia \n" + str(
                        120 - ship_Number[shipvar.get()]) + " Kursi Tersedia: " + str(
                        shipvar.get()))

            if len(entry_ND.get()) != 0 and entry_ND.get().isalpha() == True and entry_NB.get().isalpha() == True and len(
                    entry_NB.get()) != 0 and valid != False and len(shipvar.get()) != 0 and len(
                    penumpangvar.get()) != 0 and (ship_Number[shipvar.get()]) + int(penumpangvar.get()) <= 120:
                buttonToPageTwo.invoke()

        tk.Frame.__init__(self, parent)
        self.controller = controller

        global entry_ND
        global entry_NB
        global entry_Email
        global shipvar
        global penumpangvar
        global txtdisplay1
        global ship_Number


        frameHeading = tk.Frame(self)
        frameHeading.grid(row=0, columnspan=3)
        heading = tk.Label(frameHeading, text="Kapal Jaya Abadi", fg="blue", bg="beige", height="2",width="22")
        heading.config(font=("sans", 30))
        heading.grid(row=3, columnspan=2)

        label_ND = tk.Label(self, text="Nama Depan: ", font=("arial", 15), fg="black")
        label_ND.grid(row=1, column=0)
        entry_ND = tk.Entry(self, font=("", 15))
        entry_ND.grid(row=1, column=1)
        entry_ND.focus_force()

        label_NB = tk.Label(self, text="Nama Belakang: ", font=("", 15))
        label_NB.grid(row=2, column=0, pady=6)
        entry_NB = tk.Entry(self, font=("", 15))
        entry_NB.grid(row=2, column=1, pady=6)

        label_Email = tk.Label(self, text="Email: ", font=("", 15))
        label_Email.grid(row=3, column=0, pady=6)
        entry_Email = tk.Entry(self, font=("", 15))
        entry_Email.grid(row=3, column=1, pady=6)

        label_ship = tk.Label(self, text="Trip Kapal: ", font=("", 15))
        label_ship.grid(row=4, column=0, pady=6)
        ship_Number = {'Lampung-Merak': 0, 'Merak-Lampung': 0, 'Surabaya-Bali': 0, 'Bali-Surabaya': 0}
        shipvar = tk.StringVar(self)
        shipvar.set('')
        popupMenu_ship = tk.OptionMenu(self, shipvar, *ship_Number)
        popupMenu_ship.configure(font=("", 15), width=17)
        popupMenu_ship.grid(row=4, column=1, pady=6)

        label_penumpang = tk.Label(self, text="Jumlah Penumpang: ",font=("", 15))
        label_penumpang.grid(row=5, column=0, pady=6)
        penumpang_Number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        penumpangvar = tk.StringVar(self)
        penumpangvar.set('')
        popupMenu_penumpang = tk.OptionMenu(self, penumpangvar, *penumpang_Number)
        popupMenu_penumpang.configure(font=("", 15), width=17)
        popupMenu_penumpang.grid(row=5, column=1, pady=6)

        Button_Status = tk.Button(self, text="Cek Kursi", width="10", height="1", font=("", 15),command=check)
        Button_Status.grid(row=6, column=0, pady=10, padx=4)
        Button_Clear = tk.Button(self, text="Clear", width="7", height="1", font=("", 15), command=clear1)
        Button_Clear.grid(row=6, column=1, pady=10, sticky='E')

        txtdisplay1 = tk.Text(self, width=57, height=15)
        txtdisplay1.grid(row=7, column=0, columnspan=3)
        txtdisplay1.configure(state='disabled')

        Button_next = tk.Button(self, text="Next", width="7", height="1", font=("", 15),command=Validation)
        Button_next.grid(row=8, column=1, pady=10, sticky='E')

        Page_One = tk.Label(self, text="Page 1", font=("", 10)).grid(row=9, column=1,sticky='E')
        buttonToPageTwo = tk.Button(self, text="", command=lambda: controller.show_frame("PageTwo"))


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        def Calc():

            txtdisplay2.configure(
                state='normal')

            if int(Dewasavar.get()) == 0:
                messagebox.showinfo("Error",
                                    "Pilih satu orang dewasa")
            else:
                if int(penumpangvar.get()) == (int(Dewasavar.get()) + int(Anakvar.get()) + int(
                        Bayivar.get())):

                    txtdisplay2.insert(tk.END, "\n==============================================")
                    txtdisplay2.insert(tk.END, "\nJumlah Penumpang:" + str( penumpangvar.get()))
                    txtdisplay2.insert(tk.END, "\nPenumpang Dewasa:" + str(Dewasavar.get()))
                    txtdisplay2.insert(tk.END, "\nPenumpang Anak-anak:" + str(Anakvar.get()))
                    txtdisplay2.insert(tk.END, "\nPenumpang Bayi):" + str( Bayivar.get()))

                    harga = (int(Dewasavar.get()) * 200000 * 1.10) + ( int(Anakvar.get()) * 150000 * 1.15)
                    txtdisplay2.insert(tk.END, "\n==============================================")
                    txtdisplay2.insert(tk.END, "\nHarga: Rp" + str(round(harga, 2)))
                    txtdisplay2.insert(tk.END, "\n==============================================")
                    txtdisplay2.insert(tk.END,"\nHarga Penumpang Dewasa: Rp 220.000 *Termasuk Asuransi ")
                    txtdisplay2.insert(tk.END,"\nHarga Penumpang Anak-anak: Rp 165.000 *Termasuk Asuransi")
                    txtdisplay2.insert(tk.END,"\nHarga Penumpang Bayi: Tidak dikenakan biaya")
                elif int(penumpangvar.get()) > (int(Dewasavar.get()) + int(Anakvar.get()) + int(Bayivar.get())):
                    messagebox.showinfo("Error", " \n")
                else:
                    messagebox.showinfo("Error"," \n")

            txtdisplay2.configure(state='disabled')

        def Confirm():

            if int(Dewasavar.get()) == 0:
                messagebox.showinfo("Error", "Pilih Penumpang !")
            else:
                if int(penumpangvar.get()) == (int(Dewasavar.get()) + int(Anakvar.get()) + int( Bayivar.get())):
                    loadPageThree = 1
                    buttonToPageThree.invoke()

                elif int(penumpangvar.get()) > (int(Dewasavar.get()) + int(Anakvar.get()) + int(Bayivar.get())):
                    messagebox.showinfo("Error","Sesuaikan Dengan Jumlah Penumpang \n")
                else:
                    messagebox.showinfo("Error","Sesuaikan Dengan Jumlah Penumpang. \n")

        def clear2():
            txtdisplay2.configure(state='normal')
            txtdisplay2.delete('1.0', tk.END)
            txtdisplay2.configure(state='disabled')

        tk.Frame.__init__(self, parent)
        self.controller = controller

        global Dewasavar
        global Anakvar
        global Bayivar
        global txtdisplay2

        frameHeading = tk.Frame(self)
        frameHeading.grid(row=0, columnspan=3)
        heading = tk.Label(frameHeading, text="Kapal Jaya Abadi", fg="blue", bg="beige", height="2",width="22")
        heading.config(font=("", 30))
        heading.grid(row=0, columnspan=2)

        label_Dewasa = tk.Label(self, text="Jumlah Dewasa: ", font=("", 15))
        label_Dewasa.grid(row=5, column=0, pady=6)
        Dewasa_Number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        Dewasavar = tk.StringVar(self)
        Dewasavar.set(0)
        popupMenu_Dewasa = tk.OptionMenu(self, Dewasavar, *Dewasa_Number)
        popupMenu_Dewasa.configure(font=("", 15), width=17)
        popupMenu_Dewasa.grid(row=5, column=1, pady=6)
        Dewasalimit = tk.Label(self, text="*Penumpang Dewasa 17+ Tahun")
        Dewasalimit.grid(row=6, column=1, sticky='W')
        popupMenu_Dewasa.focus_force()

        label_Anak = tk.Label(self, text="Penumpang Anak-anak: ", font=("", 15))
        label_Anak.grid(row=7, column=0, pady=6)
        Anak_Number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        Anakvar = tk.StringVar(self)
        Anakvar.set(0)
        popupMenu_Anak = tk.OptionMenu(self, Anakvar,*Anak_Number)
        popupMenu_Anak.configure(font=("", 15), width=17)
        popupMenu_Anak.grid(row=7, column=1, pady=6)
        Anaklimit = tk.Label(self, text="*Penumpang Anak-anak 2-16 Tahun")
        Anaklimit.grid(row=8, column=1, sticky='W')

        label_Bayis = tk.Label(self, text="Penumpang Bayi: ", font=("", 15))
        label_Bayis.grid(row=9, column=0, pady=6)
        Bayi_Number = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
        Bayivar = tk.StringVar(self)
        Bayivar.set(0)
        popupMenu_Bayi = tk.OptionMenu(self, Bayivar, *Bayi_Number)
        popupMenu_Bayi.configure(font=("", 15), width=17)
        popupMenu_Bayi.grid(row=9, column=1, pady=6)
        Bayilimit = tk.Label(self, text="*Penumpang Bayi <2 Tahun")
        Bayilimit.grid(row=10, column=1, sticky='W')

        Button_Clear = tk.Button(self, text="Clear", width="7", height="1", font=("", 15), command=clear2)
        Button_Clear.grid(row=11, column=0, pady=6, padx=50, sticky='W')

        Button_Calculate = tk.Button(self, text="Hitung", width="8", height="1", font=("", 15),
                                command=Calc).grid(row=11, column=1, pady=6, padx=15, sticky='E')

        txtdisplay2 = tk.Text(self, width=57, height=15)
        txtdisplay2.grid(row=12, column=0, columnspan=3)
        txtdisplay2.configure(state='disabled')

        Button_back = tk.Button(self, text="Back", width="7", height="1", font=("", 15),
                                command=lambda: controller.show_frame("FirstPage"))
        Button_back.grid(row=13, column=0, pady=6, padx=50,sticky='W')
        Button_Confirm = tk.Button(self, text="Confirm", width="8", height="1", font=("", 15), command=Confirm)
        Button_Confirm.grid(row=13, column=1, pady=6, padx=15, sticky='E')

        buttonToPageThree = tk.Button(self, text="", command=lambda: controller.show_frame("PageThree"))

        Page_Two = tk.Label(self, text="Page 2", font=("", 10)).grid(row=14, column=1,sticky='E')


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        def PrintTicket():

            txtdisplay3.configure(state='normal')
            txtdisplay3.insert(tk.END, "\n==============================================")
            txtdisplay3.insert(tk.END,"\nNama Lengkap: " + entry_ND.get() + " " + entry_NB.get())
            txtdisplay3.insert(tk.END, "\nEmail: " + entry_Email.get())
            txtdisplay3.insert(tk.END,"\nJumlah Penumpang: " + penumpangvar.get())
            txtdisplay3.insert(tk.END, "\nJumlah Penumpang Dewasa: " + Dewasavar.get())
            txtdisplay3.insert(tk.END,"\nJumlah Penumpang Anak-anak: " + Anakvar.get())
            txtdisplay3.insert(tk.END,"\nJumlah Penumpang Bayi: " + Bayivar.get())
            txtdisplay3.insert(tk.END, "\n==============================================")

            TanpaAsuransi = int(Dewasavar.get()) * 200000 + int(Anakvar.get()) * 150000
            Asuransi = int(Dewasavar.get()) * 200000 * 0.10 + int(Anakvar.get()) * 150000 * 0.10
            TotalHarga = TanpaAsuransi + Asuransi

            txtdisplay3.insert(tk.END, "\nTrip Kapal: " + shipvar.get())
            txtdisplay3.insert(tk.END, "\nHarga: Rp" + str(TanpaAsuransi))
            txtdisplay3.insert(tk.END, "\nAsuransi: Rp" + str(Asuransi))
            txtdisplay3.insert(tk.END, "\nTotal Harga: Rp" + str(TotalHarga))
            txtdisplay3.insert(tk.END, "\n==============================================")
            txtdisplay3.configure(
                state='disabled')


        tk.Frame.__init__(self, parent)
        self.controller = controller

        frameHeading = tk.Frame(self)
        frameHeading.grid(row=0, columnspan=3)
        heading = tk.Label(frameHeading, text="Kapal Jaya Abadi", fg="blue", bg="beige", height="2",width="22")
        heading.config(font=("", 30))
        heading.grid(row=0, columnspan=2)

        txtdisplay3 = tk.Text(self, width=57, height=30)
        txtdisplay3.grid(row=5, column=0, columnspan=3)
        txtdisplay3.configure( state='disabled')
        ButtonPrint = tk.Button(self, text="Tekan untuk print tiket", width="20", height="2", font=("", 15),
                                command=PrintTicket).grid(row=6, column=0, pady=6, padx=15,sticky='W')


        Page_Three = tk.Label(self, text="Page 3", font=("", 10), padx=20).grid(row=7, column=1,sticky='E')


if __name__ == "__main__":
    root = JayaAbadi()
    root.geometry("512x750")
    root.title("Reservasi Kapal Jaya Abadi")
    root.mainloop()
