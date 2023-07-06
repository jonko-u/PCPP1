# Level of difficulty
#
# Medium
# Objectives
#
#     Creation of abstract classes and abstract methods;
#     multiple inheritance of abstract classes;
#     overriding abstract methods;
#     delivering multiple child classes.
#
# Scenario
#
#     You are about to create a multifunction device (MFD) that can scan and print documents;
#     the system consists of a scanner and a printer;
#     your task is to create blueprints for it and deliver the implementations;
#     create an abstract class representing a scanner that enforces the following methods:
#         scan_document – returns a string indicating that the document has been scanned;
#         get_scanner_status – returns information about the scanner (max. resolution, serial number)
#     Create an abstract class representing a printer that enforces the following methods:
#         print_document – returns a string indicating that the document has been printed;
#         get_printer_status – returns information about the printer (max. resolution, serial number)
#     Create MFD1, MFD2 and MFD3 classes that inherit the abstract classes responsible for scanning and printing:
#         MFD1 – should be a cheap device, made of a cheap printer and a cheap scanner, so device capabilities (resolution) should be low;
#         MFD2 – should be a medium-priced device allowing additional operations like printing operation history, and the resolution is better than the lower-priced device;
#         MFD3 – should be a premium device allowing additional operations like printing operation history and fax machine.
#     Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities. All devices should be capable of serving generic feature sets.

from abc import ABC, abstractmethod


class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass

    @abstractmethod
    def get_scanner_status(self):
        pass


class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

    @abstractmethod
    def get_printer_status(self):
        pass


class MFD1(Scanner, Printer):
    def scan_document(self):
        return "Document scanned with MFD1"

    def get_scanner_status(self):
        return "MFD1 scanner status: max. resolution 300dpi, serial number 12345"

    def print_document(self):
        return "Document printed with MFD1"

    def get_printer_status(self):
        return "MFD1 printer status: max. resolution 600dpi, serial number 67890"


class MFD2(Scanner, Printer):
    def scan_document(self):
        return "Document scanned with MFD2"

    def get_scanner_status(self):
        return "MFD2 scanner status: max. resolution 600dpi, serial number 23456"

    def print_document(self):
        return "Document printed with MFD2"

    def get_printer_status(self):
        return "MFD2 printer status: max. resolution 1200dpi, serial number 78901"

    def print_operation_history(self):
        return "Printing operation history for MFD2"


class MFD3(Scanner, Printer):
    def scan_document(self):
        return "Document scanned with MFD3"

    def get_scanner_status(self):
        return "MFD3 scanner status: max. resolution 1200dpi, serial number 34567"

    def print_document(self):
        return "Document printed with MFD3"

    def get_printer_status(self):
        return "MFD3 printer status: max. resolution 2400dpi, serial number 89012"

    def print_operation_history(self):
        return "Printing operation history for MFD3"

    def send_fax(self):
        return "Fax sent from MFD3"


# Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities
mfd1 = MFD1()
print(mfd1.scan_document())  # Output: Document scanned with MFD1
print(mfd1.get_scanner_status())  # Output: MFD1 scanner status: max. resolution 300dpi, serial number 12345
print(mfd1.print_document())  # Output: Document printed with MFD1
print(mfd1.get_printer_status())  # Output: MFD1 printer status: max. resolution 600dpi, serial number 67890

mfd2 = MFD2()
print(mfd2.scan_document())  # Output: Document scanned with MFD2
print(mfd2.get_scanner_status())  # Output: MFD2 scanner status: max. resolution 600dpi, serial number 23456
print(mfd2.print_document())  # Output: Document printed with MFD2
print(mfd2.get_printer_status())  # Output: MFD2 printer status: max. resolution 1200dpi, serial number 78901
print(mfd2.print_operation_history())  # Output: Printing operation history for MFD2

mfd3 = MFD3()
print(mfd3.scan_document())  # Output: Document scanned with MFD3
print(mfd3.get_scanner_status())  # Output: MFD3 scanner status: max. resolution 1200dpi, serial number 34567
print(mfd3.print_document())  # Output: Document printed with MFD3
print(mfd3.get_printer_status())  # Output: MFD3 printer status: max. resolution 2400dpi, serial number 89012
print(mfd3.print_operation_history())  # Output: Printing operation history for MFD3
print(mfd3.send_fax())  # Output: Fax sent from MFD3
