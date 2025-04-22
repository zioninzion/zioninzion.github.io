from convert_books import rcv_to_sub as replacements

def replace_keys_with_values_in_file(filename, replacements, output_filename=None):
    # Read the original file
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Apply replacements
    for key, value in replacements.items():
        text = text.replace(key, value)

    # Output result
    if output_filename:
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(text)
    else:
        print(text)

replace_keys_with_values_in_file('NT175Days.xml', replacements, 'output.txt')

