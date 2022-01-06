# desarrollador-fintual
Debes realizar la siguiente tarea y enviar link de repositorio de github con la respuesta.

Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. 
Assume each Stock has a "Price" method that receives a date and returns its price.
Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.

-----
La tarea se aborda en el lenguaje Python.

En primer lugar se genera un script con el nombre de genera_dataset.py donde se genera el archivo data.csv, el cual contiene la información de precios diaria para 3 acciones, AAPL, NVDA y TSLA, utilizando sus precios iniciales como base y generando precios aleatorios desde la fecha de lanzamiento de dichas acciones hasta el 2022-01-01.

Posteriormente utilizando flask, se genera una pequeña aplicación web, donde es posible ingresar la compra de acciones al portafolio, con el nombre, cantidad y fecha de compra. Además, dado dos fechas seleccionadas se permite calcular el profit del portafolio y el retorno anualizado.

-----
Para replicar el ambiente utilizado y ejecutar la aplicación se deben seguir los siguientes pasos:

1. conda create --name fintual --file requirements.txt
2. conda activate fintual
3. python app.py
4. ver http://127.0.0.1:5000/ en el navegador

-----
El portafolio se resetea si se recarga la pagina web ya que se vuelve a crear el objeto incial de portafolio, por lo que es un comportamiento deseado.
-----