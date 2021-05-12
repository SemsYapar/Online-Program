#Şahzı muhterem Sems tarafından bizzat kodlanmıştır, /comprehension pornosu/

from openpyxl import load_workbook
import time
import webbrowser

print("excel olarak kaydettiğiniz programın adını yazın.")
name_excel = input()
print("Derse kasıtlı geç girme süresi kaç saniye olsun?(Dersi geç açan hocalar için tavsiye edilir)")
wait_time_count = input()

wb = load_workbook(name_excel)
ws = wb.active

today = time.strftime("%A")

days_and_rows = {"Monday":1,"Tuesday":3,"Wednesday":5,"Thursday":7,"Friday":9,"Saturday":11,"Sunday":13}
time_row_num = days_and_rows[today]
lesson_row_num = time_row_num + 1

with open("ders_link.txt", "r", encoding="utf-8") as f:
	it = iter(f.readlines())
	lessons_and_links = {x.rstrip("\n"):next(it).rstrip("\n") for x in it}

time_row = [ws.cell(time_row_num, i).value for i in range(2, ws.max_column + 1)]
if time_row.count(None) == len(time_row):
	print("Bugünlük dersiniz yok.")
	input()
	exit()
lesson_row = [ws.cell(lesson_row_num, i).value for i in range(2, ws.max_column + 1)]

for index, lesson_time in enumerate(time_row):
	time_now = time.strftime("%H:%M")
	try:
		if lesson_time == None:
			raise AttributeError("Bugüne ait tanımlamadığınız ders yada dersler var, bu kabul edilemez arada boş derscik bırakmadan dersleri yazdığınızdan emin olun.\nBu hata bazende excel dosyanızdaki bugünün olduğu satırda yanlışlıkla doldurup sonra sildiğinizi sandığınız bir ders yüzünden olabilir, emin olmak için boş gözüken o yerin ait olduğu column a sağ tık->sil diyin.")
		if str(type(lesson_time)) !=  "<class 'datetime.time'>":
			raise AttributeError(f"Saat yazmanız gereken yere '{type(lesson_time)}' türünden bir değer girdiğinizi tespit ettik. Nütfen kontrol edin")
		else:
			lesson_time = lesson_time.strftime("%H:%M")
		if time_now <= lesson_time:
			lesson_next = lesson_row[index]
			print(f"Sıradaki ders {lesson_next}, başlangıç saati {lesson_time}")
			while True:
				if time.strftime("%H:%M") == lesson_time:
					if lesson_next not in lessons_and_links:# bu dözgün çalışmıyor
						raise KeyError(f"Sıradaki ders '{lesson_next}', ders_link.txt'ye kayıtlı değil")
					if(lessons_and_links[lesson_next].lower() == "empty"):
						print(f"'{lesson_next}' dersini 'boş' olarak işaretlediğinizden dolayı ders pas geçildi.")
						break
					print("lol")
					print(f"Kasıtlı bekleme süresi başlatılıyor ->{wait_time_count} saniye")
					time.sleep(int(wait_time_count))
					print(f"{lesson_next} dersine giriş yapılıyor...")
					webbrowser.open_new_tab(lessons_and_links[lesson_next])
					time.sleep(60)
					break
				time.sleep(10)
	except AttributeError as e: 
		print(e)
		exit()
	except KeyError as e:
		print(e)
		exit()
print("Bugünlük dersler bitti.")
