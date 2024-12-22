import datetime
import csv
import calendar

# Fungsi untuk menghasilkan jadwal setiap X minggu dari tanggal awal
def generate_weekly_schedule(start_date, num_weeks, holidays):
    schedule = []
    current_date = start_date

    for i in range(num_weeks):
        # Cek apakah tanggal ini jatuh pada libur
        while current_date.strftime("%d-%m-%Y") in holidays:
            # Jika jatuh pada libur, tambahkan 1 minggu dan coba lagi
            current_date += datetime.timedelta(weeks=1)
        
        # Mendapatkan nama hari dalam bahasa Inggris
        day_name = calendar.day_name[current_date.weekday()]
        formatted_date = f"{day_name}, {current_date.strftime('%d-%m-%Y')}"
        schedule.append(formatted_date)
        current_date += datetime.timedelta(weeks=1)  # Lanjutkan ke minggu berikutnya
    
    return schedule

# Fungsi untuk menghasilkan jadwal setiap hari tertentu (misalnya Senin, Kamis)
def generate_specific_day_schedule(start_date, num_weeks, holidays, target_weekday):
    schedule = []
    
    # Menyesuaikan agar tanggal awal adalah hari yang diinginkan
    days_ahead = (target_weekday - start_date.weekday()) % 7
    current_date = start_date + datetime.timedelta(days=days_ahead)

    for i in range(num_weeks):
        # Cek apakah tanggal ini jatuh pada libur
        while current_date.strftime("%d-%m-%Y") in holidays:
            # Jika jatuh pada libur, tambahkan 1 minggu dan coba lagi
            current_date += datetime.timedelta(weeks=1)
        
        # Mendapatkan nama hari dalam bahasa Inggris
        day_name = calendar.day_name[current_date.weekday()]
        formatted_date = f"{day_name}, {current_date.strftime('%d-%m-%Y')}"
        schedule.append(formatted_date)
        current_date += datetime.timedelta(weeks=1)  # Lanjutkan ke minggu berikutnya
    
    return schedule

# Fungsi untuk menyimpan jadwal ke dalam file CSV
def save_schedule_to_csv(schedule, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Tanggal Jadwal"])  # Menulis header CSV
        for date in schedule:
            writer.writerow([date])  # Menulis setiap tanggal dalam jadwal

# Fungsi untuk memilih hari yang diinginkan (Senin, Selasa, dll.)
def get_weekday_choice():
    print("Pilih hari tertentu untuk jadwal:")
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, day in enumerate(weekdays):
        print(f"{i + 1}. {day}")
    
    choice = int(input("Masukkan pilihan (1-7): "))
    if 1 <= choice <= 7:
        return choice - 1  # Mengembalikan angka yang sesuai dengan weekday
    else:
        print("Pilihan tidak valid")
        return None

def main():
    # Input pengguna untuk tanggal mulai dan jumlah minggu
    start_date_input = input("Masukkan tanggal mulai (format DD-MM-YYYY): ")
    start_date = datetime.datetime.strptime(start_date_input, "%d-%m-%Y")
    num_weeks = int(input("Masukkan jumlah minggu ke depan: "))
    
    # Input pengguna untuk tanggal libur
    holidays_input = input("Masukkan tanggal libur (format DD-MM-YYYY, pisahkan dengan koma jika lebih dari satu): ")
    holidays = {date.strip() for date in holidays_input.split(",")}

    # Pilihan jenis jadwal
    print("\nPilih jenis jadwal:")
    print("1. Setiap 1 minggu sekali")
    print("2. Setiap hari tertentu (Monday, Tuesday, Wednesday, dll.)")
    choice = input("Masukkan pilihan (1 atau 2): ")
    
    if choice == "1":
        schedule = generate_weekly_schedule(start_date, num_weeks, holidays)
        filename = "weekly_schedule.csv"
        print(f"\nJadwal setiap minggu disimpan dalam {filename}")
        save_schedule_to_csv(schedule, filename)
    
    elif choice == "2":
        target_weekday = get_weekday_choice()
        if target_weekday is not None:
            schedule = generate_specific_day_schedule(start_date, num_weeks, holidays, target_weekday)
            filename = f"schedule_{calendar.day_name[target_weekday].lower()}.csv"
            print(f"\nJadwal setiap hari {calendar.day_name[target_weekday]} disimpan dalam {filename}")
            save_schedule_to_csv(schedule, filename)
    
    else:
        print("Pilihan tidak valid")

# Menjalankan program
if __name__ == "__main__":
    main()
