# -*- coding: utf-8 -*-


from PySide6.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image
import io
import fitz  # PyMuPDF
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,QVBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
from banco import Biblioteca

class Ui_MainWindow(Biblioteca):
   

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
         MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 771, 531))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMaximumSize(QSize(16777215, 70))

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.gridLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(9, 10, 231, 431))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 17, 141, 41))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 70, 141, 41))
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 120, 141, 41))
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 170, 141, 41))
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 220, 141, 41))
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(10, 270, 141, 41))
        self.frame_2 = QFrame(self.widget)
        
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(260, 10, 501, 431))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.layout=QGridLayout(self.frame_2)
     
        self.horizontalLayout.addWidget(self.widget)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.current_page = 0  # Página atual do PDF
        self.pdf_document = None  # Documento PDF carregado
        self.label_pdf = QLabel(self.frame_2)  # Label único para exibir as páginas
        self.layout.addWidget(self.label_pdf)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        self.pushButton.clicked.connect(lambda: self.eventobutton('list_livros'))
    
        self.pushButton_2.clicked.connect(lambda: self.eventobutton('novo_usuario'))
        self.pushButton_3.clicked.connect(lambda: self.eventobutton('inserir_livros'))
        self.pushButton_4.clicked.connect(lambda: self.eventobutton('emprestar_livros'))
        self.pushButton_5.clicked.connect(lambda: self.eventobutton('livros_emprestados'))
        self.pushButton_6.clicked.connect(lambda: self.eventobutton('exibir_pdf'))
    
    


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"BIBLIOTECA", None))
        self.label.setStyleSheet("font-size: 40px; font-weight: bold; background-color: yellow;")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"LISTA LIVROS", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"INSERIR USERS", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"INSERIR LIVROS", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"EMPRESTAR LIVROS", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"LIVROS EMPRESTADOS", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"LIVROs PDF", None))
    # retranslateUi
    
    def exibir_pdf(self):
      
        self.label_pdf= QLabel(self.frame_2)
        self.layout.addWidget(self.label_pdf)

        
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.TABLE_LIVROS_PDF}")
                self.resultado = cursor.fetchall()
                colunas = 4
                for i, linha in enumerate (self.resultado):
                        text=linha[1]
                        self.pushButton_pd = QPushButton(text)
                        self.pushButton_pd.setObjectName(u"pushButton")
                        
                        row, col = divmod(i, colunas)
                        self.layout.addWidget(self.pushButton_pd, row, col)
                        slot= self.makeSlot(self.pdf_view,linha[2])
                        self.connectButtonClicked(self.pushButton_pd,slot)  
            
                
                   
                print('S')
        finally:
            connection.close()
    def connectButtonClicked(self,button,slot):
           button.clicked.connect(slot)
           
    def makeSlot(self, func,*args,**kwargs):
        def realSlot():
            func(*args,**kwargs)
        return realSlot
    def pdf_view(self, pdf_data):
        """Carrega o PDF a partir dos dados binários e exibe a primeira página."""
        self.pdf_document = fitz.open(stream=pdf_data, filetype="pdf")
        self.current_page = 0
        self.display_page(self.current_page)  # Mostra a primeira página

        # Botões de navegação
        btn_next = QPushButton("Próxima Página", self.frame_2)
        btn_next.clicked.connect(self.next_page)
        self.layout.addWidget(btn_next)

        btn_prev = QPushButton("Página Anterior", self.frame_2)
        btn_prev.clicked.connect(self.previous_page)
        self.layout.addWidget(btn_prev)

    def display_page(self, page_num):
        """Exibe a página especificada."""
        if 0 <= page_num < self.pdf_document.page_count:
            page = self.pdf_document[page_num]
            pix = page.get_pixmap()
            image = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            qt_image = ImageQt(image)
            pixmap = QPixmap.fromImage(qt_image)
            
            self.label_pdf.setPixmap(pixmap)
            self.label_pdf.setAlignment(Qt.AlignCenter)

    def next_page(self):
        """Vai para a próxima página do PDF."""
        if self.current_page < self.pdf_document.page_count - 1:
            self.current_page += 1
            self.display_page(self.current_page)

    def previous_page(self):
        """Volta para a página anterior do PDF."""
        if self.current_page > 0:
            self.current_page -= 1
            self.display_page(self.current_page)
    def testeclick_button(self):
        print('1')
    def inserir_livros(self):
          # Lógica para adicionar novo usuário
        label_titulo= QLabel(self.frame_2)
        label_titulo.setText("Adicionar Novo livro")
        label_titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(label_titulo)

        self.label_titulo = QLabel("Titulo:", self.frame_2)
        self.titulo_livro= QLineEdit(self.frame_2)
        self.titulo_livro.setObjectName(u"titulo")
        
        self.layout.addWidget(self.label_titulo)
        self.layout.addWidget(self.titulo_livro )

        self.label_autor = QLabel("Autor:", self.frame_2)
        self.titulo_autor= QLineEdit(self.frame_2)
        self.titulo_autor.setObjectName(u"autor")
        
        self.layout.addWidget(self.label_autor)
        self.layout.addWidget(self.titulo_autor )

        
        self.label_editora = QLabel("editora", self.frame_2)
        self.titulo_editora= QLineEdit(self.frame_2)
        self.titulo_editora.setObjectName(u"titulo_editora")
        
        self.layout.addWidget(self.label_editora)
        self.layout.addWidget(self.titulo_editora )

        self.label_publicacao = QLabel("publicaçao:", self.frame_2)
        self.titulo_publicacao= QLineEdit(self.frame_2)
        self.titulo_publicacao.setObjectName(u"titulo_publicacao")
        
        self.layout.addWidget(self.label_publicacao)
        self.layout.addWidget(self.titulo_publicacao )
    
        self.label_isbn = QLabel("ISBN:", self.frame_2)
        self.titulo_isbn= QLineEdit(self.frame_2)
        self.titulo_isbn.setObjectName(u"titulo_isbn")
        
        self.layout.addWidget(self.label_isbn)
        self.layout.addWidget(self.titulo_isbn )

        bnt= QPushButton('salvar',self.frame_2)
        bnt.clicked.connect(self.save_info1)
        self.layout.addWidget(bnt)

    def emprestar_livros(self):
        label_nome = QLabel("digite seu Nome:", self.frame_2)
        self.dig_nome= QLineEdit(self.frame_2)
        self.dig_nome.setObjectName(u"nome")
        # Lógica para adicionar novo usuário
         
        self.layout.addWidget(label_nome)
        self.layout.addWidget(self.dig_nome)

        label_titulo = QLabel("digite livro:", self.frame_2)
        self.dig_livro= QLineEdit(self.frame_2)
        self.dig_livro.setObjectName(u"nome")
        # Lógica para adicionar novo usuário

        self.layout.addWidget(label_titulo)
        self.layout.addWidget(self.dig_livro)

        label_data = QLabel("Data de hoje", self.frame_2)
        self.dig_data= QLineEdit(self.frame_2)
        self.dig_data.setObjectName(u"nome")
        # Lógica para adicionar novo usuário

        self.layout.addWidget(label_data)
        self.layout.addWidget(self.dig_data)
       



        bnt= QPushButton('pesquisar',self.frame_2)
        bnt.clicked.connect(self.verificar_user)
        self.layout.addWidget(bnt)

        
    def livros_emprestatos(self):
        label_emprestimo= QLabel(self.frame_2)
       
        self.layout.addWidget(label_emprestimo)
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                result= f"""
                        SELECT livros.titulo, users.nome, users.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao
                        FROM livros
                        INNER JOIN  emprestimos ON livros.id = emprestimos.id_livro
                        INNER JOIN  users ON users.id = emprestimos.id_usuario
                        WHERE emprestimos.data_devolucao IS NULL
                        """
                cursor.execute(result)
                result = cursor.fetchall()
                connection.commit()

                for i in result:
                    nova_lista=label_emprestimo.text()
                    print(i)
                    label_emprestimo.setText(f"{i}\n"+f"{nova_lista}")
       
        finally:
            connection.close()

    def list_livros(self):
        
        # Lógica para adicionar novo usuário
        label_titulo= QLabel(self.frame_2)
       
        self.layout.addWidget(label_titulo)
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.TABLE_LIVROS}")
                self.resultado = cursor.fetchall()
                for livro in self.resultado:
                    novalista=label_titulo.text()
                    a=  (f'ID: {livro[0]}\n'
                        f'Titulo: {livro[1]}\n'
                        f'Autor: {livro[2]}\n'
                        f'Editora: {livro[3]}\n'
                        f'Ano de Publicação: {livro[4]}\n'
                        f'ISBN: {livro[5]}\n'
                        '\n')
                    label_titulo.setText(f'{novalista}\n'+f' {livro} ')
                    
        finally:
            connection.close()


    def novo_usuario(self):

      
           # Lógica para adicionar novo usuário
        label_titulo= QLabel(self.frame_2)
        label_titulo.setText("Adicionar Novo Usuário")
        label_titulo.setStyleSheet("font-size: 20px; font-weight: bold;")
        self.layout.addWidget(label_titulo)

        self.label_nome = QLabel("Nome:", self.frame_2)
        self.nome= QLineEdit(self.frame_2)
        self.nome.setObjectName(u"nome")
        
        self.layout.addWidget(self.label_nome)
        self.layout.addWidget(self.nome)

            # Campo para Email
        label_email = QLabel("Email:", self.frame_2)
        self.input_email = QLineEdit(self.frame_2)
        self.input_email.setObjectName("input_email")

        self.layout.addWidget(label_email)
        self.layout.addWidget(self.input_email)

        label_endereco = QLabel("Endereço:", self.frame_2)
        self.input_endereco= QLineEdit(self.frame_2)
        self.input_endereco.setObjectName("input_endereco")

        self.layout.addWidget(label_endereco)
        self.layout.addWidget(self.input_endereco)


        bnt= QPushButton('salvar',self.frame_2)
        bnt.clicked.connect(self.save_info)
        self.layout.addWidget(bnt)

    def clear_frame_widgets(self):

        for widget in self.frame_2.findChildren(QWidget):
            widget.deleteLater()

    

    def eventobutton(self,i):
        layout = self.frame_2.layout()
        if i == 'novo_usuario' :
            # Limpa todos os widgets dentro do frame_2
           self.clear_frame_widgets
           self.novo_usuario()
        if i == 'list_livros':
            # Limpa todos os widgets dentro do frame_2
            self.clear_frame_widgets
            self.list_livros()
        if i == 'inserir_livros':
        # Limpa todos os widgets dentro do frame_2
            self.clear_frame_widgets
            self.inserir_livros()
        
        if i == 'emprestar_livros':
        # Limpa todos os widgets dentro do frame_2
            self.clear_frame_widgets
            self.emprestar_livros()

        if i == 'livros_emprestados':
        # Limpa todos os widgets dentro do frame_2
            self.clear_frame_widgets
            self.livros_emprestatos()
        if i == 'exibir_pdf':
        # Limpa todos os widgets dentro do frame_2
            self.clear_frame_widgets
            self.exibir_pdf()
        

    def verificar_user(self):
        nome=self.dig_nome.text()
        connection = self.connect()
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.TABLE_USERS}")
                self.result = cursor.fetchall()
                for i in self.result:
                    n=i[0]
                    if nome == i[1]:
                        self.save_info2(n)
                        

        finally:
          connection.close()

    def save_info2(self,b):
        livro=self.dig_livro.text()
        connection = self.connect()
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(f"SELECT * FROM {self.TABLE_LIVROS}")
                self.result = cursor.fetchall()
                for i in self.result:
                    id=i[0]
                    if livro == i[1]:
                        self.insert_emprestimo(id, b, '2024-08-11', None)                 

        finally:
          connection.close()
    
        
    def save_info(self):
        self.name= self.nome.text()
        self.email=self.input_email.text()

        
       
        self.insert_user(self.name, None, None, self.email, None)
       
        print(self.name)

    def save_info1(self):
        titulo_livro=self.titulo_livro.text()
        self.insert_book(titulo_livro, None, None, None, None)
        print(titulo_livro)
       

    
       
        print(titulo_livro)





