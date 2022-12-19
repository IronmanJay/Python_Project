import win32com.client as win32

from PIL import ImageGrab

excel = win32.Dispatch('Excel.Application')

wb = excel.Workbooks.Open('D:\\test.xlsx')

ws2 = wb.WorkSheets(2)

ws2.Range("A1").Value = 6

ws = wb.WorkSheets('Sheet1')

ws.Range("A1:B1").CopyPicture()

ws.Paste(ws.Range('K1'))  # 变成图片

# new_shape_name = 'shape_name_tmp' #通过名称定位图片

# excel.Selection.ShapeRange.Name = new_shape_name #图片的重命名

# ws.Shapes(new_shape_name).Copy() #图片至剪贴板

ws.Shapes(ws.Shapes.Count).Copy()  # 图片至剪贴板

img = ImageGrab.grabclipboard()

img.save("D:\\test.png")

wb.Save()

wb.Close()
