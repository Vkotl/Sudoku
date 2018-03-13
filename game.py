class Spot:
    def __init__(self):
        self.value = list(range(1,10))
    def set_value(self, value):
        """Set the value of the spot"""
        self.value = [value]
    def disq_value(self, value):
        """ Remove the value from the options for this spot"""
        self.value.remove(value)
        if len(self.value) is 1:
            return True
        return False

    def __len__(self):
        return len(self.value)
    def __str__(self):
        return str(self.value[0])

class Square:
    def __init__(self):
        self.value = list(range(1,10))
        self.spots = [Spot() for _ in range(9)]
    def set_spot(self, dict):
        """Set the value in this spot-1 from the dictionary where the key is spot"""
        for spot in dict.keys():
            self.spots[spot-1].set_value(dict[spot])
            self.value.remove(dict[spot])
    def __getitem__(self, item):
        """Must exist in order to use indexing"""
        return self.spots[item]

    def __str__(self):
        string = ""
        for i in range(len(self.spots)):
            if len(self.spots[i]) is 1:
                string += str(self.spots[i])
            else:
                string += ""
            if (i+1)%3 is 0:
                string += "\n"
        return string

    def check_square(self):
        """Check if there are possibilities to fill a spot by checking the square."""
        for spot in self.spots:
            # Get each spot from the list of spots and for each that has only one value and that value is in the list
            # of values
            if len(spot.value) is 1 and spot.value[0] in self.value:
                self.value.remove(spot.value[0])
        for i in range(len(self.spots)):
            if len(self.spots[i].value) is 1:
                spot = self.spots[i]
                for j in range(len(self.spots)):
                    if j is not i:
                        if self.spots[i].value[0] in self.spots[j].value:
                            if self.spots[j].disq_value(self.spots[i].value[0]):
                                return True
        if len(self.value) is 1:
            for spot in self.spots:
                if len(spot.value) is not 1:
                    spot.set_value(self.value[0])
                    return True
        return False

    def check_end(self):
        for i in range(9):
            if not (len(self.spots[i].value) is 1):
                return True
        return False

    def validate(self):
        for i in range(9):
            for j in range(9):
                if self.spots[i].value[0] is self.spots[j].value[0] and i is not j:
                    return False
        return True
class Row:
    def __init__(self, index, squares):
        self.values = list(range(1,10))
        spots = []
        for square in squares:
            for spot in range((index%3)*3,(index%3)*3+3):
                spots.append(square[spot])

        self.spots = spots
    def check_row(self):
        if len(self.values) is 1:
            for spot in self.spots:
                if len(spot.value)> 1:
                    spot.value = [self.values[0]]
                    self.values = []
                    return True
        for spot in self.spots:
            if len(spot.value) is 1 and spot.value[0] in self.values:
                if spot.value[0] in self.values:
                    self.values.remove(spot.value[0])
                    for i in range(9):
                        if spot.value[0] in self.spots[i].value and not len(self.spots[i].value) is 1 and not spot is \
                            self.spots[i]:
                            if self.spots[i].disq_value(spot.value[0]):
                                return True
    def validate(self):
        for i in range(9):
            for j in range(9):
                if self.spots[i].value[0] is self.spots[j].value[0] and i is not j:
                    return False
        return True

class Column:
    def __init__(self, index, squares):
        self.values = list(range(1,10))
        spots = []
        for square in squares:
            for spot in range((index)%3,9,3):
                spots.append(square[spot])
        self.spots = spots
    def check_column(self):
        if len(self.values) is 1:
            for spot in self.spots:
                if len(spot.value)> 1:
                    spot.value = [self.values[0]]
                    self.values = []
                    return True
        for spot in self.spots:
            # If spot length is already determined and the value is in the column possiblities
            if len(spot.value) is 1:
                if spot.value[0] in self.values:
                    self.values.remove(spot.value[0])
                # Run through the column
                for i in range(9):
                    # If the value of spot is in the list of spots[i] and the length of spots[1] is not 1
                    if spot.value[0] in self.spots[i].value and not len(self.spots[i].value) is 1:
                        # If spot is not spots[i]
                        if spot is not self.spots[i]:
                            if self.spots[i].disq_value(spot.value[0]):
                                return True
    def validate(self):
        for i in range(9):
            for j in range(9):
                if self.spots[i].value[0] is self.spots[j].value[0] and i is not j:
                    return False
        return True

""" Board class beginning"""
class Board:
    def __init__(self):
        self.game = [Square() for _ in range(9)]

    #args will be built like the following: [square, spot, value]
    def add_values(self, data):
        for v in data.keys():
            if not data[v] is {}:
                self.game[v-1].set_spot(data[v])
        self.rows = [Row(i, self.game[i-i%3:i-i%3+3]) for i in range(9)]
        self.cols = [Column(i, self.game[i//3::3]) for i in range(9)]

    def __str__(self):
        string = ""
        string += self.string_line()
        for square in [0,3,6]:
            for i in range(3):
                string += self.string_square(i,square)
            string += self.string_line()
        return string

    def string_square(self, line, square):
        string = "|"
        line_dict = {0:2, 1:5, 2:8}
        for i in range(line*3,line_dict[line]+1):
            string += str(self.game[square][i] if len(self.game[square][i]) is 1 else "").center(3)
        string += "||"
        for i in range(line*3,line_dict[line]+1):
            string += str(self.game[square+1][i] if len(self.game[square+1][i]) is 1 else "").center(3)
        string += "||"
        for i in range(line*3,line_dict[line]+1):
            string += str(self.game[square+2][i] if len(self.game[square+2][i]) is 1 else "").center(3)
        string += "||\n"

        return string

    def string_line(self):
        string = ""
        for i in range(11):
            string += "___"
        string += "\n"
        return string

    def check(self):
        for i in range(9):
            if self.rows[i].check_row():
                print(self)
        for i in range(9):
            if self.cols[i].check_column():
                print(self)
        for i in range(9):
            if self.game[i].check_square():
                print(self)

    def check_end(self):
        for i in range(9):
            if self.game[i].check_end():
                return True
        return False

    def play(self):
        print("Starting phase")
        print(self)
        while self.check_end():
            self.check()
        print("Ending phase")
        print(self)
        print(self.validate())

    def validate(self):
        for i in range(9):
            if not self.game[i].validate():
                return "Not correct."
            if not self.rows[i].validate():
                return "Not correct."
            if not self.cols[i].validate():
                return "Not correct."
        return "Perfectly done."