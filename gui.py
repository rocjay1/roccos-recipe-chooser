from tkinter import *
from tkinter import ttk

class RecipeApp:

    def __init__(self, root):
        #################################
        ########## Upper frame ##########
        #################################

        # Vars
        self.get_option = StringVar()
        self.get_option.set('ing')
        self.get_text = StringVar()
        self.search_text = StringVar()
        self.recipe_text = StringVar()
        self.ings_text = StringVar()
        self.styles_text = StringVar()

        # Widgets
        frame_upper = ttk.Frame(root)
        frame_upper.config(padding=(10,15))

        get_label = ttk.Label(frame_upper, text="Get recipes by:")
        get_ings_btn = ttk.Radiobutton(frame_upper, text="Ingredients", 
            variable=self.get_option, value = 'ing')
        get_styles_btn = ttk.Radiobutton(frame_upper, text="Styles", 
            variable=self.get_option, value='sty')
        get_entry = ttk.Entry(frame_upper)
        get_btn = ttk.Button(frame_upper, text='Submit')

        sep1 = ttk.Separator(frame_upper, orient=HORIZONTAL)

        search_label = ttk.Label(frame_upper, text = 'Search by name:')
        search_entry = ttk.Entry(frame_upper)
        search_btn = ttk.Button(frame_upper, text = 'Search')

        sep2 = ttk.Separator(frame_upper, orient=HORIZONTAL)

        recipe_label = ttk.Label(frame_upper, text = "Recipe:")
        ings_label = ttk.Label(frame_upper, text = "Ingredients:")
        styles_label = ttk.Label(frame_upper, text = "Styles:")
        recipe_entry = ttk.Entry(frame_upper)
        ings_entry = ttk.Entry(frame_upper)
        styles_entry = ttk.Entry(frame_upper)
        add_btn = ttk.Button(frame_upper, text = 'Add')
        remove_btn = ttk.Button(frame_upper, text = 'Remove')
        update_btn = ttk.Button(frame_upper, text = 'Update')
        clear_btn = ttk.Button(frame_upper, text = 'Clear')

        # Geometry
        frame_upper.grid(row=0, column=0)

        get_label.grid(row=0, column=0, sticky='w')
        get_ings_btn.grid(row=0, column=1, sticky='e', padx=5, pady=5)
        get_styles_btn.grid(row=0, column=2, sticky='w', padx=5, pady=5)
        get_entry.grid(row=1, column=0, columnspan=3, sticky='ew')
        get_btn.grid(row=1, column=3, sticky='w')

        sep1.grid(row=2, column=0, columnspan=4, sticky='nsew', pady=30)

        search_label.grid(row = 3, column = 0, sticky='e')
        search_entry.grid(row = 3, column = 1, columnspan=2, sticky='w')
        search_btn.grid(row = 3, column = 3, sticky='w')

        sep2.grid(row=4, column=0, columnspan=4, sticky='nsew', pady=30)

        recipe_label.grid(row = 5, column = 0, sticky='e')
        ings_label.grid(row = 6, column = 0, sticky='e')
        styles_label.grid(row = 7, column = 0, sticky='e')
        recipe_entry.grid(row = 5, column = 1, columnspan=3, sticky='ew')
        ings_entry.grid(row = 6, column = 1, columnspan=3, sticky='ew')
        styles_entry.grid(row = 7, column = 1, columnspan=3, sticky='ew')
        add_btn.grid(row=8, column=0, sticky="e", pady=10)
        remove_btn.grid(row=8, column=1, sticky="ew")
        update_btn.grid(row=8, column=2, sticky="ew")
        clear_btn.grid(row=8, column=3, sticky="w")

        ################################# 
        ########## Lower frame ########## 
        ################################# 

        # Vars
        self.columns = ['Recipe', 'Ingredients', 'Styles']

        # Widgets
        frame_lower = ttk.Frame(root)
        frame_lower.config(padding=(10,18))

        recipe_treeview = ttk.Treeview(frame_lower, columns=self.columns, show='headings')
        recipe_treeview.column('Recipe', width=150)
        recipe_treeview.heading('Recipe', text='Recipe')
        recipe_treeview.column('Ingredients', width=250)
        recipe_treeview.heading('Ingredients', text='Ingredients')
        recipe_treeview.column('Styles', width=250)
        recipe_treeview.heading('Styles', text='Styles')

        scrollbar = ttk.Scrollbar(frame_lower, orient=VERTICAL, command=recipe_treeview.yview)
        recipe_treeview.config(yscrollcommand=scrollbar.set)

        # Geometry
        frame_lower.grid(row=0, column=1, sticky='ns')

        recipe_treeview.pack(side=LEFT, fill=Y)

        scrollbar.pack(side=RIGHT, fill=Y)


if __name__ == '__main__':
    master = Tk()
    app = RecipeApp(master)
    master.mainloop()