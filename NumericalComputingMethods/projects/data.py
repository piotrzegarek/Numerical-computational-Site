import openpyxl
import pandas as pd


class Data:
    def __init__(self, xlsx_file, name) -> None:
        self.project_name = name
        self.excel_data = pd.read_excel(xlsx_file)
        self.columns = self.excel_data.columns.ravel()
        self.converted_excel_data = []
        self.functions = []
        
        for column in self.columns:
            self.converted_excel_data.append(self.excel_data[column].tolist())

        if len(self.converted_excel_data) % 2 == 0:
            for i in range(0,len(self.converted_excel_data)-1,2):
                self.function_data = (self.converted_excel_data[i], self.converted_excel_data[i+1])
                self.functions.append(self.function_data)
        else:
            print('Dane nie są symetryczne')

        print(self.functions)


    def __str__(self):
        return f'Title: "{self.project_name}"'

    def use_left_rectangles_method(self):
        functions_fields = []
        for function in self.functions:
            field = 0
            for i in range(len(function[0])-1):
                field += (function[0][i+1]-function[0][i])*function[1][i]
            functions_fields.append(field)
            
        return functions_fields

    def use_right_rectangles_method(self):
        functions_fields = []
        for function in self.functions:
            field = 0
            for i in range(len(function[0])-1):
                field += (function[0][i+1]-function[0][i])*function[1][i+1]
            functions_fields.append(field)
            
        return functions_fields

    def use_middle_rectangles_method(self):
        functions_fields = []
        for function in self.functions:
            field = 0
            for i in range(len(function[0])-1):
                field += (function[0][i+1]-function[0][i])*function[1][i+1]
            functions_fields.append(field)
            
        return functions_fields

    def use_triangles_method(self):
        functions_fields = []
        for function in self.functions:
            field = 0
            for i in range(len(function[0])-1):
                a = function[0][i+1] - function[0][i]
                h = function[1][i+1]
                field += 0.5*(a*h)
            functions_fields.append(field)
            
        return functions_fields

    def use_trapeze_methods(self):
        functions_fields = []
        for function in self.functions:
            field = 0
            for i in range(len(function[0])-1):
                a = function[1][i]
                b = function[1][i+1]
                h = function[0][i+1] - function[0][i]
                field += ((a+b)/2)*h
            functions_fields.append(field)
            
        return functions_fields

data = Data('test1.xlsx', 'Pierwszy projekt')
print(data.use_left_rectangles_method())
print(data.use_right_rectangles_method())
print(data.use_triangles_method())
print(data.use_trapeze_methods())


