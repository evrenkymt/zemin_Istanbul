print("Skyrim evrenine hoş geldiniz.")
print("Karakter yaratmak için girmeniz gerekenler: ırk(str), sınıf(str), isim(str), cinsiyet(str), yas(int)")

class karakter():
  def __init__(self,irk,sinif,isim,cinsiyet,yas):
    self.irk = irk
    self.sinif = sinif
    self.isim = isim
    self.cinsiyet = cinsiyet
    self.yas = yas
    self.karakterler = []
  def kayit(self,yeni_karakter):
    print("Oluşturulan karakter kaydedildi.")
    self.karakterler.append(yeni_karakter)
  def showKarakterler(self):
    for i in self.karakterler:
      print(i.isim)
irklar = ["insan", "elf" , "yaratık"]
insan_siniflari = ["nord", "imperial", "breton", "redguard"]
elf_siniflari = ["high elf","wood elf","dark elf","orc"]
yaratik_siniflari = ["argonian", "khajit"]

i = 1
while i > 0:
  irk = input("Oluşturmak istediğiniz ırk nedir ? (Mevcut ırklar : insan , elf , yaratık)")
  if irk in irklar :
    print(irk + " ırkınız seçtiniz. ") 
    print("Hangi sınıf oluşturmak istiyorsunuz ? (Mevcut sınıflar : İnsan için nord, imperial, breton, redguard || Elf için high elf, wood elf, dark elf, orc || Yaratık için argonian, khajit )")
    sinif = input("")
    if irk == "insan" :
        if sinif in insan_siniflari:
          print(irk +" ırkında "+ sinif + "  sınıfı mevcut." )

        else:
          print("insan ırkında böyle bir sınıf yok")
    if irk == "elf":
        if sinif in elf_siniflari:
          print(irk +" ırkında "+ sinif + "  sınıfı mevcut." )
        else:
          print("elf ırkında böyle bir sınıf yok")
    if irk == "yaratık":
        if sinif in yaratik_siniflari:
          print(irk +" ırkında "+ sinif + "  sınıfı mevcut." )
        else:
          print("yaratık ırkında böyle bir sınıf yok")
    print("karakterinizin ismi:")
    isim = input("")
    print("cinsiyeti:")
    cinsiyet = input("")
    print("yaşı:")
    yas = input()
    yeni_karakter = karakter(irk,sinif,isim,cinsiyet,yas)
    yeni_karakter.kayit(yeni_karakter)

  else:
    print("oluşturmak istediğiniz irk bulunmamaktadır lütfen 3 seçenekten birini seçiniz. insan - elf - yaratık")
  
  print("Karakter oluşturmaya devam etmek istiyor musunuz ? ( evet için y hayır için n giriniz)")
  cevap = input("")
  if cevap == 'n' :
    i = 0
    print("Karakter/ karakterler başarıyla oluşturuldu.")

yeni_karakter.showKarakterler()