import os


def remove_string_from_file(filepath, string_to_remove, string_to_add):
    # read the file
    with open(filepath, 'r') as file:
        filedata = file.read()

    # replace the string with the specified character
    newdata = filedata.replace(string_to_remove, string_to_add)

    # write the new data to the output file
    with open(f'{filepath}_fix.txt', 'w') as file:
        file.write(newdata)


if __name__ == '__main__':
    filepath = 'glass_inv_predictions.txt'
    string_to_remove = '\' \''
    string_to_add = '\', \''
    if os.path.isfile(filepath):
        remove_string_from_file(filepath, string_to_remove, string_to_add)
        print(f'Successfully removed {string_to_remove} from {filepath}.')
    else:
        print(f'{filepath} is not a valid file path.')
