import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import win32api,win32con
from PyQt5.QtCore import QTime
import sip
from PyQt5.QtCore import pyqtSignal
#from PyQt5.QtWidgets import pyqtSignal
#apps\\fit240\\TestRecord.dat'
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMenuBar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
import win32api,win32con
maxx=win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
maxy=win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
#print(maxx)
from PyQt5.QtCore import QTime,QRect
import sip

from PyQt5.QtCore import pyqtSignal
#from PyQt5.QtWidgets import pyqtSignal
import csv

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import time

import os
from win32gui import GetWindowText, GetForegroundWindow
import win32gui

lang=[['报告','选择csv文件','打开文件','加载记录','搜寻','选取 储存txt','全选 储存txt','另存为...','清空','关闭','档案','语言'],\
    ['報告','選擇csv檔','打開文件','加載記錄','搜尋','選取 儲存txt','全選 儲存txt','另存為...','清空','關閉','檔案','語言'],\
    ['Report','Choose csv File','Open file','Load record','Search','Save txt (Selected record)','Save txt (All records)','Save as...','Clean','Shut down','File','Language'],\
        ['Reporte','Elija el archivo csv','Abrir Documento','Carga grabación','Buscar','Guardar txt (Registro seleccionado)',\
            'Guardar txt (Todos los registros)','Guardar como...','Limpio','Apagar','El expediente','Idioma']]

confirmlang=[]


#,'30':'序号','31':'设备编号','32':'测试时间','33':'警察姓名','34':'警察编号','35':'所属部门','36':'驾驶员姓名','37':'驾驶证号码','38':'车牌号码','39':'测试模式','40':'测试结果'
#,'30':'序號','31':'設備編號','32':'測試時間','33':'警察姓名','34':'警察編號','35':'所屬部門','36':'駕駛員姓名','37':'駕駛證號碼','38':'車牌號碼','39':'測試模式','40':'測試結果'
#,'30':'Serial number','31':'Equipment number','32':'Test time','33':'Police name','34':'Police number','35':'Department','36':'Driver name','37':'Driver license number','38':'License plate number','39':'Test mode','40':'Test result'
#,'30':'Número de serie','31':'ID del dispositivo','32':'Tiempo de prueba','33':'Nombre de la policía','34':'Numero de policia','35':'Departamento','36':'Nombre del conductor','37':'Número de carnet de conducir','38':'Numero de licencia','39':'Modo de prueba','40':'Resultados de la prueba'


langdic={
    '1':{'41':'请先连接设备','42':'提示','24':'自动加载空白','25':'自动加载已选文件'                   ,   '26':'加载' ,    '27':'密码' ,   '28':'登录'         ,'29':'转档dat到csv','30':'序号','31':'设备编号','32':'测试时间','33':'警察姓名','34':'警察编号','35':'所属部门','36':'驾驶员姓名','37':'驾驶证号码','38':'车牌号码','39':'测试模式','40':'测试结果',   '1':' 搜寻 ','2':'  下载  ','3':'全词匹配','4':'全选',       '5':'多重搜寻','6':'多重匹配搜寻','7':'范围搜寻',                  '8':'搜寻','9':'重设','10':'储存',     '11':'另存',       '12':'加载設定','13':'清空',                  '14':'自動储存加载','15':'全体搜寻','16':'选项','17':'[全体]',                '18':'[未选]','19':'搜寻模式','20':'屏幕',                 '21':'窗口','22':'全屏幕','23':'进阶搜寻'},
    '2':{'41':'請先連接設備','42':'提示','24':'自動加載空白','25':'自動加載已選文件'                  ,      '26':'加載' ,   '27':'密碼' ,  '28':'登錄'         ,'29':'轉檔dat到csv','30':'序號','31':'設備編號','32':'測試時間','33':'警察姓名','34':'警察編號','35':'所屬部門','36':'駕駛員姓名','37':'駕駛證號碼','38':'車牌號碼','39':'測試模式','40':'測試結果',  '1':' 搜尋 ','2':'  下載  ','3':'全詞匹配','4':'全選',       '5':'多重搜尋','6':'多重匹配搜尋','7':'範圍搜尋',                  '8':'搜尋','9':'重設','10':'儲存',     '11':'另存',          '12':'加載設定','13':'清空',               '14':'自動儲存加載','15':'全體搜尋','16':'選項','17':'[全體]',                 '18':'[未選]','19':'搜尋模式','20':'屏幕',                 '21':'窗口','22':'全屏幕','23':'進階搜尋'},
    '3':{'41':'Please connect the device first','42':'Notice','24':'Auto Load Blank','25':'Auto Load chose File'         ,    '26':'Load'  ,   '27':'Password' , '28':'Login'     ,'29':'Convert dat to csv','30':'Serial number','31':'Equipment number','32':'Test time','33':'Police name','34':'Police number','35':'Department','36':'Driver name','37':'Driver license number','38':'License plate number','39':'Test mode','40':'Test result','1':'Search','2':'Download','3':' Exact word','4':'All',   '5':'Multiple Search','6':'Multiple Match', '7':'Range Search',   '8':'Search','9':'Reset','10':'Save','11':'Save as',          '12':'Load Configuration','13':'Clean',       '14':'Auto Save Load','15':'Whole search','16':'Options','17':'[Whole]',          '18':'[Not selected]','19':'Search mode','20':'Screen',  '21':'Window screen','22':'Full screen','23':'Advanced Search'},
    '4':{'41':'Primero conecta el dispositivo','42':'Nota','24':'Auto Carga Blanco','25':'Auto Carga escoger Archivo',     '26':'Carga' ,   '27':'Contraseña' ,  '28':'Acceso' ,'29':'Convertir dat a csv','30':'Número de serie','31':'ID del dispositivo','32':'Tiempo de prueba','33':'Nombre de la policía','34':'Numero de policia','35':'Departamento','36':'Nombre del conductor','37':'Número de carnet de conducir','38':'Numero de licencia','39':'Modo de prueba','40':'Resultados de la prueba', '1':'Buscar','2':'Descargar','3':'Exacto palabra','4':'Todas','5':'Múltiple Buscar','6':'Múltiple fósforo','7':'Alcance Buscar','8':'Buscar','9':'Reiniciar','10':'Guardar','11':'Guardar como','12':'Carga Configuración','13':'Limpiar','14':'Auto Ahorrar Carga','15':'Entero buscar','16':'Opciones','17':'[Entero]','18':'[No seleccionado]','19':'Buscar modo','20':'Pantalla','21':'Ventana pantalla','22':'Pantalla completa','23':'Avanzado Buscar'}                
}

confirmlangdic={}
confirmlangdicnum=42
confirmid=0

with open(file='Setting\\lang.txt',mode='r',encoding='utf-8')as lff:
    ook= lff.read()
    ook=ook[0]
##print(ook)
def startlang():
    global confirmid
    if str(ook) in str(1):
        for i in lang[0]:
            confirmlang.append(i)
        for i in range(confirmlangdicnum):
            confirmlangdic[str(i+1)]=langdic['1'][str(i+1)]
        confirmid=1
        return confirmid

    elif str(ook) in str(2):
        for i in lang[1]:
            confirmlang.append(i)
        for i in range(confirmlangdicnum):
            confirmlangdic[str(i+1)]=langdic['2'][str(i+1)]
        confirmid=2
        return confirmid

    elif str(ook) in str(3):
        for i in lang[2]:
            confirmlang.append(i)
        for i in range(confirmlangdicnum):
            confirmlangdic[str(i+1)]=langdic['3'][str(i+1)]
        confirmid=3
        return confirmid

    elif str(ook) in str(4):
        for i in lang[3]:
            confirmlang.append(i)
        for i in range(confirmlangdicnum):
            confirmlangdic[str(i+1)]=langdic['4'][str(i+1)]
        confirmid=4
        return confirmid
startlang()


a1langdic={
    '1':{'1':' 选择范围 ','2':'左到右，小至大',                               '3':'序号','4':'设备编号',       '5':'测试时间','6':'警察编号','7':'驾驶证号码','8':'车牌号码','9':'测试结果',    '10':'储存',     '11':'另存',       '12':'加载','13':'清空'},
    '2':{'1':' 選擇範圍 ','2':'左到右，小至大',                               '3':'序號','4':'設備編號',       '5':'測試時間','6':'警察編號','7':'駕駛證號碼','8':'車牌號碼','9':'測試結果','10':'儲存',     '11':'另存',          '12':'加載','13':'清空'},
    '3':{'1':'Choose Range','2':'Left to right, small to big',               '3':'Serial number','4':'Device ID',   '5':'Testing time','6':'Police number', '7':"Driver's license number",   '8':'License plate number','9':'Test Results','10':'Save','11':'Save as',          '12':'Load','13':'Clean'},
    '4':{'1':'Elija Rango','2':'De izquierda a derecha, de pequeño a grande','3':'Número de serie','4':'Número del dispositivo','5':'Tiempo de prueba','6':'Numero de policia','7':'Número de carnet de conducir','8':'Número de licencia','9':'Resultados de la prueba','10':'Guardar','11':'Guardar como','12':'Carga','13':'Limpiar'}
}


confirmid=0
a1langconfirmdic={}
a1langlen=13
with open(file='Setting\\lang.txt',mode='r',encoding='utf-8')as lff:
    ook= lff.read()
    ook=ook[0]
def a1startlang():
    global confirmid
    if str(ook) in str(1):
        confirmid=1
        return confirmid

    elif str(ook) in str(2):
        confirmid=2
        return confirmid

    elif str(ook) in str(3):
        confirmid=3
        return confirmid

    elif str(ook) in str(4):
        confirmid=4
        return confirmid
a1startlang()
for i in range(13):
    a1langconfirmdic[str(i+1)]=a1langdic[str(confirmid)][str(i+1)]

tableshowid=0
win22showid=0

# password
class a2():
    global lineEditDemo
    class lineEditDemo(QWidget):
        def __init__(self,parent=None):
            super(lineEditDemo, self).__init__(parent)
            self.setWindowTitle(confirmlangdic['27'])
            self.setWindowIcon(QtGui.QIcon("runico.ico"))
            self.setWindowFlags(
            #QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
            QtCore.Qt.WindowTitleHint |
            #QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowStaysOnTopHint #|
            #QtCore.Qt.FramelessWindowHint #去掉标题栏
            )
        def changeEvent(self, e):
            if e.type() == QtCore.QEvent.ActivationChange:
                if not self.isActiveWindow():
                    global windowtext1
                    windowtext1=0
                    windowtext1=winpass.pPasswordListEdit.text()
                    win1class.win1classpass()
                    self.close()
        def keyPressEvent(self, event):
            if event.key() == QtCore.Qt.Key_Escape:
                global windowtext1
                windowtext1=0
                windowtext1=winpass.pPasswordListEdit.text()
                win1class.win1classpass()
                self.close()


            if event.key() == QtCore.Qt.Key_Return:
                windowtext1=0
                windowtext1=winpass.pPasswordListEdit.text()
                win1class.win1classpass()


            if event.key() == QtCore.Qt.Key_Enter:
                windowtext1=0
                windowtext1=winpass.pPasswordListEdit.text()
                win1class.win1classpass()

        '''def changeEvent(self, e):
            global allactive
            global searchnameid

            if e.type() == QtCore.QEvent.ActivationChange:
                if not self.isActiveWindow():
                    global win2
                    win2.close()'''

        '''def closeEvent(self, event):
            global windowtext1
            windowtext1=0
            windowtext1=winpass.pPasswordListEdit.text()
            win1class.win1classpass()'''



    def a21():
        global passcheck
        passcheck=0
        global winpass
        winpass=lineEditDemo()

        #cleanlag
        #addthendeletefixloaddelay = QTimeEdit(winpass)
        #sip.delete(addthendeletefixloaddelay)

        winpass.flo=QFormLayout()
        winpass.pPasswordListEdit=QLineEdit(winpass)
        winpass.flo.addRow(confirmlangdic['27'], winpass.pPasswordListEdit)
        winpass.pPasswordListEdit.setPlaceholderText(confirmlangdic['27'])
        winpass.pPasswordListEdit.setEchoMode(QLineEdit.Password)
        winpass.setLayout(winpass.flo)
        aaa3x=200
        aaa3y=80
        aaa3px=(maxx-aaa3x)/2
        aaa3py=(maxy-aaa3y)/2
        winpass.setGeometry(int(aaa3px),int(aaa3py),int(aaa3x),int(aaa3y))

        winpass.setFixedSize(winpass.width(), winpass.height())
        def sfsfd(event):
            global windowtext1
            windowtext1=0
            windowtext1=winpass.pPasswordListEdit.text()
            win1class.win1classpass()

        btn1=QPushButton(confirmlangdic['28'],winpass)
        btn1.setGeometry(120,40,70,30)
        btn1.clicked.connect(sfsfd)
        winpass.show()

# win3
class a4(): 
    global MainWindow
    class MainWindow(QWidget):
        def __init__(self):
            super(MainWindow, self).__init__()
            #self.setWindowModality(QtCore.Qt.ApplicationModal)
            self.setWindowTitle(a1langconfirmdic['1']+' (✔ACS,✘DESC)')#choose range
            self.resize(200, 100)
            if confirmid==4:
                self.resize(220, 100)
            self.setWindowIcon(QtGui.QIcon("runico.ico"))

            # PyQT禁止调整窗口大小:
            #self.setFixedSize(self.width(), self.height())

            '''
            self.label_display = QLabel(self)
            self.label_display.setGeometry(0, 0, 100, 10)
            self.label_display.setText('Hello TEST!!!')'''

            self.label1= QLabel(self)
            self.label1.setGeometry(5, 0, 300, 15)


            self.label2= QLabel(self)
            self.label2.setGeometry(5, 15, 300, 15)
            self.label2.setText(a1langconfirmdic['2'])

            #self.pushButton = QPushButton(self)

            #self.pushButton.setGeometry(200, 70, 60, 25)

            #self.pushButton.setObjectName("pushButton")


            #self.text1 = QLineEdit(self)
            #self.text1.setGeometry(10,35,85,20)

            #self.text2 = QLineEdit(self)
            #self.text2.setGeometry(105,35,85,20)

            self.setWindowFlags(
            #QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowStaysOnTopHint
            #QtCore.Qt.WindowCloseButtonHint |
            #QtCore.Qt.WindowStaysOnTopHint #|
            #QtCore.Qt.FramelessWindowHint #去掉标题栏
            )

        '''
        def mousePressEvent(self, event):
            if event.buttons()== QtCore.Qt.LeftButton:                           # 左键按下
                #print("单击鼠标左键")  # 响应测试语句'''

        '''def leaveEvent(self,e): #鼠标离开label
            #print( 'leaveEvent')
            self.close()'''

        def changeEvent(self, e):
            '''if e.type() == QtCore.QEvent.WindowStateChange:
                if self.isVisible():
                    #print("窗口最小化")
                elif self.isMaximized():
                    #print("窗口最大化")
                elif self.isFullScreen():
                    #print("全屏显示")
                elif self.isActiveWindow():
                    #print("活动窗口")'''
            if e.type() == QtCore.QEvent.ActivationChange:
                # 当窗口被激活，也就是当用户点击了窗口在任务栏上的图标按钮
                if not self.isActiveWindow():
                    # showNor是我定义的方法，和showMini对应，相当于显示窗口
                    ##print('out')
                    self.close()




        def keyPressEvent(self, event):
            """Close application from escape key.

            results in QMessageBox dialog from closeEvent, good but how/why?
            """
            if event.key() == QtCore.Qt.Key_Escape:
                self.close()
            if event.key() == QtCore.Qt.Key_Return:
                self.close()
            if event.key() == QtCore.Qt.Key_Enter:
                self.close()

        '''def mousePressEvent(self, event):
            #print('hi')
            if event.buttons()== QtCore.Qt.LeftButton:                           # 左键按下
                #print("单击鼠标左键")  # 响应测试语句'''


        def closeEvent(self, event):
            global closecheckid
            global windowtext1,windowtext2
            if closecheckid==1:
                windowtext1=window1.text1.text()
                windowtext2=window1.text2.text()
                global aaa1dic
                aaa1dic={}
                aaa1dic['1']=windowtext1
                aaa1dic['2']=windowtext2
                bidict['1'].setText(aaa1dic['1']+'-'+aaa1dic['2'])
                

                try:
                    if aaa1dic['1']=='' or aaa1dic['2']=='' or int(aaa1dic['1'])>int(aaa1dic['2']):
                        bidict['1'].setText('')
                        aaa1dic={}
                except:
                    bidict['1'].setText('')
                    aaa1dic={}



            if closecheckid==2:
                windowtext1=window2.text1.text()
                windowtext2=window2.text2.text()
                global aaa2dic
                aaa2dic={}
                aaa2dic['1']=windowtext1
                aaa2dic['2']=windowtext2
                bidict['2'].setText(aaa2dic['1']+'-'+aaa2dic['2'])
                try:
                    if aaa2dic['1']=='' or aaa2dic['2']=='' or int(aaa2dic['1'])>int(aaa2dic['2']):
                        bidict['2'].setText('')
                        aaa2dic={}
                except:
                    bidict['2'].setText('')
                    aaa2dic={}
            if closecheckid==3:
                with open(file='Autofile/timesetsave.save',mode='w',encoding='utf-8') as strw:
                    strw.write('1:')
                    strw.write(str(window3.ycb1.currentIndex()))
                    strw.write('\n')
                    strw.write('2:')
                    strw.write(str(window3.mcb1.currentIndex()))
                    strw.write('\n')                                
                    strw.write('3:')
                    strw.write(str(window3.dcb1.currentIndex()))
                    strw.write('\n')
                    strw.write('4:')
                    asdad=timeedit1.time()
                    time1=asdad.toString('hhmm')
                    strw.write(time1)
                    strw.write('\n')       
                    strw.write('5:')
                    strw.write(str(window3.ycb2.currentIndex()))
                    strw.write('\n')                
                    strw.write('6:')
                    strw.write(str(window3.mcb2.currentIndex()))
                    strw.write('\n')                
                    strw.write('7:')
                    strw.write(str(window3.dcb2.currentIndex()))
                    strw.write('\n')
                    strw.write('8:')
                    asdad=timeedit2.time()
                    time2=asdad.toString('hhmm')
                    strw.write(time2)
                    strw.write('\n')
                    strw.write('_________\n')
                year1=window3.ycb1.currentText()
                year2=window3.ycb2.currentText()
                month1=window3.mcb1.currentText()
                month2=window3.mcb2.currentText()
                day1=window3.dcb1.currentText()
                day2=window3.dcb2.currentText()
                asdad=timeedit1.time()
                time1=asdad.toString('hhmm')
                asdad=timeedit2.time()
                time2=asdad.toString('hhmm')
                global rangesearchtimedic
                rangesearchtimedic={}
                rangesearchtimedic['1']=year1
                rangesearchtimedic['2']=month1
                rangesearchtimedic['3']=day1
                rangesearchtimedic['4']=time1
                rangesearchtimedic['5']=year2
                rangesearchtimedic['6']=month2
                rangesearchtimedic['7']=day2
                rangesearchtimedic['8']=time2
                
                printttt=rangesearchtimedic['1']+'/'+rangesearchtimedic['2']+'/'+rangesearchtimedic['3']+'/'+rangesearchtimedic['4'][:2]+':'+rangesearchtimedic['4'][-2:]+'-'+rangesearchtimedic['5']+'/'+rangesearchtimedic['6']+'/'+rangesearchtimedic['7']+'/'+rangesearchtimedic['8'][:2]+':'+rangesearchtimedic['8'][-2:]
                #bidict['3'].setFont(QFont("Timers" , 4))
                bidict['3'].setText(printttt)
            if closecheckid==5:
                windowtext1=window2.text1.text()
                windowtext2=window2.text2.text()
                global aaa5dic
                aaa5dic={}
                aaa5dic['1']=windowtext1
                aaa5dic['2']=windowtext2
                bidict['5'].setText(aaa5dic['1']+'-'+aaa5dic['2'])
                try:
                    if aaa5dic['1']=='' or aaa5dic['2']=='' or int(aaa5dic['1'])>int(aaa5dic['2']):
                        bidict['5'].setText('')
                        aaa5dic={}
                except:
                    bidict['5'].setText('')
                    aaa5dic={}
            if closecheckid==8:
                windowtext1=window2.text1.text()
                windowtext2=window2.text2.text()
                global aaa8dic
                aaa8dic={}
                aaa8dic['1']=windowtext1
                aaa8dic['2']=windowtext2
                bidict['8'].setText(aaa8dic['1']+'-'+aaa8dic['2'])
                try:
                    if aaa8dic['1']=='' or aaa8dic['2']=='' or int(aaa8dic['1'])>int(aaa8dic['2']):
                        bidict['8'].setText('')
                        aaa8dic={}
                except:
                    bidict['8'].setText('')
                    aaa8dic={}
            if closecheckid==9:
                windowtext1=window2.text1.text()
                windowtext2=window2.text2.text()
                global aaa9dic
                aaa9dic={}
                aaa9dic['1']=windowtext1
                aaa9dic['2']=windowtext2
                bidict['9'].setText(aaa9dic['1']+'-'+aaa9dic['2'])
                try:
                    if aaa9dic['1']=='' or aaa9dic['2']=='' or int(aaa9dic['1'])>int(aaa9dic['2']):
                        bidict['9'].setText('')
                        aaa9dic={}
                except:
                    bidict['9'].setText('')
                    aaa9dic={}
            if closecheckid==11:
                global checkedid
                windowtext1=window11.aaa11cb1.currentText()
                windowtext2=window11.aaa11cb2.currentText()
                checkedid=str(QBG1.checkedId())

                printml=''
                intcheckedid=int(checkedid)
                if intcheckedid==1:
                    printml=' mg/100mL'
                if intcheckedid==2:
                    printml=' mg/l'
                if intcheckedid==3:
                    printml=' %BAC'
                if intcheckedid==4:
                    printml=' ‰BAC'
    
    
                global aaa11dic
                aaa11dic={}
                aaa11dic['1']=windowtext1
                aaa11dic['2']=windowtext2
                aaa11dic['3']=checkedid
                #print(aaa11dic)

                bidict['11'].setText(aaa11dic['1']+'-'+aaa11dic['2']+printml)
                if aaa11dic['1']=='' or aaa11dic['2']=='' or int(aaa11dic['1'])>int(aaa11dic['2']):
                    bidict['11'].setText('')
                    aaa11dic={}
                




    global aaa1,aaa2,aaa3,aaa5,aaa8,aaa9,aaa11
    def aaa1():
        global window1
        #app = QApplication([])
        window1 = MainWindow()
        window1.label1.setText(a1langconfirmdic['3'])
        window1.text1 = QLineEdit(window1)
        window1.text1.setGeometry(10,35,85,20)
        window1.text2 = QLineEdit(window1)
        window1.text2.setGeometry(105,35,85,20)
        #cleanlag
        addthendeletefixloaddelay = QTimeEdit(window1)
        sip.delete(addthendeletefixloaddelay)


        def closeaaa(event):
            window1.close()
        btnmode1 = QtWidgets.QPushButton(window1)
        btnmode1.setGeometry(QtCore.QRect(105, 60, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)



        window1.setFixedSize(window1.width(), window1.height())
        window1.show()
        global closecheckid
        closecheckid=1
        #sys.exit(app.exec_())
        #app.exec_()
        #global windowtext1,windowtext2
        #windowtext1=window1.text1.text()
        #windowtext2=window1.text2.text()
    def aaa2():
        global window2
        window2 = MainWindow()
        window2.label1.setText(a1langconfirmdic['4'])
        addthendeletefixloaddelay = QTimeEdit(window2)
        sip.delete(addthendeletefixloaddelay)
        window2.text1 = QLineEdit(window2)
        window2.text1.setGeometry(10,35,85,20)
        window2.text2 = QLineEdit(window2)
        window2.text2.setGeometry(105,35,85,20)
        window2.setFixedSize(window2.width(), window2.height())


        def closeaaa(event):
            window2.close()
        btnmode1 = QtWidgets.QPushButton(window2)
        btnmode1.setGeometry(QtCore.QRect(105, 60, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)


        window2.show()
        global closecheckid
        closecheckid=2
        #global windowtext1,windowtext2
        #windowtext1=window2.text1.text()
        #windowtext2=window2.text2.text()

    def aaa3():
        global window3
        specialmonthyeardic={}
        for i in range(1924,2121):
            specialmonthyeardic[str(i+1)]='N'
        for j in range(50):
            speryear=1924+j*4
            for i in range(1924,2121):
                if i==speryear:
                    specialmonthyeardic[str(i)]='Y'
        aaa3x=200
        if confirmid==4:
            aaa3x=220
        aaa3y=180
        aaa3px=(maxx-aaa3x)/2
        aaa3py=(maxy-aaa3y)/2
        ##print(aaa3px)
        window3 = MainWindow()
        window3.label1.setText(a1langconfirmdic['5'])
        window3.setGeometry(int(aaa3px),int(aaa3py),int(aaa3x),int(aaa3y))
        window3.ycb1=QComboBox(window3)
        yearlist=[]
        for i in range(1924,2121):
            yearlist.append(str(i))
        window3.ycb1.addItems(yearlist)
        window3.mcb1=QComboBox(window3)
        yearlist=[]
        for i in range(1,13):
            yearlist.append(str(i))
        window3.mcb1.addItems(yearlist)
        window3.dcb1=QComboBox(window3)
        yearlist=[]
        for i in range(1,32):
            yearlist.append(str(i))
        window3.dcb1.addItems(yearlist)
        global timeedit1
        timeedit1 = QTimeEdit(window3)
        #timeedit.setTime(QTime.currentTime())
        timeedit1.setTimeRange(QTime(00, 00), QTime(24, 60))
        timeedit1.setDisplayFormat('hh:mm')
        window3.ycb2=QComboBox(window3)
        yearlist=[]
        for i in range(1924,2121):
            yearlist.append(str(i))
        window3.ycb2.addItems(yearlist)
        window3.mcb2=QComboBox(window3)
        yearlist=[]
        for i in range(1,13):
            yearlist.append(str(i))
        window3.mcb2.addItems(yearlist)
        window3.dcb2=QComboBox(window3)
        yearlist=[]
        for i in range(1,32):
            yearlist.append(str(i))
        window3.dcb2.addItems(yearlist)
        global timeedit2
        timeedit2 = QTimeEdit(window3)
        #timeedit.setTime(QTime.currentTime())
        timeedit2.setTimeRange(QTime(00, 00), QTime(24, 60))
        timeedit2.setDisplayFormat('hh:mm')
        window3.ycb1.setGeometry(10,35,85,20)
        window3.ycb2.setGeometry(105,35,85,20)
        window3.mcb1.setGeometry(10,60,85,20)
        window3.mcb2.setGeometry(105,60,85,20)
        window3.dcb1.setGeometry(10,85,85,20)
        window3.dcb2.setGeometry(105,85,85,20)
        timeedit1.setGeometry(10,110,85,20)
        timeedit2.setGeometry(105,110,85,20)
        try:
            with open(file='Autofile/timesetsave.save',mode='r',encoding='utf-8') as strw:
                strw=strw.readlines()
                ijid=0
                for sb in strw:
                    ijid+=1
                    if ijid==1:
                        window3.ycb1.setCurrentIndex(int(sb[2:-1]))
                    if ijid==2:
                        window3.mcb1.setCurrentIndex(int(sb[2:-1]))
                    if ijid==3:
                        window3.dcb1.setCurrentIndex(int(sb[2:-1]))
                    if ijid==4:
                        ijid1=int(sb[2:-3])
                        ijid2=int(sb[4:-1])
                        timeedit1.setTime(QTime(ijid1,ijid2))
                    if ijid==5:
                        window3.ycb2.setCurrentIndex(int(sb[2:-1]))
                    if ijid==6:
                        window3.mcb2.setCurrentIndex(int(sb[2:-1]))
                    if ijid==7:
                        window3.dcb2.setCurrentIndex(int(sb[2:-1]))
                    if ijid==8:
                        ijid1=int(sb[2:-3])
                        ijid2=int(sb[4:-1])
                        timeedit2.setTime(QTime(ijid1,ijid2))
        except:
            pass
        def print_value(i):
            day31month=[1,3,5,7,8,10,12]
            day30month=[4,6,9,11]
            previousday=int(window3.dcb1.currentText())
            if int(window3.mcb1.currentText())==2:
                if specialmonthyeardic[window3.ycb1.currentText()]=='Y':
                    window3.dcb1.clear()
                    yearlist=[]
                    for i in range(1,30):
                        yearlist.append(str(i))
                    window3.dcb1.addItems(yearlist)
                    if previousday >=29 and previousday<=31:
                        window3.dcb1.setCurrentIndex(28)
                    else:
                        window3.dcb1.setCurrentIndex(previousday-1)
                if specialmonthyeardic[window3.ycb1.currentText()]=='N':
                    window3.dcb1.clear()
                    yearlist=[]
                    for i in range(1,29):
                        yearlist.append(str(i))
                    window3.dcb1.addItems(yearlist)
                    if previousday >=29 and previousday<=31:
                        window3.dcb1.setCurrentIndex(27)
                    else:
                        window3.dcb1.setCurrentIndex(previousday-1)
            for m30 in day30month:
                if m30==int(window3.mcb1.currentText()):
                    window3.dcb1.clear()
                    yearlist=[]
                    for i in range(1,31):
                        yearlist.append(str(i))
                    window3.dcb1.addItems(yearlist)
                    if previousday >30:
                        window3.dcb1.setCurrentIndex(previousday-2)
                    else:
                        window3.dcb1.setCurrentIndex(previousday-1)
            for m in day31month:
                if m==int(window3.mcb1.currentText()):
                    window3.dcb1.clear()
                    yearlist=[]
                    for i in range(1,32):
                        yearlist.append(str(i))
                    window3.dcb1.addItems(yearlist)
                    window3.dcb1.setCurrentIndex(previousday-1)     
        def print_value2(i):
            day31month=[1,3,5,7,8,10,12]
            day30month=[4,6,9,11]
            previousday=int(window3.dcb2.currentText())
            if int(window3.mcb2.currentText())==2:
                if specialmonthyeardic[window3.ycb2.currentText()]=='Y':
                    window3.dcb2.clear()
                    yearlist=[]
                    for i in range(1,30):
                        yearlist.append(str(i))
                    window3.dcb2.addItems(yearlist)
                    if previousday >=29 and previousday<=31:
                        window3.dcb2.setCurrentIndex(28)
                    else:
                        window3.dcb2.setCurrentIndex(previousday-1)
                if specialmonthyeardic[window3.ycb2.currentText()]=='N':
                    window3.dcb2.clear()
                    yearlist=[]
                    for i in range(1,29):
                        yearlist.append(str(i))
                    window3.dcb2.addItems(yearlist)
                    if previousday >=29 and previousday<=31:
                        window3.dcb2.setCurrentIndex(27)
                    else:
                        window3.dcb2.setCurrentIndex(previousday-1)
            for m30 in day30month:
                if m30==int(window3.mcb2.currentText()):
                    window3.dcb2.clear()
                    yearlist=[]
                    for i in range(1,31):
                        yearlist.append(str(i))
                    window3.dcb2.addItems(yearlist)
                    if previousday >30:
                        window3.dcb2.setCurrentIndex(previousday-2)
                    else:
                        window3.dcb2.setCurrentIndex(previousday-1)
            for m in day31month:
                if m==int(window3.mcb2.currentText()):
                    window3.dcb2.clear()
                    yearlist=[]
                    for i in range(1,32):
                        yearlist.append(str(i))
                    window3.dcb2.addItems(yearlist)
                    window3.dcb2.setCurrentIndex(previousday-1)
        window3.ycb1.currentIndexChanged[str].connect(print_value)
        window3.mcb1.currentIndexChanged[str].connect(print_value)
        window3.ycb2.currentIndexChanged[str].connect(print_value2)
        window3.mcb2.currentIndexChanged[str].connect(print_value2)
        #window3.dcb1.currentIndexChanged[str].connect(print_value_day)
        window3.setFixedSize(window3.width(), window3.height())


        def closeaaa(event):
            window3.close()
        btnmode1 = QtWidgets.QPushButton(window3)
        btnmode1.setGeometry(QtCore.QRect(105, 135, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)


        window3.show()
        global closecheckid
        closecheckid=3

        '''with open(file='timesetsave.save',mode='w',encoding='utf-8') as strw:
            strw.write('1:')
            strw.write(str(window3.ycb1.currentIndex()))
            strw.write('\n')
            strw.write('2:')
            strw.write(str(window3.mcb1.currentIndex()))
            strw.write('\n')                                
            strw.write('3:')
            strw.write(str(window3.dcb1.currentIndex()))
            strw.write('\n')
            strw.write('4:')
            asdad=timeedit1.time()
            time1=asdad.toString('hhmm')
            strw.write(time1)
            strw.write('\n')       
            strw.write('5:')
            strw.write(str(window3.ycb2.currentIndex()))
            strw.write('\n')                
            strw.write('6:')
            strw.write(str(window3.mcb2.currentIndex()))
            strw.write('\n')                
            strw.write('7:')
            strw.write(str(window3.dcb2.currentIndex()))
            strw.write('\n')
            strw.write('8:')
            asdad=timeedit2.time()
            time2=asdad.toString('hhmm')
            strw.write(time2)
            strw.write('\n')
            strw.write('_________\n')
        year1=window3.ycb1.currentText()
        year2=window3.ycb2.currentText()
        month1=window3.mcb1.currentText()
        month2=window3.mcb2.currentText()
        day1=window3.dcb1.currentText()
        day2=window3.dcb2.currentText()
        asdad=timeedit1.time()
        time1=asdad.toString('hhmm')
        asdad=timeedit2.time()
        time2=asdad.toString('hhmm')
        global rangesearchtimedic
        rangesearchtimedic={}
        rangesearchtimedic['1']=year1
        rangesearchtimedic['2']=month1
        rangesearchtimedic['3']=day1
        rangesearchtimedic['4']=time1
        rangesearchtimedic['5']=year2
        rangesearchtimedic['6']=month2
        rangesearchtimedic['7']=day2
        rangesearchtimedic['8']=time2
        ##print(year1,year2)
        ##print(month1,month2)
        ##print(day1,day2)
        ##print(time1,time2)'''
    def aaa5():
        global window2
        window2 = MainWindow()
        window2.label1.setText(a1langconfirmdic['6'])
        addthendeletefixloaddelay = QTimeEdit(window2)
        sip.delete(addthendeletefixloaddelay)
        window2.text1 = QLineEdit(window2)
        window2.text1.setGeometry(10,35,85,20)
        window2.text2 = QLineEdit(window2)
        window2.text2.setGeometry(105,35,85,20)
        window2.setFixedSize(window2.width(), window2.height())


        def closeaaa(event):
            window2.close()
        btnmode1 = QtWidgets.QPushButton(window2)
        btnmode1.setGeometry(QtCore.QRect(105, 60, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)

        window2.show()
        global closecheckid
        closecheckid=5

        '''global windowtext1,windowtext2
        windowtext1=window2.text1.text()
        windowtext2=window2.text2.text()'''

    def aaa8():
        global window2
        window2 = MainWindow()
        window2.label1.setText(a1langconfirmdic['7'])
        addthendeletefixloaddelay = QTimeEdit(window2)
        sip.delete(addthendeletefixloaddelay)
        window2.text1 = QLineEdit(window2)
        window2.text1.setGeometry(10,35,85,20)
        window2.text2 = QLineEdit(window2)
        window2.text2.setGeometry(105,35,85,20)
        window2.setFixedSize(window2.width(), window2.height())

        def closeaaa(event):
            window2.close()
        btnmode1 = QtWidgets.QPushButton(window2)
        btnmode1.setGeometry(QtCore.QRect(105, 60, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)

        window2.show()
        global closecheckid
        closecheckid=8
        '''global windowtext1,windowtext2
        windowtext1=window2.text1.text()
        windowtext2=window2.text2.text()'''

    def aaa9():
        global window2
        window2 = MainWindow()
        window2.label1.setText(a1langconfirmdic['8'])
        addthendeletefixloaddelay = QTimeEdit(window2)
        sip.delete(addthendeletefixloaddelay)
        window2.text1 = QLineEdit(window2)
        window2.text1.setGeometry(10,35,85,20)
        window2.text2 = QLineEdit(window2)
        window2.text2.setGeometry(105,35,85,20)
        window2.setFixedSize(window2.width(), window2.height())

        def closeaaa(event):
            window2.close()
        btnmode1 = QtWidgets.QPushButton(window2)
        btnmode1.setGeometry(QtCore.QRect(105, 60, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)

        window2.show()
        global closecheckid
        closecheckid=9
        '''global windowtext1,windowtext2
        windowtext1=window2.text1.text()
        windowtext2=window2.text2.text()'''

    def aaa11():
        global window11
        window11 = MainWindow()


        aaa11x=200
        if confirmid==4:
            aaa11x=220
        aaa11y=145
        aaa11px=(maxx-aaa11x)/2
        aaa11py=(maxy-aaa11y)/2
        window11.setGeometry(int(aaa11px),int(aaa11py),int(aaa11x),int(aaa11y))



        window11.label1.setText(a1langconfirmdic['9'])
        addthendeletefixloaddelay = QTimeEdit(window11)
        sip.delete(addthendeletefixloaddelay)
        window11.aaa11cb1=QComboBox(window11)
        yearlist=[]
        for i in range(801):
            yearlist.append(str(i))
        window11.aaa11cb1.addItems(yearlist)
        window11.aaa11cb2=QComboBox(window11)
        yearlist=[]
        for i in range(801):
            yearlist.append(str(i))
        window11.aaa11cb2.addItems(yearlist)
        window11.aaa11cb1.setGeometry(10,35,85,20)
        window11.aaa11cb2.setGeometry(105,35,85,20)
        btn1 = QRadioButton("mg/100mL", window11)
        btn2 = QRadioButton("mg/l", window11)
        btn3 = QRadioButton("%BAC", window11)
        btn4 = QRadioButton("‰BAC", window11)
        btn1.move(10, 60)
        btn2.move(105, 60)
        btn3.move(10, 80)
        btn4.move(105, 80)
        global QBG1
        QBG1 = QButtonGroup()
        QBG1.addButton(btn1, 1)
        QBG1.addButton(btn2, 2)
        QBG1.addButton(btn3, 3)
        QBG1.addButton(btn4, 4)
        btn1.setChecked(True)
        ##print(cs_group.buttons())       #打印所有按钮
        ##print(cs_group.button(2))       #打印ID=2的按钮
        ##print(cs_group.checkedButton()) #打印被按下的按钮


        window11.setFixedSize(window11.width(), window11.height())




        def closeaaa(event):
            window11.close()
        btnmode1 = QtWidgets.QPushButton(window11)
        btnmode1.setGeometry(QtCore.QRect(105, 105, 85, 35))
        btnmode1.setText('OK')
        btnmode1.clicked.connect(closeaaa)
        #btnmode1.hide()
        btnmode1.setFocusPolicy(Qt.NoFocus)


        window11.show()
        global closecheckid
        closecheckid=11


        '''global checkedid
        global windowtext1,windowtext2
        windowtext1=window11.aaa11cb1.currentText()
        windowtext2=window11.aaa11cb2.currentText()
        checkedid=str(QBG1.checkedId())'''
    
    global QLineEdit
    class QLineEdit(QLineEdit):
        clicked=pyqtSignal()    #定义clicked信号
        def mouseReleaseEvent(self, QMouseEvent):
            if QMouseEvent.button()==QtCore.Qt.LeftButton:
                self.clicked.emit()     #发送clicked信号

    global win22showid
    win22showid=0

    global SearchWindow
    class SearchWindow(QWidget):
        def __init__(self):
            super(SearchWindow, self).__init__()

            #self.setWindowModality(QtCore.Qt.ApplicationModal) #只能用這window
            self.setWindowTitle(confirmlang[4])#choose range

            #self.setFixedSize(self.width(), self.height())
            
            #self.setFixedSize(800,490)
            #self.setMinimumSize(800, 490) 
            #self.setMaximumSize(800, 490)
            #self.resize(800, 490)

            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("runico.ico"),QtGui.QIcon.Selected, QtGui.QIcon.Off)
            self.setWindowIcon(icon)

            self.frame = QtWidgets.QFrame(self)
            self.frame.setGeometry(QtCore.QRect(8, 31, 240, 400))
            self.frame.setAutoFillBackground(False)
            self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame.setObjectName("frame")
            self.frame.setStyleSheet('border-width: 1px     ;border-style: solid;border-color: rgb(173, 173, 173)  ;  background-color: white;')#rgb(173, 173, 173)


            global lineEditlineEdit
            self.lineEdit=QtWidgets.QLineEdit(self.frame)
            lineEditlineEdit=self.lineEdit
            self.lineEdit.setGeometry(QtCore.QRect(40, 30, 170, 30))
            self.lineEdit.resize(190,25)
            self.lineEdit.setObjectName("lineEdit")
            self.lineEdit.setFont(QFont("Timers" , 15))
            self.lineEdit.setStyleSheet("border: 1px solid black;")
            self.lineEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)


            def sortdef(wef):
                global uutext
                #wef=[1,2,3,4,5,6,7,8,9,10,12,13,14]
                ##print(wef)
                fv=[]
                for i in range(len(wef)):
                    if i==len(wef)-1:
                        break
                    cd=wef[i+1]-wef[i]
                    if cd!=1:
                        cd=0
                    fv.append(cd)
                ##print(fv)
                ji=[]
                ji.append(wef[0])
                dsid=0
                addid=0

                lastid=0
                for i in fv:
                    lastid+=1
                    addid+=1
                    if i==1:
                        dsid+=1
                    if i!=1:
                        if dsid==0:
                            ji.append(wef[addid])
                        if dsid>1:
                            ji.append('-'+str(dsid+ji[len(ji)-1]))
                            ji.append(wef[addid])
                            dsid=0
                        if dsid==1:
                            ji.append(str(dsid+ji[len(ji)-1]))
                            ji.append(wef[addid])
                            dsid=0
                    if lastid==len(fv):
                        if dsid>1:
                            ji.append('-'+str(dsid+ji[len(ji)-1]))
                            
                            dsid=0
                        if dsid==1:
                            ji.append(str(dsid+ji[len(ji)-1]))
                            
                            dsid=0

                ##print(ji)
                prasd=0

                lastid=0
                uutext=''
                for i in ji:
                    lastid+=1
                    prasd+=1
                    if prasd==len(ji):
                        break
                    if int(ji[prasd])<0:
                        uutext=uutext+str(i)
                        ##print(str(i))
                        continue

                    uutext=uutext+str(i)+','
                    ##print(str(i)+',')


                
                uutext='['+uutext+str(ji[len(ji)-1])+']'
                return uutext

                ##print(uutext)
            def optionchange():
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                #print(id4sum)
                if id4sum==2222:
                    self.textEdit.setText(confirmlangdic['18'][1:-1])

                if id4sum==1222:
                    text1222list=[]
                    for i in range(1,12):
                        if cb1dict[str(i)].isChecked() ==True:
                            text1222list.append(i)
                    if text1222list==[]:
                        text1222list=confirmlangdic['17']
                    if text1222list==[1,2,3,4,5,6,7,8,9,10,11]:
                        text1222list=confirmlangdic['17']
                    
                    if not text1222list==confirmlangdic['17']:
                        sortdef(text1222list)
                        text1222list=uutext

                    allseleall1222=''
                    if self.mode1exactcb.isChecked()==True:
                        allseleall1222=' , '+confirmlangdic['3']


                    self.textEdit.setText(confirmlangdic['15']+str(text1222list)+allseleall1222)

                if id4sum==2122:
                    text2122list=[]
                    for i in range(1,12):
                        if cb1dict[str(i)].isChecked() ==True:
                            text2122list.append(i)
                    if text2122list==[]:
                        text2122list=confirmlangdic['18']
                    text2122list2=[] 
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2122list2.append(i)
                    if text2122list2==[]:
                        text2122list2=''
                    allseleall2122=''
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            allseleall2122=' , '+'\n'+confirmlangdic['3']
                            break
                    if not text2122list==confirmlangdic['18']:
                        sortdef(text2122list)
                        text2122list=uutext
                    if not text2122list2=='':
                        sortdef(text2122list2)
                        text2122list2=uutext
                    printtext2122list2=allseleall2122+str(text2122list2)
                    self.textEdit.setText(confirmlangdic['5']+str(text2122list)+printtext2122list2)

                if id4sum==2212:
                    text2212list=[]
                    for i in range(1,12):
                        if cb1dict[str(i)].isChecked() ==True:
                            text2212list.append(i)
                    if text2212list==[]:
                        text2212list=confirmlangdic['18']
                    text2212list2=[] 
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2212list2.append(i)
                    if text2212list2==[]:
                        text2212list2=''
                    allseleall2212=''
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            allseleall2212=' , '+'\n'+confirmlangdic['3']
                            break
                    if not text2212list==confirmlangdic['18']:
                        sortdef(text2212list)
                        text2212list=uutext
                    if not text2212list2=='':
                        sortdef(text2212list2)
                        text2212list2=uutext
                    printtext2212list2=allseleall2212+str(text2212list2)
                    self.textEdit.setText(confirmlangdic['6']+str(text2212list)+printtext2212list2)

                if id4sum==2221:
                    text2221list=[]
                    for i in range(1,12):
                        if cb1dict[str(i)].isChecked() ==True:
                            text2221list.append(i)
                    if text2221list==[]:
                        text2221list=confirmlangdic['18']
                    text2221list2=[] 
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2221list2.append(i)
                    if text2221list2==[]:
                        text2221list2=''
                    allseleall2221=''
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            allseleall2221=' , '+'\n'+confirmlangdic['3']
                            break
                    if not text2221list==confirmlangdic['18']:
                        sortdef(text2221list)
                        text2221list=uutext
                    if not text2221list2=='':
                        sortdef(text2221list2)
                        text2221list2=uutext
                    printtext2221list2=allseleall2221+str(text2221list2)
                    self.textEdit.setText(confirmlangdic['7']+str(text2221list)+printtext2221list2)

                if id4sum==2121:
                    text2121list=[]
                    for i in range(1,12):
                        if cb1dict[str(i)].isChecked() ==True:
                            text2121list.append(i)
                    if text2121list==[]:
                        text2121list=confirmlangdic['18']

                    text2121list2=[] 
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2121list2.append(i)
                    if text2121list2==[]:
                        text2121list2=''

                    allseleall2121=''
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            allseleall2121=' , '+'\n'+confirmlangdic['3']
                            break
                    
                    text2121list3=[]
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2121list3.append(i)
                    if text2121list3==[]:
                        text2121list3=''

                    removelist=[4,6,7,10]
                    text2121listrange=[]
                    for i in text2121list:
                        if text2121list==confirmlangdic['18']:
                            break
                        continueid=0
                        for y in removelist:
                            if y==i:
                                continueid=1
                        if continueid==1:
                            continue
                        text2121listrange.append(i)
                    if text2121listrange==[]:
                        text2121listrange=confirmlangdic['18']

                    if not text2121list==confirmlangdic['18']:
                        sortdef(text2121list)
                        text2121list=uutext

                    if not text2121listrange==confirmlangdic['18']:
                        sortdef(text2121listrange)
                        text2121listrange=uutext

                    if not text2121list3=='':
                        sortdef(text2121list3)
                        text2121list3=uutext

                    self.textEdit.setText(confirmlangdic['5']+str(text2121list)+' , \n'+confirmlangdic['7']+str(text2121listrange)+allseleall2121+str(text2121list3))

                if id4sum==2211:
                    text2211list=[]
                    for i in range(1,12):
                        if cb1dict[str(i)].isChecked() ==True:
                            text2211list.append(i)
                    if text2211list==[]:
                        text2211list=confirmlangdic['18']

                    text2211list2=[] 
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2211list2.append(i)
                    if text2211list2==[]:
                        text2211list2=''

                    allseleall2211=''
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            allseleall2211=' , '+'\n'+confirmlangdic['3']
                            break
                    
                    text2211list3=[]
                    for i in range(1,12):
                        if cb2dict[str(i)].isChecked() ==True:
                            text2211list3.append(i)
                    if text2211list3==[]:
                        text2211list3=''

                    removelist=[4,6,7,10]
                    text2211listrange=[]
                    for i in text2211list:
                        if text2211list==confirmlangdic['18']:
                            break
                        continueid=0
                        for y in removelist:
                            if y==i:
                                continueid=1
                        if continueid==1:
                            continue
                        text2211listrange.append(i)
                    if text2211listrange==[]:
                        text2211listrange=confirmlangdic['18']

                    if not text2211list==confirmlangdic['18']:
                        sortdef(text2211list)
                        text2211list=uutext

                    if not text2211listrange==confirmlangdic['18']:
                        sortdef(text2211listrange)
                        text2211listrange=uutext

                    if not text2211list3=='':
                        sortdef(text2211list3)
                        text2211list3=uutext

                    self.textEdit.setText(confirmlangdic['6']+str(text2211list)+' , \n'+confirmlangdic['7']+str(text2211listrange)+allseleall2211+str(text2211list3))

            def btnmode1event(event):
                global firstclickbtnmode2event
                firstclickbtnmode2event+=1
    
                self.labelmode1.show()
                self.labelmode1line.show()
                self.btnmode2.show()
                self.lineEdit.show()
                self.mode1exactcb.show()


                self.labelmode2.hide()
                self.btnmode1.hide()
                self.frame.setGeometry(QtCore.QRect(8, 31, 240, 370))



                for i in range(11):
                    cb1dict[str(i+1)].move(28, 29+i*25)
                    #labelkeydict[str(i+1)].move(48, 29+i*25)
                    numberlabeldic[str(i+1)].move(13, 29+i*25)
                    bidict[str(i+1)].hide()
                    cb2dict[str(i+1)].hide()



                self.cb2selectall.hide()
                self.frame3.move(250,267)
                self.frame2.move(13,100)
                self.cb1selectall.move(28, 5)

                self.selectalllabel.move(21, 105)
                if confirmid==4:
                    self.selectalllabel.move(10, 105)
                if confirmid==1 or confirmid==2:
                    self.selectalllabel.move(16, 105)


                self.labelmode1.raise_()
                self.labelmode1line.raise_()
                self.setFixedSize(565, 405)
                #self.resize(565, 405)
                self.textEdit.setGeometry(QtCore.QRect(250, 30, 320, 200))
                self.optionlabel.setGeometry(QtCore.QRect(255, 16, 50, 20))


                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global win2cmb1curruntdic,confirmlangdic
                global menu1,menu2,menu3,menu4

                global history2,history3,history4,history2id,history3id,history4id
                history2=win2cmb1curruntdic['2']
                history3=win2cmb1curruntdic['3']
                history4=win2cmb1curruntdic['4']
                history2id=cmb1moresearchid
                history3id=cmb1morematchid
                history4id=cmb1rangesearchid

                win2cmb1curruntdic['1']='✔'+confirmlangdic['15']
                win2cmb1curruntdic['2']=confirmlangdic['5']
                win2cmb1curruntdic['3']=confirmlangdic['6']
                win2cmb1curruntdic['4']=confirmlangdic['7']


                cmb1WholeSearchid=1000
                cmb1moresearchid=200
                cmb1morematchid=20
                cmb1rangesearchid=2
                self.menu.removeAction(menu1)
                self.menu.removeAction(menu2)
                self.menu.removeAction(menu3)
                self.menu.removeAction(menu4)

                menu1=QAction(win2cmb1curruntdic['1'], self)
                self.menu.addAction(menu1)
                menu1.triggered.connect(menu1def)

                menu2=QAction(win2cmb1curruntdic['2'], self)
                self.menu.addAction(menu2)
                menu2.triggered.connect(menu2def)

                menu3=QAction(win2cmb1curruntdic['3'], self)
                self.menu.addAction(menu3)
                menu3.triggered.connect(menu3def)

                menu4=QAction(win2cmb1curruntdic['4'], self)
                self.menu.addAction(menu4)
                menu4.triggered.connect(menu4def)

                try:
                    change11112222()
                except:
                    pass
                optionchange()

            def btnmode1eventnoe():
                self.labelmode1.show()
                self.labelmode1line.show()
                self.btnmode2.show()
                self.lineEdit.show()
                self.mode1exactcb.show()


                self.labelmode2.hide()
                self.btnmode1.hide()
                self.frame.setGeometry(QtCore.QRect(8, 31, 240, 370))



                for i in range(11):
                    cb1dict[str(i+1)].move(28, 29+i*25)
                    #labelkeydict[str(i+1)].move(48, 29+i*25)
                    numberlabeldic[str(i+1)].move(13, 29+i*25)
                    bidict[str(i+1)].hide()
                    cb2dict[str(i+1)].hide()



                self.cb2selectall.hide()
                self.frame3.move(250,267)
                self.frame2.move(13,100)
                self.cb1selectall.move(28, 5)

                self.selectalllabel.move(21, 105)
                if confirmid==4:
                    self.selectalllabel.move(10, 105)
                if confirmid==1 or confirmid==2:
                    self.selectalllabel.move(16, 105)


                self.labelmode1.raise_()
                self.labelmode1line.raise_()
                self.setFixedSize(565, 405)
                #self.resize(565, 405)
                self.textEdit.setGeometry(QtCore.QRect(250, 30, 320, 200))
                self.optionlabel.setGeometry(QtCore.QRect(255, 16, 50, 20))




                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global win2cmb1curruntdic,confirmlangdic
                global menu1,menu2,menu3,menu4

                global history2,history3,history4,history2id,history3id,history4id
                history2=win2cmb1curruntdic['2']
                history3=win2cmb1curruntdic['3']
                history4=win2cmb1curruntdic['4']
                history2id=cmb1moresearchid
                history3id=cmb1morematchid
                history4id=cmb1rangesearchid



                win2cmb1curruntdic['1']='✔'+confirmlangdic['15']
                win2cmb1curruntdic['2']=confirmlangdic['5']
                win2cmb1curruntdic['3']=confirmlangdic['6']
                win2cmb1curruntdic['4']=confirmlangdic['7']
                cmb1WholeSearchid=1000
                cmb1moresearchid=200
                cmb1morematchid=20
                cmb1rangesearchid=2
                self.menu.removeAction(menu1)
                self.menu.removeAction(menu2)
                self.menu.removeAction(menu3)
                self.menu.removeAction(menu4)

                menu1=QAction(win2cmb1curruntdic['1'], self)
                self.menu.addAction(menu1)
                menu1.triggered.connect(menu1def)

                menu2=QAction(win2cmb1curruntdic['2'], self)
                self.menu.addAction(menu2)
                menu2.triggered.connect(menu2def)

                menu3=QAction(win2cmb1curruntdic['3'], self)
                self.menu.addAction(menu3)
                menu3.triggered.connect(menu3def)

                menu4=QAction(win2cmb1curruntdic['4'], self)
                self.menu.addAction(menu4)
                menu4.triggered.connect(menu4def)


            self.btnmode1 = QtWidgets.QPushButton(self)
            self.btnmode1.setGeometry(QtCore.QRect(8, 8, 100, 25))
            self.btnmode1.setText(confirmlangdic['15'])#("Search")
            self.btnmode1.clicked.connect(btnmode1event)
            self.btnmode1.hide()
            self.btnmode1.setFocusPolicy(Qt.NoFocus)

            self.labelmode1 = QtWidgets.QLabel(self)
            self.labelmode1.setGeometry(QtCore.QRect(8, 8, 100, 25))
            self.labelmode1.setText(confirmlangdic['15'])#("Search")
            self.labelmode1.setStyleSheet('border-width: 1px     ;border-style: solid;border-color: rgb(173, 173, 173)  ;  background-color: white;')
            self.labelmode1.setAlignment(QtCore.Qt.AlignCenter)
            self.labelmode1.setFocusPolicy(Qt.NoFocus)
            
            self.labelmode1line = QtWidgets.QLabel(self)
            self.labelmode1line.setGeometry(QtCore.QRect(9, 32, 108, 5))
            self.labelmode1line.setStyleSheet('border-width: 1px     ;border-style: solid;border-color: white  ;  background-color: white;')
            self.labelmode1line.setFocusPolicy(Qt.NoFocus)



            global firstclickbtnmode2event
            firstclickbtnmode2event=0
            def btnmode2event(event):
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global win2cmb1curruntdic,confirmlangdic
                global menu1,menu2,menu3,menu4
                global history2,history3,history4,history2id,history3id,history4id

                global firstclickbtnmode2event
                firstclickbtnmode2event+=1

                if firstclickbtnmode2event>1:
    
                    history2=history2
                    history3=history3
                    history4=history4
                    history2id=history2id
                    history3id=history3id
                    history4id=history4id


                if firstclickbtnmode2event==1:
                    history2=confirmlangdic['5']
                    history3=confirmlangdic['6']
                    history4=confirmlangdic['7']
                    history2id=200
                    history3id=20
                    history4id=2
                

                self.btnmode2.hide()
                self.labelmode1line.hide()
                self.labelmode1.hide()    
                self.lineEdit.hide()
                self.mode1exactcb.hide()

                self.labelmode2.show()
                self.btnmode1.show()
                self.labelmode2line.show()

                self.frame.setGeometry(QtCore.QRect(8, 31, 360, 335))




                for i in range(11):
                    cb1dict[str(i+1)].move(150, 29+i*25)
                    numberlabeldic[str(i+1)].move(5, 29+i*25)
                    #labelkeydict[str(i+1)].move(170, 29+i*25)
                    bidict[str(i+1)].show()
                    cb2dict[str(i+1)].show()


                self.cb1selectall.move(150, 5)
                self.cb2selectall.show()


                self.frame2.move(20,60)
                self.frame3.move(370,232)


                self.selectalllabel.move(18, 66)
                if confirmid==4:
                    self.selectalllabel.move(10, 66)
                if confirmid==1 or confirmid==2:
                    self.selectalllabel.move(15, 66)


                self.labelmode2.raise_()
                self.labelmode2line.raise_()

                self.setFixedSize(685, 370)
                #self.resize(685, 370)
                self.textEdit.setGeometry(QtCore.QRect(370, 30, 320, 200))

                self.optionlabel.setGeometry(QtCore.QRect(375, 16, 50, 20))

                win2cmb1curruntdic['1']=confirmlangdic['15']
                win2cmb1curruntdic['2']=history2
                win2cmb1curruntdic['3']=history3
                win2cmb1curruntdic['4']=history4

                #print(win2cmb1curruntdic)
                cmb1WholeSearchid=2000
                cmb1moresearchid=history2id
                cmb1morematchid=history3id
                cmb1rangesearchid=history4id
                self.menu.removeAction(menu1)
                self.menu.removeAction(menu2)
                self.menu.removeAction(menu3)
                self.menu.removeAction(menu4)

                menu1=QAction(win2cmb1curruntdic['1'], self)
                self.menu.addAction(menu1)
                menu1.triggered.connect(menu1def)

                menu2=QAction(win2cmb1curruntdic['2'], self)
                self.menu.addAction(menu2)
                menu2.triggered.connect(menu2def)

                menu3=QAction(win2cmb1curruntdic['3'], self)
                self.menu.addAction(menu3)
                menu3.triggered.connect(menu3def)

                menu4=QAction(win2cmb1curruntdic['4'], self)
                self.menu.addAction(menu4)
                menu4.triggered.connect(menu4def)

                try:
                    change11112222()
                except:
                    pass
                optionchange()

            def btnmode2eventnoe():
                self.btnmode2.hide()
                self.labelmode1line.hide()
                self.labelmode1.hide()    
                self.lineEdit.hide()
                self.mode1exactcb.hide()

                self.labelmode2.show()
                self.btnmode1.show()
                self.labelmode2line.show()

                self.frame.setGeometry(QtCore.QRect(8, 31, 360, 335))




                for i in range(11):
                    cb1dict[str(i+1)].move(150, 29+i*25)
                    numberlabeldic[str(i+1)].move(5, 29+i*25)
                    #labelkeydict[str(i+1)].move(170, 29+i*25)
                    bidict[str(i+1)].show()
                    cb2dict[str(i+1)].show()


                self.cb1selectall.move(150, 5)
                self.cb2selectall.show()


                self.frame2.move(20,60)
                self.frame3.move(370,232)

                self.selectalllabel.move(18, 66)
                if confirmid==4:
                    self.selectalllabel.move(10, 66)
                if confirmid==1 or confirmid==2:
                    self.selectalllabel.move(15, 66)

                self.labelmode2.raise_()
                self.labelmode2line.raise_()

                self.setFixedSize(685, 370)
                #self.resize(685, 370)
                self.textEdit.setGeometry(QtCore.QRect(370, 30, 320, 200))
                self.optionlabel.setGeometry(QtCore.QRect(375, 16, 50, 20))

                global win2cmb1curruntdic,confirmlangdic
                win2cmb1curruntdic['1']=confirmlangdic['15']
                global menu1,menu2,menu3,menu4
                global cmb1WholeSearchid
                cmb1WholeSearchid=2000
                self.menu.removeAction(menu1)
                self.menu.removeAction(menu2)
                self.menu.removeAction(menu3)
                self.menu.removeAction(menu4)

                menu1=QAction(win2cmb1curruntdic['1'], self)
                self.menu.addAction(menu1)
                menu1.triggered.connect(menu1def)

                menu2=QAction(win2cmb1curruntdic['2'], self)
                self.menu.addAction(menu2)
                menu2.triggered.connect(menu2def)

                menu3=QAction(win2cmb1curruntdic['3'], self)
                self.menu.addAction(menu3)
                menu3.triggered.connect(menu3def)

                menu4=QAction(win2cmb1curruntdic['4'], self)
                self.menu.addAction(menu4)
                menu4.triggered.connect(menu4def)

        
            self.btnmode2 = QtWidgets.QPushButton(self)
            self.btnmode2.setGeometry(QtCore.QRect(105, 8, 100, 25))
            self.btnmode2.setText(confirmlangdic['23'])#("Advanced Search")
            self.btnmode2.clicked.connect(btnmode2event)
            self.btnmode2.setFocusPolicy(Qt.NoFocus)


            self.labelmode2 = QtWidgets.QLabel(self)
            self.labelmode2.setGeometry(QtCore.QRect(105, 8, 100, 25))
            self.labelmode2.setText(confirmlangdic['23'])#("Advanced Search")
            self.labelmode2.setStyleSheet('border-width: 1px     ;border-style: solid;border-color: rgb(173, 173, 173)  ;  background-color: white;')
            self.labelmode2.setAlignment(QtCore.Qt.AlignCenter)
            self.labelmode2.setFocusPolicy(Qt.NoFocus)
            self.labelmode2.hide()

            self.labelmode2line = QtWidgets.QLabel(self)
            self.labelmode2line.setGeometry(QtCore.QRect(85, 32, 128, 5))
            self.labelmode2line.setStyleSheet('border-width: 1px     ;border-style: solid;border-color: white  ;  background-color: white;')
            self.labelmode2line.setFocusPolicy(Qt.NoFocus)


            self.frame2 = QtWidgets.QFrame(self)
            self.frame2.setGeometry(QtCore.QRect(20, 130, 441, 350))
            self.frame2.setAutoFillBackground(False)
            self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame2.setObjectName("frame")
            self.frame2.setFocusPolicy(Qt.NoFocus)
            #self.frame2.setStyleSheet('background-color:white;')



            self.labelmode1.raise_()
            self.labelmode1line.raise_()



            global bidict,bidictid
            bidict={}
            bidictid=0
            for bi in range(11):
                bidictid+=1
                self.biline=QLineEdit(self.frame2)
                #self.biline=QtWidgets.QLineEdit(self.frame2)
                self.biline.setGeometry(QtCore.QRect(40, 26+bi*25, 100, 20))
                self.biline.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
                #self.biline.setStyleSheet("background-color: rgb(176, 196, 222)")#('border-width: 1px     ;border-style: solid;border-color: rgb(240, 240, 240)  ;  background-color: rgb(240, 240, 240);')
                bidict[str(bidictid)]=self.biline

            

            def bevent1():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa1()
                
            def bevent2():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa2()

            def bevent3():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa3()
            def bevent5():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa5()
            def bevent8():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa8()
            def bevent9():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa9()
            def bevent11():
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                if id4sum==2221 or id4sum==2121 or id4sum==2211:
                    aaa11()


            bidict['1'].clicked.connect(bevent1)
            bidict['2'].clicked.connect(bevent2)
            bidict['3'].clicked.connect(bevent3)
            bidict['5'].clicked.connect(bevent5)
            bidict['8'].clicked.connect(bevent8)
            bidict['9'].clicked.connect(bevent9)
            bidict['11'].clicked.connect(bevent11)

            def cbstatechange_changeoption():
                optionchange()



            self.cb1selectall=QCheckBox(self.frame2)
            self.cb1selectall.move(150, 5)
            global cb1alreadycheckdict
            cb1alreadycheckdict={}
            for z in range(1,12):
                cb1alreadycheckdict[str(z)]='N'
            def cb1selectallclickBox(state):
                global cb1alreadycheckdict
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid

                rangeid=[1,2,3,5,8,9,11]
                norangeid=[4,6,7,10]
                global continueid
                continueid=0
                if state==2:
                    cb1alreadycheckdict={}
                    for z in range(1,12):
                        cb1alreadycheckdict[str(z)]='N'
                    for z in range(1,12):
                        if cb1dict[str(z)].isChecked()==True:
                            cb1alreadycheckdict[str(z)]='T'

                    for i in range(1,12):
                        if id4sum==2221:
                            for j in norangeid:
                                if i==j:
                                    continueid=1
                            if continueid==1:
                                continueid=0
                                continue
                        cb1dict[str(i)].setChecked(True)

                if state==0:
                    for i in range(1,12):
                        if id4sum==2221:
                            for j in norangeid:
                                if i==j:
                                    continueid=1
                            if continueid==1:
                                continueid=0
                                continue

                        if cb1alreadycheckdict[str(i)]=='T':
                            continue
                        cb1dict[str(i)].setChecked(False)
                optionchange()
            self.cb1selectall.stateChanged.connect(cb1selectallclickBox)
            self.cb1selectall.setFocusPolicy(Qt.NoFocus)

            global keylist

            global cb1dict,cb1dictid
            cb1dict={}
            cb1dictid=0
            for i in range(11):
                cb1dictid+=1
                self.cb1 = QCheckBox(keylist[i],self.frame2)
                self.cb1
                self.cb1.move(150, 29+i*25)
                self.cb1.stateChanged.connect(cbstatechange_changeoption)
                self.cb1.setFocusPolicy(Qt.NoFocus)
                cb1dict[str(cb1dictid)]=self.cb1


            

            self.cb2selectall=QCheckBox(self.frame2)
            self.cb2selectall.move(20, 5)
            global cb2alreadycheckdict
            cb2alreadycheckdict={}
            for z in range(1,12):
                cb2alreadycheckdict[str(z)]='N'

            def cb2selectallclickBox(state):
                global cb2alreadycheckdict
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid

                rangeid=[1,2,3,5,8,9,11]
                norangeid=[4,6,7,10]
                global continueid
                continueid=0
                if state==2:

                    for z in range(1,12):
                        cb2alreadycheckdict[str(z)]='N'
                    for z in range(1,12):
                        if cb2dict[str(z)].isChecked()==True:
                            cb2alreadycheckdict[str(z)]='T'

                    for i in range(1,12):
                        if id4sum==2221:
                            for j in norangeid:
                                if i==j:
                                    continueid=1
                            if continueid==1:
                                continueid=0
                                continue
                        cb2dict[str(i)].setChecked(True)

                if state==0:
                    for i in range(1,12):
                        if id4sum==2221:
                            for j in norangeid:
                                if i==j:
                                    continueid=1
                            if continueid==1:
                                continueid=0
                                continue

                        if cb2alreadycheckdict[str(i)]=='T':
                            continue
                        cb2dict[str(i)].setChecked(False)
                optionchange()
            self.cb2selectall.stateChanged.connect(cb2selectallclickBox)
            self.cb2selectall.setFocusPolicy(Qt.NoFocus)



            global cb2dict,cb2dictid
            cb2dict={}
            cb2dictid=0
            for i in range(11):
                cb2dictid+=1
                self.cb2 = QCheckBox(self.frame2)
                self.cb2.move(20, 29+i*25)
                self.cb2.stateChanged.connect(cbstatechange_changeoption)
                self.cb2.setFocusPolicy(Qt.NoFocus)
                cb2dict[str(cb2dictid)]=self.cb2
                

            global numberlabeldic,numberlabeldicid
            numberlabeldic={}
            numberlabeldicid=0
            for i in range(11):
                numberlabeldicid+=1
                self.numberlabel= QLabel(self.frame2)
                self.numberlabel.move(5, 29+i*25)
                self.numberlabel.setText(str(i+1))
                self.numberlabel.setFocusPolicy(Qt.NoFocus)
                numberlabeldic[str(numberlabeldicid)]=self.numberlabel






            '''global labelkeydict,labelkeydictid
            labelkeydict={}
            labelkeydictid=0
            with open(file='Autofile/key.save',mode='r',encoding='utf-8')as lff:
                asda=lff.readlines()
            dfdsf=eval(asda[0])
            for i in range(11):
                labelkeydictid+=1
                self.labelkey= QLabel(self.frame2)
                self.labelkey.move(170, 29+i*25)
                self.labelkey.setText(dfdsf[i])
                labelkeydict[str(labelkeydictid)]=self.labelkey'''


            self.selectalllabel= QLabel(self)
            self.selectalllabel.move(9, 4)#All
            self.selectalllabel.setText(confirmlangdic['4'])#('All')
            self.selectalllabel.setFocusPolicy(Qt.NoFocus)

            self.selectalllabel.move(21, 105)
            if confirmid==4:
                self.selectalllabel.move(10, 105)
            if confirmid==1 or confirmid==2:
                self.selectalllabel.move(16, 105)


            self.matchlabel= QLabel(self)
            self.matchlabel.move(10, 45)
            self.matchlabel.setText(confirmlangdic['3'])#('Exact Match')
            self.matchlabel.setFocusPolicy(Qt.NoFocus)

            global mode1exactcbmode1exactcb
            self.mode1exactcb=QCheckBox(self)
            mode1exactcbmode1exactcb=self.mode1exactcb
            self.mode1exactcb.move(30, 63)
            self.mode1exactcb.stateChanged.connect(cbstatechange_changeoption)
            self.mode1exactcb.setFocusPolicy(Qt.NoFocus)





            for i in range(11):
                cb1dict[str(i+1)].move(28, 29+i*25)
                #labelkeydict[str(i+1)].move(48, 29+i*25)
                numberlabeldic[str(i+1)].move(13, 29+i*25)
                self.frame2.move(13,100)
                self.cb1selectall.move(28, 5)
                self.frame.setGeometry(QtCore.QRect(8, 31, 240, 370))
                bidict[str(i+1)].hide()
                cb2dict[str(i+1)].hide()
            self.cb2selectall.hide()



            self.frame3 = QtWidgets.QFrame(self)
            self.frame3.setGeometry(QtCore.QRect(20, 130, 441, 350))
            self.frame3.setAutoFillBackground(False)
            self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
            self.frame3.setFocusPolicy(Qt.NoFocus)
            #self.frame3.setObjectName("frame")
            #self.frame2.setStyleSheet('background-color:white;')






            self.btreset = QtWidgets.QPushButton(self.frame3)
            #self.btreset.setGeometry(QtCore.QRect(480, 350, 80, 45))
            self.btreset.setGeometry(QtCore.QRect(0, 0, 80, 45))
            self.btreset.setText(confirmlangdic['9'])#("Reset")
            self.btreset.setFocusPolicy(Qt.NoFocus)

            self.btclean = QtWidgets.QPushButton(self.frame3)
            #self.btclean.setGeometry(QtCore.QRect(560, 350, 80, 45))
            self.btclean.setGeometry(QtCore.QRect(80, 0, 80, 45))
            self.btclean.setText(confirmlangdic['13'])#("Clean")
            self.btclean.setFocusPolicy(Qt.NoFocus)

            self.btloadsetting = QtWidgets.QPushButton(self.frame3)
            #self.btloadsetting.setGeometry(QtCore.QRect(640, 350, 150, 45))
            self.btloadsetting.setGeometry(QtCore.QRect(160, 0, 150, 45))
            self.btloadsetting.setText(confirmlangdic['12'])#("Load Set Up")
            self.btloadsetting.setFocusPolicy(Qt.NoFocus)


            self.btsearchmode = QtWidgets.QPushButton(self.frame3)
            #self.btsearchmode.setGeometry(QtCore.QRect(480, 395, 160, 45))
            self.btsearchmode.setGeometry(QtCore.QRect(0, 45, 160, 45))
            self.btsearchmode.setText(confirmlangdic['19'])#("Search Mode")
            self.btsearchmode.setFocusPolicy(Qt.NoFocus)




            def loadmenuchange():
                global autoloadmodeid
                global loadmenuautoload,loadmenuloadspace,loadmenuloadchoose

                self.loadmenu.removeAction(loadmenuautoload)
                self.loadmenu.removeAction(loadmenuloadspace)
                self.loadmenu.removeAction(loadmenuloadchoose)
        
                loadmenuautoload=QAction(confirmlangdic['14'], self)
                loadmenuloadspace=QAction(confirmlangdic['24'], self)
                loadmenuloadchoose=QAction(confirmlangdic['25'], self)

                if autoloadmodeid==1:
                    loadmenuautoload=QAction('✔'+confirmlangdic['14'], self)
                    loadmenuloadspace=QAction(confirmlangdic['24'], self)
                    loadmenuloadchoose=QAction(confirmlangdic['25'], self)
                if autoloadmodeid==3:
                    loadmenuautoload=QAction(confirmlangdic['14'], self)
                    loadmenuloadspace=QAction('✔'+confirmlangdic['24'], self)
                    loadmenuloadchoose=QAction(confirmlangdic['25'], self)


                if autoloadmodeid==2:
                    loadmenuautoload=QAction(confirmlangdic['14'], self)
                    loadmenuloadspace=QAction(confirmlangdic['24'], self)
                    loadmenuloadchoose=QAction('✔'+confirmlangdic['25'], self)

                

                self.loadmenu.addAction(loadmenuautoload)
                self.loadmenu.addAction(loadmenuloadspace)
                self.loadmenu.addAction(loadmenuloadchoose)  


                loadmenuautoload.triggered.connect(loadmenuautoloaddef)
                loadmenuloadspace.triggered.connect(loadmenuloadspacedef)
                loadmenuloadchoose.triggered.connect(loadmenuloadchoosedef)

            self.loadmenu=QMenu(self)
            self.loadmenu.setFocusPolicy(Qt.NoFocus)

            self.btloadsetting.setMenu(self.loadmenu)


            loadmenusave=QAction(confirmlangdic['10'], self)
            loadmenusaveas=QAction(confirmlangdic['11'], self)
            loadmenuload=QAction(confirmlangdic['26'], self)       


            global loadmenuautoload,loadmenuloadspace,loadmenuloadchoose
            loadmenuautoload=QAction(confirmlangdic['14'], self)
            loadmenuloadspace=QAction(confirmlangdic['24'], self)
            loadmenuloadchoose=QAction(confirmlangdic['25'], self)


            self.loadmenu.addAction(loadmenusave)
            self.loadmenu.addAction(loadmenusaveas)
            self.loadmenu.addAction(loadmenuload)    

            self.loadmenu.addAction(loadmenuautoload)
            self.loadmenu.addAction(loadmenuloadspace)
            self.loadmenu.addAction(loadmenuloadchoose)    

            global change11112222
            def change11112222():
                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                rangeid=[1,2,3,5,8,9,11]
                norangeid=[4,6,7,10]
                global aaa1dic,aaa2dic,aaa3dic,aaa5dic,aaa8dic,aaa9dic,aaa11dic
                aaa1dic={}
                aaa2dic={}
                aaa3dic={}
                aaa5dic={}
                aaa8dic={}
                aaa9dic={}
                aaa11dic={}
                if id4sum==1222:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: white")
                        bidict[str(i)].setReadOnly(False)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(True)
                        cb1dict[str(i)].setEnabled(True)
                        cb2dict[str(i)].setEnabled(True)
                if id4sum==2222:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: white")
                        bidict[str(i)].setReadOnly(False)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(True)
                        cb1dict[str(i)].setEnabled(True)
                        cb2dict[str(i)].setEnabled(True)
                if id4sum==2122:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: white")
                        bidict[str(i)].setReadOnly(False)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(True)
                        cb1dict[str(i)].setEnabled(True)
                        cb2dict[str(i)].setEnabled(True)
                if id4sum==2212:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: white")
                        bidict[str(i)].setReadOnly(False)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(True)
                        cb1dict[str(i)].setEnabled(True)
                        cb2dict[str(i)].setEnabled(True)
                if id4sum==2221:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: rgb(176, 196, 222)")
                        bidict[str(i)].setText('')
                        bidict[str(i)].setReadOnly(True)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(False)
                        cb1dict[str(i)].setEnabled(False)
                        cb2dict[str(i)].setEnabled(False)

                        norangeid=[4,6,7,10]
                        for i in norangeid:
                            bidict[str(i)].setText('')
                            cb1dict[str(i)].setChecked(False)
                            cb2dict[str(i)].setChecked(False)
                if id4sum==2121:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: rgb(176, 196, 222)")
                        bidict[str(i)].setText('')
                        bidict[str(i)].setReadOnly(True)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(True)
                        cb1dict[str(i)].setEnabled(True)
                        cb2dict[str(i)].setEnabled(True)

                if id4sum==2211:
                    for i in rangeid:
                        bidict[str(i)].setStyleSheet("background-color: rgb(176, 196, 222)")
                        bidict[str(i)].setText('')
                        bidict[str(i)].setReadOnly(True)
                    for i in norangeid:
                        bidict[str(i)].setEnabled(True)
                        cb1dict[str(i)].setEnabled(True)
                        cb2dict[str(i)].setEnabled(True)
            


            def fffs():
                global menu1,menu2,menu3,menu4
                global menuB2,menuB3,menuB4
                self.menu.removeAction(menu1)
                self.menu.removeAction(menu2)
                self.menu.removeAction(menu3)
                self.menu.removeAction(menu4)

                self.menuB.removeAction(menuB2)
                self.menuB.removeAction(menuB3)
                self.menuB.removeAction(menuB4)

                menu1=QAction(win2cmb1curruntdic['1'], self)
                
                self.menu.addAction(menu1)
                menu1.triggered.connect(menu1def)

                menu2=QAction(win2cmb1curruntdic['2'], self)
                menuB2=QAction(win2cmb1curruntdic['2'], self)
                self.menu.addAction(menu2)
                self.menuB.addAction(menuB2)
                menu2.triggered.connect(menu2def)
                menuB2.triggered.connect(menu2def)

                menu3=QAction(win2cmb1curruntdic['3'], self)
                menuB3=QAction(win2cmb1curruntdic['3'], self)
                self.menu.addAction(menu3)
                self.menuB.addAction(menuB3)
                menu3.triggered.connect(menu3def)
                menuB3.triggered.connect(menu3def)

                menu4=QAction(win2cmb1curruntdic['4'], self)
                menuB4=QAction(win2cmb1curruntdic['4'], self)
                self.menu.addAction(menu4)
                self.menuB.addAction(menuB4)
                menu4.triggered.connect(menu4def)
                menuB4.triggered.connect(menu4def)

                global id4sum
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid

                if id4sum==1222:
                    btnmode1eventnoe()
                if id4sum==2222:
                    btnmode2eventnoe()
                if id4sum==2122:
                    btnmode2eventnoe()
                if id4sum==2212:
                    btnmode2eventnoe()
                if id4sum==2221:
                    btnmode2eventnoe()

                if id4sum==2121:
                    btnmode2eventnoe()

                if id4sum==2211:
                    btnmode2eventnoe()

                #change diffmode2211

                change11112222()   
                optionchange()



            global savesettingdefflag
            savesettingdefflag=0
            def loadmenusavedef():
                global savesettingdefflag
                global filesavename

                if savesettingdefflag==0:
                    filesavename,  _ = QFileDialog.getSaveFileName(self, confirmlangdic['10'], './save',"Text Files (*.txt)")#,"All Files (*);;Text Files (*.txt)")
                    if filesavename:
                        savewin2dic={}
                        fwid=0

                        fwid+=1
                        ttq=self.cb1selectall.isChecked()
                        savewin2dic[str(fwid)]=ttq

                        fwid+=1
                        ttq=self.cb2selectall.isChecked()
                        savewin2dic[str(fwid)]=ttq

                        for i in range(11):
                            fwid+=1
                            ttq=cb1dict[str(i+1)].isChecked()
                            savewin2dic[str(fwid)]=ttq

                        for i in range(11):
                            fwid+=1
                            ttq=cb2dict[str(i+1)].isChecked()
                            savewin2dic[str(fwid)]=ttq

                        fwid+=1
                        ttq=self.mode1exactcb.isChecked()
                        savewin2dic[str(fwid)]=ttq

                        
                        fwid+=1
                        ttq=self.lineEdit.text()
                        ttq.strip()
                        savewin2dic[str(fwid)]=ttq






                        for i in range(11):
                            fwid+=1
                            ttq=bidict[str(i+1)].text()

                            savewin2dic[str(fwid)]=ttq

                        fwid+=1
                        ttq=id4sum
                        savewin2dic[str(fwid)]=ttq


                        for i in range(38):
                            savewin2dic[str(i+1)]=str(savewin2dic[str(i+1)]).strip()

                        with open(file=filesavename,mode='w+',encoding='utf-8')as f:
                            for i in range(38):
                                f.write(str(savewin2dic[str(i+1)]))
                                if i==37:
                                    f.write('\n')
                                    f.write('____________')
                                    break
                                f.write('\n')


                        savesettingdefflag+=1
                if savesettingdefflag>=1:
                    savewin2dic={}
                    fwid=0

                    fwid+=1
                    ttq=self.cb1selectall.isChecked()
                    savewin2dic[str(fwid)]=ttq

                    fwid+=1
                    ttq=self.cb2selectall.isChecked()
                    savewin2dic[str(fwid)]=ttq

                    for i in range(11):
                        fwid+=1
                        ttq=cb1dict[str(i+1)].isChecked()
                        savewin2dic[str(fwid)]=ttq

                    for i in range(11):
                        fwid+=1
                        ttq=cb2dict[str(i+1)].isChecked()
                        savewin2dic[str(fwid)]=ttq




                    fwid+=1
                    ttq=self.mode1exactcb.isChecked()
                    savewin2dic[str(fwid)]=ttq

                    
                    fwid+=1
                    ttq=self.lineEdit.text()
                    ttq.strip()
                    savewin2dic[str(fwid)]=ttq


                    

                    for i in range(11):
                        fwid+=1
                        ttq=bidict[str(i+1)].text()
                        savewin2dic[str(fwid)]=ttq
                        
                    fwid+=1
                    ttq=id4sum
                    savewin2dic[str(fwid)]=ttq



                    for i in range(38):
                        savewin2dic[str(i+1)]=str(savewin2dic[str(i+1)]).strip()

                    with open(file=filesavename,mode='w+',encoding='utf-8')as f:
                        pass
                    with open(file=filesavename,mode='w+',encoding='utf-8')as f:
                        for i in range(38):
                            f.write(str(savewin2dic[str(i+1)]))
                            if i==37:
                                f.write('\n')
                                f.write('____________')
                                break
                            f.write('\n')


            def loadmenusaveasdef():
                global filesavename
                filesavename,  _ = QFileDialog.getSaveFileName(self, confirmlangdic['11'], './save',"Text Files (*.txt)")#,"All Files (*);;Text Files (*.txt)")
                if filesavename:
                    savewin2dic={}
                    fwid=0

                    fwid+=1
                    ttq=self.cb1selectall.isChecked()
                    savewin2dic[str(fwid)]=ttq

                    fwid+=1
                    ttq=self.cb2selectall.isChecked()
                    savewin2dic[str(fwid)]=ttq

                    for i in range(11):
                        fwid+=1
                        ttq=cb1dict[str(i+1)].isChecked()
                        savewin2dic[str(fwid)]=ttq

                    for i in range(11):
                        fwid+=1
                        ttq=cb2dict[str(i+1)].isChecked()
                        savewin2dic[str(fwid)]=ttq

                    fwid+=1
                    ttq=self.mode1exactcb.isChecked()
                    savewin2dic[str(fwid)]=ttq

                    
                    fwid+=1
                    ttq=self.lineEdit.text()     
                    savewin2dic[str(fwid)]=ttq

                    for i in range(11):
                        fwid+=1
                        ttq=bidict[str(i+1)].text()
                        savewin2dic[str(fwid)]=ttq

                    fwid+=1
                    ttq=id4sum
                    savewin2dic[str(fwid)]=ttq

                    for i in range(38):
                        savewin2dic[str(i+1)]=str(savewin2dic[str(i+1)]).strip()

                    with open(file=filesavename,mode='w',encoding='utf-8')as f:
                        for i in range(38):
                            f.write(str(savewin2dic[str(i+1)]))
                            if i==37:
                                f.write('\n')
                                f.write('____________')
                                break
                            f.write('\n')
                    global savesettingdefflag
                    savesettingdefflag+=1


            def loadmenuloaddef():
                global fileloadname
                fileloadname,  _ = QFileDialog.getOpenFileName(self, confirmlangdic['26'], './save',"txt (*.txt)")#,"All Files (*);;Text Files (*.txt)")
                if fileloadname:
                    with open(file=fileloadname,mode='r',encoding='utf-8')as wqe:
                        global gdread
                        gdread=wqe.readlines()

                        checklineid=0
                        for i in gdread:
                            checklineid+=1
                        if checklineid==39:
                            i=i.strip()
                            dqwid=0
                            for i in gdread:
                                dqwid+=1
                                if dqwid==1:
                                    if 'True'in i:
                                        self.cb1selectall.setChecked(True)
                                        continue
                                    if 'False'in i:
                                        self.cb1selectall.setChecked(False)
                                        continue
                                    else:
                                        self.cb1selectall.setChecked(False)
                                        continue
                                if dqwid==2:
                                    if 'True'in i:
                                        self.cb2selectall.setChecked(True)
                                        continue
                                    if 'False'in i:
                                        self.cb2selectall.setChecked(False)
                                        continue
                                    else:
                                        self.cb2selectall.setChecked(False)
                                        continue
                                if dqwid>=3:
                                    if dqwid<=13:
                                        if 'True'in i:
                                            cb1dict[str(dqwid-2)].setChecked(True)
                                            continue
                                        if 'False'in i:
                                            cb1dict[str(dqwid-2)].setChecked(False)
                                            continue
                                        else:
                                            cb1dict[str(dqwid-2)].setChecked(False)
                                            continue
                                if dqwid>=14:
                                    if dqwid<=24:
                                        if 'True'in i:
                                            cb2dict[str(dqwid-13)].setChecked(True)
                                            continue
                                        if 'False'in i:
                                            cb2dict[str(dqwid-13)].setChecked(False)
                                            continue
                                        else:
                                            cb2dict[str(dqwid-13)].setChecked(False)
                                            continue
                                if dqwid==25:
                                    if 'True'in i:
                                        self.mode1exactcb.setChecked(True)
                                        continue
                                    if 'False'in i:
                                        self.mode1exactcb.setChecked(False)
                                        continue
                                    else:
                                        self.mode1exactcb.setChecked(False)
                                        continue
                                if dqwid==26:
                                    self.lineEdit.setText(i)
                                if dqwid>=27:
                                    if dqwid<=37:
                                        bidict[str(dqwid-26)].setText(i)

                                if dqwid==38:
                                    try:
                                        i=str(i)
                                        global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                                        cmb1WholeSearchid=int(i[0])*1000
                                        cmb1moresearchid=int(i[1])*100
                                        cmb1morematchid=int(i[2])*10
                                        cmb1rangesearchid=int(i[3])
                                        global id4sum
                                        id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                                        
                                        global win2cmb1curruntdic
                                        global dic1text
                                        if cmb1WholeSearchid==2000:
                                            win2cmb1curruntdic['1']=dic1text
                                        if cmb1moresearchid==200:
                                            win2cmb1curruntdic['2']=confirmlangdic['5']
                                        if cmb1morematchid==20:
                                            win2cmb1curruntdic['3']=confirmlangdic['6']
                                        if cmb1rangesearchid==2:
                                            win2cmb1curruntdic['4']=confirmlangdic['7']

                                        if cmb1WholeSearchid==1000:
                                            win2cmb1curruntdic['1']='✔'+dic1text
                                        if cmb1moresearchid==100:
                                            win2cmb1curruntdic['2']='✔'+confirmlangdic['5']
                                        if cmb1morematchid==10:
                                            win2cmb1curruntdic['3']='✔'+confirmlangdic['6']
                                        if cmb1rangesearchid==1:
                                            win2cmb1curruntdic['4']='✔'+confirmlangdic['7']
                                        fffs()
                                    except:
                                        pass
                   
                                        


            def loadmenuautoloaddef():
                #print('hi')
                global autoloadmodeid
                with open(file='Autofile/autoloadmodeid.save',mode='w',encoding='utf-8')as rrre:
                    rrre.write('1')
                autoloadmodeid=1
                loadmenuchange()

            def loadmenuloadspacedef():
                #print('hi')
                global autoloadmodeid
                with open(file='Autofile/autoloadmodeid.save',mode='w',encoding='utf-8')as rrre:
                    rrre.write('3')
                autoloadmodeid=3
                loadmenuchange()

            def loadmenuloadchoosedef():
                global autoloadmodeid

                fileloadchoose,  _ = QFileDialog.getOpenFileName(self, confirmlangdic['25'], './save',"txt (*.txt)")#,"All Files (*);;Text Files (*.txt)")
                if fileloadchoose:
                    with open(file=fileloadchoose,mode='r',encoding='utf-8')as wqe:
                        global gdread
                        gdread=wqe.readlines()

                    with open(file='Autofile/autosaveload.save',mode='w',encoding='utf-8')as wqe:
                        checklineid=0
                        for i in gdread:
                            checklineid+=1
                        if checklineid==39:
                            for i in range(38):
                                wi=gdread[i].strip()
                                wqe.write(wi)
                                if i==37:
                                    wqe.write('\n')
                                    wqe.write('____________')
                                    break
                                wqe.write('\n')
                                    
                with open(file='Autofile/autoloadmodeid.save',mode='w',encoding='utf-8')as rrre:
                    rrre.write('2')
                autoloadmodeid=2
                loadmenuchange()


            loadmenusave.triggered.connect(loadmenusavedef)
            loadmenusaveas.triggered.connect(loadmenusaveasdef)
            loadmenuload.triggered.connect(loadmenuloaddef)

            loadmenuautoload.triggered.connect(loadmenuautoloaddef)
            loadmenuloadspace.triggered.connect(loadmenuloadspacedef)
            loadmenuloadchoose.triggered.connect(loadmenuloadchoosedef)







            def btresetdef():
                self.cb2selectall.setChecked(False)
                self.cb1selectall.setChecked(False)
                self.mode1exactcb.setChecked(False)
                self.lineEdit.setText('')
                for i in range(1,12):
                    cb1dict[str(i)].setChecked(False)
                    cb2dict[str(i)].setChecked(False)
                    bidict[str(i)].setText('')
            self.btreset.clicked.connect(btresetdef)


            def btcleandef():
                self.lineEdit.setText('')
                for i in range(1,12):
                    bidict[str(i)].setText('')

            self.btclean.clicked.connect(btcleandef)


            global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
            cmb1WholeSearchid=1000
            cmb1moresearchid=200
            cmb1morematchid=20
            cmb1rangesearchid=2



            #self.new_Button.setStyleSheet("QPushButton::menu-indicator{image:none;}") #去掉默认的向下箭头
            global dic1text
            dic1text='✔'+confirmlangdic['15']
            global win2cmb1curruntdic
            win2cmb1curruntdic={"1":dic1text,"2":confirmlangdic['5'],"3":confirmlangdic['6'],"4":confirmlangdic['7']}

            #print(win2cmb1curruntdic)
            self.menu=QMenu(self)


            def menuoptiondef2():
                global id4sum
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                #print(id4sum)

            def menu1def(event):
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global dic1text
                while True:
                    if cmb1WholeSearchid==2000:
                        win2cmb1curruntdic['1']=dic1text

                        win2cmb1curruntdic['2']=confirmlangdic['5']
                        cmb1moresearchid=200
                        win2cmb1curruntdic['3']=confirmlangdic['6']
                        cmb1morematchid=20
                        win2cmb1curruntdic['4']=confirmlangdic['7']
                        cmb1rangesearchid=2
                        
                        cmb1WholeSearchid=1000
                        fffs()
                        break
                    if cmb1WholeSearchid==1000:
                        if cmb1moresearchid==200:
                            if cmb1morematchid==20:
                                if cmb1rangesearchid==2:
                                    break
                        win2cmb1curruntdic['1']=confirmlangdic['15']
                        
                        cmb1WholeSearchid=2000
                        fffs()
                        break
                    else:
                        break
            global menu1,menu2,menu3,menu4
            menu1=QAction(win2cmb1curruntdic['1'], self)#whole search
            self.menu.addAction(menu1)
            menu1.triggered.connect(menu1def)


            def menu2def(event):
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global dic1text
                while True:
                    if cmb1moresearchid==200:
                        texttext='✔'+confirmlangdic['5']
                        win2cmb1curruntdic['2']=texttext
                        #win2cmb1.set(texttext)
                        
                        if cmb1WholeSearchid==1000:
                            win2cmb1curruntdic['1']=confirmlangdic['15']
                            cmb1WholeSearchid=2000
                        if cmb1morematchid==10:
                            win2cmb1curruntdic['3']=confirmlangdic['6']
                            cmb1morematchid=20


                        cmb1moresearchid=100
                        fffs()
                        break

                    if cmb1moresearchid==100:
                        win2cmb1curruntdic['2']=confirmlangdic['5']
                        #win2cmb1.set(confirmlangdic['5'])


                        cmb1moresearchid=200
                        if cmb1WholeSearchid==2000:
                            if cmb1moresearchid==200:
                                if cmb1morematchid==20:
                                    if cmb1rangesearchid==2:
                                        win2cmb1curruntdic['1']=dic1text
                                        cmb1WholeSearchid=1000
                        fffs()
                        break
                    else:
                        break
            menu2=QAction(win2cmb1curruntdic['2'], self)#whole search
            self.menu.addAction(menu2)
            menu2.triggered.connect(menu2def)

            def menu3def(event):
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global dic1text
                while True:
                    if cmb1morematchid==20:
                        texttext='✔'+confirmlangdic['6']
                        win2cmb1curruntdic['3']=texttext
                        #win2cmb1.set(texttext)

                        if cmb1WholeSearchid==1000:
                            win2cmb1curruntdic['1']=confirmlangdic['15']
                            cmb1WholeSearchid=2000
                        if cmb1moresearchid==100:
                            win2cmb1curruntdic['2']=confirmlangdic['5']
                            cmb1moresearchid=200


                        cmb1morematchid=10
                        fffs()
                        break

                    if cmb1morematchid==10:
                        win2cmb1curruntdic['3']=confirmlangdic['6']
                        #win2cmb1.set(confirmlangdic['6'])

        
                        cmb1morematchid=20

                        if cmb1WholeSearchid==2000:
                            if cmb1moresearchid==200:
                                if cmb1morematchid==20:
                                    if cmb1rangesearchid==2:
                                        win2cmb1curruntdic['1']=dic1text

                                        cmb1WholeSearchid=1000
                        fffs()
                        break
                    else:
                        break
            menu3=QAction(win2cmb1curruntdic['3'], self)#whole search
            self.menu.addAction(menu3)
            menu3.triggered.connect(menu3def)

            def menu4def(event):
                global cmb1WholeSearchid,cmb1moresearchid,cmb1morematchid,cmb1rangesearchid
                global dic1text
                while True:
                    if cmb1rangesearchid==2:
                        texttext='✔'+confirmlangdic['7']
                        win2cmb1curruntdic['4']=texttext


                        if cmb1WholeSearchid==1000:
                            win2cmb1curruntdic['1']=confirmlangdic['15']
                            cmb1WholeSearchid=2000


                        cmb1rangesearchid=1
                        fffs()
                        break

                    if cmb1rangesearchid==1:
                        win2cmb1curruntdic['4']=confirmlangdic['7']
                        #win2cmb1.set(win2cmb1curruntdic['4'])



                        cmb1rangesearchid=2

                        if cmb1WholeSearchid==2000:
                            if cmb1moresearchid==200:
                                if cmb1morematchid==20:
                                    if cmb1rangesearchid==2:
                                        win2cmb1curruntdic['1']=dic1text

                                        cmb1WholeSearchid=1000
                        fffs()             
                        break
                    else:
                        break
            menu4=QAction(win2cmb1curruntdic['4'], self)#whole search
            self.menu.addAction(menu4)
            menu4.triggered.connect(menu4def)



            self.btsearchmode.setMenu(self.menu)

            

            global menuB2,menuB3,menuB4
            menuB2=QAction(win2cmb1curruntdic['2'], self)
            menuB3=QAction(win2cmb1curruntdic['3'], self)
            menuB4=QAction(win2cmb1curruntdic['4'], self)


            self.btsearchmode2=QtWidgets.QPushButton(self)
            self.btsearchmode2.setGeometry(QtCore.QRect(260, 40, 100, 25))
            self.btsearchmode2.setText(confirmlangdic['19'])#("Search Mode")
            self.btsearchmode2.setFocusPolicy(Qt.NoFocus)
            self.menuB = QMenu(self)
            self.menuB.addAction(menuB2)
            self.menuB.addAction(menuB3)
            self.menuB.addAction(menuB4)
            self.btsearchmode2.setMenu(self.menuB)


    
            menuB2.triggered.connect(menu2def)
            menuB3.triggered.connect(menu3def)
            menuB4.triggered.connect(menu4def)


            self.btdownload = QtWidgets.QPushButton(self.frame3)
            #self.btdownload.setGeometry(QtCore.QRect(640, 395, 150, 45))
            self.btdownload.setGeometry(QtCore.QRect(160, 45, 150, 45))
            self.btdownload.setText(confirmlangdic['2'])#("Download Result")
            self.btdownload.setFocusPolicy(Qt.NoFocus)

            self.btsearch = QtWidgets.QPushButton(self.frame3)
            #self.btsearch.setGeometry(QtCore.QRect(480, 440, 160, 45))
            self.btsearch.setGeometry(QtCore.QRect(0, 90, 160, 45))
            self.btsearch.setText(confirmlangdic['1'])#search
            self.btsearch.setFocusPolicy(Qt.NoFocus)


            self.btup = QtWidgets.QPushButton(self.frame3)
            #self.btup.setGeometry(QtCore.QRect(640, 440, 50, 45))
            self.btup.setGeometry(QtCore.QRect(160, 90, 50, 45))
            self.btup.setText('↑')#("up")
            self.btup.setFocusPolicy(Qt.NoFocus)

            self.btdown = QtWidgets.QPushButton(self.frame3)
            #self.btdown.setGeometry(QtCore.QRect(690, 440, 50, 45))
            self.btdown.setGeometry(QtCore.QRect(210, 90, 50, 45))
            self.btdown.setText('↓')#("down")
            self.btdown.setFocusPolicy(Qt.NoFocus)

            self.btclose = QtWidgets.QPushButton(self.frame3)
            #self.btclose.setGeometry(QtCore.QRect(740, 440, 50, 45))
            self.btclose.setGeometry(QtCore.QRect(260, 90, 50, 45))
            self.btclose.setText('✕')#("close")
            self.btclose.setFocusPolicy(Qt.NoFocus)









            global btsearchdef,btupdef,btdowndef
            def btsearchdef():
                global mode1exactcbmode1exactcb
                starttime=time.time()
                global searchresult
                global searchresultid
                searchresult={}
                searchresultid=0
                global upid
                upid=0
                global searchresult2
                searchresult2={}

                for fjkosj in range(rangg):
                    searchresult[str(fjkosj+1)]='N'     

                for fjkosj in range(rangg):
                    searchresult2[str(fjkosj+1)]='0'

                global cb1selectdic
                global cb1selectdicid
                cb1selectdic={}
                cb1selectdicid=0
                for i in range(11):
                    if cb1dict[str(i+1)].isChecked()==True:
                        cb1selectdicid+=1
                        ##print(str(cb1list[str(i+1)].state()))
                        cb1selectdic[str(cb1selectdicid)]=str(i+1)

                global runallrs
                def runallrs():
                    def rs1():# rangesearch1
                        try:
                            global aaa1dic
                            querydic=aaa1dic
                            global rangesearchdic
                            global rangesearchdicid
                            rangesearchdic={}
                            rangesearchdicid=0
                            for i in range(1):
                                if cb1dict['1'].isChecked()==True:
                                    rangesearchdicid+=1
                                    rangesearchdic[str(rangesearchdicid)]=str(i+1)
                            for child in range(rangg):
                                #moresearchid=0
                                for i1 in range(rangesearchdicid):
                                    querydic1=int(querydic['1'])
                                    querydic2=int(querydic['2'])
                                    if querydic1>=0:
                                        if querydic2>=0:
                                            if querydic2 >= querydic1:
                                                if querydic2<=rangg:
                                                    for county in range(querydic1,querydic2+1):
                                                        val=first_dict[str(child+1)][rangesearchdic[str(i1+1)]]
                                                        if cb2dict['1'].isChecked()==True:
                                                            if str(county) == str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                                                        else:
                                                            if str(county) in str(val):
                                                                searchresult[str(child+1)]='Y'                                                                
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)                                                               
                                                                    break

                        except:
                            pass
                    if cb1dict['1'].isChecked()==True:
                        rs1()
                    def rs2():# rangesearch1
                        try:
                            global aaa2dic
                            querydic=aaa2dic
                            global rangesearchdic
                            global rangesearchdicid
                            rangesearchdic={}
                            rangesearchdicid=0
                            for i in range(1):
                                if cb1dict['2'].isChecked()==True:
                                    rangesearchdicid+=1
                                    rangesearchdic[str(rangesearchdicid)]=str(i+1)
                            for child in range(rangg):
                                #moresearchid=0
                                for i1 in range(rangesearchdicid):
                                    querydic1=int(querydic['1'])
                                    querydic2=int(querydic['2'])
                                    if querydic1>=0:
                                        if querydic2>=0:
                                            if querydic2 >= querydic1:
                                                if querydic2<=5000:
                                                    for county in range(querydic1,querydic2+1):
                                                        val=first_dict[str(child+1)][str(2)]
                                                        if cb2dict['2'].isChecked()==True:
                                                            if str(county) == str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                                                                
                                                        else:
                                                            if str(county) in str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                        except:
                            pass
                    if cb1dict['2'].isChecked()==True:
                        rs2()

                    def rs3():# 
                        try:
                            global rangesearchtimedic
                            querydic=rangesearchtimedic
                            ##print(querydic)

                            global wantcheck1year,wantcheck1month,wantcheck1day,wantcheck1hour,wantcheck1min
                            wantcheck1year=int(querydic['1'])
                            wantcheck1month=int(querydic['2'])
                            wantcheck1day=int(querydic['3'])
                            wantcheck1hour=int(querydic['4'][:2])
                            wantcheck1min=int(querydic['4'][-2:])
                            ##print(wantcheck1year,wantcheck1month,wantcheck1day,wantcheck1hour,wantcheck1min)
                            global wantcheck2year,wantcheck2month,wantcheck2day,wantcheck2hour,wantcheck2min
                            wantcheck2year=int(querydic['5'])
                            wantcheck2month=int(querydic['6'])
                            wantcheck2day=int(querydic['7'])
                            wantcheck2hour=int(querydic['8'][:2])
                            wantcheck2min=int(querydic['8'][-2:])
                            ##print(wantcheck2year,wantcheck2month,wantcheck2day,wantcheck2hour,wantcheck2min)
                            for child in range(rangg):
                                global val,valyear,valmonth,valday,valhour,valmin
                                val=first_dict[str(child+1)]['3']
                                valyear=int(val[6:10])
                                valmonth=int(val[3:5])
                                valday=int(val[:2])
                                valhour=int(val[-5:-3])
                                valmin=int(val[-2:])
                                ##print(valyear,valmonth,valday,valhour,valmin)
                                valflag=0 
                                        #  0=不是範圍內, 10=範圍內
                                        # 一開始輸入範圍(年1,月1,日1,時間1,年2,月2,日2,時間2)
                                        # 如果在年1,月1,日1,時間1,年2,月2,日2,時間2 之間, valflag 會加10
                                        # valflag>=10 就是在範圍內
                                if valyear>wantcheck1year:#如果年1+年2合共是3年或以上,中間的年的每天都在範圍內
                                    if valyear<wantcheck2year:
                                        valflag+=10
                                if wantcheck1year<wantcheck2year:#如果年2 大於 年1
                                    if valyear==wantcheck1year:# 如果年=年1
                                        if valmonth>wantcheck1month:# 當年當月後的當年每月每天都是在範圍內
                                            valflag+=10             

                                        if valmonth==wantcheck1month: #當年當月當日
                                            if valday>wantcheck1day: #當年當月當日後的當年當月每天都是在範圍內
                                                valflag+=10

                                            if valday==wantcheck1day:
                                                if valhour>wantcheck1hour:
                                                    valflag+=10
                                                if valhour==wantcheck1hour:
                                                    if valmin>=wantcheck1min:
                                                        valflag+=10

                                    if valyear==wantcheck2year:
                                        if valmonth<wantcheck2month:
                                            valflag+=10

                                        if valmonth==wantcheck2month:
                                            if valday<wantcheck2day:
                                                valflag+=10

                                            if valday==wantcheck2day:
                                                if valhour<wantcheck2hour:
                                                    valflag+=10
                                                if valhour==wantcheck2hour:
                                                    if valmin<=wantcheck2min:
                                                        valflag+=10
                                    
                                if wantcheck1year==wantcheck2year:#如果範圍年2=範圍年1
                                    if valyear==wantcheck1year:
                                        if valmonth>wantcheck1month:
                                            if valmonth<wantcheck2month:
                                                valflag+=10
                                        if wantcheck2month-wantcheck1month>=1:
                                            if valmonth==wantcheck1month:
                                                if valday>wantcheck1day:
                                                    valflag+=10

                                                if valday==wantcheck1day:
                                                    if valhour>wantcheck1hour:
                                                        valflag+=10
                                                    if valhour==wantcheck1hour:
                                                        if valmin>=wantcheck1min:
                                                            valflag+=10

                                            if valmonth==wantcheck2month:#
                                                if valday<wantcheck2day:
                                                    valflag+=10

                                                if valday==wantcheck2day:
                                                    if valhour<wantcheck2hour:
                                                        valflag+=10
                                                    if valhour==wantcheck2hour:
                                                        if valmin<=wantcheck2min:
                                                            valflag+=10

                                        if wantcheck2month-wantcheck1month==0:
                                            if valmonth==wantcheck1month:
                                                if valday>wantcheck1day:
                                                    if valday<wantcheck2day:
                                                        valflag+=10

                                                if wantcheck2day-wantcheck1day==1:
                                                    if valday==wantcheck1day:
                                                        if valhour>wantcheck1hour:
                                                            valflag+=10
                                                        if valhour==wantcheck1hour:
                                                            if valmin>=wantcheck1min:
                                                                valflag+=10

                                                    if valday==wantcheck2day: 
                                                        if valhour<wantcheck2hour:
                                                            valflag+=10
                                                        if valhour==wantcheck2hour:
                                                            if valmin<=wantcheck2min:
                                                                valflag+=10

                                                if wantcheck2day-wantcheck1day==0:
                                                    if valhour>wantcheck1hour:
                                                        if valhour<wantcheck2hour:
                                                            valflag+=10
                                                    if wantcheck2hour-wantcheck1hour>=1:
                                                        if valhour==wantcheck1hour:
                                                            if valmin>=wantcheck1min:
                                                                valflag+=10
                                                        if valhour==wantcheck2hour:
                                                            if valmin<=wantcheck2min:
                                                                valflag+=10

                                                    if wantcheck2hour-wantcheck1hour==0:
                                                        ##print(valyear,valmonth,valday,valhour,valmin)
                                                        if valhour==wantcheck1hour:
                                                            if valmin>=wantcheck1min:
                                                                if valmin<=wantcheck2min:
                                                                    valflag+=10
                                ##print(valflag)
                                if valflag>=10:
                                    searchresult[str(child+1)]='Y'
                                    if id4sum==2211:
                                        searchresult2int=int(searchresult2[str(child+1)])
                                        searchresult2int+=1
                                        searchresult2[str(child+1)]=str(searchresult2int)
                        except:
                            pass                          
                        
                    if cb1dict['3'].isChecked()==True:
                        rs3()
        
                    def rs5():# rangesearch1
                        try:
                            global aaa5dic
                            querydic=aaa5dic
                            global rangesearchdic
                            global rangesearchdicid
                            rangesearchdic={}
                            rangesearchdicid=0
                            for i in range(1):
                                if cb1dict['5'].isChecked()==True:
                                    rangesearchdicid+=1
                                    rangesearchdic[str(rangesearchdicid)]=str(i+1)
                            for child in range(rangg):
                                #moresearchid=0
                                for i1 in range(rangesearchdicid):
                                    querydic1=int(querydic['1'])
                                    querydic2=int(querydic['2'])
                                    if querydic1>=0:
                                        if querydic2>=0:
                                            if querydic2 >= querydic1:
                                                if querydic2<=5000:
                                                    for county in range(querydic1,querydic2+1):
                                                        val=first_dict[str(child+1)][str(5)]
                                                        if cb2dict['5'].isChecked()==True:
                                                            if str(county) == str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                                                                
                                                        else:
                                                            if str(county) in str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                        except:
                            pass
                    if cb1dict['5'].isChecked()==True:
                        rs5()



                    def rs8():# rangesearch1
                        try:
                            global aaa8dic
                            querydic=aaa8dic
                            global rangesearchdic
                            global rangesearchdicid
                            rangesearchdic={}
                            rangesearchdicid=0
                            for i in range(1):
                                if cb1dict['8'].isChecked()==True:
                                    rangesearchdicid+=1
                                    rangesearchdic[str(rangesearchdicid)]=str(i+1)
                            for child in range(rangg):
                                #moresearchid=0
                                for i1 in range(rangesearchdicid):
                                    querydic1=int(querydic['1'])
                                    querydic2=int(querydic['2'])
                                    if querydic1>=0:
                                        if querydic2>=0:
                                            if querydic2 >= querydic1:
                                                if querydic2<=5000:
                                                    for county in range(querydic1,querydic2+1):
                                                        val=first_dict[str(child+1)][str(8)]
                                                        if cb2dict['8'].isChecked()==True:
                                                            if str(county) == str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                                                        else:
                                                            if str(county) in str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                        except:
                            pass
                    if cb1dict['8'].isChecked()==True:
                        rs8()

                    def rs9():# rangesearch1
                        try:
                            global aaa9dic
                            querydic=aaa9dic
                            global rangesearchdic
                            global rangesearchdicid
                            rangesearchdic={}
                            rangesearchdicid=0
                            for i in range(1):
                                if cb1dict['9'].isChecked()==True:
                                    rangesearchdicid+=1
                                    rangesearchdic[str(rangesearchdicid)]=str(i+1)
                            for child in range(rangg):
                                #moresearchid=0
                                for i1 in range(rangesearchdicid):
                                    querydic1=int(querydic['1'])
                                    querydic2=int(querydic['2'])
                                    if querydic1>=0:
                                        if querydic2>=0:
                                            if querydic2 >= querydic1:
                                                if querydic2<=5000:
                                                    for county in range(querydic1,querydic2+1):
                                                        val=first_dict[str(child+1)][str(9)]
                                                        if cb2dict['9'].isChecked()==True:
                                                            if str(county) == str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                                                        else:
                                                            if str(county) in str(val):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                                    break
                        except:
                            pass
                    if cb1dict['9'].isChecked()==True:
                        rs9()



                    def rs11():# rangesearch1
                        try:
                            global aaa11dic
                            querydic=aaa11dic
                            #print(querydic)
                            for child in range(rangg):
                                querydic1=int(querydic['1'])
                                querydic2=int(querydic['2'])
                                querydic3=int(querydic['3'])

                                if querydic1>=0:
                                    if querydic2>=0:
                                        if querydic2 >= querydic1:
                                            if querydic2<=800:

                                                val=first_dict[str(child+1)]['11']

                                                mgtext={}
                                                mgtextlen=0
                                                if querydic3==1:
                                                    mgtext['1']='mg/100mL'
                                                    mgtextlen=1
                                                if querydic3==2:
                                                    mgtext['1']='mg/l'
                                                    mgtextlen=1
                                                if querydic3==3:
                                                    mgtext['1']='%BAC'
                                                    mgtext['2']='%'
                                                    mgtextlen=2
                                                if querydic3==4:
                                                    mgtext['1']='‰BAC'
                                                    mgtext['2']='‰'
                                                    mgtextlen=2

                                                for i in range(mgtextlen):
                                                    mgtext=mgtext[str(i+1)]

                                                    if mgtext in str(val):
                                                        strval=str(val)
                                                        mg100mls=strval.find(mgtext)

                                                        if float(strval[:mg100mls-1])>=float(querydic1):
                                                            if float(strval[:mg100mls-1])<=float(querydic2):
                                                                searchresult[str(child+1)]='Y'
                                                                if id4sum==2211:
                                                                    searchresult2int=int(searchresult2[str(child+1)])
                                                                    searchresult2int+=1
                                                                    searchresult2[str(child+1)]=str(searchresult2int)
                                                    
                                                        break
                        except:
                            pass
                    if cb1dict['11'].isChecked()==True:
                        rs11()

                if id4sum==1222:#allsearch
                    global lineEditlineEdit
                    query=lineEditlineEdit.text()
                    global allbox
                    allbox=11


                    for i in range(11):
                        if cb1dict[str(i+1)].isChecked()==True:
                            allbox-=1

                    #print(allbox)
                    if allbox==11 or allbox==0:
                        for child in range(rangg):
                            searchresult[str(child+1)]='N'
                        for child in range(rangg):
                            for i in range(11):
                                val=first_dict[str(child+1)][str(i+1)]
                                if mode1exactcbmode1exactcb.isChecked()==True:
                                    if str(query) == str(val):
                                        searchresultid+=1
                                        searchresult[str(child+1)]='Y'
                                        continue
                                else:
                                    if str(query) in str(val):
                                        searchresultid+=1
                                        searchresult[str(child+1)]='Y'


                    if allbox!=11 and allbox!=0:
                        for child in range(rangg):
                            searchresult[str(child+1)]='N'
                        for bi in range(11):
                            if cb1dict[str(bi+1)].isChecked()==True:
                                searchresultid=0
                                for child in range(rangg):
                                    val=first_dict[str(child+1)][str(bi+1)]
                                    if mode1exactcbmode1exactcb.isChecked()==True:
                                        if str(query) == str(val):
                                            searchresultid+=1
                                            searchresult[str(child+1)]='Y'
                                    if mode1exactcbmode1exactcb.isChecked()==False:
                                        if str(query) in str(val):
                                            searchresultid+=1
                                            searchresult[str(child+1)]='Y'
                    #print(searchresult)

                if id4sum==2122:#
                    for child in range(rangg):
                        for i1 in range(cb1selectdicid):
                            if searchresult[str(child+1)]=='Y':
                                continue

                            query=bidict[str(cb1selectdic[str(i1+1)])].text()
                            val=first_dict[str(child+1)][cb1selectdic[str(i1+1)]]
                            if cb2dict[str(cb1selectdic[str(i1+1)])].isChecked()==True:
                                if str(query) == str(val):
                                    searchresult[str(child+1)]='Y'
                            else:
                                if str(query) in str(val):
                                    searchresult[str(child+1)]='Y'
                
                if id4sum==2212:#
                    for child in range(rangg):
                        searchresult[str(child+1)]='N'
                        moresearchid=0

                        for i1 in range(cb1selectdicid):
                            
                            query=bidict[str(cb1selectdic[str(i1+1)])].text()
                            val=first_dict[str(child+1)][cb1selectdic[str(i1+1)]]
                            if cb2dict[str(cb1selectdic[str(i1+1)])].isChecked()==True:
                                if str(query) == str(val):
                                    moresearchid+=1
                                    if moresearchid==cb1selectdicid:
                                        searchresult[str(child+1)]='Y'

                                    searchresult2int=int(searchresult2[str(child+1)])
                                    searchresult2int+=1
                                    searchresult2[str(child+1)]=str(searchresult2int)
                                continue
                            
                            if str(query) in str(val):
                                moresearchid+=1
                                if moresearchid==cb1selectdicid:
                                    searchresult[str(child+1)]='Y'

                                searchresult2int=int(searchresult2[str(child+1)])
                                searchresult2int+=1
                                searchresult2[str(child+1)]=str(searchresult2int)
                
                if id4sum==2221:#
              
                    runallrs()

                if id4sum==2121:
                    for child in range(rangg):
                        for i1 in range(cb1selectdicid):


                            continueid=0
                            rangesnum=[1,2,3,5,8,9,11]
                            for yi in rangesnum:
                                if cb1selectdic[str(i1+1)]==1:
                                    continueid=1
                            if continueid==1:
                                continueid=0
                                continue



                            if searchresult[str(child+1)]=='Y':
                                continue


                            query=bidict[str(cb1selectdic[str(i1+1)])].text()
                            val=first_dict[str(child+1)][cb1selectdic[str(i1+1)]]
                            if cb2dict[str(cb1selectdic[str(i1+1)])].isChecked()==True:
                                if str(query) == str(val):
                                    searchresult[str(child+1)]='Y'
                            else:
                                if str(query) in str(val):
                                    searchresult[str(child+1)]='Y'
                    runallrs()

                if id4sum==2211:
                    moresearchid=0
                    ##print(cb1selectdicid)
                    for i1 in range(cb1selectdicid):
                        for child in range(rangg):
                            continueid=0
                            rangesnum=[1,2,3,5,8,9,11]
                            for yi in rangesnum:
                                if int(cb1selectdic[str(i1+1)])==yi:
                                    continueid=1

                            if continueid==0:
                                query=bidict[str(cb1selectdic[str(i1+1)])].text()

                                val=first_dict[str(child+1)][cb1selectdic[str(i1+1)]]

                                if cb2dict[str(cb1selectdic[str(i1+1)])].isChecked()==True:
                                    if str(query) == str(val):
                                        searchresult[str(child+1)]='Y'
                                        moresearchid+=1

                                        searchresult2int=int(searchresult2[str(child+1)])
                                        searchresult2int+=1
                                        searchresult2[str(child+1)]=str(searchresult2int)

                                else:
                                    if str(query) in str(val):
                                        searchresult[str(child+1)]='Y'
                                        moresearchid+=1

                                        searchresult2int=int(searchresult2[str(child+1)])
                                        searchresult2int+=1
                                        searchresult2[str(child+1)]=str(searchresult2int)
                            

                    runallrs()
                                
                            ##print(moresearchid)
       
                            
    
                    ##print(searchresult2)

                    for child in range(rangg):
                        searchresult[str(child+1)]='N'

                    for child in range(rangg):
                        if int(searchresult2[str(child+1)])==cb1selectdicid:
                            searchresult[str(child+1)]='Y'

                    if cb1selectdicid==0:
                        for child in range(rangg):
                            searchresult[str(child+1)]='N'

                if id4sum==2222:
                    for child in range(rangg):
                        searchresult[str(child+1)]='N'
                ##print(id4sum)
                addedtime=time.time() 
                global searchprint
                searchprint='Search completed '+str(addedtime-starttime)+' second'


                global selectdict
                selectdict={}


                #print(searchresult)



                global tableViewtableView
                #tableViewtableView.clearSelection()                
                #tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)



                '''searchydict={}
                searchydictid=0
                for i in range(rangg):
                    if searchresult[str(i+1)] == 'Y':
                        searchydictid+=1
                        searchydict[str(searchydictid)]=str(i)'''

                #print(searchydict)
 
                #for i in range(searchydictid):
                    #i=int(searchydict[str(i+1)])
                    #tableViewtableView.selectRow(i)


                #tableViewtableView.selectRow(i)


                #selectionModel = QItemSelectionModel(modelmodel)
                #tableViewtableView.setSelectionModel(selectionModel)





                #tableViewtableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
                #tableViewtableView.setSelectionMode(QAbstractItemView.NoSelection)
                #tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)
                #tableViewtableView.setSelectionBehavior(QAbstractItemView.SelectRows)

                
                
                
                
                global updowndict,updowndictid,updowndictcurrent
                updowndict={}
                updowndictid=0
                updowndictcurrent=0
                for i in range(rangg):
                    if searchresult[str(i+1)] == 'Y':
                        updowndictid+=1
                        updowndict[str(updowndictid)]=str(i+1)
                #print(updowndict)
                #print(updowndictid)
                updowndictcurrent=updowndictid
                #print(first_dict)
                #print(updowndict)
                tableViewtableView.hide()




                global resulttableViewresulttableView
                try:
                    resulttableViewresulttableView.show()
                    resulttableViewresulttableView.close()
                except:
                    pass



                win.resultmodel=QStandardItemModel(updowndictid,11)
                win.resultmodel.setHorizontalHeaderLabels(keylist)
                setiemid=0
                for i in range(updowndictid):
                    for j in range(11):
                        item=QStandardItem(first_dict[updowndict[str(i+1)]][str(j+1)])
                        win.resultmodel.setItem(setiemid,j,item)
                    setiemid+=1


                for i in range(updowndictid):
                    for j in range(11):
                        item=win.resultmodel.item(i,j)
                        item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)


                global windowscreenid
                if windowscreenid==1:
                    windowxwhat=0.7
                if windowscreenid==2:
                    windowxwhat=1
                if windowscreenid==3:
                    windowxwhat=0.5


                tablew=maxx*windowxwhat*0.9
                tableh=maxy*windowxwhat*0.9
                tablex=(maxx*windowxwhat-tablew)/2
                tabley=(maxy*windowxwhat-tableh)/2

                tablew=maxx*windowxwhat
                tableh=maxy*windowxwhat

                
                win.resulttableView=QtWidgets.QTableView(win)
                resulttableViewresulttableView=win.resulttableView
                win.resulttableView.setGeometry(QtCore.QRect(int(0), int(20), int(tablew), int(tableh-20)))
                win.resulttableView.setModel(win.resultmodel)


                twofourone=41
                if updowndictid>=0:
                    twofourone=41-7
                if updowndictid>=10:
                    twofourone=41
                if updowndictid>=100:
                    twofourone=41+7
                if updowndictid>=1000:
                    twofourone=41+7+7
                if updowndictid>=10000:
                    twofourone=41+7+7+7
                if updowndictid>=100000:
                    twofourone=41+7+7+7+7


                othercw=(tablew-twofourone-125-110-110)/8
                for i in range(11):
                    win.resulttableView.setColumnWidth(i, int(othercw))
    
                win.resulttableView.setColumnWidth(1, 125)
                win.resulttableView.setColumnWidth(2, 110)
                win.resulttableView.setColumnWidth(10, 110)

                intfirst=int(tablew-(int((tablew-twofourone-125-110-110)/8)*8+125+twofourone+110+110))

                if intfirst/11<1:
                    for i in range(intfirst):
                        if i==1:
                            win.resulttableView.setColumnWidth(1, 126)
                        if i==2:
                            win.resulttableView.setColumnWidth(2, 111)
                        if i==10:
                            win.resulttableView.setColumnWidth(10, 111)
                        if i!=1 and i!=2 and i!=10:
                            win.resulttableView.setColumnWidth(i, int(othercw+1))
                
                if (tablew-twofourone-125)/10>=110:
                    if (tablew-twofourone-125)/10<=124:
                        for i in range(11):

                            win.resulttableView.setColumnWidth(i, int((tablew-twofourone-125)/10))
                        win.resulttableView.setColumnWidth(1, 125)

                        int110to124=int(tablew-(int((tablew-twofourone-125)/10)*10+125+twofourone))
                        if int110to124/11<1:
                            for i in range(int110to124):
                                if i==1:
                                    win.resulttableView.setColumnWidth(1, 126)
                                if i!=1:
                                    win.resulttableView.setColumnWidth(i, int((tablew-twofourone-125)/10+1))

                if (tablew-twofourone)/11>=125:
                    for i in range(11):
                        win.resulttableView.setColumnWidth(i, int((tablew-twofourone)/11))


                    intmore125=int(tablew-(int((tablew-twofourone)/11)*11+twofourone))

                    if intmore125/11<1:
                        for i in range(intmore125):
                            win.resulttableView.setColumnWidth(i, int((tablew-twofourone)/11+1))



                win.resulttableView.setEditTriggers(QAbstractItemView.NoEditTriggers)


                def showContextMenu2(): 
                    win.rightclickmenu.popup(QCursor.pos())
                    win.rightclickmenu.show()

                win.resulttableView.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
                win.resulttableView.customContextMenuRequested.connect(showContextMenu2)

                win.resulttableView.show()
                #resultableshowid=1



                #tableViewtableView.selectRow(int(updowndict[str(updowndictid)])-1)


            def btupdef():
                
                global resulttableViewresulttableView

                try:
                    resulttableViewresulttableView.hide()
                    tableViewtableView.show()
                except:
                    pass

                try:
                    global updowndict,updowndictid,updowndictcurrent
                    updowndictcurrent-=1
                    if updowndictcurrent<=0:
                        updowndictcurrent=updowndictid
                    #global tableViewtableView
                    tableViewtableView.clearSelection()                
                    tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)
                    tableViewtableView.selectRow(int(updowndict[str(updowndictcurrent)])-1)
                    tableViewtableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
                    tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)
                    tableViewtableView.setSelectionBehavior(QAbstractItemView.SelectRows)
                except:
                    pass

            def btdowndef():

                global resulttableViewresulttableView

                try:
                    resulttableViewresulttableView.hide()
                    tableViewtableView.show()
                except:
                    pass


                try:
                    global updowndict,updowndictid,updowndictcurrent

                    updowndictcurrent+=1

                    if updowndictcurrent>updowndictid:
                        updowndictcurrent=1

                    #global tableViewtableView
                    tableViewtableView.clearSelection()                
                    tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)
                    tableViewtableView.selectRow(int(updowndict[str(updowndictcurrent)])-1)
                    tableViewtableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
                    tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)
                    tableViewtableView.setSelectionBehavior(QAbstractItemView.SelectRows)      
                except:
                    pass
            def btclosedef():
                self.close()
            
            def btdownloaddef():
                def ffw():
                    #ff.write(searchprint)
                    #ff.write('\n')
                    keyprint=keylist[0]+','+keylist[1]+','+keylist[2]+','+keylist[3]+','+keylist[4]+','+keylist[5]+','+keylist[6]+','+keylist[7]+','+keylist[8]+','+keylist[9]+','+keylist[10]
                    ff.write(keyprint)
                    #ff.write('\n')
                    for i in range(rangg):
                        if searchresult[str(i+1)] == 'Y':
                            lres=first_dict[str(i+1)][str(1)]+','+first_dict[str(i+1)][str(2)]+','+first_dict[str(i+1)][str(3)]+','+first_dict[str(i+1)][str(4)]+','+first_dict[str(i+1)][str(5)]\
                                +','+first_dict[str(i+1)][str(6)]+','+first_dict[str(i+1)][str(7)]+','+first_dict[str(i+1)][str(8)]+','+first_dict[str(i+1)][str(9)]\
                                    +','+first_dict[str(i+1)][str(10)]+','+first_dict[str(i+1)][str(11)]
                            ff.write('\n')
                            ff.write(str(lres))
                            


                try:
                    isCreated=os.path.exists('Result')
                    if not isCreated:
                        os.makedirs('Result')
                    e=1
                    if os.path.exists('Result\\result.txt') is True:
                        if not os.path.exists('Result\\result-%s.txt' % e):
                            with open(file='Result\\result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
                                ffw()
                        else:
                            while os.path.exists('Result\\result-%s.txt' % e):
                                e=e+1
                            with open(file='Result\\result-%s.txt' % e,mode='w',newline='',encoding='gbk') as ff:
                                ffw()
                    else:
                        with open(file='Result\\result.txt',mode='w',newline='',encoding='gbk') as ff:
                            ffw()
                except:
                    pass
            
            
            self.btsearch.clicked.connect(btsearchdef)

            self.btup.clicked.connect(btupdef)
            self.btdown.clicked.connect(btdowndef)

            self.btclose.clicked.connect(btclosedef)

            self.btdownload.clicked.connect(btdownloaddef)


            self.frame3.move(250,267)
            self.setFixedSize(565, 405)
            #self.resize(565, 405)


            self.textEdit=QTextEdit(self)
            self.textEdit.setGeometry(QtCore.QRect(300, 20, 200, 200))
            self.textEdit.setStyleSheet('border-width: 1px     ;border-style: solid;border-color: rgb(240, 240, 240)  ;  background-color: rgb(240, 240, 240);')
            self.textEdit.setReadOnly(True)
            self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus) 
            self.textEdit.setText(confirmlangdic['15'])
            self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)#重设右键
            

            self.optionlabel= QLabel(self)
            self.optionlabel.setGeometry(QtCore.QRect(255, 16, 50, 20))
            self.optionlabel.setText(confirmlangdic['16']+' : ')





            
            optionchange()

            cmb1WholeSearchid=1000
            cmb1moresearchid=200
            cmb1morematchid=20
            cmb1rangesearchid=2
            global id4sum
            id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid

            #self.textEdit.customContextMenuRequested[QtCore.QPoint].connect(self.myListWidgetContext)#绑定信号槽

            self.textEdit.setGeometry(QtCore.QRect(250, 30, 320, 200))
            self.optionlabel.setGeometry(QtCore.QRect(255, 16, 50, 20))
            global autoloadmodeid
            try:
                with open(file='Autofile/autoloadmodeid.save',mode='r',encoding='utf-8')as rrre:
                    dsaread=rrre.readlines()
                    for i in dsaread:
                        i=i.strip()
                        autoloadmodeid=int(i)
                        break
            except:
                with open(file='Autofile/autoloadmodeid.save',mode='w+',encoding='utf-8')as rrre:
                    rrre.write('1')
                    autoloadmodeid=1


            if autoloadmodeid==1 or autoloadmodeid==2:
                try:
                    with open(file='Autofile/autosaveload.save',mode='r',encoding='utf-8')as wqe:
                        global gdread
                        gdread=wqe.readlines()

                        checklineid=0
                        for i in gdread:
                            checklineid+=1
                        if checklineid==39:
                            dqwid=0
                            for i in gdread:
                                i=i.strip()
                                dqwid+=1
                                if dqwid==1:
                                    if 'True'in i:
                                        self.cb1selectall.setChecked(True)
                                        continue
                                    if 'False'in i:
                                        self.cb1selectall.setChecked(False)
                                        continue
                                    else:
                                        self.cb1selectall.setChecked(False)
                                        continue
                                if dqwid==2:
                                    if 'True'in i:
                                        self.cb2selectall.setChecked(True)
                                        continue
                                    if 'False'in i:
                                        self.cb2selectall.setChecked(False)
                                        continue
                                    else:
                                        self.cb2selectall.setChecked(False)
                                        continue
                                if dqwid>=3:
                                    if dqwid<=13:
                                        if 'True'in i:
                                            cb1dict[str(dqwid-2)].setChecked(True)
                                            continue
                                        if 'False'in i:
                                            cb1dict[str(dqwid-2)].setChecked(False)
                                            continue
                                        else:
                                            cb1dict[str(dqwid-2)].setChecked(False)
                                            continue
                                if dqwid>=14:
                                    if dqwid<=24:
                                        if 'True'in i:
                                            cb2dict[str(dqwid-13)].setChecked(True)
                                            continue
                                        if 'False'in i:
                                            cb2dict[str(dqwid-13)].setChecked(False)
                                            continue
                                        else:
                                            cb2dict[str(dqwid-13)].setChecked(False)
                                            continue
                                if dqwid==25:
                                    if 'True'in i:
                                        self.mode1exactcb.setChecked(True)
                                        continue
                                    if 'False'in i:
                                        self.mode1exactcb.setChecked(False)
                                        continue
                                    else:
                                        self.mode1exactcb.setChecked(False)
                                        continue
                                if dqwid==26:
                                    self.lineEdit.setText(i)
                                if dqwid>=27:
                                    if dqwid<=37:
                                        bidict[str(dqwid-26)].setText(i)
                                if dqwid==38:
                                    try:
                                        i=str(i)
                                    
                                        cmb1WholeSearchid=int(i[0])*1000
                                        cmb1moresearchid=int(i[1])*100
                                        cmb1morematchid=int(i[2])*10
                                        cmb1rangesearchid=int(i[3])

                                        id4sum=cmb1WholeSearchid+cmb1moresearchid+cmb1morematchid+cmb1rangesearchid
                                        
                                        
                                        if cmb1WholeSearchid==2000:
                                            win2cmb1curruntdic['1']=dic1text
                                        if cmb1moresearchid==200:
                                            win2cmb1curruntdic['2']=confirmlangdic['5']
                                        if cmb1morematchid==20:
                                            win2cmb1curruntdic['3']=confirmlangdic['6']
                                        if cmb1rangesearchid==2:
                                            win2cmb1curruntdic['4']=confirmlangdic['7']

                                        if cmb1WholeSearchid==1000:
                                            win2cmb1curruntdic['1']='✔'+dic1text
                                        if cmb1moresearchid==100:
                                            win2cmb1curruntdic['2']='✔'+confirmlangdic['5']
                                        if cmb1morematchid==10:
                                            win2cmb1curruntdic['3']='✔'+confirmlangdic['6']
                                        if cmb1rangesearchid==1:
                                            win2cmb1curruntdic['4']='✔'+confirmlangdic['7']
                                        fffs()


                                    except:
                                        pass
                except:
                    with open(file='Autofile/autoloadmodeid.save',mode='w',encoding='utf-8')as rrre:
                        rrre.write('3')
                    autoloadmodeid=3

            if autoloadmodeid==3:
                self.cb1selectall.setChecked(False)
                self.cb2selectall.setChecked(False)
                self.mode1exactcb.setChecked(False)
                self.lineEdit.setText('')
                for i in range(1,12):
                    cb1dict[str(i)].setChecked(False)
                    cb2dict[str(i)].setChecked(False)
                    bidict[str(i)].setText('')

            loadmenuchange()

            self.setWindowFlags(
            #QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowCloseButtonHint |
            QtCore.Qt.WindowStaysOnTopHint #|
            #QtCore.Qt.FramelessWindowHint #去掉标题栏
            )

        '''def mousePressEvent(self, event):
            #print(event)
            if event.buttons()== QtCore.Qt.LeftButton:                           # 左键按下
                #print("单击鼠标左键")  # 响应测试语句'''



        '''def leaveEvent(self,e): #鼠标离开label
            #print( 'leaveEvent')
            self.close()'''

        '''def changeEvent(self, e):
            if e.type() == QtCore.QEvent.WindowStateChange:
                if self.isVisible():
                    #print("窗口最小化")
                elif self.isMaximized():
                    #print("窗口最大化")
                elif self.isFullScreen():
                    #print("全屏显示")
                elif self.isActiveWindow():
                    #print("活动窗口")


            if e.type() == QtCore.QEvent.ActivationChange:
                # 当窗口被激活，也就是当用户点击了窗口在任务栏上的图标按钮
                if not self.isActiveWindow():
                    # showNor是我定义的方法，和showMini对应，相当于显示窗口
                    ##print('out')
                    self.close()'''
        #win2 close
        def closeEvent(self, event):
            global canshowwin2
            canshowwin2='NO'

            global autoloadmodeid
            if autoloadmodeid==1:
                savewin2dic={}
                fwid=0
                fwid+=1
                ttq=self.cb1selectall.isChecked()
                savewin2dic[str(fwid)]=ttq
                fwid+=1
                ttq=self.cb2selectall.isChecked()
                savewin2dic[str(fwid)]=ttq
                for i in range(11):
                    fwid+=1
                    ttq=cb1dict[str(i+1)].isChecked()
                    savewin2dic[str(fwid)]=ttq
                for i in range(11):
                    fwid+=1
                    ttq=cb2dict[str(i+1)].isChecked()
                    savewin2dic[str(fwid)]=ttq
                fwid+=1
                ttq=self.mode1exactcb.isChecked()
                savewin2dic[str(fwid)]=ttq
                fwid+=1
                ttq=self.lineEdit.text()
                ttq.strip()
                savewin2dic[str(fwid)]=ttq
                for i in range(11):
                    fwid+=1
                    ttq=bidict[str(i+1)].text()
                    ttq.strip()
                    savewin2dic[str(fwid)]=ttq

                fwid+=1
                ttq=id4sum
                savewin2dic[str(fwid)]=ttq

                for i in range(38):
                    savewin2dic[str(i+1)]=str(savewin2dic[str(i+1)]).strip()
                with open(file='Autofile/autosaveload.save',mode='w+',encoding='utf-8')as f:
                    for i in range(38):
                        f.write(str(savewin2dic[str(i+1)]))
                        if i==37:
                            f.write('\n')
                            f.write('____________')
                            break
                        f.write('\n')
            global win22showid
            win22showid=0

            try:
                resulttableViewresulttableView.close()
            except:
                pass

            global tableViewtableView
            tableViewtableView.show()
            tableViewtableView.clearSelection()                
            tableViewtableView.setSelectionMode(QAbstractItemView.ExtendedSelection)
            tableViewtableView.setSelectionBehavior(QAbstractItemView.SelectItems)

            

        #search
        global allactive
        allactive='YES'


        #win2
        def changeEvent(self, e):
            try:
                global allactive
                global searchnameid
                global canshowwin2

                if e.type() == QtCore.QEvent.ActivationChange:
                    if not self.isActiveWindow():
                        #print('win2 no active')
                        ##print(GetWindowText(GetForegroundWindow()))
                        ##print(GetForegroundWindow())
                        fw=GetForegroundWindow()

                        if GetForegroundWindow()!=reportnameid:
                            
                            self.setWindowFlags(
                            #QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint #|
                            #QtCore.Qt.WindowStaysOnTopHint #|
                            #QtCore.Qt.FramelessWindowHint #去掉标题栏
                            )

                            allactive='NO'
                            
                    if self.isActiveWindow():
                        if allactive=='NO':
                            #print('hi')
                            self.setWindowFlags(
                            #QtCore.Qt.Window |
                            QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
                            QtCore.Qt.WindowTitleHint |
                            QtCore.Qt.WindowCloseButtonHint #|
                            #QtCore.Qt.WindowStaysOnTopHint #|
                            #QtCore.Qt.FramelessWindowHint #去掉标题栏
                            )

                            if canshowwin2=='YES':
                                self.show()
    
                            allactive='YES'


                if e.type() == QtCore.QEvent.WindowStateChange:
                    if self.isMinimized():
                        win.setWindowState(Qt.WindowMinimized)
                        #print("win2 unmap")

                    #elif self.isMaximized():
                        #print("窗口最大化")

                    elif self.isActiveWindow():
                        win.setWindowState(Qt.WindowNoState)
                        self.activateWindow()
                        #print("活动窗口")
            except:
                pass


        def keyPressEvent(self, event):

        
            """Close application from escape key.

            results in QMessageBox dialog from closeEvent, good but how/why?
            """
            if event.key() == QtCore.Qt.Key_Escape:
                self.close()
            if event.key() == QtCore.Qt.Key_Return:
                btsearchdef()
            if event.key() == QtCore.Qt.Key_Enter:
                btsearchdef()
            if event.key() == QtCore.Qt.Key_Up:
                btupdef()
            if event.key() == QtCore.Qt.Key_Down:
                btdowndef()
    def a41():
        
        global win2
        try:
            win2.close()
        except:
            pass
        #app = QApplication([])
        win2=SearchWindow()
        addthendeletefixloaddelay = QTimeEdit(win2)
        sip.delete(addthendeletefixloaddelay)
        win2.show()
        global win22showid
        win22showid=1

        #print(GetWindowText(GetForegroundWindow()))
        #print(GetForegroundWindow())
        global searchnameid
        searchnameid=GetForegroundWindow()

        #app.exec_()

    def a41close():
        win2.close()


global passcorrect
passcorrect=0

class win1class(QWidget):
    def __init__(self,parent=None):
        super(win1class, self).__init__(parent)
        self.setWindowTitle(confirmlang[0])
        self.setWindowIcon(QtGui.QIcon("runico.ico"))
        self.bar=QMenuBar(self)
        self.bar.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.bar.resize(self.width(), self.bar.height())
        

        global files
        files=self.bar.addMenu(confirmlang[10])#file
        files.addAction(confirmlang[3]).setShortcut('Ctrl+O')#open

        #files=self.bar.addMenu(confirmlangdicnum['29'])#file
        #files.addAction(confirmlangdic['29'])#.setShortcut('Ctrl+O')#open

        #menuofsearch=QAction(confirmlang[4],self)
        #menuofsearch.setShortcut('Ctrl+F')
        #self.files.addAction(menuofsearch)

        menuofclean=QAction(confirmlang[8],self)
        menuofclean.setShortcut('Esc')
        files.addAction(menuofclean)

        #edit=files.addMenu('Edit')
        #edit.addAction('Copy')
        #edit.addAction('Paste')

        menuofquit=QAction(confirmlang[9],self)
        menuofquit.setShortcut('Alt+F4')
        files.addAction(menuofquit)


        files.triggered[QAction].connect(self.processtrigger)

        global windowscreenid
        windowscreenid=1
        class screenmenuclass():  
            global passcorrect
            def s1():
                global windowscreenid
                global tableshowid,win22showid
                global tableView
                if windowscreenid!=1:
                    try:
                        self.tableView.close()
                    except:
                        pass


                    self.hide()
                    self.showNormal()
                    self.hide()
                    aaa3x=maxx*0.7
                    aaa3y=maxy*0.7
                    aaa3px=(maxx-aaa3x)/2
                    aaa3py=(maxy-aaa3y)/2
                    self.resize(int(aaa3x), int(aaa3y))
                    self.setFixedSize(int(aaa3x), int(aaa3y))
                    #self.setWindowState(Qt.WindowNoState)
                    self.show()
                    windowscreenid=1
                    with open(file='Autofile/screenmode.save',mode='w',encoding='utf-8')as rrre:
                        rrre.write('1')

                    try:
                        global importedid
                        if importedid==1:
                            try:
                                if passcorrect==1:
                                    try:
                                        win2.close()
                                    except:
                                        pass
                                    opentreetable(0.7)
                                    #win2.show()
                            except:
                                pass
                    except:
                        pass
                    


            def s2():
                global windowscreenid
                global tableshowid,win22showid
                global tableView
                if windowscreenid!=2:
                    
                    #self.setWindowState(Qt.WindowFullScreen)
                    try:
                        self.tableView.close()
                    except:
                        pass

                    self.showFullScreen()
                    windowscreenid=2
                    with open(file='Autofile/screenmode.save',mode='w',encoding='utf-8')as rrre:
                        rrre.write('2')

                    try:
                        global importedid
                        if importedid==1:
                            if passcorrect==1:
                                try:
                                    win2.close()
                                except:
                                    pass
                                opentreetable(1)
                                #win2.show()
  
                    except:
                        pass

            def s3():
                global windowscreenid
                global tableshowid,win22showid
                global tableView
                if windowscreenid!=3:
                    try:
                        self.tableView.close()
                    except:
                        pass


                    self.hide()
                    self.showNormal()
                    self.hide()
                    aaa3x=maxx*0.5
                    aaa3y=maxy*0.5
                    aaa3px=(maxx-aaa3x)/2
                    aaa3py=(maxy-aaa3y)/2
                    self.resize(int(aaa3x), int(aaa3y))
                    self.setFixedSize(int(aaa3x), int(aaa3y))
                    #self.setWindowState(Qt.WindowNoState)
                    self.show()
                    windowscreenid=3
                    with open(file='Autofile/screenmode.save',mode='w',encoding='utf-8')as rrre:
                        rrre.write('3')

                    try:
                        global importedid
                        if importedid==1:
                            try:
                                if passcorrect==1:
                                    try:
                                        win2.close()
                                    except:
                                        pass
                                    opentreetable(0.5)
                                    #win2.show()
                            except:
                                pass
                    except:
                        pass


        screenMenu=self.bar.addMenu(confirmlangdic['20'])
        screenMenu.addAction(confirmlangdic['21']+' 50%').triggered.connect(screenmenuclass.s3)
        screenMenu.addAction(confirmlangdic['21']+' 70%').triggered.connect(screenmenuclass.s1)
        screenMenu.addAction(confirmlangdic['22']).triggered.connect(screenmenuclass.s2)


        class langmenuclass():
            def l1():
                with open(file='Setting\\lang.txt',mode='r',encoding='utf-8')as lff:
                    ook= lff.readlines()
                with open(file='Setting\\lang.txt',mode='w',encoding='utf-8')as lff:
                    tgrhid=0
                    for i in ook:
                        tgrhid+=1
                        if tgrhid==1:
                            lff.write('1\n')
                            continue
                        lff.write(ook)
                startlang()
                wqew=sys.executable
                os.execl(wqew, wqew, *sys.argv)
            def l2():
                with open(file='Setting\\lang.txt',mode='r',encoding='utf-8')as lff:
                    ook= lff.readlines()
                with open(file='Setting\\lang.txt',mode='w',encoding='utf-8')as lff:
                    tgrhid=0
                    for i in ook:
                        tgrhid+=1
                        if tgrhid==1:
                            lff.write('2\n')
                            continue
                        lff.write(ook)
                startlang()

                wqew=sys.executable
                os.execl(wqew, wqew, *sys.argv)                
            def l3():
                with open(file='Setting\\lang.txt',mode='r',encoding='utf-8')as lff:
                    ook= lff.readlines()
                with open(file='Setting\\lang.txt',mode='w',encoding='utf-8')as lff:
                    tgrhid=0
                    for i in ook:
                        tgrhid+=1
                        if tgrhid==1:
                            lff.write('3\n')
                            continue
                        lff.write(ook)
                startlang()
                wqew=sys.executable
                os.execl(wqew, wqew, *sys.argv)              
            def l4():
                with open(file='Setting\\lang.txt',mode='r',encoding='utf-8')as lff:
                    ook= lff.readlines()
                with open(file='Setting\\lang.txt',mode='w',encoding='utf-8')as lff:
                    tgrhid=0
                    for i in ook:
                        tgrhid+=1
                        if tgrhid==1:
                            lff.write('4\n')
                            continue
                        lff.write(ook)
                startlang()

                wqew=sys.executable
                os.execl(wqew, wqew, *sys.argv)


        langMenu=self.bar.addMenu(confirmlang[11])#language
        langMenu.addAction('简体中文').triggered.connect(langmenuclass.l1)#open
        langMenu.addAction('繁體中文').triggered.connect(langmenuclass.l2)#open
        langMenu.addAction('English').triggered.connect(langmenuclass.l3)#open
        langMenu.addAction('Español').triggered.connect(langmenuclass.l4)#open


        screenxwhat=0.7
        try:
            with open(file='Autofile/screenmode.save',mode='r',encoding='utf-8')as rrre:
                rrrrr=rrre.readlines()
            windowscreenid=int(rrrrr[0])
            if windowscreenid==1:
                screenxwhat=0.7
            if windowscreenid==3: 
                screenxwhat=0.5
        except:
            screenxwhat=0.7
        

        aaa3x=maxx*screenxwhat
        aaa3y=maxy*screenxwhat
        aaa3px=(maxx-aaa3x)/2
        aaa3py=(maxy-aaa3y)/2
        self.setGeometry(int(aaa3px),int(aaa3py),int(aaa3x),int(aaa3y))
        self.setFixedSize(int(aaa3x), int(aaa3y))
        global first_dict
        first_dict=dict()

        if windowscreenid==2:
            self.showFullScreen()


        global rightclickmenurightclickmenu
        global rightclickmenuopen,rightclickmenusearch,rightclickmenuclean,rightclickmenuquit
        #global rightclickmenuchangedatcsv
        self.rightclickmenu=QMenu(self)
        rightclickmenurightclickmenu=self.rightclickmenu
        rightclickmenurightclickmenu=self.rightclickmenu

        rightclickmenuopen=QAction(confirmlang[3], self)#open
        #rightclickmenusearch=QAction(confirmlang[4], self)#"搜寻"
        #rightclickmenuchangedatcsv=QAction(confirmlangdic['29'], self)  #"轉檔"
        rightclickmenuclean=QAction(confirmlang[8], self)  #"清空"
        rightclickmenuquit=QAction(confirmlang[9], self)  #"關閉"
        self.rightclickmenu.addAction(rightclickmenuopen)
        #self.rightclickmenu.addAction(rightclickmenuchangedatcsv)
        #self.rightclickmenu.addAction(rightclickmenusearch)
        self.rightclickmenu.addAction(rightclickmenuclean)    
        self.rightclickmenu.addAction(rightclickmenuquit)


        self.rightclickmenu.triggered[QAction].connect(self.processtrigger)


        def showContextMenu1():  # 创建右键菜单  # 1
            self.rightclickmenu.popup(QCursor.pos()) 
            self.rightclickmenu.show()

        self.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
        self.customContextMenuRequested.connect(showContextMenu1)


    global tabledict
    tabledict={}




    def processtrigger(self,q):
        global rightclickmenuopen,rightclickmenusearch,rightclickmenuclean,rightclickmenuquit
        global win2
        global passcorrect
        global tableshowid,win22showid
        global tableView
        #global tableViewtableView

        global passcorrect
        global canshowwin2
        global resulttableViewresulttableView
        ##print(q.text()+'is triggeres')

        while True:
            if q.text()==confirmlang[3]:#open
                
                
                passcorrect=0
                try:
                    canshowwin2='NO'
                    win2.close()
                except:
                    pass

                try:
                    resulttableViewresulttableView.show()
                except:
                    pass
                try:
                    resulttableViewresulttableView.close()
                except:
                    pass
                try:
                    self.tableView.show()
                except:
                    pass
                try:
                    self.tableView.close()
                except:
                    pass

                try:
                    self.rightclickmenu.removeAction(rightclickmenusearch)
                except:
                    pass
                if win22showid==1:
                    #from a4 import a41close
                    a4.a41close()
                    win22showid=0
                files.clear()
                
                files.addAction(confirmlang[3]).setShortcut('Ctrl+O')#open
                #files.addAction(confirmlangdic['29'])
                files.addAction(confirmlang[8]).setShortcut('Esc')#open
                files.addAction(confirmlang[9]).setShortcut('Alt+F4')#open'''


                global opencsvfile
                import win32api
                from pathlib import Path  

                try:
                    isCreated=os.path.exists('csvdat')
                    if not isCreated:
                        os.makedirs('csvdat')
                except:
                    pass

                import os
                while True:
                    try:
                        pathc=os.getcwd()
                    
                        import string
                        import os
                        
                        disk_list = []
                        for c in string.ascii_uppercase:
                            disk = c+':'
                            if os.path.isdir(disk):
                                disk_list.append(disk)

                        for i in disk_list:
                            i=i+'\\'+'apps\\fit240\\TestRecord.dat'
                            #print(i)
                            try:
                                with open(file=i,mode='r') as y:
                                    #y.readline()
                                    #print(i)
                                    k=i
                                    break
                            except:
                                pass
                        try:
                            print(k)
                        except:
                            import win32api,win32con
 


                            win32api.MessageBox(0, confirmlangdic['41'],confirmlangdic['42'],win32con.MB_ICONASTERISK)
                            break

                        filedatname=' '+k
                        filename=' '+pathc+'\\'+'csvdat\\'+'TestRecord.csv'

                        path=pathc+'\\recode2csv.exe'+filedatname+filename
                        print(path)
                        with open(file='recode2csv.bat',mode='w') as batt:
                            batt.write(path)
                            #batt.write('\n')
                            #batt.write('pause')
                        import subprocess
                        subprocess.Popen('recode2csv.bat', close_fds=True,shell=True)

                        
                        csvfilename='TestRecord.csv'
                        opencsvfile=pathc+'\\'+csvfilename
                        opencsvfile=csvfilename

                        breakid=0
                        
                        starttt=time.time()

                        while True:
                            if time.time()-starttt>10:
                                breakid=1
                                break
                            if os.path.exists('csvdat\\'+csvfilename) is True:
                                #print('sdfdf')
                                break
                        time.sleep(1)

                        if breakid==1:
                            break

                        opencsvfile='csvdat/TestRecord.csv'
                        #print(opencsvfile)
                        with open(file=opencsvfile,newline='',mode='r') as f:
                            #global key
                            global first_dict
                            global widthcount
                            global importedid
                            global your_list
                            global rangg
                            global conpletepass

                            '''import threading
                            class MyThread(threading.Thread):

                                def __init__(self, bat_path, **kwargs):

                                    threading.Thread.__init__(self, **kwargs)

                                    self.bat_path = bat_path

                                    

                                def run(self):

                                    win32api.ShellExecute(0, None, self.bat_path, None, "c:", True)
                            t = MyThread("recode2csv.bat")
                            t.start()
                            time.sleep(0.5)'''
                            #break
                            #if opencsvfile[-3:]=='csv':
                            global conpletepass
                            #global importedid
                            importedid=0
                            #global widthcount
                            widthcount=0
                            #global first_dict
                            reader=csv.reader(f)
                            #global your_list
                            your_list=list(reader)
                            second_dict={}
                            #global key
                            #key=your_list.pop(0)
                    
                            #global rangg
                            rangg=(len(your_list))
                            for i in range(len(your_list)):
                                second_dict={}
                                #for y in range(len(key)):
                                for y in range(11):
                                    second_dict[str(y+1)]=your_list[i][y]
                                first_dict[str(i+1)]=second_dict

                            your_list=[]
                            ##print(key)
                            ##print(first_dict)
                            importedid=1

                            #print('hihi')
                            a2.a21()

                            global opentreetable
                            def opentreetable(windowxwhat):
                                try:
                                    self.tableView.close()
                                except:
                                    pass
                                global modelmodel
                                self.model=QStandardItemModel(rangg,11)
                                modelmodel=self.model
                                global keylist
                                keylist=[confirmlangdic['30'],confirmlangdic['31'],confirmlangdic['32'],confirmlangdic['33'],confirmlangdic['34'],confirmlangdic['35'],confirmlangdic['36'],confirmlangdic['37'],confirmlangdic['38'],confirmlangdic['39'],confirmlangdic['40']]
                                self.model.setHorizontalHeaderLabels(keylist)
                                setiemid=0
                                for i in range(rangg):
                                    for j in range(11):
                                        item=QStandardItem(first_dict[str(i+1)][str(j+1)])
                                        self.model.setItem(setiemid,j,item)
                                    setiemid+=1


                                for i in range(rangg):
                                    for j in range(11):
                                        item=self.model.item(i,j)
                                        item.setTextAlignment(Qt.AlignRight|Qt.AlignVCenter)


                                tablew=maxx*windowxwhat*0.9
                                tableh=maxy*windowxwhat*0.9
                                tablex=(maxx*windowxwhat-tablew)/2
                                tabley=(maxy*windowxwhat-tableh)/2


                                tablew=maxx*windowxwhat
                                tableh=maxy*windowxwhat
                                ##print(tablew)

                                global tableViewtableView
                                self.tableView=QtWidgets.QTableView(self)
                                tableViewtableView=self.tableView
                                self.tableView.setGeometry(QtCore.QRect(int(0), int(20), int(tablew), int(tableh-20)))
                                self.tableView.setModel(self.model)


                                twofourone=41
                                if rangg>=0:
                                    twofourone=41-7
                                if rangg>=10:
                                    twofourone=41
                                if rangg>=100:
                                    twofourone=41+7
                                if rangg>=1000:
                                    twofourone=41+7+7
                                if rangg>=10000:
                                    twofourone=41+7+7+7
                                if rangg>=100000:
                                    twofourone=41+7+7+7+7


                                othercw=(tablew-twofourone-125-110-110)/8
                                for i in range(11):
                                    self.tableView.setColumnWidth(i, int(othercw))
                    
                                self.tableView.setColumnWidth(1, 125)
                                self.tableView.setColumnWidth(2, 110)
                                self.tableView.setColumnWidth(10, 110)

                                

                                intfirst=int(tablew-(int((tablew-twofourone-125-110-110)/8)*8+125+twofourone+110+110))
                                ##print(intfirst)
                                if intfirst/11<1:
                                    for i in range(intfirst):
                                        #print(i)
                                        if i==1:
                                            self.tableView.setColumnWidth(1, 126)
                                        if i==2:
                                            self.tableView.setColumnWidth(2, 111)
                                        if i==10:
                                            self.tableView.setColumnWidth(10, 111)
                                        if i!=1 and i!=2 and i!=10:
                                            self.tableView.setColumnWidth(i, int(othercw+1))
                                
                                
                                #39-twofourone
                                if (tablew-twofourone-125)/10>=110:
                                    if (tablew-twofourone-125)/10<=124:
                                        for i in range(11):
                                            #self.tableView.setColumnWidth(i, 122)
                                        #self.tableView.setColumnWidth(1, tablew/11-39)


                                            self.tableView.setColumnWidth(i, int((tablew-twofourone-125)/10))
                                        self.tableView.setColumnWidth(1, 125)



                                        int110to124=int(tablew-(int((tablew-twofourone-125)/10)*10+125+twofourone))
                                        ##print(int110to124)
                                        if int110to124/11<1:
                                            for i in range(int110to124):
                                                if i==1:
                                                    self.tableView.setColumnWidth(1, 126)
                                                if i!=1:
                                                    self.tableView.setColumnWidth(i, int((tablew-twofourone-125)/10+1))




                    

                                if (tablew-twofourone)/11>=125:
                                    for i in range(11):
                                        self.tableView.setColumnWidth(i, int((tablew-twofourone)/11))
                                    #self.tableView.setColumnWidth(1, int((tablew-twofourone)/11))

                                    intmore125=int(tablew-(int((tablew-twofourone)/11)*11+twofourone))
                                    ##print(intmore125)
                                    if intmore125/11<1:
                                        for i in range(intmore125):
                                            self.tableView.setColumnWidth(i, int((tablew-twofourone)/11+1))

                                #self.tableView.setStyleSheet('border-style: solid;border-color: rgb(240, 240, 240) ;')

                                self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

                                def showContextMenu2():  # 创建右键菜单
                                    #self.tableView.contextMenu = QMenu(self)
                                    #self.actionA = self.tableView.contextMenu.addAction(u'动作a')
                                    # self.actionA = self.tableView.contextMenu.exec_(self.mapToGlobal(pos))  # 1
                                    self.rightclickmenu.popup(QCursor.pos())  # 2菜单显示的位置
                                    #self.actionA.triggered.connect(self.actionHandler)
                                    # self.view.contextMenu.move(self.pos())  # 3
                                    self.rightclickmenu.show()

                                #def actionHandler(self):
                                    #print ("成功")

                                self.tableView.setContextMenuPolicy(Qt.CustomContextMenu)  # 右键菜单，如果不设为CustomContextMenu,无法使用customContextMenuRequested
                                self.tableView.customContextMenuRequested.connect(showContextMenu2)

                                #tableViewtableView=self.tableView

                                #self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)#设置只有行选中
        
                                self.tableView.show()
                                tableshowid=1

                            break
                            '''global windowscreenid
                            if windowscreenid==1:
                                opentreetable(0.7)
                            if windowscreenid==2:
                                opentreetable(1)
                            if windowscreenid==3:
                                opentreetable(0.5)


                            self.rightclickmenu.removeAction(rightclickmenuopen)
                            try:
                                self.rightclickmenu.removeAction(rightclickmenusearch)
                            except:
                                pass
                            self.rightclickmenu.removeAction(rightclickmenuclean)
                            self.rightclickmenu.removeAction(rightclickmenuquit)

                            rightclickmenuopen=QAction(confirmlang[3], self)#open
                            rightclickmenusearch=QAction(confirmlang[4], self)#"搜寻"
                            rightclickmenuclean=QAction(confirmlang[8], self)  #"清空"
                            rightclickmenuquit=QAction(confirmlang[9], self)  #"關閉"
                            self.rightclickmenu.addAction(rightclickmenuopen)
                            self.rightclickmenu.addAction(rightclickmenusearch)
                            self.rightclickmenu.addAction(rightclickmenuclean)    
                            self.rightclickmenu.addAction(rightclickmenuquit)


                            files.clear()
                            files.addAction(confirmlang[3])#open
                            files.addAction(confirmlang[4]).setShortcut('Ctrl+F')
                            files.addAction(confirmlang[8])#open
                            files.addAction(confirmlang[9])#open'''
                        
                            break


                    except:
                        break
            
                break

            if q.text()==confirmlang[4]:#serach
                ##print(key)
                #with open(file='Autofile/key.save',mode='w',encoding='utf-8')as lff:
                    #lff.write(str(key))

                #from a4 import win22showid
                if win22showid==0:
                    #from a4 import a41
                    a4.a41()
                    global tableViewtableView
                    #tableViewtableView.clearSelection()                
                    #tableViewtableView.setSelectionMode(QAbstractItemView.MultiSelection)
                    #tableViewtableView.setSelectionBehavior(QAbstractItemView.SelectRows)
                    #from a4 import win22showid

                canshowwin2='YES'
                break

            if q.text()==confirmlang[8]:#clean


                passcorrect=0
                try:
                    canshowwin2='NO'
                    win2.close()
                except:
                    pass


                try:
                    resulttableViewresulttableView.show()
                except:
                    pass
                try:
                    resulttableViewresulttableView.close()
                except:
                    pass
                try:
                    self.tableView.show()
                except:
                    pass
                try:
                    self.tableView.close()
                except:
                    pass







                try:
                    self.rightclickmenu.removeAction(rightclickmenusearch)

                except:
                    pass
                passcorrect=0

                files.clear()
                files.addAction(confirmlang[3]).setShortcut('Ctrl+O')#open
                #files.addAction(confirmlangdic['29'])
                files.addAction(confirmlang[8]).setShortcut('Esc')#open
                files.addAction(confirmlang[9]).setShortcut('Alt+F4')#open'''




                if win22showid==1:
                    #from a4 import a41close
                    a4.a41close()
                    win22showid=0
                

                importedid=0

                break

            if q.text()==confirmlang[9]:
                sys.exit()
            else:
                break
    
    
    def win1classpass():
        global passcorrect
        passcorrect=0
        global windowtext1
        #print(windowtext1)
        #print('win1hi')    
    
        if windowtext1=='0000':
            
            passcorrect=1
            global winpass
            winpass.close()


            global windowscreenid
            if windowscreenid==1:
                opentreetable(0.7)
            if windowscreenid==2:
                opentreetable(1)
            if windowscreenid==3:
                opentreetable(0.5)


            global rightclickmenuopen,rightclickmenusearch,rightclickmenuclean,rightclickmenuquit
            #global rightclickmenuchangedatcsv
            global rightclickmenurightclickmenu
            rightclickmenurightclickmenu.removeAction(rightclickmenuopen)
            '''try:
                rightclickmenurightclickmenu.removeAction(rightclickmenusearch)
            except:
                pass'''
            rightclickmenurightclickmenu.removeAction(rightclickmenuclean)
            rightclickmenurightclickmenu.removeAction(rightclickmenuquit)

            rightclickmenuopen=QAction(confirmlang[3], rightclickmenurightclickmenu)#open
            rightclickmenusearch=QAction(confirmlang[4], rightclickmenurightclickmenu)#"搜寻"
            rightclickmenuclean=QAction(confirmlang[8], rightclickmenurightclickmenu)  #"清空"
            rightclickmenuquit=QAction(confirmlang[9], rightclickmenurightclickmenu)  #"關閉"
            rightclickmenurightclickmenu.addAction(rightclickmenuopen)
            #rightclickmenurightclickmenu.addAction(rightclickmenuchangedatcsv)
            rightclickmenurightclickmenu.addAction(rightclickmenusearch)
            rightclickmenurightclickmenu.addAction(rightclickmenuclean)    
            rightclickmenurightclickmenu.addAction(rightclickmenuquit)


            files.clear()
            files.addAction(confirmlang[3]).setShortcut('Ctrl+O')#open
            #files.addAction(confirmlangdic['29'])
            files.addAction(confirmlang[4]).setShortcut('Ctrl+F')
            files.addAction(confirmlang[8]).setShortcut('Esc')#open
            files.addAction(confirmlang[9]).setShortcut('Alt+F4')#open'''


    #class winsearch():
        #def s():
            #print('hi')
    def closeEvent(self, event):
        sys.exit()

    global canshowwin2
    canshowwin2='YES'


    def resizeEvent(self, event):
        # calling the base class resizeEvent function is not usually
        # required, but it is for certain widgets (especially item views 
        # or scroll areas), so just call it anyway, just to be sure, as
        # it's a good habit to do that for most widget classes
        super(win1class, self).resizeEvent(event)
        # now that we have a direct reference to the menubar widget, we are
        # also able to resize it, allowing all actions to be shown (as long
        # as they are within the provided size
        self.bar.resize(self.width(), self.bar.height())


    #win
    def changeEvent(self, e):
        try:
            global allactive
            global searchnameid
            global win2
            global canshowwin2

            if e.type() == QtCore.QEvent.ActivationChange:
                
                if not self.isActiveWindow():
                    ##print('win no ac')
                    ##print(GetWindowText(GetForegroundWindow()))
                    ##print(GetForegroundWindow())

    
                    if GetForegroundWindow()!=searchnameid:
                        win2.setWindowFlags(
                        #QtCore.Qt.Window |
                        QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
                        QtCore.Qt.WindowTitleHint |
                        QtCore.Qt.WindowCloseButtonHint #|
                        #QtCore.Qt.WindowStaysOnTopHint #|
                        #QtCore.Qt.FramelessWindowHint #去掉标题栏
                        )

                        allactive='NO'

            
                if self.isActiveWindow():
                    if allactive=='NO':
                        #print('hi')
                        win2.setWindowFlags(
                        #QtCore.Qt.Window |
                        QtCore.Qt.CustomizeWindowHint | # 有透明边框 去掉标题栏
                        QtCore.Qt.WindowTitleHint |
                        QtCore.Qt.WindowCloseButtonHint |
                        QtCore.Qt.WindowStaysOnTopHint #|
                        #QtCore.Qt.FramelessWindowHint #去掉标题栏
                        )

                        if canshowwin2=='YES':
                            win2.show()
                            self.activateWindow()



                        allactive='YES'


            
            #if e.type() == QtCore.QEvent.ActivationChange:
            if e.type() == QtCore.QEvent.WindowStateChange:
                if self.isMinimized():
                    win2.setWindowState(Qt.WindowMinimized)
                    #print("窗口最小化")


                #elif self.isMaximized():
                    #print("窗口最大化")
                #elif self.isFullScreen():
                    #print("全屏显示")
                elif self.isActiveWindow():
                    win2.setWindowState(Qt.WindowNoState)
                    self.activateWindow()
                    #print("活动窗口")
        except:
            pass

if __name__ == '__main__':


    isCreated=os.path.exists('Autofile')
    if not isCreated:
        os.makedirs('Autofile')

    isCreated=os.path.exists('Save')
    if not isCreated:
        os.makedirs('Save')

    isCreated=os.path.exists('Result')
    if not isCreated:
        os.makedirs('Result')


    isCreated=os.path.exists('Setting')
    if not isCreated:
        os.makedirs('Setting')
        with open(file='Setting\\lang.txt',mode='w',encoding='utf-8')as lff:
            lff.write('1\n')




    app=QApplication(sys.argv)
    global win
    demo=win1class()
    win=demo
    demo.show()
   

    #print(GetWindowText(GetForegroundWindow()))
    #print(GetForegroundWindow())
    global reportnameid
    reportnameid=GetForegroundWindow()
    sys.exit(app.exec_())