import json

def is_digit(item):
    try:
        float(item)
        i = 1
    except ValueError:
        i = 0
    return i


def predict(mileage):
    with open('coefs.json', 'r') as file:
        dict_t = json.load(file)
        t0 = dict_t.get('t0', 0)
        t1 = dict_t.get('t1', 0)
        price = t0 + t1 * mileage
        if price < 0:
            price = 0
        return round(price, 2)


if __name__ == "__main__":
    try:
        print('Please enter a mileage:')
        mileage = input()
        if is_digit(mileage):
            mileage = float(mileage)
            if mileage < 0:
                print('A mileage should be positive')
                exit()
            price = predict(mileage)
            if price - int(price) == 0:
                price = int(price)
            print("This car worths", price)
        else:
            print('Mileage should be a digit')
    except Exception as exp:
        print('Something went wrong: ', exp)
