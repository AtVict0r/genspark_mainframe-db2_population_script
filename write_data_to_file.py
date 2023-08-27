def send_to_file(file_line_s, file_name):
  print(*file_line_s)
  
  my_file = open(file_name, "w")
  
  for line in file_line_s:
  
    if len(line) <= 70:
      
      my_file.write(line)
    
    else:
      
      split_index = line[:71].rindex(',') + 1
      
      new_line = [line[:split_index] + "\n", 
                  line[split_index:]]
      
      my_file.writelines(new_line)
  
  my_file.close()