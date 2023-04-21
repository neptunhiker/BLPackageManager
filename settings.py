THEMENAME = "beginnerluftearthy"
THEMENAME = "beginnerluftdark"
THEMENAME = "beginnerluftclassic"
THEMENAME = "superhero"
THEMENAME = "beginnerluftclassic"
# THEMENAME = "vapor"
# THEMENAME = "beginnerluftdark"


FONT = "DIN condensed"
SIZE_ADJUSTER = 3
FONT_SIZE_XXXL = 96 + SIZE_ADJUSTER
FONT_SIZE_XXL = 64 + SIZE_ADJUSTER
FONT_SIZE_XL = 48 + SIZE_ADJUSTER
FONT_SIZE_L = 32 + SIZE_ADJUSTER
FONT_SIZE_M = 24 + SIZE_ADJUSTER
FONT_SIZE_S = 16 + SIZE_ADJUSTER
FONT_SIZE_XS = 14 + SIZE_ADJUSTER
FONT_SIZE_XXS = 10 + SIZE_ADJUSTER

if THEMENAME == "beginnerluftclassic":
    ALL_BOOTSTYLE_FRAME_BOTTOM = "secondary"
    ALL_BOOTSTYLE_FRAME_TOP_BG = "primary"
    ALL_BOOTSTYLE_HOVER = "info"
    ALL_BOOTSTYLE_SELECT = "primary"
    ALL_BOOTSTYLE_SUBHEADING = ""
    HOME_BOOTSTYLE_BG = "light"
    HOME_BOOTSTYLE_TITLE_FG = "inverse-light"
    OVERVIEW_BOOTSTYLE_HEADING = ""
    PACKAGE_BOOTSTYLE_DESCRIPTION = ""
elif THEMENAME == "beginnerluftdark":
    ALL_BOOTSTYLE_FRAME_BOTTOM = "secondary"
    ALL_BOOTSTYLE_FRAME_TOP_BG = "primary"
    ALL_BOOTSTYLE_HOVER = "info"
    ALL_BOOTSTYLE_SELECT = "primary"
    ALL_BOOTSTYLE_SUBHEADING = "primary"
    HOME_BOOTSTYLE_BG = "bg"
    HOME_BOOTSTYLE_TITLE_FG = "primary"
    OVERVIEW_BOOTSTYLE_HEADING = "primary"
    PACKAGE_BOOTSTYLE_DESCRIPTION = "primary"
elif THEMENAME == "vapor":
    ALL_BOOTSTYLE_FRAME_BOTTOM = "secondary"
    ALL_BOOTSTYLE_FRAME_TOP_BG = "primary"
    ALL_BOOTSTYLE_HOVER = "secondary"
    ALL_BOOTSTYLE_SELECT = "success"
    ALL_BOOTSTYLE_SUBHEADING = "secondary"
    HOME_BOOTSTYLE_BG = "bg"
    HOME_BOOTSTYLE_TITLE_FG = "primary"
    OVERVIEW_BOOTSTYLE_HEADING = "secondary"
    PACKAGE_BOOTSTYLE_DESCRIPTION = "light"
else:
    ALL_BOOTSTYLE_FRAME_BOTTOM = "secondary"
    ALL_BOOTSTYLE_FRAME_TOP_BG = "primary"
    ALL_BOOTSTYLE_HOVER = "info"
    ALL_BOOTSTYLE_SELECT = "success"
    ALL_BOOTSTYLE_SUBHEADING = "primary"
    HOME_BOOTSTYLE_BG = "bg"
    HOME_BOOTSTYLE_TITLE_FG = "primary"
    OVERVIEW_BOOTSTYLE_HEADING = "primary"
    PACKAGE_BOOTSTYLE_DESCRIPTION = "primary"


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