
class parse_output:
    
    def __init__(self) -> None:
        pass

    def count_for_invalid_match(self):
        file_name = str(input("input the file name you want to read:"))
        total_lines = 0
        invalid_lines = 0
        try:
            with open(file_name + ".txt") as file:
                for line in file:
                    if (line[-4:] != 'nan '):
                        print(len(line[-4:]))
                        
                        invalid_lines += 1
                    total_lines += 1
            print(f"total listings: {total_lines}")
            print(f"invalid listings: {invalid_lines}")
            print(f"match percent: {(total_lines - invalid_lines) / total_lines}")
                
        except FileNotFoundError:
            print("File not found")
        except (FileNotFoundError, PermissionError):
            print("Error: file not found or permission denied")
        else:
            print("File opened successfully")


def main():
    parse_output().count_for_invalid_match()


if __name__ == '__main__':
    main()