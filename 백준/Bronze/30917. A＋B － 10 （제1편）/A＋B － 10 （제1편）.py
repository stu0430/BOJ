for a in range(1, 10):
    print(f'? A {a}', flush=True)

    response = int(input())

    if response == 1:
        for b in range(1, 10):
            print(f'? B {b}', flush=True)
            
            response = int(input())
            
            if response == 1:
                print(f'! {a + b}')
                break
        break