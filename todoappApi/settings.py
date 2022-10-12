from configparser import ConfigParser
config = ConfigParser()
def write_to():
    global config # making config variable global

    config['postgres'] = {'host':'localhost',
                            'port':'5432',
                            'password': '55132',
                            'user':'postgres',
                            'dbname':'todo_app'
                                            } # registering the section postgress to config
    with open('db.ini', 'w') as configure_file:
        config.write(configure_file) # writing registered section into the file db.ini

def read_from(filename:str, section:str) -> dict:
    '''return information from the configuration file'''
    global config
    data = {}
    config.read(filename) # reading from the configuration filename using configparser
    
    for i in config.options(section): #looping throughj all the optipons in the desired section of the configuration file
        data[i] = config.get(section, i) # registering the file to data

    # config_item = config.items(section)
    # for item in config_item:
    #     data[item[0]] = item[1]
    # print(data)
    return data


