from colorama import Fore, Style
import sys, os
import platform
class DataBaseError(Exception):
    pass
class DataBase:
    def __init__(self, DBName: str):
        """
        DataBase is a module that allows the user to easily manage their data via many methods.
        """
        self.data: dict = {}
        self.dbname: str = DBName.replace("\n", "").replace(r"\n", "<CHAR>")
        self.connected: bool = False
    def __repr__(self) -> str:
        return f"DataBase({self.dbname})"
    def __eq__(self, other):
        if isinstance(other, DataBase):
            return id(self) == id(other) and self.data == other.data and self.dbname == other.dbname
        else:
            return NotImplemented
    def __neq__(self, other):
        if isinstance(other, DataBase):
            return id(self) != id(other) and self.data != other.data and self.dbname != other.dbname
        else:
            return NotImplemented
    def __enter__(self):
        print(f"Loading DataBase: {self.dbname}")
        self.connected = True
        print(f"Connected to DataBase: {self.dbname}.")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.connected = False
        if exc_type:
            print(f"An error occurred: {exc_value}")
            sys.exit(1)
        print(f"Disconnected from DataBase: {self.dbname}")
        return True
    def adddatafrom(self, source: dict) -> bool:
        """
        Add data to the DataBase from a dict.
        If a key from the DataBase`s data is also in source data, the source data will overwrite the existing data.
        """
        if isinstance(source, dict) != True:
            raise DataBaseError(f"Can only source data from dict, not {source.__class__.__name__}.")
        else:
            self.data = {**self.data, **source}
            return True
class DBSH:
    def __init__(self, db):
        """
        DBSH is a verified module for DataBase that allows the user to manage their DataBase via a shell.
        """
        try:
            if db.__class__.__name__ != "DataBase":
                raise DataBaseError(f'Supplied DataBase must be of type DataBase, not {db.__class__.__name__}.')
        except AttributeError:
            print('Supplied DataBase must be of type DataBase.')
        if db.connected == True:
            raise DataBaseError("Cannot start DBSH on an active database.")
        print(f"{Fore.CYAN}Loading DataBase{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}{db.dbname}{Style.RESET_ALL}")
        self.db: dict = dict(db.data)
        self.connecteddb: DataBase = db
        self.dbname: str = db.dbname
        db.connected = True
        self.command_hive_helptext: str = f"""{Fore.GREEN}Hive{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}Usage{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL}
    {Fore.GREEN}hive{Style.RESET_ALL} {Fore.BLUE}create{Style.RESET_ALL} {Fore.CYAN}<HIVE>{Style.RESET_ALL}
    {Fore.GREEN}hive{Style.RESET_ALL} {Fore.BLUE}edit{Style.RESET_ALL} {Fore.CYAN}<HIVE>{Style.RESET_ALL} {Fore.CYAN}<CONTENT>{Style.RESET_ALL}
    {Fore.GREEN}hive{Style.RESET_ALL} {Fore.BLUE}show{Style.RESET_ALL} {Fore.CYAN}<HIVE>{Style.RESET_ALL}
    {Fore.GREEN}hive{Style.RESET_ALL} {Fore.BLUE}delete{Style.RESET_ALL} {Fore.CYAN}<HIVE>{Style.RESET_ALL}""".center(50)
        print(f"{Fore.CYAN}Connected to DataBase{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}{db.dbname}{Style.RESET_ALL}")
    def __repr__(self) -> str:
        return f"DBSH(DataBase({self.dbname}))"
    def __command_clear(self, args: list) -> None:
        os.system('cls' if platform.system() == "Windows" else 'clear')
    def __command_print(self, args: list) -> None:
        out = ""
        sc = ""
        for i in args:
            out = out + sc + i
            sc = " "
        print(out)
        del out
        del sc
    def __command_getfile(self, args: list) -> None:
        try:
            with open(args[0], 'r') as file:
                print(file.read(), end="")
        except IndexError:
            print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}Please provide a file path.{Style.RESET_ALL}")
        except FileNotFoundError:
            print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}File not found.{Style.RESET_ALL}")
        except Exception as e:
            print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}{e}{Style.RESET_ALL}")
    def __command_hive(self, args: list) -> None:
        if args == []:
            print(self.command_hive_helptext)
        elif args[0] == 'create':
            try:
                self.db[args[1]] = None
            except IndexError:
                print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}Syntax:{Style.RESET_ALL} {Fore.GREEN}hive create <HIVE>{Style.RESET_ALL}")
        elif args[0] == 'edit':
            try:
                self.db[args[1]] = args[2]
            except IndexError:
                print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}Syntax:{Style.RESET_ALL} {Fore.GREEN}hive edit <HIVE> <CONTENT>{Style.RESET_ALL}")
        elif args[0] == 'show':
            try:
                print(self.db[args[1]])
            except KeyError:
                print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}DataBase entry not found:{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}{args[1]}{Style.RESET_ALL}{Fore.BLUE}.{Style.RESET_ALL}")
            except IndexError:
                print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}Syntax:{Style.RESET_ALL} {Fore.GREEN}hive show <HIVE>{Style.RESET_ALL}")
        elif args[0] == 'delete':
            try:
                del self.db[args[1]]
            except IndexError:
                print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}Syntax:{Style.RESET_ALL} {Fore.GREEN}hive delete <HIVE>{Style.RESET_ALL}")
        else:
            print(self.command_hive_helptext)
    def __command_help(self, args: list) -> None:
        print(f"""{Fore.GREEN}hive: Change hive data.
print: Print text to the console.
clear: Clear the console, may not work in al OSes.
Get-File: Get file content.
help, ?: Show this help text.
exit: Exit NNSH.{Style.RESET_ALL}""")
    def run(self) -> None:
        """
        Run NNSH
        """
        while True:
            try:
                command = str(input(f"{Fore.CYAN}DataBase{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.CYAN}{self.dbname}{Style.RESET_ALL} {Fore.LIGHTBLACK_EX}>{Style.RESET_ALL} {Fore.GREEN}"))
            except KeyboardInterrupt:
                print()
                sys.exit()
            finally:
                print(Style.RESET_ALL, end="")
            commands = {
                "exit": "!!BREAKLOOP!!",
                "help": self.__command_help,
                "?": self.__command_help,
                "hive": self.__command_hive,
                "clear": self.__command_clear,
                "print": self.__command_print,
                "Get-File": self.__command_getfile
            }
            parts = command.split()
            if parts:
                basecmd = parts[0]
                args = parts[1:]
                if basecmd in commands:
                    if commands[basecmd] == '!!BREAKLOOP!!':
                        break
                    else:
                        commands[basecmd](args)
                else:
                    print(f"{Fore.RED}[!]{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}{basecmd}{Style.RESET_ALL}{Fore.LIGHTBLACK_EX}:{Style.RESET_ALL} {Fore.BLUE}DataBase command not found.{Style.RESET_ALL}")
            else:
                continue
        self.connecteddb.data = self.db
if __name__ == "__main__":
    raise DataBaseError("Run DataBase as a module.")
  
