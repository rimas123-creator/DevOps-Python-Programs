def update_env(input_key, input_value, file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()
    
    with open(file_path, "w") as file:
        for line in lines:
            if input_key in line:
                file.write(input_key + "=" + input_value + "\n")
                print(input_key + "=" + input_value)
            else:
                file.write(line)

key = "PORT"
value = "9005"
filepath = ".env-dummy"

update_env(key, value, filepath)