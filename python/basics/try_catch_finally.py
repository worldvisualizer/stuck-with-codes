
def raise_exception():
    raise


if __name__ == '__main__':
    try:
        x = 2
        raise_exception()
        print(x)
    except Exception as e:
        print('exception')
    finally:
        print(x)
