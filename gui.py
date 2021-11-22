from tkinter import *
from tkinter import ttk
from read_write import *
from recipe_classes import *

class RecipeApp:

    def __init__(self, root):

        self.db = read_JSON("recipes.json")

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
            variable=self.get_option, value='ing')
        get_styles_btn = ttk.Radiobutton(frame_upper, text="Styles", 
            variable=self.get_option, value='sty')
        get_entry = ttk.Entry(frame_upper)
        get_btn = ttk.Button(frame_upper, text='Submit')

        # sep1 = ttk.Separator(frame_upper, orient=HORIZONTAL)
        sep1 = ttk.Label(frame_upper, text="")

        search_label = ttk.Label(frame_upper, text='Search by name:')
        search_entry = ttk.Entry(frame_upper)
        search_btn = ttk.Button(frame_upper, text='Search')

        # sep2 = ttk.Separator(frame_upper, orient=HORIZONTAL)
        sep2 = ttk.Label(frame_upper, text="")

        recipe_label = ttk.Label(frame_upper, text="Recipe:")
        ings_label = ttk.Label(frame_upper, text="Ingredients:")
        styles_label = ttk.Label(frame_upper, text="Styles:")
        self.recipe_entry = ttk.Entry(frame_upper, textvariable=self.recipe_text)
        self.ings_entry = ttk.Entry(frame_upper, textvariable=self.ings_text)
        self.styles_entry = ttk.Entry(frame_upper, textvariable=self.styles_text)
        add_btn = ttk.Button(frame_upper, text='Add', command=self.add_recipe)
        remove_btn = ttk.Button(frame_upper, text='Remove')
        update_btn = ttk.Button(frame_upper, text='Update')
        clear_btn = ttk.Button(frame_upper, text='Clear', command=self.clear_text)

        # Geometry
        frame_upper.grid(row=0, column=0)

        get_label.grid(row=0, column=0, sticky='w')
        get_ings_btn.grid(row=0, column=1, sticky='e', padx=5, pady=5)
        get_styles_btn.grid(row=0, column=2, sticky='w', padx=5, pady=5)
        get_entry.grid(row=1, column=0, columnspan=3, sticky='ew')
        get_btn.grid(row=1, column=3, sticky='w')

        sep1.grid(row=2, column=0, columnspan=4, sticky='nsew', pady=10)

        search_label.grid(row=3, column=0, sticky='e')
        search_entry.grid(row=3, column=1, columnspan=2, sticky='w')
        search_btn.grid(row=3, column=3, sticky='w')

        sep2.grid(row=4, column=0, columnspan=4, sticky='nsew', pady=10)

        recipe_label.grid(row=5, column=0, sticky='e')
        ings_label.grid(row=6, column=0, sticky='e')
        styles_label.grid(row=7, column=0, sticky='e')
        self.recipe_entry.grid(row=5, column=1, columnspan=3, sticky='ew')
        self.ings_entry.grid(row=6, column=1, columnspan=3, sticky='ew')
        self.styles_entry.grid(row=7, column=1, columnspan=3, sticky='ew')
        add_btn.grid(row=8, column=0, sticky="e", pady=10)
        remove_btn.grid(row=8, column=1, sticky="ew")
        update_btn.grid(row=8, column=2, sticky="ew")
        clear_btn.grid(row=8, column=3, sticky="w")

        ################################# 
        ########## Lower frame ########## 
        ################################# 

        # Vars

        # Widgets
        frame_lower = ttk.Frame(root)
        frame_lower.config(padding=(10,18))

        self.recipe_treeview = ttk.Treeview(frame_lower)
        self.recipe_treeview.column("#0", width=250)
        self.recipe_treeview.bind('<<TreeviewSelect>>', self.select_recipe)

        scrollbar = ttk.Scrollbar(frame_lower, orient=VERTICAL, command=self.recipe_treeview.yview)
        self.recipe_treeview.config(yscrollcommand=scrollbar.set)

        # Geometry
        frame_lower.grid(row=0, column=1, sticky='ns')

        self.recipe_treeview.pack(side=LEFT, fill=Y)

        scrollbar.pack(side=RIGHT, fill=Y)

    def format_to_list(self, str):
        lst = str.split(",") 
        lst = list(map(lambda s: s.lower().strip(), lst))
        return lst

    def format_to_string(self, str):
        return str.lower().strip()
    
    def open_children(self, parent):
        self.recipe_treeview.item(parent, open=True)
        for child in self.recipe_treeview.get_children(parent):
            self.open_children(child)

    def close_children(self, parent):
        self.recipe_treeview.item(parent, open=False)
        for child in self.recipe_treeview.get_children(parent):
            self.open_children(child)

    def delete_children(self):
        self.recipe_treeview.delete(*self.recipe_treeview.get_children())

    def populate_from_recipebook(self):
        self.delete_children()

        for recipe in self.db.recipes:
            self.recipe_treeview.insert('', 'end', f'name_{recipe}', text=f'{recipe}')
            self.recipe_treeview.insert(f'name_{recipe}', 'end', f'ings_{recipe}', 
                text="Ingredients")
            for ingredient in self.db.recipes[recipe].ingredients:
                self.recipe_treeview.insert(f'ings_{recipe}', 'end', f'ing_{ingredient}', 
                    text=f'{ingredient}')
            self.recipe_treeview.insert(f'name_{recipe}', 'end', f'styles_{recipe}', text="Styles")
            for style in self.db.recipes[recipe].styles:
                self.recipe_treeview.insert(f'styles_{recipe}', 'end', f'style_{style}', text=f'{style}')

    def select_recipe(self, event):
        for child in self.recipe_treeview.get_children():
            self.close_children(child)

        node = self.recipe_treeview.selection()[0]
        if self.recipe_treeview.parent(node) == '':
            self.open_children(node)

            self.recipe_entry.delete(0, END)
            self.recipe_entry.insert(END, self.recipe_treeview.item(node)['text'])

            ings_node = self.recipe_treeview.get_children(node)[0]
            ings_node_children = self.recipe_treeview.get_children(ings_node)
            ing_str = ''
            for child in ings_node_children:
                ing = self.recipe_treeview.item(child)['text']
                if ing_str == '':
                    ing_str += ing
                else:
                    ing_str += f', {ing}'
            self.ings_entry.delete(0, END)
            self.ings_entry.insert(END, ing_str)

            styles_node = self.recipe_treeview.get_children(node)[1]
            styles_node_children = self.recipe_treeview.get_children(styles_node)
            style_str = ''
            for child in styles_node_children:
                style = self.recipe_treeview.item(child)['text']
                if style_str == '':
                    style_str += style
                else:
                    style_str += f', {style}'
            self.styles_entry.delete(0, END)
            self.styles_entry.insert(END, style_str)

    def clear_text(self):
        self.recipe_entry.delete(0, END)
        self.ings_entry.delete(0, END)
        self.styles_entry.delete(0, END)

    def add_recipe(self):
        name = self.format_to_string(self.recipe_text.get())
        ings = self.format_to_list(self.ings_text.get())
        styles = self.format_to_list(self.styles_text.get())
        self.db.add_recipe(name, ings, styles)
        self.clear_text()
        self.populate_from_recipebook()
        self.recipe_treeview.selection_add(f'name_{name}')
        
        
if __name__ == '__main__':
    master = Tk()
    app = RecipeApp(master)
    app.populate_from_recipebook()
    master.mainloop()