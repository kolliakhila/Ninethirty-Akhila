def safe_file(filename):
    try:
        with open(filename,'r')as file:
            content=file.read()
    except FileNotFoundError:
        print("The file was not found")
    except Exception as e:
        print("Some other type of error was occurred")
    else:
        print("File was found successfully")
    finally:
        print("Finally file was there")
safe_file("Exception")