from PyPDF2 import PdfReader, PdfWriter
input_pdf = input("Enter the name of input pdf: ")
ouput_pdf = input("Enter the name of output pdf: ")
reader = PdfReader(input_pdf)
writer = PdfWriter()



def start_end():
    start = int(input("Enter the starting page :"))
    end = int(input("Enter the ending page: "))
   

    try:
        for i in range(start-1,end):
            writer.add_page(reader.pages[i])
    except Exception as IndexError:
        print(IndexError)


def manual_entering():
    print("Enter page numbers in the sequence . Press 'Q' when you are done")
    no_list = []
    while True:
        num = (input())
        if(num == "Q"):
            break
        no_list.append(int(num))
    try:
        for num in no_list:
            writer.add_page(reader.pages[num - 1])
    except Exception as IndexError:
        print(IndexError)



option = int(input("Enter '1' if you want to give the start and end page number or '2' to enter the page numbers manually"))
if(option == 1):
    start_end()
elif(option == 2):
    manual_entering()
else:
    print("Invalid option.")



# Write to pypdf-output.pdf.
with open(ouput_pdf+".pdf", "wb") as fp:
    writer.write(fp)
    


