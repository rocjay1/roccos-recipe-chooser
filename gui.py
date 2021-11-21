from tkinter import *
from tkinter import ttk

class RecipeApp:

    def __init__(self, root):
        #################################
        ########## Upper frame ##########
        #################################

        # Widgets
        frame_upper = ttk.Frame(root)
        notebook = ttk.Notebook(frame_upper)

        # Geometry
        frame_upper.pack()
        notebook.pack()

        ############################
        ########## Tab 1 ###########
        ############################

        # Vars
        self.edit_option = StringVar()
        self.add_option = IntVar()
        self.edit_option.set("Recipe")
        self.add_option.set(1)
        
        # Widgets
        tab1 = ttk.Frame(notebook)
        notebook.add(tab1, text = "Add/Delete")
        
        tab1_recipe_btn = ttk.Radiobutton(tab1, text = 'Recipe', variable = self.edit_option, 
            value = 'Recipe', command = self.disable_tab1_entries)
        tab1_attrs_btn = ttk.Radiobutton(tab1, text = 'Attributes', variable = self.edit_option, 
            value = 'Attributes', command = self.disable_tab1_entries)
        tab1_spacer1 = ttk.Label(tab1, text="")
        tab1_add_btn = ttk.Radiobutton(tab1, text = 'Add', variable = self.add_option, 
            value = 1, command = self.disable_tab1_entries)
        tab1_del_btn = ttk.Radiobutton(tab1, text = 'Delete', variable = self.add_option, 
            value = 0, command = self.disable_tab1_entries)

        tab1_recipe_label = ttk.Label(tab1, text = "Recipe:")
        tab1_ings_label = ttk.Label(tab1, text = "Ingredients:")
        tab1_styles_label = ttk.Label(tab1, text = "Styles:")
        tab1_recipe_entry = ttk.Entry(tab1, width = 30)
        self.tab1_ings_entry = ttk.Entry(tab1, width = 30)
        # self.entry_ings.configure(state = 'disabled') 
        self.tab1_styles_entry = ttk.Entry(tab1, width = 30)
        # self.entry_styles.configure(state = 'disabled')

        tab1_submit_btn = ttk.Button(tab1, text = 'Submit')

        # Geometry
        tab1_recipe_btn.grid(row=0, column=0)
        tab1_attrs_btn.grid(row=0, column=1)
        tab1_spacer1.grid(row=0, column=3, padx=10)
        tab1_add_btn.grid(row=0, column=4)
        tab1_del_btn.grid(row=0, column=5)

        tab1_recipe_label.grid(row = 1, column = 0, sticky='e')
        tab1_ings_label.grid(row = 2, column = 0, sticky='e')
        tab1_styles_label.grid(row = 3, column = 0, sticky='e')
        tab1_recipe_entry.grid(row = 1, column = 1, columnspan=5)
        self.tab1_ings_entry.grid(row = 2, column = 1, columnspan=5)
        self.tab1_styles_entry.grid(row = 3, column = 1, columnspan=5)

        tab1_submit_btn.grid(row = 4, column = 0, columnspan = 6)

        ############################
        ########## Tab 2 ###########
        ############################

    #     # Vars
    #     self.edit_option = StringVar()
    #     self.add_option = IntVar()
    #     self.edit_option.set("Recipe")
    #     self.add_option.set(1)
        
    #     # Widgets
    #     tab1 = ttk.Frame(notebook)
    #     notebook.add(tab1, text = "Add/Delete")
        
    #     btn1 = ttk.Radiobutton(tab1, text = 'Recipe', variable = self.edit_option, 
    #         value = 'Recipe', command = self.check_disabled)
    #     btn2 = ttk.Radiobutton(tab1, text = 'Ingredient', variable = self.edit_option, 
    #         value = 'Ingredient', command = self.check_disabled)
    #     btn3 = ttk.Radiobutton(tab1, text = 'Style', variable = self.edit_option, 
    #         value = 'Style', command = self.check_disabled)
    #     spacer1 = ttk.Label(tab1, text="")
    #     btn4 = ttk.Radiobutton(tab1, text = 'Add', variable = self.add_option, 
    #         value = 1)
    #     btn5 = ttk.Radiobutton(tab1, text = 'Delete', variable = self.add_option, 
    #         value = 0)

    #     ttk.Label(tab1, text = "Recipe:").grid(row = 1, column = 0, sticky='e')
    #     ttk.Label(tab1, text = "Old Name:").grid(row = 2, column = 0, sticky='e')
    #     ttk.Label(tab1, text = "New Name:").grid(row = 3, column = 0, sticky='e')
    #     entry_Recipe = ttk.Entry(tab1, width = 30)
    #     self.entry_Old_Name = ttk.Entry(tab1, width = 30)
    #     self.entry_Old_Name.configure(state = 'disabled') 
    #     entry_New_Name = ttk.Entry(tab1, width = 30)

    #     ttk.Button(tab1, text = 'Submit').grid(row = 4, column = 0, columnspan = 6)

    #     # Geometry
    #     btn1.grid(row=0, column=0)
    #     btn2.grid(row=0, column=1)
    #     btn3.grid(row=0, column=2)
    #     spacer1.grid(row=0, column=3, padx=10)
    #     btn4.grid(row=0, column=4)
    #     btn5.grid(row=0, column=5)

    #     entry_Recipe.grid(row = 1, column = 1, columnspan=5)
    #     self.entry_Old_Name.grid(row = 2, column = 1, columnspan=5)
    #     entry_New_Name.grid(row = 3, column = 1, columnspan=5)

    # # def disable(self):
    # #     if self.edit_option.get() == 'Recipe':
    # #         self.entry_Old_Name.configure(state = 'disabled')
    # #         self.entry_Old_Name.update()
    # #     else:
    # #         self.entry_Old_Name.configure(state = 'normal')
    # #         self.entry_Old_Name.update()

    def disable_tab1_entries(self):
        if self.edit_option.get() == 'Recipe' and self.add_option.get() == 0:
            self.tab1_ings_entry.configure(state = 'disabled')
            self.tab1_ings_entry.update()
            self.tab1_styles_entry.configure(state = 'disabled')
            self.tab1_styles_entry.update()     
        else:
            self.tab1_ings_entry.configure(state = 'normal')
            self.tab1_ings_entry.update()
            self.tab1_styles_entry.configure(state = 'normal')
            self.tab1_styles_entry.update()
        

if __name__ == '__main__':
    master = Tk()
    app = RecipeApp(master)
    master.mainloop()