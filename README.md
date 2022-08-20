# MONITOREO DE LA CALIDAD DE AIRE MEDIANTE SENSOR AIRBEAM EN LA UNIVERSIDAD AUTÓNOMA DE OCCIDENTE. - Proyecto Final
## Ingeniería de Datos e Inteligencia Artificial
### 2° Semestre
### Estudiantes
* Maria de los Ángeles Amu Moreno
* Samuel Alexander Escalante Gutierrez
* Manuela Mayorga Rojas
* Laura Ximena Reyes Arcila
* Gerson Yarce Franco

## 1. Definir el contexto en el que se ha recolectado la información, donde se explique por qué se ha escogido el sitio web y el contexto para la captura de datos.
    El proyecto que hemos empezado a llevar a cabo trata sobre una de las grandes problemáticas a nivel mundial: la contaminación del aire. El transporte, la generación de energía, las fuentes industriales y domésticas han dado lugar a la contaminación y a cambios en la composición del aire ambiente; además, esta puede afectar gravemente a la salud humana, causando problemas respiratorios, enfermedades cardíacas y cáncer.

    Nosotros como equipo, nos enfocamos en la Universidad Autónoma de Occidente, en donde además de ser un sitio de nuestro fácil acceso, posee ayudas como un sensor de monitoreo de la calidad del aire, en donde podremos recolectar muy buena información para la captura de datos y así poder abordar este proyecto.

    Al momento de hacer el respectivo web scraping, nos basamos en https://aqicn.org/station/colombia/cali/call-51/es/ y https://waqi.info/es/#/c/-0.418/-59.302/3.8z; que son dos links con muy buena informaciòn y los escogimos ya que nos muestran de una manera factible el índice de calidad del aire en tiempo real. En el primer link podemos ver más a detalle el índice en ciertos sectores de la ciudad de Cali. Sin embargo, en el segundo podemos evidenciar  los datos a nivel mundial. Ambos clasifican sus niveles de índice en distintas escalas como: “bueno”, “moderado”, “no es saludable para grupos que son sensibles”, “insalubre”, “muy poco saludable” y por último “peligroso”; y además su manejo nos permite ver de una manera autónoma los datos para posteriormente realizar la respectiva comparación con la información del sensor de la Universidad.

## 2. Definir un título para el proyecto.

    MONITOREO DE LA CALIDAD DE AIRE MEDIANTE SENSOR AIRBEAM EN LA UNIVERSIDAD AUTÓNOMA DE OCCIDENTE.

## 3. Antecedentes (5)

* Uso de sensores electroquímicos de bajo costo para el monitoreo de la calidad del aire en el distrito de San Isidro - Lima - Perú
https://repositorio.up.edu.pe/handle/11354/1845
    En este trabajo se muestran los resultados preliminares del monitoreo y de la estimación de contaminantes atmosféricos en un punto estratégico dentro del distrito de San Isidro, Lima - Perú. Se emplearon sensores electroquímicos de bajo costo, portátiles, inalámbricos y geolocalizables para la captura de los niveles de contaminación que permiten obtener en tiempo real valores confiables que podrían emplearse no sólo para cuantificar la exposición de contaminación atmosférica sino también para prevención y control, e incluso para fines legislativos.

* Modelado de un sistema de supervisión de la calidad del aire usando técnicas de fusión de sensores y redes neuronales.
https://oa.upm.es/4839/
    El modelo, integra a las variables meteorológicas de dirección y velocidad de viento para determinar los efectos de estas en las concentraciones de contaminantes y determinar el nivel de contaminación atmosférica. La metodología consistió en analizar las series temporales (por minuto) de las concentraciones de contaminantes y las variables de dirección y velocidad de viento para generar patrones de entrenamiento con información relevante y representativa que puedan ser usados para entrenar una RNA de Mapas Auto-organizados (SOM).

* SENSORES DE BAJO COSTO PARA EL MONITOREO DE CALIDAD DEL AIRE
https://epistemus.unison.mx/index.php/epistemus/article/view/108
    En el marco actual de su uso se cuenta con disposición de estos dispositivos en el mercado y con gran variedad de principios de operación por lo que la estandarización y calibración de su aplicación aún se encuentra en desarrollo. Las variables de selección dependerán de la variable de interés y se vuelve fácil de adaptar a lo comercialmente disponible. El funcionamiento, principios de operación, así como las ventajas y desventajas de esta tecnología se presentan en el desarrollo del artículo.

* Prototipo de bajo costo para monitoreo de calidad del aire en ambientes interiores. http://repository.unipiloto.edu.co/handle/20.500.12277/4880
    Contextualización, diseño e implementación de un prototipo de bajo costo para el monitoreo de la calidad del aire en ambientes interiores.

* Validación de una red de sensores inalámbricos para el control de la calidad del aire en la zona industrial de Bucaramanga https://repository.unab.edu.co/handle/20.500.12749/1398
    Tomando como base una nueva tecnología que surge en el área de las telecomunicaciones, las redes de sensores inalámbricos; nace la idea de automatizar la medición y el control de la concentración de monóxido de carbono de las emisiones atmosféricas de las zonas industriales, mediante la integración de hardware (sensores de monóxido de carbono y módulos de radio transmisión) y software (una aplicación que permita la captura de los datos obtenidos por la red y establezca una interfaz amigable con el usuario final) para optimizar el método actual de regulación de la calidad del aire.

## 4. Responder: ¿Por qué es importante y qué pregunta/problema pretende responder de los datos que se extraerán?
    Es importante tener en cuenta el contexto universitario en el cual pasamos la mayor parte de nuestro tiempo, en donde muchas veces no nos fijamos cuáles son las condiciones del aire que estamos respirando en todo momento. Por eso, a partir de lo anterior nos planteamos si  “¿es óptima la calidad de aire que respiran los estudiantes autónomos?”. A partir de este interrogante, con el equipo de trabajos nos comprometemos a buscar una solución que nos demuestre cómo se encuentra la calidad de aire en el entorno universitario, para así poder tomar riendas y evaluar qué aspectos se pueden llevar a cabo para contrarrestar si el problema se encuentra en escalas de muy mala calidad.

## 5. Clasificar el tipo de problema en un campo de aplicación de análisis de datos.
    Queremos enfocar el proyecto hacia un enfoque descriptivo que nos permita dar una opción visible a la comunidad universitaria sobre el estado actual de la calidad del aire en comparación con las múltiples estaciones a través de la ciudad.
