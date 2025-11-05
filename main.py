from classes.studenta_nd_grade.student import Student,GradeCalculator
from classes.order_and_printing.order import Order,InvoicePrinter
if __name__ == "__main__":
    # s = Student("hagay",[1,2,3,4,5,6,7,8,9,10])
    # g  = GradeCalculator
    # g.average_grade(s)

    o = Order(["a","b","s"],5.5)
    i = InvoicePrinter()
    i.print_items(o)