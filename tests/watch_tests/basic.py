def main():
    ps = pyscriber.Scriber()
    x = 5
    ps.watch(x)
    x = 3
    y = "world"
    x = 7
    x += 1

if __name__=="__main__":
    main()
