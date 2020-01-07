class Vehicle:

    def __init__(self, starting_top_speed=100):
        self.top_speed = starting_top_speed
        self.__warnings = []

    def add_warnings(self, warning_text):
        self.__warnings.append(warning_text)

    def get_warnings(self):
        return self.__warnings

    def __repr__(self):
        print('Printing ...')
        return 'top_speed: {}, warning: {}'.format(self.top_speed, len(self.__warnings))

    def drive(self):
        print('I am driving but certainly not faster than {}'.format(self.top_speed))
