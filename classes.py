class Computer():
    def __init__(self, name, manufacture, location):
        self.name = name
        self.manufacture = manufacture
        self.location = location
        self.hardware = []
        self.software = []

    def addHardware(self, hardware):
        self.hardware.append(hardware)

    def addSoftware(self, software):
        self.software.append(software)

    def showHardware(self):
        for hard in self.hardware:
            hard.show_hardware()

    def showSoftware(self):
        for soft in self.software:
            soft.show_software()

    def full_specs(self):
        print('Manufacturer: ', self.manufacture)
        print('Hardwares are: ')
        self.showHardware()
        print('Softwares are: ')
        self.showSoftware()


class Hardware():
    def __init__(self, name, installed_date):
        self.name = name
        self.install_date = installed_date

    def show_hardware(self):
        print('Name is : ', self.name,' Installed Date is: ',self.install_date)


class Software():
    def __init__(self, name, installed_date):
        self.name = name
        self.install_date = installed_date

    def show_software(self):
        print('Name is : ', self.name, ' Installed Date is: ', self.install_date)

hd = Hardware('RAM','02-12-2017')
soft = Software('VS','05-02-2017')
comp = Computer('core i7', 'Intel','HOME')
comp.addHardware(hd)
comp.addSoftware(soft)
comp.full_specs()