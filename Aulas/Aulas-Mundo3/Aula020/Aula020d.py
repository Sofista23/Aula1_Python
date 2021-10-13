def count(*x):
    for v in x:
        print(v)
    print("-="*20)
    print(len(x))
    print("-="*20)
    print(f"Recebi os valor {x} e ao todo são {len(x)}.")
count(1,5,4,8,9,1,5,4,6)