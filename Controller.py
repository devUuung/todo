import Model
import View

def controller(num):
    if num == 1:
        if Model.create(View.print_question()):
            return True
        else:
            return False
    if num == 2:
        if Model.delete(View.print_question()):
            return True
        else:
            return False
    if num == 0:
        return False