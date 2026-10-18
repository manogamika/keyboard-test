import tkinter as tk
from tkinter import font as tkfont
import webbrowser

BG         = "#0b1020"
PANEL      = "#151c30"
KEY        = "#1f2a44"
KEY_HOVER  = "#2a3757"
KEY_BORDER = "#33415f"
TEXT       = "#e2e8f0"
MUTED      = "#8b9ab8"
ACCENT     = "#38bdf8"
ACTIVE     = "#22c55e"
ACTIVE_FG  = "#052e16"
KEY_TOP    = "#253253"
KEY_TOP_H  = "#2c3b60"

U     = 44
GAP   = 5
KR    = 7
ROW_H = U - GAP

F_ROW = [
    ("Esc","Escape",1,False,True,0),
    ("F1","F1",1,False,True,1.0),
    ("F2","F2",1,False,True,0),
    ("F3","F3",1,False,True,0),
    ("F4","F4",1,False,True,0),
    ("F5","F5",1,False,True,0.5),
    ("F6","F6",1,False,True,0),
    ("F7","F7",1,False,True,0),
    ("F8","F8",1,False,True,0),
    ("F9","F9",1,False,True,0.5),
    ("F10","F10",1,False,True,0),
    ("F11","F11",1,False,True,0),
    ("F12","F12",1,False,True,0),
]
F_ROW_NAV = [("PrtSc","PrintScreen",1,False,True,0),
             ("ScrLk","ScrollLock",1,False,True,0),
             ("Pause","Pause",1,False,True,0)]
F_ROW_NP  = [("Num","NumLock",1,False,True,0),
             ("/","NumpadDivide",1,False,True,0),
             ("*","NumpadMultiply",1,False,True,0),
             ("−","NumpadSubtract",1,False,True,0)]

ROW1_MAIN = [
    ("`","Backquote",1,False,False,0),("1","Digit1",1,False,False,0),
    ("2","Digit2",1,False,False,0),   ("3","Digit3",1,False,False,0),
    ("4","Digit4",1,False,False,0),   ("5","Digit5",1,False,False,0),
    ("6","Digit6",1,False,False,0),   ("7","Digit7",1,False,False,0),
    ("8","Digit8",1,False,False,0),   ("9","Digit9",1,False,False,0),
    ("0","Digit0",1,False,False,0),   ("-","Minus",1,False,False,0),
    ("=","Equal",1,False,False,0),
    ("Backspace","Backspace",2,False,False,0),
]
ROW1_NAV = [("Ins","Insert",1,False,False,0),
            ("Home","Home",1,False,False,0),
            ("PgUp","PageUp",1,False,False,0)]
ROW1_NP  = [("7","Numpad7",1,False,False,0),
            ("8","Numpad8",1,False,False,0),
            ("9","Numpad9",1,False,False,0),
            ("+","NumpadAdd",1,True,False,0)]

ROW2_MAIN = [
    ("Tab","Tab",1.5,False,False,0),
    ("Q","KeyQ",1,False,False,0),("W","KeyW",1,False,False,0),
    ("E","KeyE",1,False,False,0),("R","KeyR",1,False,False,0),
    ("T","KeyT",1,False,False,0),("Y","KeyY",1,False,False,0),
    ("U","KeyU",1,False,False,0),("I","KeyI",1,False,False,0),
    ("O","KeyO",1,False,False,0),("P","KeyP",1,False,False,0),
    ("[","BracketLeft",1,False,False,0),
    ("]","BracketRight",1,False,False,0),
    ("\\","Backslash",1.5,False,False,0),
]
ROW2_NAV = [("Del","Delete",1,False,False,0),
            ("End","End",1,False,False,0),
            ("PgDn","PageDown",1,False,False,0)]
ROW2_NP  = [("4","Numpad4",1,False,False,0),
            ("5","Numpad5",1,False,False,0),
            ("6","Numpad6",1,False,False,0)]

ROW3_MAIN = [
    ("Caps","CapsLock",1.75,False,False,0),
    ("A","KeyA",1,False,False,0),("S","KeyS",1,False,False,0),
    ("D","KeyD",1,False,False,0),("F","KeyF",1,False,False,0),
    ("G","KeyG",1,False,False,0),("H","KeyH",1,False,False,0),
    ("J","KeyJ",1,False,False,0),("K","KeyK",1,False,False,0),
    ("L","KeyL",1,False,False,0),
    (";","Semicolon",1,False,False,0),
    ("'","Quote",1,False,False,0),
    ("Enter","Enter",2.25,False,False,0),
]
ROW3_NP = [("1","Numpad1",1,False,False,0),
           ("2","Numpad2",1,False,False,0),
           ("3","Numpad3",1,False,False,0),
           ("↵","NumpadEnter",1,True,False,0)]

ROW4_MAIN = [
    ("Shift","ShiftLeft",2.25,False,False,0),
    ("Z","KeyZ",1,False,False,0),("X","KeyX",1,False,False,0),
    ("C","KeyC",1,False,False,0),("V","KeyV",1,False,False,0),
    ("B","KeyB",1,False,False,0),("N","KeyN",1,False,False,0),
    ("M","KeyM",1,False,False,0),
    (",","Comma",1,False,False,0),
    (".","Period",1,False,False,0),
    ("/","Slash",1,False,False,0),
    ("Shift","ShiftRight",2.75,False,False,0),
]
ROW4_NAV = [(None,None,1,False,False,0),
            ("↑","ArrowUp",1,False,False,0),
            (None,None,1,False,False,0)]
ROW4_NP  = [("0","Numpad0",2,False,False,0),
            (".","NumpadDecimal",1,False,False,0)]

ROW5_MAIN = [
    ("Ctrl","ControlLeft",1.25,False,False,0),
    ("Win","MetaLeft",1.25,False,False,0),
    ("Alt","AltLeft",1.25,False,False,0),
    ("Space","Space",6.25,False,False,0),
    ("Alt","AltRight",1.25,False,False,0),
    ("Win","MetaRight",1.25,False,False,0),
    ("Menu","ContextMenu",1.25,False,False,0),
    ("Ctrl","ControlRight",1.25,False,False,0),
]
ROW5_NAV = [("←","ArrowLeft",1,False,False,0),
            ("↓","ArrowDown",1,False,False,0),
            ("→","ArrowRight",1,False,False,0)]
ROW5_NP  = []

DISPLAY_NAMES = {
    "Escape":"Esc","Backspace":"Bksp","Enter":"Enter","Tab":"Tab",
    "CapsLock":"Caps","Shift":"Shift","Control":"Ctrl","Alt":"Alt",
    "Meta":"Win","ContextMenu":"Menu","Insert":"Ins","Delete":"Del",
    "Home":"Home","End":"End","PageUp":"PgUp","PageDown":"PgDn",
    "ArrowUp":"↑","ArrowDown":"↓","ArrowLeft":"←","ArrowRight":"→",
    "PrintScreen":"PrtSc","ScrollLock":"ScrLk","Pause":"Pause",
    "NumLock":"Num","NumpadDivide":"/","NumpadMultiply":"*",
    "NumpadSubtract":"−","NumpadAdd":"+","NumpadEnter":"↵",
    "NumpadDecimal":"."," ":"Space",
}

TK_TO_CODE = {
    "Escape":"Escape","F1":"F1","F2":"F2","F3":"F3","F4":"F4",
    "F5":"F5","F6":"F6","F7":"F7","F8":"F8","F9":"F9",
    "F10":"F10","F11":"F11","F12":"F12",
    "Print":"PrintScreen","Scroll_Lock":"ScrollLock","Pause":"Pause",
    "Num_Lock":"NumLock","KP_Divide":"NumpadDivide","KP_Multiply":"NumpadMultiply",
    "KP_Subtract":"NumpadSubtract","KP_Add":"NumpadAdd","KP_Enter":"NumpadEnter",
    "KP_Decimal":"NumpadDecimal",
    "KP_7":"Numpad7","KP_8":"Numpad8","KP_9":"Numpad9",
    "KP_4":"Numpad4","KP_5":"Numpad5","KP_6":"Numpad6",
    "KP_1":"Numpad1","KP_2":"Numpad2","KP_3":"Numpad3","KP_0":"Numpad0",
    "BackSpace":"Backspace","Tab":"Tab","Return":"Enter",
    "Caps_Lock":"CapsLock","Shift_L":"ShiftLeft","Shift_R":"ShiftRight",
    "Control_L":"ControlLeft","Control_R":"ControlRight",
    "Alt_L":"AltLeft","Alt_R":"AltRight",
    "Super_L":"MetaLeft","Super_R":"MetaRight","Menu":"ContextMenu",
    "Insert":"Insert","Delete":"Delete","Home":"Home","End":"End",
    "Prior":"PageUp","Next":"PageDown",
    "Up":"ArrowUp","Down":"ArrowDown","Left":"ArrowLeft","Right":"ArrowRight",
    "grave":"Backquote","minus":"Minus","equal":"Equal",
    "bracketleft":"BracketLeft","bracketright":"BracketRight",
    "backslash":"Backslash","semicolon":"Semicolon",
    "apostrophe":"Quote","comma":"Comma","period":"Period","slash":"Slash",
    "space":"Space",
}

KEYCODE_MAP = {
    "Escape":27,"F1":112,"F2":113,"F3":114,"F4":115,"F5":116,
    "F6":117,"F7":118,"F8":119,"F9":120,"F10":121,"F11":122,"F12":123,
    "PrintScreen":44,"ScrollLock":145,"Pause":19,
    "NumLock":144,"NumpadDivide":111,"NumpadMultiply":106,
    "NumpadSubtract":109,"NumpadAdd":107,"NumpadEnter":13,
    "NumpadDecimal":110,
    "Numpad0":96,"Numpad1":97,"Numpad2":98,"Numpad3":99,"Numpad4":100,
    "Numpad5":101,"Numpad6":102,"Numpad7":103,"Numpad8":104,"Numpad9":105,
    "Backspace":8,"Tab":9,"Enter":13,
    "CapsLock":20,"ShiftLeft":16,"ShiftRight":16,
    "ControlLeft":17,"ControlRight":17,"AltLeft":18,"AltRight":18,
    "MetaLeft":91,"MetaRight":92,"ContextMenu":93,
    "Insert":45,"Delete":46,"Home":36,"End":35,"PageUp":33,"PageDown":34,
    "ArrowUp":38,"ArrowDown":40,"ArrowLeft":37,"ArrowRight":39,
    "Space":32,"Backquote":192,"Minus":189,"Equal":187,
    "BracketLeft":219,"BracketRight":221,"Backslash":220,
    "Semicolon":186,"Quote":222,"Comma":188,"Period":190,"Slash":191,
}

LOCATION_MAP = {
    "ShiftLeft":1,"ShiftRight":2,"ControlLeft":1,"ControlRight":2,
    "AltLeft":1,"AltRight":2,"MetaLeft":1,"MetaRight":2,
}
for i in range(10):
    LOCATION_MAP[f"Numpad{i}"] = 3
for k in ("NumpadDivide","NumpadMultiply","NumpadSubtract","NumpadAdd",
          "NumpadEnter","NumpadDecimal","NumLock"):
    LOCATION_MAP[k] = 3
LOCATION_MAP["ArrowUp"] = LOCATION_MAP["ArrowDown"] = 0
LOCATION_MAP["ArrowLeft"] = LOCATION_MAP["ArrowRight"] = 0


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Keyboard Check — Full Layout")
        self.root.configure(bg=BG)
        self.root.geometry("1360x860")
        self.root.minsize(1000, 700)

        self.sticky = False
        self.menu_open = False
        self.key_widgets = {}
        self.touched = set()
        self.log_count = 0

        try:
            self.mono = tkfont.Font(family="Consolas", size=10, weight="bold")
            self.mono_small = tkfont.Font(family="Consolas", size=8, weight="bold")
            self.ui_font = tkfont.Font(family="Segoe UI", size=10)
            self.ui_bold = tkfont.Font(family="Segoe UI", size=10, weight="bold")
            self.ui_small = tkfont.Font(family="Segoe UI", size=8)
            self.ui_small_bold = tkfont.Font(family="Segoe UI", size=8, weight="bold")
            self.ui_tiny = tkfont.Font(family="Segoe UI", size=7)
            self.big_font = tkfont.Font(family="Segoe UI", size=34, weight="bold")
            self.mid_font = tkfont.Font(family="Consolas", size=12, weight="bold")
        except Exception:
            self.mono = tkfont.Font(family="Courier", size=10, weight="bold")
            self.mono_small = tkfont.Font(family="Courier", size=8, weight="bold")
            self.ui_font = tkfont.Font(size=10)
            self.ui_bold = tkfont.Font(size=10, weight="bold")
            self.ui_small = tkfont.Font(size=8)
            self.ui_small_bold = tkfont.Font(size=8, weight="bold")
            self.ui_tiny = tkfont.Font(size=7)
            self.big_font = tkfont.Font(size=34, weight="bold")
            self.mid_font = tkfont.Font(family="Courier", size=12, weight="bold")

        self._build_header()
        self._build_body()
        self._build_fab()

        self.root.bind_all("<KeyPress>", self.on_key_press)
        self.root.bind_all("<KeyRelease>", self.on_key_release)
        self.root.protocol("WM_DELETE_WINDOW", self.root.destroy)
        self.root.after(200, lambda: self.keyboard_frame.focus_set())

    def _build_header(self):
        bar = tk.Frame(self.root, bg=PANEL, height=56)
        bar.pack(side="top", fill="x")
        bar.pack_propagate(False)

        brand = tk.Frame(bar, bg=PANEL)
        brand.pack(side="left", padx=16, pady=10)
        tk.Label(brand, text="Keyboard Check", bg=PANEL, fg=TEXT,
                 font=self.ui_bold).pack(side="left")

        tk.Label(bar, text="Tekan tombol apa saja untuk mulai mengecek",
                 bg=PANEL, fg=MUTED, font=self.ui_small).pack(side="left", padx=12)

        right = tk.Frame(bar, bg=PANEL)
        right.pack(side="right", padx=16)

        sticky_wrap = tk.Frame(right, bg=PANEL)
        sticky_wrap.pack(side="left", padx=(0, 10))
        tk.Label(sticky_wrap, text="Tahan warna", bg=PANEL, fg=MUTED,
                 font=self.ui_tiny).pack(side="left", padx=(0, 6))

        self.sticky_canvas = tk.Canvas(sticky_wrap, width=44, height=26,
                                       bg=PANEL, highlightthickness=0, bd=0)
        self.sticky_canvas.pack(side="left")
        self._draw_sticky_toggle()
        self.sticky_canvas.bind("<Button-1>", lambda e: self.toggle_sticky())
        self.sticky_canvas.configure(cursor="hand2")

        self.burger_canvas = tk.Canvas(right, width=42, height=42,
                                       bg=PANEL, highlightthickness=0, bd=0)
        self.burger_canvas.pack(side="left")
        self._draw_burger()
        self.burger_canvas.bind("<Button-1>", lambda e: self.toggle_menu())
        self.burger_canvas.configure(cursor="hand2")

        self.menu_frame = tk.Frame(self.root, bg=PANEL, bd=0,
                                   highlightbackground=KEY_BORDER,
                                   highlightthickness=1)

        reset_btn = tk.Label(self.menu_frame, text="↺   Reset tampilan",
                             bg=PANEL, fg=TEXT, font=self.ui_font,
                             anchor="w", padx=12, pady=10, cursor="hand2")
        reset_btn.pack(fill="x")
        reset_btn.bind("<Button-1>", lambda e: self.reset_display())
        reset_btn.bind("<Enter>", lambda e: reset_btn.configure(bg=KEY_HOVER))
        reset_btn.bind("<Leave>", lambda e: reset_btn.configure(bg=PANEL))

        sep = tk.Frame(self.menu_frame, bg=KEY_BORDER, height=1)
        sep.pack(fill="x", padx=6, pady=(4, 4))

        tk.Label(self.menu_frame,
                 text="104-key ANSI · numpad & panah standar",
                 bg=PANEL, fg=MUTED, font=self.ui_tiny,
                 anchor="w", padx=12, pady=6).pack(fill="x")

    def _draw_sticky_toggle(self):
        c = self.sticky_canvas
        c.delete("all")
        on = self.sticky
        bg_color = "#1f2a44"
        border = ACTIVE if on else KEY_BORDER
        if on:
            bg_color = "#16301f"
        c.create_oval(2, 2, 42, 24, fill=bg_color, outline=border, width=1)
        knob_x = 30 if on else 12
        knob_color = ACTIVE if on else MUTED
        c.create_oval(knob_x - 9, 4, knob_x + 9, 22,
                      fill=knob_color, outline=knob_color)

    def _draw_burger(self):
        c = self.burger_canvas
        c.delete("all")
        c.create_rectangle(1, 1, 41, 41, fill=PANEL, outline=KEY_BORDER)
        if self.menu_open:
            c.create_line(12, 12, 30, 30, fill=TEXT, width=2)
            c.create_line(30, 12, 12, 30, fill=TEXT, width=2)
        else:
            for y in (14, 21, 28):
                c.create_line(12, y, 30, y, fill=TEXT, width=2)

    def toggle_sticky(self):
        self.sticky = not self.sticky
        self._draw_sticky_toggle()
        if not self.sticky:
            for w in self.key_widgets.values():
                self._set_key_pressed(w, False)
        self.status_label.configure(
            text="Mode tahan warna AKTIF — tombol tetap hijau sampai Reset tampilan"
            if self.sticky else "Mode tahan warna nonaktif"
        )

    def toggle_menu(self):
        self.menu_open = not self.menu_open
        self._draw_burger()
        if self.menu_open:
            self.menu_frame.place(relx=1.0, x=-16, y=58, anchor="ne",
                                  width=260)
            self.menu_frame.lift()
        else:
            self.menu_frame.place_forget()

    def _build_body(self):
        outer = tk.Frame(self.root, bg=BG)
        outer.pack(fill="both", expand=True, padx=12, pady=(70, 12))

        self.main_content = tk.Frame(outer, bg=BG)
        self.main_content.pack(side="left", fill="both", expand=True)

        self.key_display = tk.Frame(self.main_content, bg=PANEL, bd=0,
                                    highlightbackground=KEY_BORDER,
                                    highlightthickness=2)
        self.key_display.pack(pady=(0, 12))
        self.key_name_label = tk.Label(self.key_display, text="—",
                                       bg=PANEL, fg=ACCENT,
                                       font=self.big_font,
                                       width=20, height=1)
        self.key_name_label.pack(padx=20, pady=14)

        info = tk.Frame(self.main_content, bg=BG)
        info.pack(fill="x", pady=(0, 12))
        for i in range(4):
            info.columnconfigure(i, weight=1, uniform="info")

        self.val_key      = self._make_info_card(info, 0, "event.key")
        self.val_code     = self._make_info_card(info, 1, "event.code")
        self.val_keycode  = self._make_info_card(info, 2, "event.keyCode")
        self.val_location = self._make_info_card(info, 3, "event.location")

        self.keyboard_frame = tk.Frame(self.main_content, bg=PANEL, bd=0,
                                       highlightbackground=KEY_BORDER,
                                       highlightthickness=1)
        self.keyboard_frame.pack(pady=(0, 10))
        self._build_keyboard(self.keyboard_frame)

        self.status_label = tk.Label(self.main_content,
                                     text="Menunggu input… (☰ untuk reset)",
                                     bg=BG, fg=MUTED, font=self.ui_small)
        self.status_label.pack(pady=(4, 0))

        self.side_panel = tk.Frame(outer, bg=PANEL, bd=0,
                                   highlightbackground=KEY_BORDER,
                                   highlightthickness=1, width=300)
        self.side_panel.pack(side="right", fill="y", padx=(20, 0))
        self.side_panel.pack_propagate(False)

        header = tk.Frame(self.side_panel, bg="#1a2238")
        header.pack(fill="x")
        tk.Label(header, text="TOMBOL DISENTUH", bg="#1a2238", fg=MUTED,
                 font=self.ui_small_bold, padx=14, pady=10).pack(side="left")

        self.log_count_label = tk.Label(header, text="0", bg="#152c3f",
                                        fg=ACCENT, font=self.mono_small,
                                        padx=8, pady=1)
        self.log_count_label.pack(side="left", padx=4)

        clear_btn = tk.Label(header, text="Hapus", bg="#1a2238", fg=MUTED,
                             font=self.ui_tiny, padx=8, pady=3,
                             cursor="hand2")
        clear_btn.pack(side="right", padx=10)
        clear_btn.bind("<Button-1>", lambda e: self.clear_log())
        clear_btn.bind("<Enter>", lambda e: clear_btn.configure(fg=TEXT))
        clear_btn.bind("<Leave>", lambda e: clear_btn.configure(fg=MUTED))

        tk.Frame(self.side_panel, bg=KEY_BORDER, height=1).pack(fill="x")

        list_wrap = tk.Frame(self.side_panel, bg=PANEL)
        list_wrap.pack(fill="both", expand=True, padx=6, pady=6)

        self.log_canvas = tk.Canvas(list_wrap, bg=PANEL,
                                    highlightthickness=0, bd=0)
        scrollbar = tk.Scrollbar(list_wrap, orient="vertical",
                                 command=self.log_canvas.yview)
        self.log_canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        self.log_canvas.pack(side="left", fill="both", expand=True)

        self.log_inner = tk.Frame(self.log_canvas, bg=PANEL)
        self.log_window = self.log_canvas.create_window(
            (0, 0), window=self.log_inner, anchor="nw"
        )
        self.log_inner.bind("<Configure>", self._on_log_configure)
        self.log_canvas.bind("<Configure>", self._on_log_canvas_configure)

    def _on_log_configure(self, event=None):
        self.log_canvas.configure(scrollregion=self.log_canvas.bbox("all"))

    def _on_log_canvas_configure(self, event):
        self.log_canvas.itemconfigure(self.log_window, width=event.width)

    def _make_info_card(self, parent, col, label_text):
        card = tk.Frame(parent, bg=PANEL, bd=0,
                        highlightbackground=KEY_BORDER,
                        highlightthickness=1)
        card.grid(row=0, column=col, sticky="nsew", padx=4, pady=2)
        tk.Label(card, text=label_text.upper(), bg=PANEL, fg=MUTED,
                 font=self.ui_tiny, anchor="w").pack(fill="x", padx=10,
                                                      pady=(6, 0))
        val = tk.Label(card, text="—", bg=PANEL, fg=ACCENT,
                       font=self.mid_font, anchor="w")
        val.pack(fill="x", padx=10, pady=(0, 8))
        return val

    def _make_key(self, parent, label, code, units, tall, is_fkey, x, y,
                  col_offset_extra=0):
        w = int(U * units - GAP)
        h = int(U * 2 - GAP) if tall else ROW_H
        xpos = x
        frame = tk.Frame(parent, bg=KEY_BORDER, bd=0)
        frame.place(x=xpos, y=y, width=w, height=h)
        inner = tk.Frame(frame, bg=KEY)
        inner.place(x=0, y=0, width=w, height=h - 2)

        fnt = self.mono_small if is_fkey else self.mono
        lbl = tk.Label(inner, text=label, bg=KEY, fg=TEXT, font=fnt)
        lbl.place(relx=0.5, rely=0.5, anchor="center")

        widget = {
            "frame": frame, "inner": inner, "label": lbl,
            "code": code, "w": w, "h": h, "pressed": False,
        }
        if code:
            self.key_widgets[code] = widget
        return widget

    def _build_keyboard(self, parent):
        pad = 14
        main_w = int(U * 15 - GAP)
        nav_w  = int(U * 3 - GAP)
        np_w   = int(U * 4 - GAP)
        margin = int(U * 0.25)

        total_w = main_w + margin + nav_w + margin + np_w
        total_h = (ROW_H + GAP) * 6 + pad * 2

        parent.configure(width=total_w + pad * 2, height=total_h)
        parent.pack_propagate(False)

        rows = [
            (F_ROW, F_ROW_NAV, F_ROW_NP),
            (ROW1_MAIN, ROW1_NAV, ROW1_NP),
            (ROW2_MAIN, ROW2_NAV, ROW2_NP),
            (ROW3_MAIN, None, ROW3_NP),
            (ROW4_MAIN, ROW4_NAV, ROW4_NP),
            (ROW5_MAIN, ROW5_NAV, ROW5_NP),
        ]

        for r_idx, (main, nav, np_row) in enumerate(rows):
            y = pad + r_idx * (ROW_H + GAP)

            x = pad
            for label, code, units, tall, is_fkey, pre_gap in main:
                if pre_gap:
                    x += int(U * pre_gap)
                self._make_key(parent, label, code, units, tall, is_fkey, x, y)
                x += int(U * units)

            x_main_end = pad + main_w + margin

            if nav is not None:
                x = x_main_end
                for label, code, units, tall, is_fkey, pre_gap in nav:
                    if label is None:
                        x += int(U * units)
                        continue
                    self._make_key(parent, label, code, units, tall,
                                   is_fkey, x, y)
                    x += int(U * units)

            x = x_main_end + nav_w + margin
            for label, code, units, tall, is_fkey, pre_gap in np_row:
                self._make_key(parent, label, code, units, tall,
                               is_fkey, x, y)
                x += int(U * units)

    def _build_fab(self):
        size = 52
        fab = tk.Canvas(self.root, width=size, height=size, bg=BG,
                        highlightthickness=0, bd=0, cursor="hand2")
        fab.place(relx=1.0, rely=1.0, x=-20, y=-20, anchor="se")

        fab.create_oval(1, 1, size - 1, size - 1, fill=PANEL,
                        outline=KEY_BORDER, width=1)
        fab.create_oval(6, 6, size - 6, size - 6, fill=KEY,
                        outline=KEY_BORDER, width=1)

        cx = cy = size / 2
        r = 13
        fab.create_arc(cx - r, cy - r, cx + r, cy + r,
                       start=20, extent=320, style="arc",
                       outline=TEXT, width=2)
        fab.create_line(cx, cy - r, cx, cy - r + 8, fill=TEXT, width=2)
        fab.create_line(cx + 4, cy - r + 4, cx, cy - r, fill=TEXT, width=2)
        fab.create_line(cx - 4, cy - r + 4, cx, cy - r, fill=TEXT, width=2)

        def on_click(e):
            webbrowser.open("https://github.com/manogamika/keyboard-test")

        fab.bind("<Button-1>", on_click)

    def _set_key_pressed(self, widget, pressed):
        widget["pressed"] = pressed
        if pressed:
            widget["frame"].configure(bg=ACTIVE)
            widget["inner"].configure(bg=ACTIVE)
            widget["label"].configure(bg=ACTIVE, fg=ACTIVE_FG)
        else:
            widget["frame"].configure(bg=KEY_BORDER)
            widget["inner"].configure(bg=KEY)
            widget["label"].configure(bg=KEY, fg=TEXT)

    def _display_name_from_code(self, code, keysym):
        if code in DISPLAY_NAMES:
            return DISPLAY_NAMES[code]
        if keysym == "space":
            return "Space"
        if len(keysym) == 1:
            return keysym.upper()
        return keysym

    def on_key_press(self, event):
        if self.menu_open:
            self.toggle_menu()

        keysym = event.keysym
        code = TK_TO_CODE.get(keysym)
        if code is None:
            if len(keysym) == 1 and keysym.isalpha():
                code = "Key" + keysym.upper()
            elif len(keysym) == 1 and keysym.isdigit():
                code = "Digit" + keysym

        if code is None:
            return

        self._update_display(code, keysym, pressed=True)
        self._add_log_entry(code, keysym)

        widget = self.key_widgets.get(code)
        if widget:
            self._set_key_pressed(widget, True)

    def on_key_release(self, event):
        keysym = event.keysym
        code = TK_TO_CODE.get(keysym)
        if code is None:
            if len(keysym) == 1 and keysym.isalpha():
                code = "Key" + keysym.upper()
            elif len(keysym) == 1 and keysym.isdigit():
                code = "Digit" + keysym

        if code is None:
            return

        self._update_display(code, keysym, pressed=False)

        widget = self.key_widgets.get(code)
        if widget and not self.sticky:
            self._set_key_pressed(widget, False)

    def _update_display(self, code, keysym, pressed):
        name = self._display_name_from_code(code, keysym)
        self.key_name_label.configure(text=name,
                                      fg=ACTIVE if pressed else ACCENT)

        self.val_key.configure(text=name)
        self.val_code.configure(text=code)

        keycode = KEYCODE_MAP.get(code, "—")
        self.val_keycode.configure(text=str(keycode))

        loc = LOCATION_MAP.get(code, 0)
        loc_names = ["Standar", "Kiri", "Kanan", "Numpad"]
        self.val_location.configure(text=loc_names[loc])

        if pressed:
            self.status_label.configure(
                text=f"Tombol ditekan: {name} — lepaskan untuk reset")
        else:
            self.status_label.configure(
                text="Menunggu input… (☰ untuk reset)")

        if pressed:
            self.key_display.configure(highlightbackground=ACTIVE)
        else:
            self.key_display.configure(highlightbackground=KEY_BORDER)

    def _short_label(self, code, keysym):
        if code in DISPLAY_NAMES:
            return DISPLAY_NAMES[code]
        if keysym == "space":
            return "Space"
        if len(keysym) == 1:
            return keysym.upper()
        return keysym

    def _add_log_entry(self, code, keysym):
        if code in self.touched:
            return
        self.touched.add(code)

        item = tk.Frame(self.log_inner, bg="#1a2338",
                        highlightbackground=KEY_BORDER, highlightthickness=1)
        item.pack(fill="x", pady=3)

        badge = tk.Label(item, text=self._short_label(code, keysym),
                         bg=KEY, fg=TEXT, font=self.mono_small,
                         padx=8, pady=4)
        badge.pack(side="left", padx=6, pady=6)

        meta = tk.Frame(item, bg="#1a2338")
        meta.pack(side="left", fill="both", expand=True, pady=4)

        tk.Label(meta, text=code, bg="#1a2338", fg=ACCENT,
                 font=self.mono_small, anchor="w").pack(fill="x")
        tk.Label(meta, text=time.strftime("%H:%M:%S"), bg="#1a2338",
                 fg=MUTED, font=self.ui_tiny,
                 anchor="w").pack(fill="x")

        self.log_count += 1
        self.log_count_label.configure(text=str(self.log_count))

        self.root.after(50, lambda: self.log_canvas.yview_moveto(1.0))

    def clear_log(self):
        for child in self.log_inner.winfo_children():
            child.destroy()
        self.touched.clear()
        self.log_count = 0
        self.log_count_label.configure(text="0")

    def reset_display(self):
        self.toggle_menu()
        self.key_name_label.configure(text="—", fg=ACCENT)
        self.val_key.configure(text="—")
        self.val_code.configure(text="—")
        self.val_keycode.configure(text="—")
        self.val_location.configure(text="—")
        self.key_display.configure(highlightbackground=KEY_BORDER)
        self.status_label.configure(text="Menunggu input… (☰ untuk reset)")
        for widget in self.key_widgets.values():
            self._set_key_pressed(widget, False)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
