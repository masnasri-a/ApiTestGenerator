import srsly
from util import folder_creator


class Core:
    """
    Base Logic Engine
    """

    def __init__(self, path_file: str, base_dir: str) -> None:
        """_summary_

        Args:
            path_file (str): _description_
        """
        self.path = path_file
        self.base_dir = base_dir

    def __extractor(self):
        """
        Extract a jsonfile from path
        """
        json_file = srsly.read_json(self.path)
        self.json_file = json_file

    def __get_variable(self):
        """
        Getting Variable data from json file
        """
        self.variable = {}
        if 'variable' in self.json_file:
            varibles = [(item) for item in self.json_file['variable']
                        if 'disabled' not in item]
            self.variable = {item['key']: item['value'] for item in varibles}

    def __item_search(self, data):
        result = []
        if isinstance(data, dict):
            if "request" in data:
                result.append(data)
            for _, value in data.items():
                if isinstance(value, (dict, list)):
                    result.extend(self.__item_search(value))
        elif isinstance(data, list):
            for item in data:
                result.extend(self.__item_search(item))
        return result

    def __create_test_by_name(self):
        self.flat_item = self.__item_search(self.json_file.get('item'))
        for item in self.flat_item:
            name = item['name'][1:] if item['name'][0] == "/" else item['name']
            paths = '/'.join(name.split("/")[:-1])
            folder_creator(self.base_dir+"/"+paths)
        print("-"*100,"\nApi Testing Foldering has been created 😄")

    def run(self):
        self.__extractor()
        self.__get_variable()
        self.__create_test_by_name()
