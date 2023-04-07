class BarcodeScanner:
    def __init__(self, subject):
        self.subject = subject

    def scan(self, barcode):
        self.subject.notify_observers(barcode)