from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from backend import *

class RecipeApp:

    def __init__(self, root):

        self.db = read_JSON("recipes.json")

        #################################
        ########## Upper frame ##########
        #################################

        # Vars
        self.get_option = StringVar()
        self.get_option.set('nm')
        self.get_text = StringVar()
        self.search_text = StringVar()
        self.recipe_text = StringVar()
        self.ings_text = StringVar()
        self.styles_text = StringVar()

        # Widgets
        frame_upper = ttk.Frame(root)
        frame_upper.config(padding=(10,5))

        btn_frame = ttk.Frame(frame_upper) # Radiobuttons
        get_name_btn = ttk.Radiobutton(btn_frame, text="Name", variable=self.get_option, value='nm')
        get_ings_btn = ttk.Radiobutton(btn_frame, text="Ingredients", variable=self.get_option, value='ing')
        get_styles_btn = ttk.Radiobutton(btn_frame, text="Styles", variable=self.get_option, value='sty')

        get_label = ttk.Label(frame_upper, text="Get recipes by:")
        get_entry = ttk.Entry(frame_upper)
        get_btn = ttk.Button(frame_upper, text='Submit')

        sep1 = ttk.Label(frame_upper, text="")

        recipe_label = ttk.Label(frame_upper, text="Recipe:")
        ings_label = ttk.Label(frame_upper, text="Ingredients:")
        styles_label = ttk.Label(frame_upper, text="Styles:")
        self.recipe_entry = ttk.Entry(frame_upper, textvariable=self.recipe_text)
        self.ings_entry = ttk.Entry(frame_upper, textvariable=self.ings_text)
        self.styles_entry = ttk.Entry(frame_upper, textvariable=self.styles_text)

        add_btn = ttk.Button(frame_upper, text='Add', command=self.add_recipe) # Action buttons
        remove_btn = ttk.Button(frame_upper, text='Remove')
        update_btn = ttk.Button(frame_upper, text='Update', command=self.update_recipe)
        clear_btn = ttk.Button(frame_upper, text='Clear', command=self.clear_text)

        # Geometry
        frame_upper.grid(row=0, column=0, sticky='nsew')

        btn_frame.grid(row=0, column=1, columnspan=3, sticky='w', pady=10)
        get_name_btn.pack(side=LEFT, padx=5)
        get_ings_btn.pack(side=LEFT, padx=5)
        get_styles_btn.pack(side=LEFT, padx=5)

        get_label.grid(row=0, column=0, sticky='w')
        get_entry.grid(row=1, column=0, columnspan=3, sticky='ew')
        get_btn.grid(row=1, column=3, sticky='w')

        sep1.grid(row=2, column=0, columnspan=4, sticky='nsew')

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
        frame_lower.config(padding=(10,5))

        self.recipe_treeview = ttk.Treeview(frame_lower, height=12)
        self.recipe_treeview.column("#0", width=300)
        self.recipe_treeview.bind('<<TreeviewSelect>>', self.select_recipe)

        scrollbar = ttk.Scrollbar(frame_lower, orient=VERTICAL, 
            command=self.recipe_treeview.yview)
        self.recipe_treeview.config(yscrollcommand=scrollbar.set)

        ref_btn = ttk.Button(frame_lower, text="Refresh")

        # Geometry
        frame_lower.grid(row=1, column=0)

        self.recipe_treeview.grid(row=0, column=0, sticky='nsew')

        scrollbar.grid(row=0, column=0, sticky='nse')

        ref_btn.grid(row=1, column=0, pady=10)

    #############################  
    ########## Methods ########## 
    #############################  

    # Formatting helper methods

    def format_to_list(self, str):
        lst = str.split(",") 
        lst = list(map(lambda s: s.lower().strip(), lst))
        return lst

    def format_to_string(self, str):
        return str.lower().strip()
    
    # Treeview helper methods

    def open_node_children(self, parent):
        self.recipe_treeview.item(parent, open=True)
        for child in self.recipe_treeview.get_children(parent):
            self.open_node_children(child)

    def close_node_children(self, parent):
        self.recipe_treeview.item(parent, open=False)
        for child in self.recipe_treeview.get_children(parent):
            self.open_node_children(child)

    def delete_all_children(self):
        self.recipe_treeview.delete(*self.recipe_treeview.get_children())

    def insert_recipe(self, recipe, index='end'):
        self.recipe_treeview.insert('', str(index), f'name_{recipe}', text=f'{recipe}')

        self.recipe_treeview.insert(f'name_{recipe}', 'end', 
            f'name_{recipe}_ing', text="ingredients")
        for ingredient in self.db.recipes[recipe].ingredients:
            self.recipe_treeview.insert(f'name_{recipe}_ing', 'end', 
                f'name_{recipe}_ing_{ingredient}', text=f'{ingredient}')

        self.recipe_treeview.insert(f'name_{recipe}', 'end', 
            f'name_{recipe}_style', text="styles")
        for style in self.db.recipes[recipe].styles:
            self.recipe_treeview.insert(f'name_{recipe}_style', 'end', 
                f'name_{recipe}_style_{style}', text=f'{style}')
    
    def delete_recipe(self, recipe):
        self.recipe_treeview.delete(f'name_{recipe}')

    # Main methods/callbacks

    def populate_from_recipebook(self, recipes=[]):
        if not recipes:
            recipes = self.db.recipes
        self.delete_all_children()
        for recipe in recipes:
            self.insert_recipe(recipe)

    def select_recipe(self, event):
        # Refresh tree
        for child in self.recipe_treeview.get_children():
            self.close_node_children(child)
        
        # If nothing is selected, do nothing
        if not self.recipe_treeview.selection():
            return
        
        # Otherwise, if a recipe is selected, display contents and populate entry fields
        node = self.recipe_treeview.selection()[0]
        global sel_recipe
        sel_recipe = self.recipe_treeview.item(node)['text']
        if self.recipe_treeview.parent(node) == '':
            self.open_node_children(node)

            # Populate name
            self.recipe_entry.delete(0, END)
            self.recipe_entry.insert(END, self.recipe_treeview.item(node)['text'])

            # Populate ingredients and styles
            attrs = []
            for i in range(0, 2):
                sub_node = self.recipe_treeview.get_children(node)[i]
                children = self.recipe_treeview.get_children(sub_node)
                fin_str = ''
                for child in children:
                    add_str = self.recipe_treeview.item(child)['text']
                    if fin_str == '':
                        fin_str += add_str
                    else:
                        fin_str += f', {add_str}'
                attrs.append(fin_str)

            self.ings_entry.delete(0, END)
            self.ings_entry.insert(END, attrs[0])
            self.styles_entry.delete(0, END)
            self.styles_entry.insert(END, attrs[1])

    def clear_text(self):
        if not self.recipe_treeview.selection():
            pass
        else:
            # If something is selected, unselect
            self.recipe_treeview.selection_remove(self.recipe_treeview.selection()[0])
        self.recipe_entry.delete(0, END)
        self.ings_entry.delete(0, END)
        self.styles_entry.delete(0, END)

    def add_recipe(self):
        # If the recipe already exists, prompt user for update instead of add
        name = self.format_to_string(self.recipe_text.get())
        if name in self.db.recipes:
            prompt = messagebox.askyesno("Update?", 
            "A recipe with that name already exists. Woud you like to update it?")
            if prompt == True:
                self.update_recipe()
            return
        # Else add as usual
        ings = self.format_to_list(self.ings_text.get())
        styles = self.format_to_list(self.styles_text.get())
        self.db.add_recipe(name, ings, styles)
        self.insert_recipe(name)
        self.recipe_treeview.selection_set(f'name_{name}')

    def update_recipe(self):
        # To update, something must be selected
        if not self.recipe_treeview.selection():
            messagebox.showerror('No recipe selected', 'Please select a recipe to update')
            return
        name = self.format_to_string(self.recipe_text.get())
        ings = self.format_to_list(self.ings_text.get())
        styles = self.format_to_list(self.styles_text.get())
        self.db.update_recipe(sel_recipe, name, ings, styles)
        i = self.recipe_treeview.index(f'name_{sel_recipe}')
        self.delete_recipe(sel_recipe)
        self.insert_recipe(name, i)
        self.recipe_treeview.selection_set(f'name_{name}')
        

if __name__ == '__main__':
    master = Tk()
    app = RecipeApp(master)
    app.populate_from_recipebook()
    master.mainloop()