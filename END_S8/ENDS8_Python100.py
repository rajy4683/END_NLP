
# Write a python function to derive slope given 2 points (x1,y1) and (x2, y2)
def get_slope(x1,y1, x2,y2):
    if (x1 == x2 ):
        return ValueError
    return -((y2-y1)/(x2-x1))


# Write a python function to rotate a point (x,y) around a given origix (ox,oy) by an angle
def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    radian_angle = math.radians(angle)
    qx = ox + math.cos(radian_angle) * (px - ox) - math.sin(radian_angle) * (py - oy)
    qy = oy + math.sin(radian_angle) * (px - ox) + math.cos(radian_angle) * (py - oy)
    return qx, qy


# Write a python function to copy the sign bit from one variable to another
def copysign(dst, src) :
    return math.copysign(dst, src)

# Write a python function Split a given file path into filename and parent directory
def split_filename(input_file_name):
    if( isinstance(input_file_name,str) ==False ):
        raise TypeError
    tokens = input_file_name.split("/")
    return "/".join(tokens[:-1]),tokens[-1]

# Write a python function to join directory names to create a path
def join_filename(base_dir, *args):
    file_path_args = [base_dir ,*args]
    for file_name in file_path_args:
        if( isinstance(file_name,str) ==False ):
            raise TypeError
    return "/".join(file_path_args)

# Write a python function to find linear interpolation between two points x and y given a variable t
def linear_interpolate(x, y, t ):
    if( t >=1 or t <= 0):
        raise ValueError
    return t*x + (1-t)*y

# Write a python function to find bilinear interpolation of a point x, y given 4 points represented as a list
def bilinear_interpolation(x, y, points):
    points = sorted(points)               # order points by x, then by y
    (x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

    if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
        raise ValueError('points do not form a rectangle')
    if not x1 <= x <= x2 or not y1 <= y <= y2:
        raise ValueError('(x, y) not within the rectangle')

    return (q11 * (x2 - x) * (y2 - y) +
            q21 * (x - x1) * (y2 - y) +
            q12 * (x2 - x) * (y - y1) +
            q22 * (x - x1) * (y - y1)
           ) / ((x2 - x1) * (y2 - y1) + 0.0) 

# Write a python function to raise error when an input is not a string type
def check_string(new_str):
    return isinstance(new_str,str)

## Write a python function to extract only alphabets from a given string and also exclude spaces
def extract_alpha(my_string):
    return "".join([ c for c in my_string if c.isalpha()])

# Write a python function to extract only alphabets from a given string and also include spaces
def extract_alpha(my_string):
    return "".join([ c for c in my_string if (c.isalpha() or c.isspace())])

# Write a python function to remove all non-alphabets except space from a given string using re library
import re
def extract_not_alpha(my_string):
    #result = re.findall(r'[^a-zA-Z]+',my_string)
    return re.sub('[^a-zA-Z\s]+', "", my_string)
    #return "".join(result)

# Write a python function to remove all digits and underscores from a Unicode strings
import re
def extract_unicode(my_string):
    regex = re.compile(r'[^\W\d_]+', re.UNICODE)    
    return regex.findall(my_string)

# Write a python function to find all email-id patterns in a given string and write to a user input file
import re
def extract_mailid(my_string, outfile):
    regex = re.compile(r'[\w]+@[\w]+\.[\w]+', re.UNICODE)    
    mailids = regex.findall(my_string)
    if(len(mailids) > 0):
        with open(outfile, 'w') as mailfile:
            for mailid in mailids:
                mailfile.write(mailid+"\n")
        mailfile.close()

# Write a python function to generate a random hexadecimal key of length n
import random
def rand_run_name(n):
    ran = random.randrange(10**80)
    myhex = "%064x" % ran
    #limit string to 64 characters
    myhex = myhex[:n]
    return myhex

# Write a python function to create an argument parser that takes inputs as program name and description of program and filename as inputs for variable length of args
import argparse
def create_parser(prog_name, prog_description, arg_name):
    parser = argparse.ArgumentParser(prog = prog_name, description = prog_description)
    parser.add_argument(arg_name, nargs='+')
    #args = parser.parse_args()
    return parser

# Write a python function check if a given directory exists and has any files
import os
def check_dir_files(src_dir_path):
    if(os.path.exists(src_dir_path) == False):
        print("Destination Path doesn't exist")
        return False
    files_in_dir = glob.glob(src_dir_path+"/*.*")
    if (len(files_in_dir) <= 0):
        print("No files present in:",src_dir_path)
        return False
    print("The directory ", src_dir_path, " has ",len(files_in_dir), " files.")
    return True

# Write a python function to get user specified attributes such as day, month, year from a date
import datetime
def get_attributes_from_date(date_string,*args):
    if(isinstance(date_string, datetime.datetime) == False):
        print("Input string is not a valid datetime type")
        raise TypeError
    get_attrs = [ i for i in dir(date_string) if not callable(i) ]
    arg_list = []
    for attr in args:
        if(attr not in get_attrs):
            print("Invalid argument passed",attr)
            raise AttributeError
        print(attr, ':', getattr(date_string, attr))
        arg_list.append((attr,getattr(date_string, attr)))
    return arg_list

# Write a python function to find all files with a given pattern in a source directory to a different destination directory
import glob
import os
def find_move_files(src_dir_path, dst_dir_path, file_pattern):
    if(os.path.exists(dst_dir_path) == False):
        print("Destination Path doesn't exist")
        return
    all_png_files = glob.glob(src_dir_path+"/*"+file_pattern)
    if (len(all_png_files) > 0):
        for file_name in all_png_files:
            base_file_name=os.path.basename(file_name)
            os.replace(file_name, os.path.join(dst_dir_path, base_file_name))
        return 
    else:
        print("No files with matching pattern found")
        return

# Write a python function to select a random number of files from a given path of a given pattern
import glob
import os
import random
def retrieve_random_file(src_dir_path, file_pattern, count):
    if(os.path.exists(src_dir_path) == False):
        print("Destination Path doesn't exist")
        return
    
    files_in_dir = glob.glob(src_dir_path+"/*"+file_pattern)
    if (count > len(files_in_dir)):
        print("Requested count more than file count in:",src_dir_path," for pattern:",file_pattern)
        return
    return random.sample(files_in_dir, count)

# Write a python function to return the content of a directory and the last modified date
import glob
import os
import time
def retrieve_files_bydate(src_dir_path,*args):
    if(os.path.exists(src_dir_path) == False):
        print("Destination Path doesn't exist")
        return
    files_in_dir = glob.glob(src_dir_path+"/*.*")
    if (len(files_in_dir) <= 0):
        print("No files present in:",src_dir_path)
        return
    file_date_list = [ (filename, time.ctime(os.path.getmtime(filename)))for filename in files_in_dir]
    return file_date_list

# Write a python function to return the content of a directory sorted by last modified date
import glob
import os
import datetime
def retrieve_files_sort_bydate(src_dir_path):
    if(os.path.exists(src_dir_path) == False):
        print("Destination Path doesn't exist")
        return
    files_in_dir = glob.glob(src_dir_path+"/*.*")
    if (len(files_in_dir) <= 0):
        print("No files present in:",src_dir_path)
        return
    files_in_dir.sort(key=os.path.getmtime)    
    return files_in_dir

# Write a python function to select files from a directory that have been modified in last x hours given by the user
import glob
import os
import random
import datetime
def retrieve_last_files(src_dir_path, last_modified_hour):
    if(os.path.exists(src_dir_path) == False):
        print("Destination Path doesn't exist")
        return
    if( last_modified_hour <0 or last_modified_hour>24):
        print("Invalid delta requested")
        raise ValueError
    
    files_in_dir = glob.glob(src_dir_path+"/*.*")
    if (len(files_in_dir) <= 0):
        print("No files present in:",src_dir_path)
        return
    return [ filename for filename in files_in_dir if (datetime.datetime.fromtimestamp(os.path.getmtime(filename)) < datetime.datetime.now() + datetime.timedelta(hours=last_modified_hour)) ]


# Write a python function to print the size of all the files in a directory only at topmost level
import os
def get_filesize_for_dir(src_dir_path):
    if(os.path.exists(src_dir_path) == False):
        print("Destination Path doesn't exist")
        return
    files_in_dir = glob.glob(src_dir_path+"/*.*")
    if (len(files_in_dir) <= 0):
        print("No files present in:",src_dir_path)
        return
    total_size = 0
    for filename in files_in_dir:
        #(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
        total_size += os.stat(filename)[6]
    return total_size

# Write a python function to read a user specified csv file and a delimiter and return the number of rows and number of columns in the first row.
import csv
def read_csv_length(csv_file_name, delimiter_pattern):
    if(os.path.exists(csv_file_name) == False):
        print("Destination File doesn't exist")
        return
    with open(csv_file_name, newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=delimiter_pattern)
        csv_list = list(csv_reader)
        return len(csv_list), len(csv_list[0])

# Write a python function to convert a list of strings to equivalent character array using itertools
import itertools
def extract_characters(input_list):
    return [ char_val for char_val in itertools.chain.from_iterable(input_list) ]

# Write a python function to generate a random combination from user provided list and user specified length.
import itertools
def get_random_combination(input_list, combination_length):
    if(len(input_list) < combination_length):
        print("Requested combination length less than length of list")
        return
    combination_list = list(itertools.combinations(input_list, combination_length))
    return random.sample(combination_list, 1)

# Write a python function to generate amortization schedule given initial loan amount, interest rate, annual payments and tenure.
import itertools
def loan_schedule(principal, interest_rate, annual_payment, tenure):
    if(tenure <= 0):
        print("Invalid tenure",tenure)
        raise ValueError
    if(interest_rate > 1 or interest_rate < 0):
        print("Invalid interest rate",interest_rate," Expected between 0 and 1")
        raise ValueError
    cashflows = [principal, *list(itertools.repeat(-annual_payment, tenure))]
    effective_interest_rate = 1+interest_rate
    return [ val for val in list(itertools.accumulate(cashflows, lambda bal, pmt: (bal*effective_interest_rate + pmt))) if val > 0]

# Write a python function to generate amortization schedule given initial loan amount, interest rate, annual payments and tenure.
import itertools
def loan_schedule(principal, interest_rate, annual_payment, tenure):
    if(tenure <= 0):
        print("Invalid tenure",tenure)
        raise ValueError
    if(interest_rate > 1 or interest_rate < 0):
        print("Invalid interest rate",interest_rate," Expected between 0 and 1")
        raise ValueError
    cashflows = [principal, *list(itertools.repeat(-annual_payment, tenure))]
    effective_interest_rate = 1+interest_rate
    return [ val for val in list(itertools.accumulate(cashflows, lambda bal, pmt: (bal*effective_interest_rate + pmt))) if val > 0]

# Write a python function to accept user defined file, user-defined loglevel and create a file-based and invoke the user-defined function with this logger.
import logging
def create_logging_level(user_func, user_filename, user_loglevel):
    logger = logging.getLogger('simple_example')
    logger.setLevel(user_loglevel)
    ch = logging.FileHandler(user_filename)
    ch.setLevel(user_loglevel)
    logger.addHandler(ch)

    if callable(user_func):
        user_func(logger)


# Write a python function to simulate an exception and log the error using logger provided by the user.
def exception_simulator(logger):
    try:
        raise ValueError
    except ValueError:
        logger.exception("ValueError occured in the function")

# Write a python function to call a user-input function with default exception handling and re-raise the exception again.
def default_exception_simulator(user_func):
    try:
        if callable(user_func):
            user_func()
    except:
        print("An exception occured")
        raise