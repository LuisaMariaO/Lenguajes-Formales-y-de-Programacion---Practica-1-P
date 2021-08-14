from os import sep
from tkinter import Tk
from tkinter.constants import N
from tkinter.filedialog import askopenfilename
from random import randint
from array import array

course=""
names_list=[]
notes_list=[]
#Alumnos en forma ascendente
ASC_names=[]
ASC_notes=[]

#Alumnos en forma descendente
DESC_names=[]
DESC_notes=[]

#Promedio
average=0

#Nota mínima
MIN_student=""
MIN_note=0

#Nota máxima
MAX_student=""
MAX_note=0

#Aprobados
apr=0

#Reprobados
rep=0

params=[]
def load():
    global ASC_names, ASC_notes, course, names_list, notes_list, DESC_notes, DESC_names, average, MIN_student, MIN_note, MAX_note, MAX_student, apr, rep, params
    ASC_names=[]
    ASC_notes=[]
    DESC_notes=[]
    DESC_names=[]
    average=0
    MIN_student=""
    MIN_note=0
    MAX_student=""
    MAX_note=0
    apr=0
    rep=0
    params=[]
    try:
        Tk().withdraw()
        filename = askopenfilename(filetypes=[("Archivo lfp","*.lfp")])
        file=open(filename,"r",encoding = "utf-8")
        content=file.readlines()
        #Obteniendo el nombre del curso
     
        course=content[0]
        #Ignorando símbolos y guiones
        course=course.replace("=","")
        course=course.replace("{","")
        course=course.replace("_"," ")

        
        #Creando una lista de estudiantes
        
        students=content[1:len(content)-1:1]
        
        newstudents=[]
        studentnames=[]
        
        for s in students:
            s=s.replace('\t',"")
            s=s.replace('\n',"")
            s=s.replace("<","")
            s=s.replace(">","")
            s=s.replace(",","")
            newstudents.append(s)
            
            

        for s in newstudents:
            studentnames.append(s.split(sep=";")) 

        names=[]
        names_list=[]
        notes=[]
        notes_list=[]

    
        dicstudent=dict(studentnames)
        
        for student in dicstudent:
            #Se eliminan los espacios que contienen las notas
            dicstudent[student]=dicstudent[student].replace(" ","")
            student=student.replace('"',"")
            #Creando una lista solo de nombres
            names.append(student)
            names_list.append(student)

        
            
            
        for note in dicstudent:
            #Se castea a enteros para realizar el ordenamiento 
            dicstudent[note]=int(dicstudent[note])
            notes.append(dicstudent[note])
            notes_list.append(dicstudent[note])
        
        #Guardando en una cadena los parámetros
        parameter=content[len(content)-1]
        parameter=parameter.replace("} ","")
        parameter=parameter.replace(" ","")
        #Guardando los parametros en una lista

        parameterlist=parameter.split(sep=",")
        params=parameterlist
        print("¡Archivo procesado exitosamente!\n")
        file.close()
        #Leyendo los parámetros
        for parameter in parameterlist:
            if parameter=="ASC":
                ASC_sort()
                
            elif parameter=="DESC":
                DESC_sort()
            elif parameter=="AVG":
                promedio(notes_list)
            elif parameter=="MIN":
                DESC_sort()
            elif parameter=="MAX":
                ASC_sort()
            elif parameter=="APR":
                aprobados()
            elif parameter=="REP":
                reprobados()
    except:
        print("Ha ocurrido un error, por favor intente de nuevo.")

def ASC_sort():
    '''Ordena de manera ascendente'''
    global ASC_names,ASC_notes, names_list, notes_list, MAX_note, MAX_student
    ASC_names=[]
    ASC_notes=[]
    ASC_names+=names_list
    ASC_notes+=notes_list
    MAX_student=""
    MAX_note=0
    if len(ASC_notes)>1:
        for nota in range (len(ASC_notes)-1,0,-1):
            for i in range(nota):
                if ASC_notes[i]>ASC_notes[i+1]:
                    aux=ASC_notes[i]
                    auxn=ASC_names[i]

                    ASC_notes[i]=ASC_notes[i+1]
                    ASC_names[i]=ASC_names[i+1]

                    ASC_notes[i+1]=aux
                    ASC_names[i+1]=auxn  
    MAX_student+=ASC_names[len(ASC_names)-1]
    MAX_note=+ASC_notes[len(ASC_notes)-1]

def DESC_sort():
    '''Ordena de manera ascendente'''
    global DESC_names,DESC_notes, names_list, notes_list, MIN_note, MIN_student
    
    DESC_names=[]
    DESC_notes=[]
    
    DESC_names+=names_list
    DESC_notes+=notes_list

    MIN_student=""
    MIN_note=0
    
    if len(DESC_notes)>1:
        for nota in range (len(DESC_notes)-1,0,-1):
            for i in range(nota):
                if DESC_notes[i]<DESC_notes[i+1]:
                    aux=DESC_notes[i]
                    auxn=DESC_names[i]

                    DESC_notes[i]=DESC_notes[i+1]
                    DESC_names[i]=DESC_names[i+1]

                    DESC_notes[i+1]=aux
                    DESC_names[i+1]=auxn  
    MIN_note=DESC_notes[len(DESC_notes)-1]
    MIN_student=DESC_names[len(DESC_names)-1]


def promedio(notes):
    global  average
    average=0
    average=sum(notes)/len(notes)
    average=round(average,2)


def aprobados():
    global notes_list, apr
    apr=0
    for nota in notes_list:
        if nota>=61:
            apr+=1
        
def reprobados():
    global notes_list, rep
    rep=0
    for nota in notes_list:
        if nota<61:
            rep+=1        

def report():
    global names_list, notes_list,course, params, ASC_names, ASC_notes, average, MIN_note, MIN_student, MAX_note, MAX_student
    
    print("\nCurso: "+course+"\n")
    print("Total de estudiantes assignados: "+str(len(names_list)))
    print("{:<30}{:<5}".format(' Estudiante','Nota'))
    for name,note in zip(names_list,notes_list):
        print("{:<30}{:<5}".format(name,note))
        
    for param in params:
        if param=="ASC":
            print("\nESTUDIANTES EN ORDEN ASCENDENTE")
            print("{:<30}{:<5}".format(' Estudiante','Nota'))
            for name, note in zip(ASC_names, ASC_notes):
                print("{:<30}{:<5}".format(name,note))
        elif param=="DESC":
            print("\nESTUDIANTES EN ORDEN DESCENDENTE")
            print("{:<30}{:<5}".format(' Estudiante','Nota'))
            for name, note in zip(DESC_names, DESC_notes):
                print("{:<30}{:<5}".format(name,note))
        elif param=="AVG":
            print("\nPROMEDIO DE NOTAS: " )
            print(average)
        elif param=="MIN":
            print("\nNOTA MÍNIMA")
            print("{:<30}{:<5}".format(' Estudiante','Nota'))
            print("{:<30}{:<5}".format(MIN_student,MIN_note))
        elif param=="MAX":
            print("\nNOTA MÁXIMA")
            print("{:<30}{:<5}".format(' Estudiante','Nota'))
            print("{:<30}{:<5}".format(MAX_student,MAX_note))
        elif param=="APR":
            print("\nESTUDIANTES APROBADOS: ", apr)
        elif param=="REP":
            print("\nESTUDIANTES REPROBADOS: ", rep)

    
    
def report_html():
    global names_list, notes_list, params, ASC_names, ASC_notes, DESC_names, DESC_notes, MIN_note, MIN_student, MAX_student, MAX_student, apr, rep,average
    try:
        report=open("Reporte-Control Académico.html","w")
        body="""
        <!DOCTYPE html>
        <html>
        <head>
        <title>Reporte-Control Académico</title>
        <img src="logo_azul.png" alt="FIUSAC" width="500px" align="right"/>
        </head>
        <body>"""
        body+="""
        <h1 style= "font-family: Georgia"> Curso: """
        body+=course+"""</h1>
        <h2 style= "font-family: Georgia"> Total de estudiantes asignados: """
        body+=str(len(names_list))+"""
        <br>
        <h2 style= "font-family: Georgia"> Estudiantes Asignados </h2>
        <table width="1200 px">
        <tr>
        <th align="left" width="1000 px">Estudiante</th>
        <th align="left">Nota</th>
        </tr>
    
        """
        for name, note in zip(names_list, notes_list):
            if note>=61:
                body+="""<tr>"""
                body+="""<td style="border-bottom: 1px solid silver ">"""+name+"""</td>"""
                body+="""<td style="border-bottom: 1px solid silver; color: blue">"""+str(note)+"""</td>"""
                body+="</tr>"
            else:
                body+="""<tr>"""
                body+="""<td style="border-bottom: 1px solid silver ">"""+name+"""</td>"""
                body+="""<td style="border-bottom: 1px solid silver; color: red">"""+str(note)+"""</td>"""
                body+="</tr>" 
        body+="</table>"

        for param in params:
            if param=="ASC":
                body+="""
                <br>
                <h2 style= "font-family: Georgia"> Listado de forma ascendente (ASC) </h2>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px">Estudiante</th>
                <th align="left">Nota</th>
                </tr>
                """
                for name, note in zip(ASC_names, ASC_notes):
                    if note>=61:
                        body+="""<tr>"""
                        body+="""<td style="border-bottom: 1px solid silver ">"""+name+"""</td>"""
                        body+="""<td style="border-bottom: 1px solid silver; color: blue">"""+str(note)+"""</td>"""
                        body+="</tr>"
                    else:
                        body+="""<tr>"""
                        body+="""<td style="border-bottom: 1px solid silver ">"""+name+"""</td>"""
                        body+="""<td style="border-bottom: 1px solid silver; color: red">"""+str(note)+"""</td>"""
                        body+="</tr>" 
                body+="</table>"
            elif param=="DESC":
                body+="""
                <br>
                <h2 style= "font-family: Georgia"> Listado de forma descendente (DESC) </h2>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px">Estudiante</th>
                <th align="left">Nota</th>
                </tr>
                """
                for name, note in zip(DESC_names, DESC_notes):
                    if note>=61:
                        body+="""<tr>"""
                        body+="""<td style="border-bottom: 1px solid silver ">"""+name+"""</td>"""
                        body+="""<td style="border-bottom: 1px solid silver; color: blue">"""+str(note)+"""</td>"""
                        body+="</tr>"
                    else:
                        body+="""<tr>"""
                        body+="""<td style="border-bottom: 1px solid silver ">"""+name+"""</td>"""
                        body+="""<td style="border-bottom: 1px solid silver; color: red">"""+str(note)+"""</td>"""
                        body+="</tr>" 
                body+="</table>"

            elif param=="MIN":
                body+="""
                <br>
                <h2 style= "font-family: Georgia"> Nota mínima (MIN) </h2>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px">Estudiante</th>
                <th align="left">Nota</th>
                </tr>
                """
                if MIN_note>=61:
                    body+="""<tr>"""
                    body+="""<td style="border-bottom: 1px solid silver ">"""+MIN_student+"""</td>"""
                    body+="""<td style="border-bottom: 1px solid silver; color: blue">"""+str(note)+"""</td>"""
                    body+="</tr>" 
                else:
                    body+="""<tr>"""
                    body+="""<td style="border-bottom: 1px solid silver ">"""+MIN_student+"""</td>"""
                    body+="""<td style="border-bottom: 1px solid silver; color: red">"""+str(note)+"""</td>"""
                    body+="</tr>" 
                body+="</table>"
            elif param=="MAX":
                body+="""
                <br>
                <h2 style= "font-family: Georgia"> Nota máxima (MAX) </h2>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px">Estudiante</th>
                <th align="left">Nota</th>
                </tr>
                """
                if MAX_note>=61:
                    body+="""<tr>"""
                    body+="""<td style="border-bottom: 1px solid silver ">"""+MAX_student+"""</td>"""
                    body+="""<td style="border-bottom: 1px solid silver; color: blue">"""+str(MAX_note)+"""</td>"""
                    body+="</tr>" 
                else:
                    body+="""<tr>"""
                    body+="""<td style="border-bottom: 1px solid silver ">"""+MAX_student+"""</td>"""
                    body+="""<td style="border-bottom: 1px solid silver; color: red">"""+str(MAX_note)+"""</td>"""
                    body+="</tr>" 
                body+="</table>"


            elif param=="APR":
                body+="""
                <br>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px" style="border-bottom: 1px solid silver">Estudiantes aprobados (APR)</th>
                <td align="left" style="border-bottom: 1px solid silver; color: white; background-color: PaleGreen">"""+str(apr)+"""</th>
                </tr>  
                </table>
                """  
            elif param=="REP":
                body+="""
                <br>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px" style="border-bottom: 1px solid silver">Estudiantes reprobados (REP)</th>
                <td align="left" style="border-bottom: 1px solid silver; color: white; background-color: Crimson">"""+str(rep)+"""</th>
                </tr>  
                </table>
                """  
            elif param=="AVG":
                body+="""
                <br>
                <table width="1200 px">
                <tr>
                <th align="left" width="1000 px" style="border-bottom: 1px solid silver">Promedio de notas (AVG)</th>
                <td align="left" style="border-bottom: 1px solid silver; color: white; background-color: Coral">"""+str(average)+"""</th>
                </tr>  
                </table>
                """  
        body+="""
        </body>
        </html>
        """
        report.write(body)
        report.close
        print("¡Reporte generado con éxito!")
    except:
        print("Ha ocurrido un error, por favor intente de nuevo.")

while True:
    print("\nREPORTE DE NOTAS, CONTROL ACADÉMICO")
    print("\t      FIUSAC")
    print("-----------------------------------")
    print("Menú:")
    print("1.Cargar archivo")
    print("2.Mostrar reporte")
    print("3.Exportar reporte")
    print("4.Salir")  
    option=input("Selecciona una opción: ")
    if option=="1":
        load()
    elif option=="2":
        report()
    elif option=="3":
        report_html()
    elif option=="4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inexistente")

