import Collection
import LoadNeetsDevice

dataLoader = LoadNeetsDevice.DeviceDataLoader()

dataLoader.setAddress("C:/Users/fhu/Desktop/PyCode - Copy/Fohhn-D-4.1200 - Copy.dvc")
dataLoader.loadDevice()
dataLoader.createSection()

dataLoader.printList(dataLoader.rsList)




