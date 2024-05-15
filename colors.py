class Colors:
    dark_grey = (26, 31, 40)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_blue = (44, 44, 127)
    light_blue = (59, 85, 162)
    pink = (255, 192, 203)
    deep_pink = (255, 20, 147)
    light_grey = (211, 211, 211)
    grey = (105, 105, 105)
    violet = (238,130,238)
    dark_violet = (148,0,211)


    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.light_grey, cls.white, cls.violet, cls.dark_violet, cls.purple, cls.cyan, cls.deep_pink]