THEMENAME = "beginnerluftearthy"

FONT = "YuMincho"
FONT_SIZE_XXXL = 96
FONT_SIZE_XXL = 64
FONT_SIZE_XL = 48
FONT_SIZE_L = 32
FONT_SIZE_M = 24
FONT_SIZE_S = 16
FONT_SIZE_XS = 14
FONT_SIZE_XXS = 10

if THEMENAME == "beginnerluftclassic":
    HEADING_BOOTSTYLE = ""
    HOVER_BOOTSTYLE = "info"
    NAV_HEADER_BOOTSTYLE = "danger"
    OVERVIEW_HEADING_BOOTSTYLE = ""
    SELECTION_BOOTSTYLE = "primary"
    TITLESCREEN_BG_BOOTSTYLE = "light"
    TITLE_SCREEN_FG_BOOTSTYLE = "inverse-light"
elif THEMENAME == "beginnerluftdark":
    HEADING_BOOTSTYLE = "primary"
    HOVER_BOOTSTYLE = "info"
    OVERVIEW_HEADING_BOOTSTYLE = "primary"
    SELECTION_BOOTSTYLE = "primary"
    TITLESCREEN_BG_BOOTSTYLE = "bg"
    TITLE_SCREEN_FG_BOOTSTYLE = "primary"
else:
    HEADING_BOOTSTYLE = "secondary"
    HOVER_BOOTSTYLE = "info"
    OVERVIEW_HEADING_BOOTSTYLE = "success"
    SELECTION_BOOTSTYLE = "success"
    TITLESCREEN_BG_BOOTSTYLE = "primary"
    TITLE_SCREEN_FG_BOOTSTYLE = "inverse-primary"


if __name__ == "__main__":
    import tkinter as tk
    from tkinter import font

    root = tk.Tk()

    fonts = list(font.families())
    fonts.sort()

    for f in fonts:
        label = tk.Label(root, text=f, font=(f, 12))
        label.pack()
        print(f)

    root.mainloop()