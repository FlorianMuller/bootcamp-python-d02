from csvreader import CsvReader

# Subject tests

# if __name__ == "__main__":
#     with CsvReader('good.csv') as file:
#         data = file.getdata()
#         header = file.getheader()

# if __name__ == "__main__":
#     with CsvReader('bad.csv') as file:
#         if file is None:
#             print("File is corrupted")


# My tests

if __name__ == "__main__":
    with CsvReader('good.csv', header=True, skip_top=8, skip_bottom=8) as file:
        if file is None:
            print("File is corrupted")
        else:
            print("getheader: ", file.getheader())
            print("getdata: ", *file.getdata(), sep="\n")


if __name__ == "__main__":
    # Should be corrupted
    with CsvReader('bad.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            print("File is ~GOOD~")

    # Should be good
    with CsvReader('bad.csv', allow_empty_value=True) as file:
        if file is None:
            print("File is corrupted")
        else:
            print("File is ~GOOD~")

    # Should be corrupted (too few elements)
    with CsvReader('bad_too_few.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            print("File is ~GOOD~")

    # Should be corrupted (too many elements)
    with CsvReader('bad_too_many.csv') as file:
        if file is None:
            print("File is corrupted")
        else:
            print("File is ~GOOD~")

    # File that doesn't exist
    with CsvReader('unknown.csv') as file:
        if file is None:
            print("File doesn't exist")
        else:
            print("File is ~GOOD~")
