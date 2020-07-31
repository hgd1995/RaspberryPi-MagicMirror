# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mirrorUI_1260_800.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 1260)
        MainWindow.setMinimumSize(QtCore.QSize(567, 869))
        MainWindow.setStyleSheet("background-color: rgb(63, 63, 63);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_head = QtWidgets.QHBoxLayout()
        self.horizontalLayout_head.setObjectName("horizontalLayout_head")
        self.verticalLayout_headL = QtWidgets.QVBoxLayout()
        self.verticalLayout_headL.setObjectName("verticalLayout_headL")
        self.gridLayout_headL = QtWidgets.QGridLayout()
        self.gridLayout_headL.setObjectName("gridLayout_headL")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_temperature = QtWidgets.QLabel(self.centralwidget)
        self.label_temperature.setMinimumSize(QtCore.QSize(0, 0))
        self.label_temperature.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 73 BdEx")
        font.setPointSize(70)
        self.label_temperature.setFont(font)
        self.label_temperature.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_temperature.setLineWidth(0)
        self.label_temperature.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temperature.setObjectName("label_temperature")
        self.verticalLayout_3.addWidget(self.label_temperature)
        self.label_humidity = QtWidgets.QLabel(self.centralwidget)
        self.label_humidity.setMinimumSize(QtCore.QSize(220, 0))
        self.label_humidity.setMaximumSize(QtCore.QSize(16777215, 80))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 73 BdEx")
        font.setPointSize(40)
        self.label_humidity.setFont(font)
        self.label_humidity.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_humidity.setLineWidth(0)
        self.label_humidity.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_humidity.setObjectName("label_humidity")
        self.verticalLayout_3.addWidget(self.label_humidity)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.label_weathericon = QtWidgets.QLabel(self.centralwidget)
        self.label_weathericon.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_weathericon.sizePolicy().hasHeightForWidth())
        self.label_weathericon.setSizePolicy(sizePolicy)
        self.label_weathericon.setMinimumSize(QtCore.QSize(140, 140))
        self.label_weathericon.setMaximumSize(QtCore.QSize(140, 140))
        self.label_weathericon.setLineWidth(0)
        self.label_weathericon.setText("")
        self.label_weathericon.setPixmap(QtGui.QPixmap("source/太阳.png"))
        self.label_weathericon.setScaledContents(True)
        self.label_weathericon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_weathericon.setWordWrap(False)
        self.label_weathericon.setObjectName("label_weathericon")
        self.horizontalLayout.addWidget(self.label_weathericon)
        self.horizontalLayout.setStretch(0, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label_weather = QtWidgets.QLabel(self.centralwidget)
        self.label_weather.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(35)
        self.label_weather.setFont(font)
        self.label_weather.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_weather.setLineWidth(0)
        self.label_weather.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_weather.setObjectName("label_weather")
        self.verticalLayout_2.addWidget(self.label_weather)
        self.label_weathertips = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(25)
        self.label_weathertips.setFont(font)
        self.label_weathertips.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_weathertips.setLineWidth(0)
        self.label_weathertips.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_weathertips.setWordWrap(True)
        self.label_weathertips.setObjectName("label_weathertips")
        self.verticalLayout_2.addWidget(self.label_weathertips)
        self.verticalLayout_2.setStretch(0, 1)
        self.gridLayout_headL.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_headL.addLayout(self.gridLayout_headL)
        self.horizontalLayout_head.addLayout(self.verticalLayout_headL)
        self.verticalLayout_headR = QtWidgets.QVBoxLayout()
        self.verticalLayout_headR.setContentsMargins(-1, 10, -1, -1)
        self.verticalLayout_headR.setObjectName("verticalLayout_headR")
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("HelveticaNeueLT Pro 73 BdEx")
        font.setPointSize(75)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_time.setLineWidth(0)
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout_headR.addWidget(self.label_time)
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(35)
        self.label_date.setFont(font)
        self.label_date.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_date.setLineWidth(0)
        self.label_date.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_date.setObjectName("label_date")
        self.verticalLayout_headR.addWidget(self.label_date)
        self.label_week = QtWidgets.QLabel(self.centralwidget)
        self.label_week.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("华文琥珀")
        font.setPointSize(35)
        self.label_week.setFont(font)
        self.label_week.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_week.setAlignment(QtCore.Qt.AlignCenter)
        self.label_week.setObjectName("label_week")
        self.verticalLayout_headR.addWidget(self.label_week)
        self.label_historyhead = QtWidgets.QLabel(self.centralwidget)
        self.label_historyhead.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(30)
        self.label_historyhead.setFont(font)
        self.label_historyhead.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_historyhead.setLineWidth(0)
        self.label_historyhead.setObjectName("label_historyhead")
        self.verticalLayout_headR.addWidget(self.label_historyhead)
        self.label_historymsg = QtWidgets.QLabel(self.centralwidget)
        self.label_historymsg.setMinimumSize(QtCore.QSize(0, 80))
        self.label_historymsg.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(25)
        self.label_historymsg.setFont(font)
        self.label_historymsg.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_historymsg.setLineWidth(0)
        self.label_historymsg.setScaledContents(False)
        self.label_historymsg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_historymsg.setWordWrap(True)
        self.label_historymsg.setObjectName("label_historymsg")
        self.verticalLayout_headR.addWidget(self.label_historymsg)
        self.verticalLayout_headR.setStretch(0, 1)
        self.verticalLayout_headR.setStretch(1, 1)
        self.verticalLayout_headR.setStretch(2, 1)
        self.verticalLayout_headR.setStretch(3, 1)
        self.verticalLayout_headR.setStretch(4, 1)
        self.horizontalLayout_head.addLayout(self.verticalLayout_headR)
        self.horizontalLayout_head.setStretch(0, 1)
        self.horizontalLayout_head.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_head)
        self.horizontalLayout_center = QtWidgets.QHBoxLayout()
        self.horizontalLayout_center.setObjectName("horizontalLayout_center")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_center.addItem(spacerItem)
        self.label_communicate = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(40)
        self.label_communicate.setFont(font)
        self.label_communicate.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(63, 63, 63);")
        self.label_communicate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_communicate.setLineWidth(0)
        self.label_communicate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_communicate.setWordWrap(True)
        self.label_communicate.setObjectName("label_communicate")
        self.horizontalLayout_center.addWidget(self.label_communicate)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_center.addItem(spacerItem1)
        self.horizontalLayout_center.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_center)
        self.horizontalLayout_end = QtWidgets.QHBoxLayout()
        self.horizontalLayout_end.setObjectName("horizontalLayout_end")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_todohead = QtWidgets.QLabel(self.centralwidget)
        self.label_todohead.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(35)
        self.label_todohead.setFont(font)
        self.label_todohead.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_todohead.setLineWidth(0)
        self.label_todohead.setObjectName("label_todohead")
        self.verticalLayout_10.addWidget(self.label_todohead)
        self.label_todomsg = QtWidgets.QLabel(self.centralwidget)
        self.label_todomsg.setMinimumSize(QtCore.QSize(0, 240))
        self.label_todomsg.setMaximumSize(QtCore.QSize(16777215, 240))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(30)
        self.label_todomsg.setFont(font)
        self.label_todomsg.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_todomsg.setLineWidth(0)
        self.label_todomsg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_todomsg.setWordWrap(True)
        self.label_todomsg.setObjectName("label_todomsg")
        self.verticalLayout_10.addWidget(self.label_todomsg)
        self.horizontalLayout_end.addLayout(self.verticalLayout_10)
        self.label_gif = QtWidgets.QLabel(self.centralwidget)
        self.label_gif.setMinimumSize(QtCore.QSize(125, 150))
        self.label_gif.setMaximumSize(QtCore.QSize(125, 150))
        self.label_gif.setLineWidth(0)
        self.label_gif.setText("")
        self.label_gif.setTextFormat(QtCore.Qt.PlainText)
        self.label_gif.setPixmap(QtGui.QPixmap("source/洛天依_黑.gif"))
        self.label_gif.setScaledContents(True)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.setObjectName("label_gif")
        self.horizontalLayout_end.addWidget(self.label_gif)
        self.horizontalLayout_end.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_end)
        self.horizontalLayout_news = QtWidgets.QHBoxLayout()
        self.horizontalLayout_news.setObjectName("horizontalLayout_news")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_headlineshead = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(30)
        self.label_headlineshead.setFont(font)
        self.label_headlineshead.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_headlineshead.setLineWidth(0)
        self.label_headlineshead.setObjectName("label_headlineshead")
        self.verticalLayout_9.addWidget(self.label_headlineshead)
        self.label_headlinesmsg = QtWidgets.QLabel(self.centralwidget)
        self.label_headlinesmsg.setMinimumSize(QtCore.QSize(0, 90))
        self.label_headlinesmsg.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("造字工房稚言体（非商用）")
        font.setPointSize(25)
        self.label_headlinesmsg.setFont(font)
        self.label_headlinesmsg.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_headlinesmsg.setLineWidth(0)
        self.label_headlinesmsg.setWordWrap(True)
        self.label_headlinesmsg.setObjectName("label_headlinesmsg")
        self.verticalLayout_9.addWidget(self.label_headlinesmsg)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)
        self.horizontalLayout_news.addLayout(self.verticalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_news)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MagicMirror"))
        self.label_temperature.setText(_translate("MainWindow", "--.-°"))
        self.label_humidity.setText(_translate("MainWindow", "--%"))
        self.label_weather.setText(_translate("MainWindow", "多云转晴"))
        self.label_weathertips.setText(_translate("MainWindow", "天气很好出去走走吧~"))
        self.label_time.setText(_translate("MainWindow", "12:00"))
        self.label_date.setText(_translate("MainWindow", "2020年4月1日"))
        self.label_week.setText(_translate("MainWindow", "星期三"))
        self.label_historyhead.setText(_translate("MainWindow", "历史上的今天："))
        self.label_historymsg.setText(_translate("MainWindow", "第四届核安全峰会在美国首都华盛顿举行"))
        self.label_communicate.setText(_translate("MainWindow", "WoW！你今天有点帅！"))
        self.label_todohead.setText(_translate("MainWindow", "今日事项"))
        self.label_todomsg.setText(_translate("MainWindow", "今天没事，可以好好休息啦~"))
        self.label_headlineshead.setText(_translate("MainWindow", "时事热点"))
        self.label_headlinesmsg.setText(_translate("MainWindow", "美股史上第四次熔断!\n"
"美股史上第五次熔断!"))

