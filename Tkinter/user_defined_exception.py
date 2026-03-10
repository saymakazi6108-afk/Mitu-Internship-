class FailStudentError(Exception):
    pass

try:
    mark = int(input("Enter your marks : "))
    if mark < 40 :
        raise FailStudentError("unfortunately, you are fail...")
    else:
        print("congratulation !! you are pass")
except FailStudentError as e :
    print(e)
finally:
    print("BEST OF THE LUCK FOR NEXT JOURNEY")