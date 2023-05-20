

from ITransportation import ITransportation


class Traveler:
    def __init__(self, t: ITransportation) -> None:
        self.transporter = t
        pass

    def go(self):
        print("운송 수단 타고 감")
        self.transporter.run()
