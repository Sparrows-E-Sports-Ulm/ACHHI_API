from pyhocon import ConfigFactory, ConfigTree
from dataclasses import dataclass, fields, is_dataclass

def dataclass_from_config_tree(ct: ConfigTree, data_class: dataclass): 
    args= [
        typed_value_from_config_tree(ct, field.type, field.name)
        for field in fields(data_class)
    ]

def typed_value_from_config_tree(hocon: ConfigTree, field_type: type, field_name: str):
    if field_type == str:
        return hocon.get_string(field_name)
    if field_type == int: 
        return hocon.get_int(field_name)
    if is_dataclass(field_type):
        sub_config = hocon.get_config(field_name)
        return dataclass_from_config_tree(sub_config, field_type)







@dataclass
class Database:
    host: str
    port: int 
    user: str
    password: str


@dataclass
class Config():
    database: Database
    def __init__(self, config_file=None):
        hocon = ConfigFactory.parse_file(config_file)

        for field_obj in fields(Config):
            field_name = field_obj.name
            field_type = field_obj.type

            if hocon.get(field_name, None) is not None: 
                try:
                    config_subtree = hocon.get_config(field_name)
                    setattr(
                        self,
                        field_name,
                        dataclass_from_config_tree(config_subtree, field_type)
                    )
                except Exception as e:
                    setattr(self, field_name, None)
                    raise ValueError(f"{field_name} not found")
            else: 
                setattr(self, field_name, None)