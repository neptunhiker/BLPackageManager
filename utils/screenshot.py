from PIL import ImageGrab

def save_app_window_as_png(app, file_name: str, height_adjustment: int=0) -> None:
    """
    Save the screen to a png file
    :param app: the application that is being used
    :param file_name: the name under which the screenshot shall be saved
    :param height_adjustment: adjust the height up or down for fine tuning
    :return None
    """
    geometry = app.winfo_geometry()

    # Split the string into a list of four strings
    geometry = geometry.split("+")
    width, height, left, top = map(int, geometry[0].split("x") + geometry[1:])

    height += height_adjustment

    image = ImageGrab.grab(bbox=(left, top, width, height + top))

    if not file_name.endswith(".png"):
        raise ValueError("File name must end with .png")
    
    image.save(file_name)
