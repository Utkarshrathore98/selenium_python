with open("demo_file.txt", "a") as fw:
    fw.write("\n I am appending this line using write method in python.")

with open("demo_file.txt", "r") as fr:
    print(fr.read())

