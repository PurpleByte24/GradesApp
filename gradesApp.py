from guizero import *
import importlib
import savedGrades as ext_file
    
class GRADES_APP():
    def __init__(self):
        self.mode = 0        
        self.GRADE_BUTTONS = None
        self.ALL_TESTS = None
        self.BACK = None
        self.AVERAGE = None
        self.subject = None
        self.new_tst = None
        self.chosen_field = 1
        
    def get_grades(self):
        m_names, m_grades, m_weights = ext_file.m_names, ext_file.m_grades, ext_file.m_weights
        i_names, i_grades, i_weights = ext_file.i_names, ext_file.i_grades, ext_file.i_weights
        c_names, c_grades, c_weights = ext_file.c_names, ext_file.c_grades, ext_file.c_weights
        phy_names, phy_grades, phy_weights = ext_file.phy_names, ext_file.phy_grades, ext_file.phy_weights
        b_names, b_grades, b_weights = ext_file.b_names, ext_file.b_grades, ext_file.b_weights
        d_names, d_grades, d_weights = ext_file.d_names, ext_file.d_grades, ext_file.d_weights
        e_names, e_grades, e_weights = ext_file.e_names, ext_file.e_grades, ext_file.e_weights
        f_names, f_grades, f_weights = ext_file.f_names, ext_file.f_grades, ext_file.f_weights
        wr_names, wr_grades, wr_weights = ext_file.wr_names, ext_file.wr_grades, ext_file.wr_weights
        ges_names, ges_grades, ges_weights = ext_file.ges_names, ext_file.ges_grades, ext_file.ges_weights
        geo_names, geo_grades, geo_weights = ext_file.geo_names, ext_file.geo_grades, ext_file.geo_weights
        mu_names, mu_grades, mu_weights = ext_file.mu_names, ext_file.mu_grades, ext_file.mu_weights
        päd_names, päd_grades, päd_weights = ext_file.päd_names, ext_file.päd_grades, ext_file.päd_weights
        phi_names, phi_grades, phi_weights = ext_file.phi_names, ext_file.phi_grades, ext_file.phi_weights
        self.all_grades = [m_grades, i_grades, c_grades, phy_grades, b_grades, d_grades, e_grades, f_grades, wr_grades, ges_grades, geo_grades, mu_grades, päd_grades, phi_grades]
        self.all_names = [m_names, i_names, c_names, phy_names, b_names, d_names, e_names, f_names, wr_names, ges_names, geo_names, mu_names, päd_names, phi_names]
        self.all_weights = [m_weights, i_weights, c_weights, phy_weights, b_weights, d_weights, e_weights, f_weights, wr_weights, ges_weights, geo_weights, mu_weights, päd_weights, phi_weights]
        Mathematik = self.get_average(m_grades, m_weights)    
        Informatik = self.get_average(i_grades, i_weights)
        Chemie = self.get_average(c_grades, c_weights)
        Physik = self.get_average(phy_grades, phy_weights)
        Biologie = self.get_average(b_grades, b_weights)
        Deutsch = self.get_average(d_grades, d_weights)
        Englisch = self.get_average(e_grades, e_weights)
        Französisch = self.get_average(f_grades, f_weights)
        Wirtschaft_Recht = self.get_average(wr_grades, wr_weights)
        Geschichte = self.get_average(ges_grades, ges_weights)
        Geographie = self.get_average(geo_grades, geo_weights)
        Musik = self.get_average(mu_grades, mu_weights)
        Päd = self.get_average(päd_grades, päd_weights)
        Philosophie = self.get_average(phi_grades, phi_weights)
        self.all_subjects = [
            Mathematik,
            Informatik,
            Chemie,
            Physik,
            Biologie,
            Deutsch,
            Englisch,
            Französisch,
            Wirtschaft_Recht,
            Geschichte,
            Geographie,
            Musik,
            Päd,
            Philosophie]
        self.grades = [(classes[0], Mathematik),
                   (classes[1], Informatik),
                   (classes[2], Chemie),
                   (classes[3], Physik),
                   (classes[4], Biologie),
                   (classes[5], Deutsch),
                   (classes[6], Englisch),
                   (classes[7], Französisch),
                   (classes[8], Wirtschaft_Recht),
                   (classes[9], Geschichte),
                   (classes[10], Geographie),                   
                   (classes[11], Musik),
                   (classes[12], Päd),
                   (classes[13], Philosophie)]
        self.make_grade_buttons()
        
    def get_average(self, grades, weights):
        try:
            sum_product = sum(grade*weight for grade, weight in zip(grades, weights))
            sum_weights = sum(weights)
            
            average = sum_product/sum_weights
        except ZeroDivisionError:
            average = 0
        return round(average, 3)

    def make_grade_buttons(self):
        self.GRADE_BUTTONS = [PushButton(app, text=(f"{i[0]}: {i[1]}"), grid=[0, index], width=15, command=self.button_commands, args=[i[0], index])for index, i in enumerate(self.grades)]
        
    def button_commands(self, commander, index):
        for button in self.GRADE_BUTTONS:
            button.destroy()
        self.index = index
        self.commander = commander
        self.subject = Text(app, text=commander, grid=[1, 0], size=30, color="white")
        if self.all_subjects[index] != 0:
            avr = self.all_subjects[index]
            self.AVERAGE = Text(app, text=f"Average = {avr}", grid=[1, 1], size=20, color="red")
        self.ALL_LABELS = Text(app, text=f"Name:	Grade:	Weight:", grid=[1, 2], size=20, color="white")
        self.ALL_TESTS = [Text(app, text=f"{name}	|{grade}|	{weight}", grid=[1, index+3], size=20, color="white")for index, (grade, name, weight) in enumerate(zip(self.all_grades[index], self.all_names[index], self.all_weights[index]))]
        self.BACK = PushButton(app, text="Back", grid=[0, 0], width=8, command=self.go_back, args=[1])
        self.new_tst = PushButton(app, text="New Test", grid=[0, 1], width=8, command=self.create_new_test)
        
    def go_back(self, mode):
        self.BACK.destroy()
        self.new_tst.destroy()
        self.subject.destroy()
        try:
            self.AVERAGE.destroy()
        except (AttributeError, ValueError):
            pass        
        for test in self.ALL_TESTS:
            try:
                test.destroy()                
            except AttributeError:
                pass
        self.ALL_LABELS.destroy()
        self.index = None
        self.commander = None
        if mode == 1:
            self.make_grade_buttons()
        
    def create_new_test(self):
        self.new_window = Window(app, height=150, width=200, title="Create a New Test")
        app.hide()
        
        self.enter_grade = Text(self.new_window, text="Enter The Grade", width=self.new_window.width, align="top", size=23, color="white")
        self.enter_name = Text(self.new_window, text="Enter The Name", width=self.new_window.width, align="top", size=23, color="white")
        self.enter_weight = Text(self.new_window, text="Enter The Weight", width=self.new_window.width, align="top", size=23, color="white")
        self.NEXT = PushButton(self.new_window, text="Next", align="top", width=8, command=self.get_chosen_field, args=[])
        self.NEXT.disable()
                
        self.new_window.when_key_pressed = self.key_pressed
        
    def get_chosen_field(self):
        global first, predot, decis
        first = True
        self.chosen_field += 1
        self.NEXT.disable()
        if self.chosen_field > 3:
            self.return_from_new_tst()
            first = True
            predot = True       
            decis = 0
            
    def key_pressed(self, event):
        global first, predot, decis
        key = event.key
        if self.chosen_field == 1:
            if key in all_numbers:
                if predot and key != "0" and key in numbers:
                    if first:
                        first = False
                        self.enter_grade.value = ""
                    self.enter_grade.append(key)
                    self.enter_grade.append(".")
                    if key == "6":
                        self.enter_grade.append("0")
                        decis += 1
                    predot = False                
                elif not predot and decis <= 2 and self.enter_grade.value[0] != "6" and key in all_numbers:
                    decis += 1
                    self.enter_grade.append(key)            
            elif event.tk_event.keysym == "BackSpace" and not first:
                if self.enter_grade.value[0] == "6":
                    self.enter_grade.value = self.enter_grade.value[:-1]
                if self.enter_grade.value[-1] == ".":
                    self.enter_grade.value = self.enter_grade.value[:-1]
                self.enter_grade.value = self.enter_grade.value[:-1]                                                        
                if decis > 0:
                    decis -= 1
                if self.enter_grade.value == "":
                    self.enter_grade.value = "Enter The Grade"
                    first = True
                    predot = True
                    decis = 0
            if decis >= 1:
                self.NEXT.enable()
            else:
                self.NEXT.disable()
                
        if self.chosen_field == 2:
            predot = True
            decis = 0
            if key in letters:
                if first:
                    first = False
                    self.enter_name.value = ""
                self.enter_name.append(key)                            
            elif event.tk_event.keysym == "BackSpace" and not first:
                self.enter_name.value = self.enter_name.value[:-1]                                                        
                if self.enter_name.value == "":
                    self.enter_name.value = "Enter The Name"
                    first = True                    
                    self.NEXT.disable()
            if self.enter_name.value != "Enter The Name":
                self.NEXT.enable()
        
        if self.chosen_field == 3:
            if key in numbers:
                if predot:
                    if first:
                        first = False
                        self.enter_weight.value = ""
                    self.enter_weight.append(key)
                    self.enter_weight.append(".")
                    predot = False                
                elif not predot and decis <= 2:
                    decis += 1
                    self.enter_weight.append(key)            
            elif event.tk_event.keysym == "BackSpace" and not first:
                if self.enter_weight.value[-1] == ".":
                    self.enter_weight.value = self.enter_weight.value[:-1]
                self.enter_weight.value = self.enter_weight.value[:-1]                                                        
                if decis > 0:
                    decis -= 1
                if self.enter_weight.value == "":
                    self.enter_weight.value = "Enter The Weight"
                    first = True
                    predot = True            
            if decis >= 1:
                self.NEXT.enable()
            else:
                self.NEXT.disable()
   
    def return_from_new_tst(self):
        new_grade = self.enter_grade.value
        new_name = self.enter_name.value
        new_weight = self.enter_weight.value
        self.new_window.destroy()
        app.show()
        self.modify_file(new_grade, new_name, new_weight)
        self.mode = 0
        self.go_back(0)
        self.update()
        self.chosen_field = 1
        
    def modify_file(self, adding_grade, adding_name, adding_weight):
        with open("savedGrades.py", "r") as file:
            lines = file.readlines()            
        if lines[self.index].strip()[-2] == "[":
            line1 = lines[self.index].strip()[:-1] + f"{str(adding_grade)}]\n"
            line2 = lines[self.index+14].strip()[:-1] + f"'{str(adding_name)}']\n"
            line3 = lines[self.index+2*14].strip()[:-1] + f"{str(adding_weight)}]\n"            
        else:
            line1 = lines[self.index].strip()[:-1] + f", {str(adding_grade)}]\n"
            line2 = lines[self.index+14].strip()[:-1] + f", '{str(adding_name)}']\n"
            line3 = lines[self.index+2*14].strip()[:-1] + f", {str(adding_weight)}]\n"
        lines[self.index] = line1
        lines[self.index+14] = line2
        lines[self.index+2*14] = line3        
        with open("savedGrades.py", "w") as file:
            file.writelines(lines)
            file.close()
        
    def update(self):        
        if self.mode == 0:
            importlib.reload(ext_file)
            self.get_grades()            
            self.mode = 1 



## inizialization
app = App(title="grades", width=500, height= 645, layout="grid")
classes = ["Mathematik", 
    "Informatik",
    "Chemie", 
    "Physik", 
    "Biologie", 
    "Deutsch", 
    "Englisch", 
    "Französisch", 
    "Wirtschaft & Recht", 
    "Geschichte", 
    "Geographie", 
    "Musik", 
    "Pädagogik", 
    "Philosophie"]

first = True
predot = True       
decis = 0
numbers = ["0", "1", "2", "3", "4", "5", "6"]
all_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

go = GRADES_APP()
go.update()

app.display()
