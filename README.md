# **Создание новой БД с помощью *dbca*.**
    1. Запустить `dbca` на сервере или виртуальной машине. 
        Database Operations: Выбрать опцию *"Create a database"* и нажать "Next".
    
    2. Выбор шаблона базы данных (Creation Mode):
        Выбрать "Advanced Mode" для большего контроля над параметрами. 
        Deployment Type: Затем выбрать шаблон "General Purpose or Transaction Processing".
    
    3. Базовая информация о базе данных (Database Identification):
        Ввести имя базы данных (Global Database Name) и SID (System Identifier). В моем случае:
            Global Database Name: finalproject
            SID: finalproject
        Убрать галочку с "Create as Container Database", если она стоит
        
    4. Storage option: Переключить radiobutton на "Use folowing for the ...." и убрать галочку с "Use Oracle-Managed Files"

    5. Fast recovery option: убрать все галочки и нажать Next

    6. Network Configuration: выбрать существующий Listener или создать новый

    7. Data Vault Option: убрать все галочки, если они стоят

    8. Configuration options: Выбрать метод управления памятью "Automatic Shared Memory Management". Настроить параметры SGA и PGA, если это необходимо.
        Затем в вкладке Sample Schemas поставить галочку на "Add sample...".

    9. Managments Options: убрать все галочки

    10. User credentials: выбрать "Use the same administative..." и ввести пароль

    11. Creation Option: ставим галочку только на Create Database и нажимаем Next
    Далее нажимаем Finish и ждем загрузки. При окончании загруски нажимаем close.
