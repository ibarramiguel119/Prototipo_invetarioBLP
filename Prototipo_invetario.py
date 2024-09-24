# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 17:42:17 2022

@author: MiguelElibert
"""
import keyboard
from ast import If
from tkinter import ttk
from tkinter import *
import sqlite3 as sql
from tkinter import messagebox
from unittest import result
import serial
import threading



class Ctl:
    
    def __init__(self,root):
        self.wind = root
        self.wind.title("BLPINVENTARY")
        self.wind.geometry("1500x800")
    
        left = Label(root, text = "Control de inventario",bg='#f0f0f0',font=(30))
        left.pack()

        

        
        
        
        #Agrega los datos del Boton Dar de alta 
        def addbasedatosA():
            result7=textExample7.get("1.0","end")
            result8=textExample8.get("1.0","end")
            r5=int(0)
            r7=int(0)
            insertFila(result7,r5,result8,r7)
        def insertFila(producto,cantidad,codigo,Estatus):
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"INSERT INTO controlinv VALUES('{producto}',{cantidad},{codigo},{Estatus})"
            cursor.execute(instruccion)
            conn.commit()
            conn.close()
        
        def getTextInputA():
            result3=textExample3.get("1.0","end")
            print(result3)
            result3=int(result3)
            if result3 == 1010:
                redBDR1()
            elif result3== 2020:
                redBDR2()    
            elif result3== 3030:
                redBDR3()
            elif result3== 4040:
                redBDR4()
            elif result3== 5050:
                redBDR5()
            elif result3== 6060:
                redBDR6()
            elif result3== 7070:
                redBDR7()
            elif result3== 8080:
                redBDR8()
            elif result3== 1111:
                redBDR9()
            elif result3== 2121:
                redBDR10()
            elif result3== 3131:
                redBDR11()
            elif result3==4141:
                redBDR12()
            elif result3==5151:
                redBDR13()
            elif result3==6161:
                redBDR14()
            elif result3==7171:
                redBDR15()
            elif result3==8181:
                redBDR16()
            elif result3==7501055310883:
                redBDR17()
            elif result3==9090:
                redBDR18()
            elif result3==1212:
                redBDR19()
            elif result3==2222:
                redBDR20()
            elif result3==2323:
                redBDR21()
            elif result3==8081:
                redBDR22()


        def getTextInputB():
            result6=textExample6.get("1.0","end")
            print(result6)
            result6=int(result6)
            if result6 == 1010:
                redBDV1()
            elif result6== 2020:
                redBDV2()    
            elif result6== 3030:
                redBDV3()
            elif result6== 4040:
                redBDV4()
            elif result6== 5050:
                redBDV5()
            elif result6== 6060:
                redBDV6()
            elif result6== 7070:
                redBDV7()
            elif result6== 8080:
                redBDV8()
            elif result6== 1111:
                redBDV9()
            elif result6== 2121:
                redBDV10()
            elif result6== 3131:
                redBDV11() 
            elif result6==4141:
                redBDV12()  
            elif result6== 5151:
                redBDV13() 
            elif result6== 6161:
                redBDV14()
            elif result6== 7171:
                redBDV15()                
            elif result6== 8181:
                redBDV16()
            elif result6== 7501055310883:
                redBDV17() 
            elif result6== 9090:
                redBDV18()
            elif result6== 1212:
                redBDV19()     
            elif result6== 2222:
                redBDV20()
            elif result6== 2323:
                redBDV21() 
            elif result6== 8081:
                redBDV22()   


     
    ################################################################################
    #Coca600
        ##Intaracion de de base de datos con en el la interface usuario
        def redBDV1():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'1010')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]### Cantidad
                 a1=i[3]####Estatus
                 a2=i[2]#Codigo
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 parametros=(b1,'1010')
                 if a2=='1010':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR1():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'1010')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                 parametros=(b1,'1010')
                 if a2=='1010':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
    ###Coca355
    #################################################################################
        def redBDV2():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'2020')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]#Cantidad
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 #print(b1,b,a2)
                 parametros=(b1,'2020')
                 if a2=='2020':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR2():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'2020')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
               
                 parametros=(b1,'2020')
                 if a2=='2020':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        
   ######################################################################################
   #CocaChica 
        def redBDV3():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'3030')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'3030')
                 if a2=='3030':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR3():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'3030')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'3030')
                 if a2=='3030':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
    ####################################################################################
    #Coca_lata 
        def redBDV4():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'4040')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'4040')
                 if a2=='4040':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR4():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'4040')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'4040')
                 if a2=='4040':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
    

    ####################################################################################
    #FantaFresa
        def redBDV5():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'5050')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'5050')
                 if a2=='5050':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR5():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'5050')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'5050')
                 if a2=='5050':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
    ####################################################################################
    #####FantaFresa600
        def redBDV6():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'6060')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'6060')
                 if a2=='6060':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR6():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'6060')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'6060')
                 if a2=='6060':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()


        #######################################################################
        #####FantaNaranja_355
        def redBDV7():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'7070')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'7070')
                 if a2=='7070':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR7():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'7070')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'7070')
                 if a2=='7070':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()

#######################################################################
#### Fanta de naranja de 600 
        def redBDV8():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'8080')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'8080')
                 if a2=='8080':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR8():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'8080')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'8080')
                 if a2=='8080':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        #########################################################
            ###### JValle_Mango 
        def redBDV9():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'1111')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'1111')
                 if a2=='1111':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR9():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'1111')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'1111')
                 if a2=='1111':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        ###############################################
        #Valle de Durazno

        def redBDV10():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'2121')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'2121')
                 if a2=='2121':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR10():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'2121')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'2121')
                 if a2=='2121':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()



##########################################33
#Valle_De_Gullaba
        def redBDV11():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'3131')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'3131')
                 if a2=='3131':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR11():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'3131')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'3131')
                 if a2=='3131':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()    
        #### Valle de Manzana######################################
         
        def redBDV12():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'4141')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'4141')
                 if a2=='4141':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR12():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'4141')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'4141')
                 if a2=='4141':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()

############################################################
#Sprite600
        def redBDV13():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'5151')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'5151')
                 if a2=='5151':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR13():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'5151')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'5151')
                 if a2=='5151':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()

################################################
#Spr355
        def redBDV14():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'6161')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'6161')
                 if a2=='6161':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR14():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'6161')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'6161')
                 if a2=='6161':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        
        #############################################
        ###Agua_ciel_600
        def redBDV15():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'7171')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'7171')
                 if a2=='7171':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR15():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'7171')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'7171')
                 if a2=='7171':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        ##############################
        #Ciel_Litro 
        def redBDV16():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'8181')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 
                 parametros=(b1,'8181')
                 if a2=='8181':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def  redBDR16():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'8181')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                
                 parametros=(b1,'8181')
                 if a2=='8181':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()

        #Ciel_Nueva
        ##Intaracion de de base de datos con en el la interface usuario
        def redBDV17():
            result5=textExample5.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result5,'7501055310883')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]### Cantidad
                 a1=i[3]####Estatus
                 a2=i[2]#Codigo
                 b=int(a)
                 b1=int(a1)
                 b1=b1+b
                 parametros=(b1,'7501055310883')
                 if a2=='7501055310883':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        def redBDR17():
            result2=textExample2.get("1.0","end")
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            parametros=(result2,'7501055310883')
            instruccion= "UPDATE controlinv SET cantidad= ?  WHERE Codigo= ?"
            cursor.execute(instruccion,parametros)
            conn.commit()
            conn.close()

            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            instruccion= f"SELECT * FROM controlinv"
            cursor.execute(instruccion)
            datos= cursor.fetchall()
            conn.commit()
            conn.close()
            for i in datos:
                 a=i[1]
                 a1=i[3]
                 a2=i[2]
                 b=int(a)
                 b1=int(a1)
                 b1=b1-b
                 parametros=(b1,'7501055310883')
                 if a2=='7501055310883':
                    conn=sql.connect("controlinv.db")
                    cursor=conn.cursor()
                    instruccion1= "UPDATE controlinv SET Estatus= ?  WHERE Codigo= ?"
                    cursor.execute(instruccion1,parametros)
                    conn.commit()
                    conn.close()
        


    ####################################################################################    
        def comfirmarA():
            messagebox.showinfo(message="Tu producto ha sido restado exitosamente!", title="Confirmacion")

        def comfirmarB():   
            messagebox.showinfo(message="Tu producto ha sido sumado exitosamente!", title="Confirmacion")

        def comfirmarC():
             messagebox.showinfo(message="Tu producto se dio de altaA exitosamente!", title="Confirmacion")

        def comfirmarD():
             messagebox.showinfo(message="Actualizacion exitosa!", title="Confirmacion")
     

        boton1 =Button(text="RESTAR PRODUCTO",height=5,width=20,bg='#DC0C3F',command=lambda:[comfirmarA(),getTextInputA()])
        boton1.bind("<Return>", comfirmarA)
        boton1.place(x=50, y=300)
        boton2=Button(text='SUMAR PRODUCTO',height=5,width=20,bg='#189F14',command=lambda:[comfirmarB(),getTextInputB()])
        boton2.bind("<Return>", comfirmarB)
        boton2.place(x=250, y=300)
        boton3=Button(text='ALTA PRODUCTO',height=5,width=20,bg='#A4A7A1',command=lambda:[comfirmarC(),addbasedatosA()])
        boton3.bind("<Return>", comfirmarC)
        boton3.place(x=1200, y=300)
        boton4=Button(text='ACTUALIZAR DATOS',height=5,width=20,bg='#A4A7A1',command=lambda:[comfirmarD(),update_table()])
        boton4.bind("<Return>", comfirmarD)
        boton4.place(x=650, y=300)

        #Contenedores entry
        mi_Frame = Frame(root,height=800,width=600)
        mi_Frame.pack(fill='x')
        mi_Frame.config(bg='#D6DBDF')
        mi_Frame.config(width="150", height="400")

        #Contenedor entry para el segundo frame fuerea de l tabla
        #Secon_Frame=Frame(root,height=800,width=600)



        ####Nuevo algoritmo para crear una nueva tabla 
        # Crear la tabla en la interfaz gráfica
        table= ttk.Treeview(mi_Frame,columns=("col1","col2","col3","col4"))
        table['columns'] = ('column1', 'column2', 'column3',"column4")
        table.place(x=50,y=400)
        table.column('column1', width=110,anchor=CENTER)
        table.column('column2', width=110,anchor=CENTER)
        table.column('column3', width=110,anchor=CENTER)
        table.column('column4', width=110,anchor=CENTER)
        table.heading('column1', text='Producto')
        table.heading('column2', text='Cantidad')
        table.heading('column3', text='Codigo')
        table.heading('column4', text='Estatus')
        
        table.pack()

# Función para actualizar la tabla con los resultados de la base de datos
        def update_table():
     #Borrar todos los registros anteriores de la tabla
            
            table.delete(*table.get_children())

                # Obtener los registros de la base de datos
            conn=sql.connect("controlinv.db")
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM controlinv")
            rows = cursor.fetchall()
             # Agregar los registros a la tabla
            for row in rows:
                 table.insert('', 'end', values=row)

    # Actualizar la tabla después de 1 segundo
            root.after(1000, update_table)

# Llamar a la función para actualizar la tabla
        ##update_table()
  #############################################


  #Forma en que se van a obtener los datos de la base de datos 
  #Funcion Actualizar la tabla del usuario        
        mi_Label = Label(mi_Frame, text="Producto")
        mi_Label.place(x=50,y=10)

        textExample1=Text(root, height=1, width=20)
        textExample1.place(x=50,y=50)

        
        mi_Label2= Label(mi_Frame,text='Cantidad')
        mi_Label2.place(x=50,y=80)

        textExample2=Text(root, height=1, width=20)
        textExample2.place(x=50,y=120)
        #textExample1.insert('1.0',B)       


        mi_Label3=Label(mi_Frame,text='Codigo')
        mi_Label3.place(x=50,y=140)
        
        textExample3=Text(root, height=1, width=20)
        textExample3.place(x=50,y=190)

        mi_Label4=Label(mi_Frame,text='Producto')
        mi_Label4.place(x=250,y=10)

        textExample4=Text(root, height=1, width=20)
        textExample4.place(x=250,y=50)

        mi_Label5=Label(mi_Frame,text='Cantidad')
        mi_Label5.place(x=250,y=80)

        textExample5=Text(root, height=1, width=20)
        textExample5.place(x=250,y=120)

        mi_Label6=Label(mi_Frame,text='Codigo')
        mi_Label6.place(x=250,y=140)

        textExample6=Text(root, height=1, width=20)
        textExample6.place(x=250,y=190)

        mi_Label7=Label(mi_Frame,text='Producto')
        mi_Label7.place(x=1200,y=10)

        textExample7=Text(root, height=1, width=20)
        textExample7.place(x=1200,y=50)

        mi_Label8=Label(mi_Frame,text='Codigo')
        mi_Label8.place(x=1200,y=80)

        textExample8=Text(root, height=1, width=20)
        textExample8.place(x=1200,y=120)

       

        
if __name__ =='__main__':
    root=Tk()
    s= Ctl(root)
    root.mainloop()
  