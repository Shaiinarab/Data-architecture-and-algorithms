from collections import deque

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = deque()

    def arrive(self, car_id):
        if len(self.queue) < self.capacity:
            self.queue.append(car_id)
            print(f"🚗 ماشین {car_id} وارد شد.")
        else:
            print(f"❌ پارکینگ پر است. ماشین {car_id} نمی‌تواند وارد شود.")

    def depart(self):
        if self.queue:
            car_id = self.queue.popleft()
            print(f"🚙 ماشین {car_id} خارج شد.")
        else:
            print("⚠️ پارکینگ خالی است.")

    def status(self):
        print("📊 وضعیت فعلی پارکینگ:")
        if self.queue:
            for i, car in enumerate(self.queue, start=1):
                print(f"{i}. ماشین {car}")
        else:
            print("هیچ ماشینی در پارکینگ نیست.")

def main():
    print("\n🚘 شبیه‌ساز صف پارکینگ")
    try:
        capacity = int(input("ظرفیت پارکینگ را وارد کنید: "))
    except ValueError:
        print("❌ مقدار نامعتبر. ظرفیت باید عدد صحیح باشد.")
        return

    parking = ParkingLot(capacity)

    while True:
        print("\nمنو:")
        print("1. ورود ماشین")
        print("2. خروج ماشین")
        print("3. نمایش وضعیت پارکینگ")
        print("4. خروج از برنامه")
        choice = input("انتخاب شما: ")

        if choice == "1":
            car_id = input("شماره ماشین را وارد کنید: ")
            parking.arrive(car_id)
        elif choice == "2":
            parking.depart()
        elif choice == "3":
            parking.status()
        elif choice == "4":
            print("👋 خروج از شبیه‌ساز پارکینگ.")
            break
        else:
            print("❌ گزینه نامعتبر. لطفاً دوباره تلاش کنید.")