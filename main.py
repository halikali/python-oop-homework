import employee
import department
import engineer

muhendis_1 = engineer.Engineer()
muhendis_1.Name       = "Ali Tunç"
muhendis_1.Price      = 5800
muhendis_1.Adress     = "Vişnezade Mahallesi İstanbul/Beşiktaş"
muhendis_1.Department = department.Department("üretim", "250")
muhendis_1.Abilities  = ["PLC", "Python" , "S71200"]
muhendis_1.showProfile()

print("--------------------")

isci_1 = employee.Employee()
isci_1.Name       = "Muhammed Furkan Abasıkeleş"
isci_1.Adress     = "Tek Rampası Sakarya/Adapazarı"
isci_1.Department = department.Department("İK" , "128")
isci_1.Price      = 4600
isci_1.showProfile()