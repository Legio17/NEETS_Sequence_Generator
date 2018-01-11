import LoadNeetsDevice
import Sequence

loader = LoadNeetsDevice.DeviceDataLoader()
loader.setAddress("D:/data/NEETS/PyCode - Copy/PyCode - Copy/Fohhn-D-4.1200 - Copy.dvc");
loader.createSection();

#print('[%s]' % ', '.join(map(str, loader.seqholder.irList))) #print all ir sequences in device driver

controlCMD = Sequence.ControlSeq();
controlCMD.toString()
