#!/usr/bin/env python3

import os 
import sys 
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *








class ha(QMainWindow):
    def __init__(self):
      super().__init__()
      self.setWindowTitle('levanditor')
      self.setWindowIcon(QIcon('Le.png'))
      self.statusBar().showMessage('Ready')
      self.setGeometry(500,500,420,420)
      self.setStyleSheet('background-color:white; ')
      self.editor = QTextEdit()
      self.editor.setStyleSheet('background-color:white;')
      self.setCentralWidget(self.editor)
      font = QFont("Monospace",10)
      self.editor.setFont(font)
      menubar = self.menuBar()
      menubar.setStyleSheet('background-color: grey;')
      filemenu = menubar.addMenu('&File')
      opena = QAction('Open File', self)
      opena.setStatusTip('Open a file.')
      opena.triggered.connect(self.file_open)
      filemenu.addAction(opena)
      save = QAction('Save',self)
      save.setStatusTip('Save your progress')
      save.setShortcut('Ctrl+S')
      save.triggered.connect(self.file_save)
      filemenu.addAction(save)
      saveas = QAction('Save as',self)
      saveas.setStatusTip('Save')
      saveas.triggered.connect(self.file_saveas)
      filemenu.addAction(saveas)
      
      exitAct = QAction('&Exit', self)
      exitAct.setShortcut('Ctrl+Q')
      exitAct.setStatusTip('close the application')
      exitAct.triggered.connect(qApp.quit)
      impMenu = menubar.addMenu('Exit')
      impMenu.addAction(exitAct)
      impMen = menubar.addMenu('View')
      act = QAction('StatusBar', self, checkable=True)
      act.setStatusTip('view status bar')
      act.setChecked(True)
      act.triggered.connect(self.toggleMenu)
      impMen.addAction(act)
      menw = menubar.addMenu('Edit')
      undoact = QAction('undo',self)
      undoact.setShortcut('Ctrl+U')
      undoact.setStatusTip('undo action')
      undoact.triggered.connect(self.editor.undo)
      menw.addAction(undoact)
      redoact = QAction('redo',self)
      redoact.setStatusTip('redo action')
      redoact.setShortcut('Ctrl+L')
      redoact.triggered.connect(self.editor.redo)
      menw.addAction(redoact)
      fontbtn = QAction('Font',self)
      fontbtn.setStatusTip('Select Font')
      fontbtn.triggered.connect(self.set_font)
      impMen.addAction(fontbtn)
      
      mode = QAction('Dark Mode',self, checkable=True)
      mode.setStatusTip('Dark Mode')
      mode.setChecked(False)
      mode.triggered.connect(self.dark_mode)
      impMen.addAction(mode)
      
      About = menubar.addMenu('About')
      abo = QAction('About',self)
      abo.setStatusTip('About')
      abo.triggered.connect(self.About_dlg)
      About.addAction(abo)

  

  
    def toggleMenu(self,state):
      if state:
        self.statusBar().setVisible(True)
      else:
        self.statusBar().setVisible(False)
      

    
    def closeEvent(self, event):
     reply = QMessageBox.question(self, 'Quit',  'Are You Sure?',              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
     if reply == QMessageBox.Yes:
       event.accept()
     else:
       event.ignore()
  
    def dialog_critical(self,s):
      dlg = QMessageBox(self)
      dlg.setText(s)
      dlg.setIcon(QMessageBox.Critical)
      dlg.show()

    def update_title(self):
       self.setWindowTitle("%s - levanditor" %(os.path.basename(self.path)         if self.path else "Untitled"))
      
  
    def file_save(self):
      path, _ = QFileDialog.getSaveFileName(self, "Save File","","Text documents (*.txt);All files(*.*)")
      if not path:
        return

    def set_font(self):
      font , ok = QFontDialog.getFont(self.editor.font(),self)
      if ok:
        self.editor.setFont(font)
        print("Display Fonts", font)
        
    def file_saveas(self):
      path, _ = QFileDialog.getSaveFileName(self, "Save file", "",                  "Text documents (*.txt);All files (*.*)")
      if not path:
        return
      self._save_to_path(path)
    def _save_to_path(self,path):
      text = self.editor.toPlainText()
      try:
        with open(path,'w') as f:
          f.write(text)
      except Exception as e:
        self.dialog_critical(str(e))
      else:
        self.path = path
        self.update_title()
        
    def file_open(self):
      name, _ = QFileDialog.getOpenFileName(self,"Open File")
      fileo = open(name, 'r')
      
      
      with fileo:
        text = fileo.read()
        self.editor.setText(str(text))
        
      
    def dark_mode(self):
      self.editor.setStyleSheet('background-color:black;color:white;')
      self.setStyleSheet('background-color:black; color:white;')
      
    def About_dlg(self):
      dlg = QMessageBox(self)
      font = QFont("Monospace",15)
      dlg.setWindowTitle('[About]')
      dlg.setFont(font)
      dlg.setText("<center><b>Levanditor v0.1  By Levande</b></center>")
      dlg.exec()

  

app = QApplication(sys.argv)
win = ha()
win.show()
sys.exit(app.exec_())
  
  
