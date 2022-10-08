#-------------------------------------------------------------------------------
# Name:        MouseAutomove
# Purpose:
#
# Author:      Gürol Güngör
#
# Created:     08.10.2022
# Copyright:   (c) Gürol Güngör 2022
# Licence:     GNU - General Public Licence
#-------------------------------------------------------------------------------
def main():
    pass

if __name__ == '__main__':
    main()

# pyautogui ve time kitaplığını kullanma
import pyautogui
import time

# sonsuz döngüyü baslatiyoruz.
while True:
  pyautogui.moveRel(1, 10)
  time.sleep(5)