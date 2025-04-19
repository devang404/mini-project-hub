FILEPATH = r"C:\Users\Devang\Desktop\rock paper scissor\todo.txt"
def get_tdos(filepath=FILEPATH):
    with open(filepath, "r") as f:
        tdos_l=f.readlines()
    return tdos_l

def write_tdos(tdos_arg,filepath=FILEPATH):
    with open(filepath, "w") as f:
        f.writelines(tdos_arg)
if __name__=="__main__":
    print("Hello")
    print(get_tdos())