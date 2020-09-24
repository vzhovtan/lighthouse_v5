import yaml

with open('new_data_entry_format.yml', 'r') as file:
        data = yaml.load(file, Loader=yaml.FullLoader)
        print(data)
        # for key in data:
        #     valid_line_card.append(key)