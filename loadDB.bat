mongoimport --db meteorcsv --collection landings --type csv --file "Meteorite_Landings.csv" --headerline  --uri "mongodb://root:student@localhost:27017" --authenticationDatabase=admin

mongofiles --db meteorcsv put acapulco.jpg --local ./staging/assets/TEMPimgs/acapulco.jpg -u root -p student --authenticationDatabase=admin
mongofiles --db meteorcsv put aguada.jpg --local ./staging/assets/TEMPimgs/aguada.jpg -u root -p student --authenticationDatabase=admin
mongofiles --db meteorcsv put "aguila blanca.jpg" --local ./staging/assets/TEMPimgs/"aguila blanca.jpg" -u root -p student --authenticationDatabase=admin
mongofiles --db meteorcsv put "aioun el atrouss.jpg" --local ./staging/assets/TEMPimgs/"aioun el atrouss.jpg" -u root -p student --authenticationDatabase=admin
mongofiles --db meteorcsv put "bahjoi".jpg --local ./staging/assets/TEMPimgs/"bahjoi".jpg -u root -p student --authenticationDatabase=admin
mongofiles --db meteorcsv put "bald mountain".jpg --local ./staging/assets/TEMPimgs/"bald mountain".jpg -u root -p student --authenticationDatabase=admin
mongofiles --db meteorcsv put baldwyn.jpg --local ./staging/assets/TEMPimgs/baldwyn.jpg -u root -p student --authenticationDatabase=admin