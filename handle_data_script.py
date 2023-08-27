# TODO: Break program into smaller functions 
new_file_line_s = []

def read_data_from_file(tables):
  # make a function that finds complete strings in an array of strings
  # a complete string will have a '"' at the beginning to signify its start and a '"' at the end to specify its end.
  # return the complete string and the range of index(es) it occupies in the array
  def find_complete_string(given_arr):
    start = -1000
    for index, word in enumerate(given_arr):
      if word[0] == '"':
        start = index
      if word[-1] == '"':
        return ' '.join(given_arr[start:index+1])[1:-1], (start, index)
        
  
  # use a for loop to get all the data from the string array holding the name of all the txt files
  for table in tables:  
    
    # get data from file be opening file in read mode
    with open(table, "r") as file:
      new_file_line_s.append("--INSERT FROM " + table + "\n")
      # get and store all the lines in the file in an array
      lines = file.readlines()

      # get table name from the file
      # table name should be stored on  the first line of the file
      table_name = lines[0]

      # get total number of table column
      # number of table column should be stored on the second line of the file
      number_of_columns = int(lines[1])

      # TODO change if to try
      column_data_type = lines[2].split()
      if len(column_data_type) != number_of_columns:
          print("Column size of", table_name, "is wrong")
          print("Number of column data type(s) does not match")

      # TODO change if to try
      null_allowed = lines[3].split()
      if len(null_allowed) != number_of_columns:
          print("Column size of", table_name, "is wrong")
          print("Number of null(s) allowed does not match")

      # TODO change if to try
      column_name_s = lines[4].replace(' ', ',')
      if len(column_name_s.split(',')) != number_of_columns:
          print("Column size of", table_name, "is wrong")
          print("Number of column name(s) does not match")
      
      for line in lines[5:]:
        new_file_line_s.append("INSERT INTO " + table_name + "(" + str(column_name_s).strip() + ")\n")
        
        data = line.split()
        if len(data) != number_of_columns:
          temp_data = find_complete_string(data)
          data = data[:temp_data[1][0]] + [temp_data[0]] + data[temp_data[1][1] + 1:]
  
        new_data = []
        for value in range(len(data)):
          if data[value] == '-' and null_allowed[value] == 'Y':
            data[value] = 'NULL'
          elif data[value] == '-' and null_allowed[value] == 'N' and column_data_type[value] == 'C':
            data[value] = ' '
          
          if column_data_type[value] == 'C' and data[value] != 'NULL' and data[value][0] != "'":
            new_data.append("\'" + data[value] + "\'")
          else:
            new_data.append(data[value])
        new_file_line_s.append("VALUES (" + ",".join(new_data) + ");\n\n")

  return new_file_line_s