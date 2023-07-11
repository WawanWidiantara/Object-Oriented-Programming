from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1360x680+0+0")

        self.id = StringVar()
        self.kategori = StringVar()
        self.nkategori = StringVar()
        self.produk = StringVar()
        self.seri = StringVar()
        self.stok = StringVar()
        self.terjual = StringVar()
        self.harga = StringVar()

        img = Image.open(
            "D:\Code\py_code\Object-Oriented-Programming\projek inventory\inv_ill.jpg"
        )
        img = img.resize((1360, 314), Image.ANTIALIAS)
        self.photoImg = ImageTk.PhotoImage(img)
        lbl_img = Label(self.root, image=self.photoImg)
        lbl_img.place(x=0, y=80)

        lbltitle = Label(
            self.root,
            bd=20,
            relief=RIDGE,
            text="INVENTORY MANAGEMENT",
            fg="green",
            bg="white",
            font=("arial", 40, "bold"),
        )
        lbltitle.pack(side=TOP, fill=X)

        # ===== [ Dataframe ] =====
        dataFrame = Frame(self.root, bd=20, padx=20, relief=RIDGE)
        dataFrame.place(x=0, y=280, width=1360, height=400)

        dataFrameKiri = LabelFrame(
            dataFrame,
            bd=10,
            padx=20,
            relief=RIDGE,
            font=("arial", 12, "bold"),
            text=" Informasi Produk ",
        )
        dataFrameKiri.place(x=0, y=5, width=520, height=250)

        dataFrameKanan = LabelFrame(dataFrame, bd=10, padx=20, pady=20, relief=RIDGE)
        dataFrameKanan.place(x=540, y=10, width=740, height=325)

        # ===== [ button frame ] =====
        buttonFrame = LabelFrame(
            dataFrame,
            bd=10,
            padx=10,
            pady=5,
            relief=RIDGE,
            font=("arial", 12, "bold"),
            text=" Action ",
        )
        buttonFrame.place(x=0, y=260, width=520, height=75)

        # ===== { Informasi Produk } =====
        lblKategori = Label(
            dataFrameKiri, font=("arial", 12, "bold"), text="Kategori ", padx=2, pady=6
        )
        lblKategori.grid(row=0, column=0, sticky=W)
        comKategori = ttk.Combobox(
            dataFrameKiri,
            textvariable=self.kategori,
            state="readonly",
            font=("arial", 12, "bold"),
            width=30,
        )
        comKategori["value"] = (
            "Laptop",
            "Aksesoris",
            "Software",
            "Printer",
            "Komputer",
        )
        comKategori.current(0)
        comKategori.grid(row=0, column=1)

        lblNamaProduk = Label(
            dataFrameKiri, font=("arial", 12, "bold"), text="Nama Produk ", padx=2
        )
        lblNamaProduk.grid(row=1, column=0, sticky=W)
        txtNamaProduk = Entry(
            dataFrameKiri,
            textvariable=self.produk,
            font=("arial", 12, "bold"),
            width=32,
        )
        txtNamaProduk.grid(row=1, column=1)

        lblSeri = Label(
            dataFrameKiri,
            font=("arial", 12, "bold"),
            text="Seri Produk ",
            padx=2,
            pady=6,
        )
        lblSeri.grid(row=2, column=0, sticky=W)
        txtSeri = Entry(
            dataFrameKiri, textvariable=self.seri, font=("arial", 12, "bold"), width=32
        )
        txtSeri.grid(row=2, column=1)

        lblStok = Label(
            dataFrameKiri,
            font=("arial", 12, "bold"),
            text="Stok Tersedia ",
            padx=2,
            pady=6,
        )
        lblStok.grid(row=3, column=0, sticky=W)
        txtStok = Entry(
            dataFrameKiri, textvariable=self.stok, font=("arial", 12, "bold"), width=32
        )
        txtStok.grid(row=3, column=1)

        lblTerjual = Label(
            dataFrameKiri, font=("arial", 12, "bold"), text="Terjual ", padx=2, pady=6
        )
        lblTerjual.grid(row=4, column=0, sticky=W)
        txtTerjual = Entry(
            dataFrameKiri,
            textvariable=self.terjual,
            font=("arial", 12, "bold"),
            width=32,
        )
        txtTerjual.grid(row=4, column=1)

        lblHarga = Label(
            dataFrameKiri, font=("arial", 12, "bold"), text="Harga ", padx=2, pady=6
        )
        lblHarga.grid(row=5, column=0, sticky=W)
        txtHarga = Entry(
            dataFrameKiri, textvariable=self.harga, font=("arial", 12, "bold"), width=32
        )
        txtHarga.grid(row=5, column=1)

        # ===== [ Button ] =====
        btnInsert = Button(
            buttonFrame,
            command=self.insert,
            text="Insert",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=6,
            pady=1,
        )
        btnInsert.grid(row=6, column=0)

        btnUpdate = Button(
            buttonFrame,
            command=self.update,
            text="Update",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=6,
            pady=1,
        )
        btnUpdate.grid(row=6, column=1)

        btnDelete = Button(
            buttonFrame,
            command=self.delete,
            text="Delete",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=6,
            pady=1,
        )
        btnDelete.grid(row=6, column=2)

        btnClear = Button(
            buttonFrame,
            command=self.clear,
            text="Clear",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=6,
            pady=1,
        )
        btnClear.grid(row=6, column=3)

        btnShow = Button(
            buttonFrame,
            command=self.show_all,
            text="Show All",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=12,
            pady=1,
        )
        btnShow.grid(row=6, column=5)

        btnFilter = Button(
            buttonFrame,
            command=self.newWindow,
            text="Filter",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=6,
            pady=1,
        )
        btnFilter.grid(row=6, column=4)

        # ======================== [ Tabel ] ========================
        # Scrollbar
        scroll_x = ttk.Scrollbar(dataFrameKanan, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(dataFrameKanan, orient=VERTICAL)
        self.inventory = ttk.Treeview(
            dataFrameKanan,
            column=("id", "kategori", "produk", "seri", "stok", "terjual", "harga"),
            show="headings",
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.inventory.xview)
        scroll_y = ttk.Scrollbar(command=self.inventory.yview)

        self.inventory.heading("id", text="Id")
        self.inventory.heading("kategori", text="Kategori")
        self.inventory.heading("produk", text="Nama Produk")
        self.inventory.heading("seri", text="Seri")
        self.inventory.heading("stok", text="Stok Barang")
        self.inventory.heading("terjual", text="Terjual")
        self.inventory.heading("harga", text="Harga")

        self.inventory.column("id", width=50)
        self.inventory.column("kategori", width=100)
        self.inventory.column("produk", width=100)
        self.inventory.column("seri", width=100)
        self.inventory.column("stok", width=100)
        self.inventory.column("terjual", width=100)
        self.inventory.column("harga", width=100)

        self.inventory.pack(fill=BOTH, expand=1)
        self.inventory.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_all()

    # ========== [ fungsional ] ==========
    def insert(self):
        if (
            self.kategori.get() == ""
            or self.produk.get() == ""
            or self.seri.get() == ""
            or self.stok.get() == ""
            or self.terjual.get() == ""
            or self.harga.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = sqlite3.connect("database.db")
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Inventory (kategori, nama_produk, seri, stok, terjual, harga) VALUES (?, ?, ?, ?, ?, ?)",
                (
                    self.kategori.get(),
                    self.produk.get(),
                    self.seri.get(),
                    self.stok.get(),
                    self.terjual.get(),
                    self.harga.get(),
                ),
            )

            conn.commit()
            self.show_all()
            conn.close()
            messagebox.showinfo("Succsess", "Record has been inserted")

    def update(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute(
            "UPDATE Inventory SET kategori = ?, nama_produk = ?, seri = ?, stok = ?, terjual = ?, harga = ? WHERE id=?",
            (
                self.kategori.get(),
                self.produk.get(),
                self.seri.get(),
                self.stok.get(),
                self.terjual.get(),
                self.harga.get(),
                self.id,
            ),
        )
        conn.commit()
        self.show_all()
        conn.close()
        messagebox.showinfo("Succsess", "Record has been updated")

    def delete(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM Inventory WHERE id=?", (self.id,))

        conn.commit()
        self.show_all()
        conn.close()
        messagebox.showinfo("Succsess", "Record has been deleted")

    def show_all(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Inventory")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.inventory.delete(*self.inventory.get_children())
            for i in rows:
                self.inventory.insert("", END, values=i)
            conn.commit()
        conn.close()

    def clear(self):
        self.kategori.set("")
        self.produk.set("")
        self.seri.set("")
        self.stok.set("")
        self.terjual.set("")
        self.harga.set("")

    def get_cursor(self, event=""):
        cursor_row = self.inventory.focus()
        content = self.inventory.item(cursor_row)
        row = content["values"]
        self.id = row[0]
        self.kategori.set(row[1])
        self.produk.set(row[2])
        self.seri.set(row[2])
        self.stok.set(row[4])
        self.terjual.set(row[5])
        self.harga.set(row[6])

    def newWindow(self):
        self.newWindowFilter = Toplevel(self.root)
        self.newWindowFilter.title("Filter List")
        self.newWindowFilter.geometry("450x40+570+595")

        comKategori = ttk.Combobox(
            self.newWindowFilter,
            textvariable=self.nkategori,
            state="readonly",
            font=("arial", 12, "bold"),
            width=30,
        )
        comKategori["value"] = (
            "Laptop",
            "Aksesoris",
            "Software",
            "Printer",
            "Komputer",
        )
        comKategori.place(relx=0.2, rely=0.025)

        btnClear = Button(
            self.newWindowFilter,
            command=self.filter,
            text="Filter",
            bg="green",
            fg="white",
            font=("arial", 12, "bold"),
            width=7,
            height=1,
        )
        btnClear.place(relx=0.01, rely=0.01)

    def filter(self):
        conn = sqlite3.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM Inventory WHERE kategori=?", (self.nkategori.get(),))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.inventory.delete(*self.inventory.get_children())
            for i in rows:
                self.inventory.insert("", END, values=i)
            conn.commit()
        else:
            messagebox.showerror("Error", "Category is Empty")
        conn.close()
        self.newWindowFilter.destroy()


if __name__ == "__main__":
    root = Tk()
    ob = Inventory(root)
    root.mainloop()
