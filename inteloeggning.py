import logging

logging.basicConfig(
    filename = 'app.log',
    filemode = 'w',
)

name = 'John'

logging.error(f'{name} raised an error')