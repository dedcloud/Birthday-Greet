while True:
    print("="*30)
    nums = ""
    inp = 0
    while True: 
        inp = input(">>").strip()

        if inp=="q":break
        if inp=="":
            op = input("[+-*/%]:")
            break
        if not(inp.isdigit()):
            print("[!]Invalid Number")
            continue

        nums += inp+" "

    if op=="":
        print("[!]No Operator Selected")
        continue

    op = op[0]
    if op not in "+-*/%":
        print("[!]Invalid Operator")
        continue


    exec("print('==>',"+nums.rstrip().replace(' ',op)+")")

    
