#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Harshita Singh, 2022-Dec-02, Changed File
#------------------------------------------#

import os
# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    
    cd_id = 0
    cd_title = ''
    cd_artist = ''
    
    def __init__(self, cd_id, cd_title, cd_artist):
        self.cd_id = str(cd_id)
        self.cd_title = str(cd_title)
        self.cd_artist = str(cd_artist)

    
    
    def contents(self):
        return [self.cd_id, self.cd_title, self.cd_artist]
    
    def display(self):
        return '{}\t{} (by:{})'.format(*self.contents()) 
    
    def __str__(self):
        return ','.join(self.contents())
    
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    
    @staticmethod
    def save_inventory(self, file_name, lst_Inventory):
         
        """Function to write data from a list of lists into a file

        Reads the data from 2D table (list of lists) row by row
        and write into the file

        Args:
            file_name (string): name of file used to write the data into
            table (list of list): 2D data structure (list of lists) that holds the data during runtime

        Returns:
            None.
        """

        with open(file_name, 'w') as f:
            for cds in lst_Inventory:
                f.write(str(cds) + '\n')
            f.close() 
                
    @staticmethod
    def load_inventory(self, file_name):
        """Function to manage data ingestion from file to a list of lists

        Reads the data from file identified by file_name into a 2D table
        (list of lists) table one line in the file represents one list row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of list): 2D data structure (list of lists) that holds the data during runtime

        Returns:
            None.
        """
        lstOfCDObjects.clear()
        
        # Check if file exists or not
        if os.path.exists(file_name): 
            with open(file_name, 'r') as f:
                for line in f.readlines():
                    data = line[:-1].split(',')
                    lstOfCDObjects.append(CD(data[0], data[1], data[2]))
   

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Handling Input / Output"""
    
    @staticmethod
    def print_menu(self):
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def menu_choice(self):
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice


    @staticmethod
    def show_inventory(self, table):
        """Displays current inventory table


        Args:
            table (list of lists): 2D data structure (list of lists) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in table:
            print(cd.display())
        print('======================================')
        
        
    @staticmethod
    def ask_user(self):
         """Asks user input for ID, CD Title and Artist
         

         Args:
             None

         Returns:
             user inputs(ID, Title and Artist Name).

         """
         
         CD_id = int(input('Enter ID: '))
         Title = input('What is the CD\'s title? ').strip()
         Artist = input('What is the Artist\'s name? ').strip()
         
         return CD_id, Title, Artist

# -- Main Body of Script -- #    
# Load data from file into a list of CD objects on script start
# Display menu to user
while True:
    IO.print_menu(IO)
    user_choice = IO.menu_choice(IO)
     
    if user_choice == 'l':
         print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
         strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled ')
         if strYesNo.lower() == 'yes':
             print('reloading...')
             FileIO.load_inventory(FileIO, strFileName)
             IO.show_inventory(IO, lstOfCDObjects)
         else:
             input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
             IO.show_inventory(lstOfCDObjects)
         continue  # start loop back at top.
         
    
    elif user_choice == 'a':
        cd_id, cd_title, cd_artist = IO.ask_user(IO)
        cd = CD(cd_id, cd_title, cd_artist)
        lstOfCDObjects.append(cd)
        continue # start loop back at top.
    
    elif user_choice == 'i':
        IO.show_inventory(IO, lstOfCDObjects)
        continue # start loop back at top.
    
    elif user_choice == 's':
        FileIO.save_inventory(FileIO, strFileName, lstOfCDObjects)
        continue # start loop back at top.
    
    elif user_choice == 'x':
        break
