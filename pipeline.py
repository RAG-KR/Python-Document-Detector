# import os
# # 
# # Specify the directory paths
# input_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/input'
# output_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/outputtestpipeline'
# # 
# # Get a list of all files in the input directory
# file_list = os.listdir(input_directory)
# # 
# # Filter only the files with specific extensions (e.g., '.jpg')
# image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png'))]
# # 
# # Ensure the output directory exists, create if not
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)
# # 
# # Run the command for each image file
# for image_file in image_files:
#     input_path = os.path.join(input_directory, image_file)
#     output_path = os.path.join(output_directory, f'output_{image_file}')
#     print(f"Input path: {input_path}")
#     print(f"Output path: {output_path}")

#     command = f"python3 page_extractor.py -i '{input_path}'"
#     result = os.system(command)
#     print(f"Command result: {result}")

#     result = os.system(command)
#     print(f"Command result: {result}")


#     os.system(command)
# 

# #################################################################################################################3



# import os
# import time

# # Specify the directory paths
# input_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/input'
# output_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/outputtestpipeline'

# # Get a list of all files in the input directory
# file_list = os.listdir(input_directory)

# # Filter only the files with specific extensions (e.g., '.jpg')
# image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# # Ensure the output directory exists, create if not
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # Run the command for each image file
# for image_file in image_files:
#     input_path = os.path.join(input_directory, image_file)

#     # Append a timestamp to the output filename to avoid overwriting
#     timestamp = time.strftime("%Y%m%d%H%M%S")
#     output_filename = f'output_{image_file[:-4]}_{timestamp}.jpg'
#     output_path = os.path.join(output_directory, output_filename)

#     print(f"Input path: {input_path}")
#     print(f"Output path: {output_path}")

#     command = f"python3 page_extractor.py -i '{input_path}'"
#     result = os.system(command)
#     print(f"Command result: {result}")


##################################################################################3333


# import os
# import time

# # Specify the directory paths
# input_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/input'
# output_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/outputtestpipeline'

# # Get a list of all files in the input directory
# file_list = os.listdir(input_directory)

# # Filter only the files with specific extensions (e.g., '.jpg')
# image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# # Ensure the output directory exists, create if not
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # Run the command for each image file
# for image_file in image_files:
#     input_path = os.path.join(input_directory, image_file)

#     # Append a timestamp to the output filename to avoid overwriting
#     timestamp = time.strftime("%Y%m%d%H%M%S")
#     output_filename = f'output_{image_file[:-4]}_{timestamp}.jpg'
#     output_path = os.path.join(output_directory, output_filename)

#     print(f"Input path: {input_path}")
#     print(f"Output path: {output_path}")

#     # Run the page_extractor.py script without -o argument
#     os.system(f"python3 page_extractor.py -i '{input_path}'")

#     print(f"Processed: {output_path}")


##################################################3######################################3

# in cmd line things happen but op dir not updating

# import os
# import time

# # Specify the directory paths
# input_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/input'
# output_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Python-Document-Detector/outputtestpipeline'

# # Get a list of all files in the input directory
# file_list = os.listdir(input_directory)

# # Filter only the files with specific extensions (e.g., '.jpg')
# image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# # Ensure the output directory exists, create if not
# if not os.path.exists(output_directory):
#     os.makedirs(output_directory)

# # Run the command for each image file
# for image_file in image_files:
#     input_path = os.path.join(input_directory, image_file)

#     # Use the same filename for the output file to avoid overwriting
#     output_filename = f'{image_file[:-4]}_{time.strftime("%Y%m%d%H%M%S")}.jpg'
#     output_path = os.path.join(output_directory, output_filename)

#     print(f"Input path: {input_path}")
#     print(f"Output path: {output_path}")

#     # Run the page_extractor.py script without -o argument
#     os.system(f"python3 page_extractor.py -i '{input_path}'")

#     print(f"Processed: {output_path}")

#######################################################################################


import os
import time

# Specify the directory paths
input_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Document-Detector/input'
output_directory = '/media/raghav/New Volume/Python projects/internship task/Dx_test_files 1/Document-Detector/outputtestpipeline'

# Get a list of all files in the input directory
file_list = os.listdir(input_directory)

# Filter only the files with specific extensions (e.g., '.jpg')
image_files = [file for file in file_list if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

# Ensure the output directory exists, create if not
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Run the command for each image file
for image_file in image_files:
    input_path = os.path.join(input_directory, image_file)

    # Use the same filename for the output file to avoid overwriting
    output_filename = f'{image_file[:-4]}_{time.strftime("%Y%m%d%H%M%S")}.jpg'
    output_path = os.path.join(output_directory, output_filename)

    print(f"Input path: {input_path}")
    print(f"Output path: {output_path}")

    # Print the command before executing
    command = f"python3 page_extractor.py -i '{input_path}'"
    print(f"Command: {command}")

    # Run the page_extractor.py script without -o argument
    os.system(command)

    print(f"Processed: {output_path}")
