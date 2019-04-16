# General Python utility functions

import inspect
import csv



def MSG(body):
  # print a message, preceded by the calling function's file and line number
  try:
    stack = inspect.stack()
    frame = stack[1]

    # filename: only show the last part
    fn = frame[1]
    slash = fn.rfind('/')
    if slash != -1:
      fn = fn[slash + 1 :]

    print("{}:{} {}".format(fn, frame[2], body))

  except Exception as e:
    print("Exception encountered in MSG(): {}".format(e))
    print(body)



def TODO(body = ''):
  # print a really big 'TODO' message
  try:
    stack = inspect.stack()
    frame = stack[1]

    # filename: only show the last part
    fn = frame[1]
    slash = fn.rfind('/')
    if slash != -1:
      fn = fn[slash + 1 :]

      print("\n!!!!!!!!!!!!!!!!!!!!!!!!!! TODO: {}:{}:{}(): {}\n".\
            format(fn, frame[2], frame[3], body))

  except Exception as e:
    print("Exception encountered in TODO(): {}".format(e))
    print(body)



def read_csv_file_to_list_of_dicts(filename, delimiter = ','):
    '''
    Read csv file filename, and return it as a list of dicts

    The first row becomes the keys for each other row
    '''

    headers = []
    thelist = []

    with open(filename, 'r') as csvfile:

        reader = csv.reader(csvfile, delimiter = delimiter)

        for row in reader:

            # first row defines the headers
            if len(headers) == 0:
                headers = row
                #MSG('headers: {}\n'.format(headers))
                continue

            # other lines are items for the dictionary
            single_row_list = row
            if len(headers) != len(single_row_list):
                MSG("Bad line: {}".format(single_row_list))
                raise Exception("ERROR: length of headers ({}) must be the same as "
                                "the length of each rowdict ({})!"
                                .format(len(headers), len(single_row_list)))

            # create a new dict for this rowdict
            rowdict = {}
            for i in range(len(headers)):
                rowdict[headers[i]] = single_row_list[i]
            #MSG('rowdict: {}\n'.format(rowdict))

            # add it to the list
            thelist.append(rowdict)

    return thelist
