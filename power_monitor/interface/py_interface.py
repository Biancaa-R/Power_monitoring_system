import pyserial
import curses

port ="COM3"
ser=serial.Serial(port,115200,timeout=0)
screen=curses.initser()
screen.refresh()

row=0
col=0
screen.addstr(row,col,"Data :")