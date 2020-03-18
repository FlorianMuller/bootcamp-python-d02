import csv


class CsvReader():
    def __init__(self, name, sep=',', skipinitialspace=True, header=False,
                 skip_top=0, skip_bottom=0, allow_empty_value=False):
        try:
            self.file = open(name, "r")
            # Getting data
            reader = csv.reader(self.file, delimiter=sep, strict=True,
                                skipinitialspace=skipinitialspace)
            self.header = next(reader) if header else None
            self.raw_data = list(reader)

            # Checking if csv's data is valid
            if self.__is_valid(allow_empty_value):
                self.wanted_data = self.raw_data[skip_top:(reader.line_num
                                                           - 1) - skip_bottom]
            else:
                self.wanted_data = None

        except FileNotFoundError:
            self.wanted_data = None

    def __is_valid(self, allow_empty_value):
        """Check if each csv raw has the right amount of element"""
        elem_nbr = len(self.header) if self.header else len(self.raw_data[0])

        for row in self.raw_data:
            if len(row) != elem_nbr or (not allow_empty_value and '' in row):
                return False
        return True

    def __enter__(self):
        if self.wanted_data is None:
            return None
        return self

    def __exit__(self, type, value, traceback):
        if self.wanted_data is not None:
            self.file.close()

    def getdata(self):
        return self.wanted_data

    def getheader(self):
        return self.header
