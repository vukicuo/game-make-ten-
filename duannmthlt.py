import random
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Game Make Ten")
root.geometry("680x460")
root.resizable(False, False)

so_hang = 10
so_cot = 17
do_lon_o = 40

diem = 0
bd_x = 0
bd_y = 0 
vung_keo = None



bang_so = [[0 for _ in range(so_cot)] for _ in range(so_hang)]
bang_id = [[None for _ in range(so_cot)] for _ in range(so_hang)]

khung_tren = tk.Frame(root, bg="#dc21c3")
khung_tren.pack(fill="x")
khung_game = tk.Canvas(root, width=so_cot * do_lon_o, height=so_hang * do_lon_o, bg="#bba3c9")
khung_game.pack()
diem_so = tk.Label(
    khung_tren,
    text="Điểm: 0",
    fg="white",
    bg="#c524a5",
)
diem_so.pack(side="left", padx=15, pady=8)
tieu_de = tk.Label(
    khung_tren,
    text="TÔI YÊU PTIT VIỆT NAM !",
    fg="white",
    bg="#cf0e4b",
    font=("Segoe UI", 14, "bold"),
)
tieu_de.pack(side="left", padx=140)

def reset_game():
  global diem
  diem = 0
  diem_so.config(text="Điểm: 0")

  khung_game.delete("all") 

  for r in range(so_hang):
    for c in range(so_cot):
      val = random.randint(1, 9)
      bang_so[r][c] = val

      x1, y1 = c * do_lon_o, r * do_lon_o
      x2, y2 = x1 + do_lon_o, y1 + do_lon_o

      rect = khung_game.create_rectangle(
          x1 + 2, y1 + 2, x2 - 2, y2 - 2, fill="#d20e80", outline="#6b045a"
      )
      text = khung_game.create_text(
          (x1 + x2) // 2,
          (y1 + y2) // 2,
          text=str(val),
          font=("Segoe UI", 13, "bold"),
          fill="#ebe0e0",
      )

      bang_id[r][c] = (rect, text)

choi_lai = tk.Button(
    khung_tren,
    text="Chơi mới",
    command=reset_game,
    bg="#e81d90",
    fg="white",
    font=("Segoe UI", 9, "bold"),
)
choi_lai.pack(side="right", padx=15)

#logic game
def an_chuot(event):
  global bd_x, bd_y, vung_keo
  bd_x = event.x
  bd_y = event.y
  vung_keo = khung_game.create_rectangle(
      bd_x, bd_y, bd_x, bd_y, 
      outline="#1b0430", width=2, dash=(4, 4)
    )

def keo_chuot(event):
  if vung_keo is not None:
    khung_game.coords(vung_keo, bd_x, bd_y, event.x, event.y)
  
def tha_chuot(event):
    global diem, vung_keo
    if not vung_keo:
        return
    kt_x, kt_y = event.x, event.y
    khung_game.delete(vung_keo)
    vung_keo = None
    c1 = max(0, min(bd_x, kt_x)) // do_lon_o
    c2 = min(so_cot - 1, max(bd_x, kt_x) // do_lon_o)
    r1 = max(0, min(bd_y, kt_y)) // do_lon_o
    r2 = min(so_hang - 1, max(bd_y, kt_y) // do_lon_o)

    o_chon = []
    tong_o_chon = 0
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            val = bang_so[r][c]
            if val is not None:
                tong_o_chon += val
                o_chon.append((r, c))

    if tong_o_chon == 10 and o_chon:
        for r, c in o_chon:
            bang_so[r][c] = None
            rect, text = bang_id[r][c]
            khung_game.delete(rect)
            khung_game.delete(text)
        diem += len(o_chon)
        diem_so.config(text=f"Điểm: {diem}")

        #neu xoa het 
        ktr_het = True
        for r in range(so_hang):
            for c in range(so_cot):
                if bang_so[r][c] is not None:
                    ktr_het = False
                    break
            if not ktr_het:
                break
        if ktr_het:
            tk.messagebox.showinfo("Hay quá!", f"Bạn đã xóa hết các ô! Điểm của bạn: {diem}")
            reset_game()

khung_game.bind("<ButtonPress-1>", an_chuot)
khung_game.bind("<B1-Motion>", keo_chuot)
khung_game.bind("<ButtonRelease-1>", tha_chuot)

reset_game()
root.mainloop()