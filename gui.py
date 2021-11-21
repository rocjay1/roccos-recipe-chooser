from tkinter import *
from tkinter import ttk

class RecipeApp:

    def __init__(self, root):
        #################################
        ########## Upper frame ##########
        #################################

        # Widgets
        frame_upper = ttk.Frame(root)
        frame_upper.config(padding=(10,0))

        search_label = ttk.Label(frame_upper, text = 'Search by name:')
        search_entry = ttk.Entry(frame_upper, width = 30)
        search_btn = ttk.Button(frame_upper, text = 'Search')

        recipe_label = ttk.Label(frame_upper, text = "Recipe:")
        ings_label = ttk.Label(frame_upper, text = "Ingredients:")
        styles_label = ttk.Label(frame_upper, text = "Styles:")
        recipe_entry = ttk.Entry(frame_upper, width = 30)
        ings_entry = ttk.Entry(frame_upper, width = 30)
        styles_entry = ttk.Entry(frame_upper, width = 30)
        add_btn = ttk.Button(frame_upper, text = 'Add Recipe')
        remove_btn = ttk.Button(frame_upper, text = 'Remove Recipe')
        update_btn = ttk.Button(frame_upper, text = 'Update Recipe')
        clear_btn = ttk.Button(frame_upper, text = 'Clear Input')

        # Geometry
        frame_upper.pack()
        
        search_label.grid(row = 0, column = 0, pady=20, sticky='e')
        search_entry.grid(row = 0, column = 1, columnspan=2, sticky='ew')
        search_btn.grid(row = 0, column = 3, sticky='nsew')

        recipe_label.grid(row = 1, column = 0, sticky='e')
        ings_label.grid(row = 2, column = 0, sticky='e')
        styles_label.grid(row = 3, column = 0, sticky='e')
        recipe_entry.grid(row = 1, column = 1, columnspan=4, sticky='w')
        ings_entry.grid(row = 2, column = 1, columnspan=4, sticky='w')
        styles_entry.grid(row = 3, column = 1, columnspan=4, sticky='w')
        add_btn.grid(row=4, column=0, pady=10, sticky="nsew")
        remove_btn.grid(row=4, column=1, sticky="nsew")
        update_btn.grid(row=4, column=2, sticky="nsew")
        clear_btn.grid(row=4, column=3, sticky="nsew")

if __name__ == '__main__':
    master = Tk()
    app = RecipeApp(master)
    master.mainloop()