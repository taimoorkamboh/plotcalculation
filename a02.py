### YOUR CODE FOR calculateArea() FUNCTION GOES HERE ###
def calculateArea(plot_width, plot_length):
    area = plot_width * plot_length
    return area

#### End OF MARKER



### YOUR CODE FOR checkTilesFit() FUNCTION GOES HERE ###
def checkTilesFit(plot_width, plot_length, tile_width, tile_length):
    tiles_area = tile_width * tile_length
    
    if plot_width < 0 or plot_length <0 or tile_length <0 or tile_width<0:
        return False
    if calculateArea(plot_width, plot_length) >= tiles_area:
        if  calculateArea(plot_width, plot_length) % tiles_area == 0:
                return True
        else:
            return False

#### End OF MARKER



### YOUR CODE FOR calculateTiles() FUNCTION GOES HERE ###
def calculateTiles(plot_width, plot_length, tile_width, tile_length):
    
    if type(plot_width) == str or type(plot_length) == str or type(tile_width) == str or type(tile_length) == str:
        return "Invalid Input"
    
    if (plot_width) == 0 or (plot_length) == 0 or (tile_width) == 0 or (tile_length) == 0:
        return None
    
    if checkTilesFit(plot_width, plot_length, tile_width, tile_length) == True:
        return calculateArea(plot_width, plot_length) // (tile_width * tile_length)
    else:
        return "Not Possible"
        

#### End OF MARKER
