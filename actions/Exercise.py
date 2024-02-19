# Difficulties
BEGINNER = 0
INTERMEDIATE = 1
ADVANCED = 2

# Priorities
MAIN_MOVEMENT = "main_movement"
ASSISTANCE = "assistance"
TERTIARY = "tertiary"

# Entity's names
EXERCISE = "ejercicio"

# Slot's names
AGE = "edad"
PHYSICAL_CONDITION = "condicion_fisica"
SPORT_EXPERIENCE = "experiencia_deporte"
OBJECTIVE = "objetivo"
CONDITION_PROGRESS = "mejora_condicion_fisica"
ROUTINE_TIME = "tiempo_rutina"
DAY = "dia"
ROUTINE_CREATED = "rutina_generada"
DAY_SEPARATION = "separacion_dias"
EXERCISES = "ejercicios"
SETS = "series"
REPS = "repeticiones"

EXERCISE_PRIORITY = (MAIN_MOVEMENT, ASSISTANCE, MAIN_MOVEMENT, ASSISTANCE, TERTIARY, ASSISTANCE, TERTIARY, ASSISTANCE,
                     MAIN_MOVEMENT)

# Definicion de los ejercicios
hinge_exercises = {
    "Peso muerto rumano": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 6,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "De pie, sostén una barra frente a tus muslos con las piernas rectas y los pies a la altura de los hombros. Mantén la "
                       "espalda recta y los hombros hacia atrás. Inclínate hacia adelante desde la cadera mientras mantienes las piernas "
                       "ligeramente flexionadas, manteniendo la barra cerca de las piernas a medida que te inclinas. Llega hasta que sientas un "
                       "estiramiento en los músculos isquiotibiales, luego regresa a la posición inicial enderezando la cadera y manteniendo la "
                       "espalda recta. "
    },
    "Zancada inversa": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Párate derecho con los pies juntos. Da un paso hacia atrás con una de las piernas, flexionando ambas rodillas para bajar tu "
                       "cuerpo. La rodilla trasera debe acercarse al suelo, y la pierna delantera debe estar en un ángulo de 90 grados. Luego, "
                       "empuja con la pierna delantera para volver a la posición inicial. Alterna entre las piernas para realizar el ejercicio de "
                       "manera equilibrada. "
    },
    "Elevación de glúteos": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Comienza por arrodillarte en una máquina para Elevación de Glúteos, con los tobillos sujetos debajo de los soportes "
                       "acolchados. Asegúrate de que tus muslos estén apoyados en el cojín y que tus pies estén sujetos. Desde esta posición, "
                       "flexiona las caderas para bajar el torso hacia el suelo, manteniendo la espalda recta. Luego, contrae los glúteos y los "
                       "tendones de la corva para elevar tu cuerpo de nuevo a la posición inicial. Mantén el control y evita balancearte durante el "
                       "ejercicio. "
    },
    "Hiperextensión": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Para realizar una hiperextensión, acuéstate boca abajo en un banco de hiperextensión o en una máquina diseñada para este "
                       "ejercicio. Asegura tus pies bajo los soportes acolchados y coloca tus caderas en el cojín de forma que tus caderas queden "
                       "justo por debajo del borde del banco. Mantén las manos cruzadas sobre el pecho o detrás de la cabeza. Desde esta posición, "
                       "eleva el torso mientras mantienes la espalda recta, evitando arquearla en exceso. Luego, regresa lentamente a la posición "
                       "inicial. "
    },
    "Curl de isquiotibiales acostado": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Acuéstate boca abajo en un banco especialmente diseñado para este ejercicio. Asegura tus tobillos debajo de los rodillos "
                       "acolchados y flexiona las piernas hacia los glúteos, manteniendo los muslos en el banco. Luego, extiende lentamente las "
                       "piernas hacia abajo, manteniendo los muslos en posición, y luego vuelve a contraer los músculos de los femorales para "
                       "llevar las piernas de regreso a la posición inicial. Repite el movimiento. "
    },
    "Empuje de cadera con barra": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 5,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Siéntate en el suelo con tus piernas dobladas y los hombros apoyados en un banco. Coloca una barra con pesas sobre tus "
                       "caderas y sosténla con las manos a ambos lados de tus caderas. Mantén los pies planos en el suelo, cerca de tus glúteos. "
                       "Desde esta posición, empuja las caderas hacia arriba, elevando la barra y extendiendo las caderas completamente. Luego, "
                       "baja las caderas de manera controlada de vuelta a la posición inicial. Repite el movimiento. "
    },
    "Máquina para glúteos": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Siéntate en la máquina de glúteos con la parte superior de tus muslos apoyada en el cojín acolchado y tus manos en los "
                       "agarres. Asegúrate de que tus pies estén apoyados en las almohadillas y que tus rodillas estén dobladas a 90 grados. "
                       "Contrae tus glúteos y empuja hacia atrás tus piernas mientras exhalas, estirando completamente las piernas. Luego, "
                       "inhala y lleva las piernas de regreso a la posición inicial controladamente. Repite el movimiento. "
    },
    "Hiperextensión inversa": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Para realizar una hiperextensión inversa, acuéstate boca abajo en una máquina diseñada para este ejercicio. Asegúrate de "
                       "que tus caderas estén alineadas con el borde del banco y tus piernas cuelguen libremente. Sujeta la parte inferior de la "
                       "máquina con tus manos para mantener el equilibrio. Luego, levanta tus piernas hacia arriba lo más alto posible sin "
                       "flexionar las caderas, manteniendo las piernas estiradas. Desciende las piernas de manera controlada. "
    },
    "Curl de isquiotibiales sentado": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Siéntate en la máquina de curl de isquiotibiales con las piernas extendidas frente a ti. Ajusta la almohadilla acolchada "
                       "contra la parte posterior de tus tobillos. Sujeta las asas de la máquina para mantener tu torso en su lugar. Flexiona las "
                       "piernas, llevando los talones hacia los glúteos, contrayendo los músculos de los isquiotibiales en el proceso. Luego, "
                       "regresa las piernas a la posición inicial de manera controlada. Repite el movimiento. "
    },
    "Remo en barra-T": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Para realizar el Remo en barra-T, comienza por colocar una barra T-Bar en el soporte correspondiente, añadiendo el peso "
                       "deseado en el otro extremo de la barra. Ponte de pie en el lado opuesto de la barra, inclínate hacia adelante desde la "
                       "cadera para que tu espalda esté paralela al suelo, y sujeta la barra con ambas manos, manteniendo los brazos extendidos. "
                       "Luego, tira de la barra hacia tu abdomen, doblando los codos y apretando los omóplatos juntos en la parte superior del "
                       "movimiento. A continuación, baja la barra de regreso a la posición inicial y repite el ejercicio. "
    },
    "Tirón con cable hacia atrás": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate de pie frente a una máquina de poleas con una polea baja y un accesorio de cuerda. Ajusta el peso deseado en la "
                       "máquina. Agarra la cuerda con ambas manos y da un paso hacia adelante para crear tensión en el cable. Mantén tus pies a la "
                       "altura de los hombros, con las rodillas ligeramente flexionadas. Inclina las caderas hacia atrás y mantén la espalda recta "
                       "mientras llevas la cuerda entre tus piernas. Luego, realiza un movimiento de cadera hacia adelante y estira tus caderas "
                       "para enderezar el cuerpo, llevando la cuerda hacia arriba y hacia adelante hasta que tus caderas estén completamente "
                       "extendidas. Mantén la espalda recta en todo momento. Invierte el movimiento para volver a la posición inicial. "
    },
    "Puente de glúteos con barra en el suelo": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en el suelo boca arriba con las rodillas dobladas y los pies apoyados en el suelo, a la altura de las caderas. "
                       "Coloca una barra sobre tu regazo, asegurándote de que esté estable y equilibrada. Luego, contrae los glúteos y levanta las "
                       "caderas del suelo, manteniendo la barra en su lugar. Asegúrate de que tu cuerpo forme una línea recta desde los hombros "
                       "hasta las rodillas en la posición elevada. Baja las caderas de nuevo al suelo y repite el movimiento. "
    },
    "Peso muerto rumano a una pierna": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 8,
        "min_reps": 10,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie, sostén una barra o mancuernas frente a tus muslos con una mano. Levanta una pierna hacia atrás y manténla recta, "
                       "manteniendo el equilibrio sobre la otra pierna. Inclínate hacia adelante desde la cadera mientras bajas la parte superior "
                       "del cuerpo hacia el suelo, manteniendo la espalda recta. La pierna levantada y el torso deben formar una línea recta. Baja "
                       "la barra o las mancuernas lo más cerca posible de la pierna en movimiento. Luego, regresa a la posición vertical, "
                       "manteniendo el equilibrio en una sola pierna. Repite el movimiento en la otra pierna. "
    },
    "Balanceo de pesa rusa": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "De pie con las piernas separadas a la altura de los hombros, coloca una pesa rusa (kettlebell) frente a ti. Inclínate hacia "
                       "adelante desde las caderas, doblando las rodillas ligeramente, manteniendo la espalda recta y agarrando la pesa rusa con "
                       "ambas manos. En un movimiento explosivo, balancea la pesa rusa hacia adelante y hacia arriba, utilizando la fuerza de tus "
                       "caderas y glúteos para impulsarla. Mantén los brazos rectos. Una vez que la pesa rusa llegue a la altura de los hombros, "
                       "invierte el movimiento y balancea hacia abajo entre las piernas. Continúa este patrón de movimiento de balanceo de la pesa "
                       "rusa hacia adelante y hacia atrás, manteniendo un control constante y un buen ritmo. "
    },
    "Peso muerto con piernas rígidas": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "De pie, con los pies a la altura de los hombros y una barra en las manos, mantén las piernas casi completamente rectas, "
                       "con una ligera flexión en las rodillas. Mantén la espalda recta mientras te inclinas hacia adelante desde la cadera, "
                       "bajando el peso hacia el suelo. Siente la tensión en los músculos de la parte posterior de las piernas y los glúteos. "
                       "Luego, regresa a la posición inicial manteniendo la espalda recta y los músculos de la espalda baja contraídos. "
    },
    "Empuje de cadera con una pierna": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Siéntate en el suelo con las piernas dobladas y los pies apoyados en el suelo. Extiende una pierna hacia afuera, "
                       "manteniendo la otra doblada. Coloca tu espalda baja y los hombros en un banco o superficie elevada. Levanta las caderas "
                       "hacia arriba mientras mantienes la pierna extendida en el aire. Aprieta los glúteos en la parte superior del movimiento y "
                       "luego baja las caderas de regreso al suelo. Repite el ejercicio con la misma pierna antes de cambiar a la otra. "
    },
    "Buenos días": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "De pie, coloca una barra en la parte posterior de tus hombros, detrás de la cabeza. Mantén una postura recta, los pies a la "
                       "altura de los hombros y las rodillas ligeramente flexionadas. Mantén la espalda recta y el torso inclinado hacia adelante "
                       "desde la cadera, manteniendo la barra cerca del cuerpo. Luego, endereza lentamente la espalda y vuelve a la posición "
                       "vertical. "
    },
    "Peso muerto convencional": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 4,
        "min_reps": 3,
        "max_reps": 8,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate de pie frente a una barra con pesas, con los pies a la altura de los hombros y los dedos de los pies debajo de la "
                       "barra. Flexiona las caderas y las rodillas para agacharte y sujetar la barra con las manos separadas a una distancia un "
                       "poco mayor que el ancho de los hombros. Mantén la espalda recta, el pecho hacia afuera y la mirada al frente. Con un "
                       "movimiento explosivo, endereza las caderas y las rodillas, levantando la barra del suelo hasta que estés completamente de "
                       "pie. Luego, baja la barra de manera controlada hasta el suelo. "
    },
    "Peso muerto sumo": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 4,
        "min_reps": 3,
        "max_reps": 8,
        "priority": MAIN_MOVEMENT,
        "description": "Para realizar el Peso Muerto Sumo, párate frente a una barra con los pies separados a una distancia mayor que el ancho de "
                       "tus hombros y los dedos de los pies ligeramente hacia afuera. Inclínate hacia adelante desde las caderas y agarra la barra "
                       "con las manos dentro de las piernas. Mantén la espalda recta y el pecho hacia arriba. Luego, levanta la barra estirando las "
                       "piernas y las caderas, manteniendo los brazos extendidos. Finaliza el movimiento al estar completamente erguido y luego "
                       "baja la barra controladamente de regreso al suelo. "
    },
    "Sentadilla en estocada": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Comienza de pie con los pies juntos. Da un paso hacia adelante con un pie y un paso hacia atrás con el otro, creando una "
                       "distancia cómoda entre tus pies. Mantén la espalda recta y el torso erguido. Dobla ambas rodillas para bajar tu cuerpo "
                       "hacia el suelo, asegurándote de que ambas piernas formen ángulos de 90 grados. Luego, empuja con la pierna delantera para "
                       "volver a la posición inicial. Alterna las piernas en cada repetición. "
    },
    "Jefferson Curl": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Colócate de pie con los pies a la altura de los hombros. Sujeta una barra o pesa con los brazos extendidos frente a ti. A "
                       "continuación, comienza a flexionar lentamente la columna vertebral hacia adelante, vértebra por vértebra, "
                       "como si estuvieras tratando de alcanzar tus dedos de los pies. Mantén las piernas rectas durante el movimiento. Luego, "
                       "revierte el proceso, desenrollando lentamente la columna vertebral para volver a la posición inicial. "
    },
    "Curl nórdico de isquiotibiales ": {
        "difficulty": ADVANCED,
        "effectiveness": 6,
        "min_reps": 6,
        "max_reps": 15,
        "priority": TERTIARY,
        "description": "Para realizar el curl nórdico de isquiotibiales, necesitas un compañero o algo en lo que puedas enganchar tus tobillos, "
                       "como una barra horizontal o un soporte estable. Arrodíllate en el suelo, con los tobillos asegurados por tu compañero o el "
                       "soporte. Mantén tus manos cruzadas sobre el pecho o detrás de la cabeza. Luego, inclínate hacia adelante desde las caderas, "
                       "manteniendo la espalda recta, y baja lentamente tu cuerpo hacia el suelo, controlando la caída con los músculos de los "
                       "isquiotibiales. Cuando no puedas bajar más, utiliza tus manos para empujar el suelo y levantarte de nuevo a la posición "
                       "inicial. "
    },
}

squat_exercises = {
    "Sentadilla con talón elevado": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 5,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate de pie con los talones apoyados en una superficie elevada, como una placa o un step. Tus pies deben estar a la "
                       "altura de los hombros y los dedos mirando ligeramente hacia afuera. Luego, realiza una sentadilla descendiendo tu cuerpo "
                       "hacia abajo mientras mantienes los talones elevados y la espalda recta. Asegúrate de que tus rodillas no se desplacen hacia "
                       "adelante más allá de los dedos de los pies. Luego, vuelve a la posición inicial empujando a través de los talones y "
                       "extendiendo las caderas. Repite el movimiento. "
    },
    "Sentadilla en máquina Smith": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate debajo de la barra de la Máquina Smith con la barra apoyada en tus hombros. Parado con los pies a la altura de tus "
                       "hombros y la espalda recta, flexiona las rodillas y las caderas para bajar tu cuerpo hacia abajo. Mantén la barra en su "
                       "lugar y desciende hasta que tus muslos estén paralelos al suelo o incluso más abajo si es posible. Luego, empuja con las "
                       "piernas para volver a la posición inicial. Asegúrate de mantener una forma adecuada durante todo el ejercicio. "
    },
    "Sentadilla sumo en déficit": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Colócate de pie con los pies más anchos que el ancho de los hombros y con los dedos de los pies mirando hacia afuera, "
                       "en una posición similar a la de una sentadilla sumo. Coloca dos plataformas, pesas o superficies elevadas debajo de tus "
                       "pies. A continuación, realiza una sentadilla sumo, bajando tu cuerpo hacia abajo y manteniendo la espalda recta. Asegúrate "
                       "de que tus muslos estén paralelos al suelo o incluso por debajo de la línea de tus rodillas si es posible, aprovechando la "
                       "elevación proporcionada por el deficit. Luego, vuelve a la posición inicial. "
    },
    "Extensión de piernas": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Siéntate en una máquina de extensiones de piernas con la espalda apoyada en el respaldo y las piernas en ángulo recto con "
                       "tus muslos contra los cojines acolchados. Agarra las asas de la máquina para mantener el equilibrio y extiende tus piernas "
                       "completamente hacia arriba, elevando los pies hacia el techo. Luego, baja lentamente las piernas de regreso a la posición "
                       "inicial, manteniendo un control constante. Repite el movimiento. "
    },
    "Sentadilla con barra alta": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 3,
        "max_reps": 12,
        "priority": MAIN_MOVEMENT,
        "description": "Coloca una barra en tus hombros a la altura de la parte superior de la espalda, sosteniéndola con las manos a una distancia "
                       "un poco mayor que el ancho de tus hombros. Párate con los pies a la altura de los hombros y la espalda recta. Desciende "
                       "flexionando las rodillas y las caderas, manteniendo la espalda recta y los talones en el suelo. Baja hasta que tus muslos "
                       "estén al menos paralelos al suelo, y luego empuja hacia arriba para volver a la posición de pie. "
    },
    "Zancada": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Comienza de pie con los pies separados a la distancia de un paso largo. Da un paso hacia adelante con una pierna y coloca "
                       "la otra pierna detrás de ti, manteniendo el equilibrio. Asegúrate de que tus pies estén separados a la altura de los "
                       "hombros. Luego, dobla ambas rodillas para bajar el cuerpo hacia el suelo, manteniendo la espalda recta y el tronco "
                       "vertical. Continúa bajando hasta que la rodilla de la pierna trasera casi toque el suelo o llegue a una posición cómoda. "
                       "Luego, impúlsate hacia arriba con la pierna delantera para regresar a la posición inicial. Alterna entre las piernas para "
                       "realizar repeticiones. "
    },
    "Sentadilla Hack": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Para realizar una sentadilla Hack, colócate en una máquina de sentadilla Hack con los hombros apoyados en los cojines y los "
                       "pies en una posición ligeramente adelantada. Agarra las barras de la máquina con las manos y libera el seguro. Luego, "
                       "dobla las rodillas y baja el cuerpo hacia abajo, manteniendo la espalda recta. Asegúrate de que tus rodillas no se "
                       "extiendan más allá de los dedos de los pies. Luego, empuja con las piernas para volver a la posición inicial. Repite el "
                       "movimiento. "
    },
    "Sentadilla en caja": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate de pie frente a una caja o banco resistente. Los pies deben estar a la anchura de los hombros. Mantén la espalda "
                       "recta y los brazos extendidos frente a ti o cruzados sobre el pecho. Desciende lentamente hacia la caja, doblando las "
                       "rodillas y las caderas, como si te estuvieras sentando en la caja. Asegúrate de mantener los talones en contacto con el "
                       "suelo y la espalda recta. Una vez que tus glúteos toquen la caja, invierte el movimiento y vuelve a ponerte de pie. "
    },
    "Máquina de aductores": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 30,
        "priority": TERTIARY,
        "description": "Siéntate en la máquina de aductores con las piernas en las almohadillas, manteniendo la espalda recta. Ajusta el peso de "
                       "acuerdo a tu nivel de resistencia. Comienza el ejercicio presionando las piernas hacia adentro, contra la resistencia, "
                       "manteniendo las rodillas y los pies juntos. Luego, regresa las piernas lentamente a la posición inicial. Repite el "
                       "movimiento. "
    },
    "Sentadilla con pesa rusa": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Sujeta una pesa (como una pesa rusa o una mancuerna) con ambas manos cerca de tu pecho, manteniéndola en posición vertical, "
                       "como si sostuvieras una copa. Coloca tus pies a la altura de los hombros o ligeramente más anchos. Mantén tu espalda recta "
                       "y el pecho erguido. Luego, flexiona las rodillas y las caderas para bajar tu cuerpo hacia abajo, como si te estuvieras "
                       "sentando en una silla. Asegúrate de mantener la pesa cerca de tu pecho mientras desciendes. Luego, empuja a través de los "
                       "talones para volver a la posición de pie. Repite el movimiento. "
    },
    "Sentadilla frontal con barra landmine": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Coloca una barra en el anclaje de landmine, asegurándola en posición vertical. Párate frente a la barra con los pies a la "
                       "altura de los hombros y sujétala con ambas manos a la altura del pecho, manteniendo los codos hacia arriba. Realiza una "
                       "sentadilla manteniendo la barra en su lugar, asegurándote de que tus rodillas estén alineadas con los dedos de los pies y "
                       "tu espalda esté recta. Desciende hasta que tus muslos estén paralelos al suelo o incluso un poco más abajo si puedes. "
                       "Luego, impúlsate hacia arriba para volver a la posición inicial. "
    },
    "Prensa de piernas": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Siéntate en una máquina de prensa de piernas con la espalda contra el respaldo y los pies en una plataforma que está a una "
                       "distancia cómoda. Desbloquea el mecanismo de seguridad y baja lentamente las piernas doblando las rodillas hasta que tus "
                       "muslos estén cerca de tu pecho. Luego, presiona la plataforma hacia arriba estirando las piernas, manteniendo la espalda "
                       "contra el respaldo en todo momento. Vuelve a la posición inicial flexionando las rodillas y repite el movimiento. "
    },
    "Sentadilla Hack inversa": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate en una máquina de sentadilla hack inversa, con los hombros apoyados en los cojines y los pies en la plataforma. "
                       "Mantén los pies a la altura de los hombros y las rodillas ligeramente dobladas. Empuja la plataforma hacia arriba con los "
                       "talones, extendiendo las piernas completamente, y luego regresa a la posición inicial flexionando las rodillas. Realiza el "
                       "movimiento de subida y bajada controladamente. "
    },
    "Sentadilla búlgara": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Para realizar una Sentadilla Búlgara, colócate de espaldas a un banco o superficie elevada. Extiende una de tus piernas "
                       "hacia atrás y apoya la parte superior de tu pie en el banco. La otra pierna adelantada es la que realizará el ejercicio. "
                       "Mantén la espalda recta y baja tu cuerpo hacia abajo doblando la rodilla de la pierna adelantada hasta que tu muslo esté "
                       "paralelo al suelo o ligeramente por debajo. Luego, vuelve a la posición inicial. Repite el movimiento y luego cambia de "
                       "pierna. "
    },
    "Sentadilla Platz": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate de pie con los pies separados a la altura de los hombros y los talones ligeramente elevados sobre una superficie. "
                       "Sujeta una barra en la espalda. Asegúrate de que tus pies esten separados a un poco menos de la anchura de tus hombros. "
                       "Luego, comienza a descender en una sentadilla profunda, permitiendo que tus rodillas sobrepasen ligeramente tus pies. "
                       "Mantén la espalda recta y el pecho erguido durante todo el movimiento. Luego, vuelve a la posición inicial al levantarte. "
    },
    "Sentadilla frontal": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 7,
        "min_reps": 4,
        "max_reps": 12,
        "priority": MAIN_MOVEMENT,
        "description": "Para realizar una sentadilla frontal, coloca una barra en tus hombros delanteros, cruzando los brazos y sujetando la barra "
                       "con las manos. Asegúrate de que tus codos estén apuntando hacia adelante y tus pies estén a la altura de los hombros. Baja "
                       "lentamente tu cuerpo doblando las rodillas y las caderas, manteniendo la espalda recta y el pecho erguido. Lleva tus "
                       "caderas hacia atrás y hacia abajo como si te estuvieras sentando en una silla invisible. Luego, regresa a la posición "
                       "inicial empujando a través de los talones. "
    },
    "Sentadilla Hack con barra": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Coloca una barra cargada en el suelo detrás de tus piernas. Párate frente a la barra con los pies a la altura de los "
                       "hombros. Agarra la barra con las manos detrás de tus piernas, manteniendo la espalda recta. Lentamente, flexiona las "
                       "rodillas y las caderas para bajar tu cuerpo hacia abajo, manteniendo la barra cerca de las piernas. Asegúrate de mantener "
                       "una buena forma y evitar que las rodillas se desplacen hacia adelante. Luego, extiende las caderas y las rodillas para "
                       "volver a la posición inicial. "
    },
    "Sentadilla zombie": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 7,
        "min_reps": 5,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Ponte de pie con los pies a la altura de los hombros y los brazos extendidos hacia adelante, paralelos al suelo, "
                       "como si fueras un zombie. Mantén los brazos en esta posición durante todo el ejercicio. Dobla las rodillas y baja el cuerpo "
                       "como si estuvieras sentándote en una silla, manteniendo la espalda recta y los brazos extendidos. Luego, "
                       "vuelve a la posición inicial levantando lentamente el cuerpo. Repite el movimiento. "
    },
    "Sentadilla Jefferson": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Coloca una barra o una barra de pesas en el suelo de manera que esté en posición diagonal, formando un ángulo de "
                       "aproximadamente 45 grados. De pie al lado de la barra, asegúrate de que tus pies estén separados a la altura de los "
                       "hombros. Luego, cruza un pie por delante de la barra y el otro por detrás. Agarra la barra con ambas manos, "
                       "una en cada lado de tu cuerpo. Desde esta posición, realiza una sentadilla como lo harías normalmente, manteniendo la "
                       "espalda recta y descendiendo hasta que tus muslos estén paralelos al suelo. Luego, vuelve a la posición inicial. Asegúrate "
                       "de cambiar la posición de tus pies cruzados para trabajar ambos lados por igual. "
    },
    "Sentadilla con barra baja": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 3,
        "max_reps": 12,
        "priority": MAIN_MOVEMENT,
        "description": "Coloca una barra en tus hombros, justo por debajo de la parte superior de la espalda, y sosténla con un agarre amplio. "
                       "Mantén tus pies a la altura de los hombros y los dedos de los pies ligeramente girados hacia afuera. Desciende lentamente "
                       "hacia abajo, manteniendo tu espalda recta y tu pecho hacia adelante. Dobla las caderas y las rodillas mientras te aseguras "
                       "de que tus rodillas no se extiendan más allá de tus pies. Baja hasta que tus muslos estén al menos paralelos al suelo o "
                       "incluso más abajo, y luego empuja hacia arriba para volver a la posición inicial. "
    },
    "Sentadilla Zercher": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 2,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Coloca una barra en el rack de sentadillas a la altura de tus codos. Parado frente a la barra, engancha tus brazos debajo "
                       "de ella y cruza tus manos para sostenerla. Levanta la barra con control y llévala hasta la parte frontal de tu torso, "
                       "con los codos doblados. Mantén la espalda recta y los pies separados al ancho de los hombros. Realiza una sentadilla "
                       "bajando tu cuerpo hasta que tus muslos estén al menos paralelos al suelo. Luego, vuelve a la posición inicial manteniendo "
                       "la barra cerca de tu cuerpo. "
    },
    "Sentadilla Sissy": {
        "difficulty": ADVANCED,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Colócate de pie, manteniendo los pies a la altura de los hombros y sosteniéndote de un soporte firme, como una barra o un "
                       "mueble. Inclina tu torso hacia atrás, manteniendo las piernas rectas, y baja tu cuerpo hacia el suelo flexionando las "
                       "rodillas. Después, inclina el torso hacia adelante y empuja las caderas hacia adelante mientras mantienes las piernas "
                       "extendidas. Regresa a la posición inicial, manteniendo siempre una buena forma y control en el movimiento. "
    },
    "Sentadilla en una pierna": {
        "difficulty": ADVANCED,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie, levanta una pierna del suelo mientras extiendes el otro pie hacia adelante. Mantén la pierna extendida mientras te "
                       "agachas, manteniendo el equilibrio en una sola pierna. Desciende hasta que tu glúteo casi toque el talón del pie que tienes "
                       "extendido. Luego, extiende la pierna y vuelve a ponerte de pie. Realiza el ejercicio en ambas piernas. "
    }
}

row_exercises = {
    "Remo inclinado con barra-ez": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Para realizar este ejercicio, siéntate en un banco inclinado con un ángulo de alrededor de 45 grados. Agarra una barra Z ("
                       "barra curvada) con un agarre supino (palmas hacia adelante) y brazos extendidos. Mantén la barra cerca de tu torso y tira "
                       "de ella hacia tu abdomen, manteniendo los codos cerca del cuerpo. Luego, baja la barra de manera controlada hasta la "
                       "posición inicial. "
    },
    "Remo con mancuerna": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Coloca un banco horizontal a tu lado. De pie, con una mancuerna en una mano, coloca el brazo del lado opuesto sobre el "
                       "banco para apoyar tu cuerpo. Deja que la mancuerna cuelgue en el brazo extendido. Luego, lleva la mancuerna hacia arriba "
                       "hacia la cadera, doblando el codo y apretando el omóplato. Mantén la posición superior por un momento y luego baja la "
                       "mancuerna de nuevo hacia la posición inicial. Repite el movimiento con el mismo brazo antes de cambiar al otro lado. "
    },
    "Remo": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Para realizar un remo, necesitas una barra horizontal. Comienza de pie, frente a la barra, con las piernas extendidas y el "
                       "cuerpo inclinado hacia atrás. Agarra la barra con las manos, manteniendo los brazos estirados y los talones en el suelo. "
                       "Luego, tira de tu cuerpo hacia arriba hacia la barra, flexionando los codos y manteniendo el cuerpo en una línea recta "
                       "desde la cabeza hasta los talones. Baja lentamente el cuerpo de regreso a la posición inicial. Repite el movimiento. "
    },
    "Remo supino en anillas": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Para realizar un remo supino en anillas, agarra las anillas con las palmas de las manos mirando hacia arriba (supinadas) y "
                       "asegúrate de que las anillas estén suspendidas a la altura de tu cadera. Mantén tu cuerpo en posición horizontal con los "
                       "brazos extendidos. Desde esta posición, flexiona los codos y tira de tu cuerpo hacia arriba hasta que el pecho toque las "
                       "anillas. Luego, baja tu cuerpo de nuevo hacia abajo, manteniendo el control en todo momento. Repite el movimiento. "
    },
    "Remo unilateral con polea sentado": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Siéntate en un banco frente a una máquina de poleas con el cable ajustado a una altura baja. Agarra el asa con una mano y "
                       "mantén una postura erguida. Tira del cable hacia ti, llevando el codo hacia atrás y contrayendo los músculos de la espalda. "
                       "Asegúrate de mantener el torso estable y los hombros nivelados. Regresa la manija a la posición inicial de manera "
                       "controlada y repite con la otra mano. "
    },
    "Remo Meadows": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Colócate a un lado de una barra fija en el suelo. Inclínate hacia adelante desde la cadera, manteniendo la espalda recta y "
                       "sosteniendo la barra con una mano, con la palma mirando hacia adentro. Mantén la rodilla y el pie del lado correspondiente "
                       "ligeramente flexionados. Realiza el movimiento de remo, llevando la barra hacia la cadera, manteniendo el codo cerca del "
                       "torso. Luego, baja la barra de manera controlada hacia el suelo y repite el ejercicio. Cambia de lado para trabajar ambos "
                       "brazos. "
    },
    "Remo con mancuernas apoyado en el pecho": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Acuéstate boca abajo sobre un banco inclinado, de manera que tu pecho quede apoyado en el respaldo y tus pies toquen el "
                       "suelo. Con una mancuerna en cada mano, deja que tus brazos cuelguen directamente hacia el suelo. Luego, "
                       "realiza el movimiento de remo levantando las mancuernas hacia tus costados, manteniendo los codos cerca del cuerpo. "
                       "Asegúrate de contraer los músculos de la espalda alta al llevar las mancuernas hacia arriba. Baja las mancuernas lentamente "
                       "y repite el ejercicio. "
    },
    "Remo en anillas": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Ajusta las anillas a una altura adecuada y colócalas de manera que estén suspendidas por encima del suelo. Agarra las "
                       "anillas con ambas manos, estirando tu cuerpo debajo de ellas. Mantén los pies en el suelo y el cuerpo en posición "
                       "horizontal. Tira del cuerpo hacia arriba, llevando el pecho hacia las anillas, manteniendo los codos cerca del cuerpo. "
                       "Después, baja el cuerpo de manera controlada a la posición inicial. Repite el movimiento. "
    },
    "Remo con cable sentado": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Siéntate frente a una máquina de poleas con un asiento ajustable. Asegúrate de sujetar la barra de la polea con ambas "
                       "manos, manteniendo los brazos extendidos frente a ti. Con la espalda recta, tira de la barra hacia tu torso flexionando los "
                       "codos, llevando los omóplatos hacia atrás al final del movimiento. Luego, extiende los brazos lentamente para volver a la "
                       "posición inicial. "
    },
    "Remo Yates": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Párate con los pies a la altura de los hombros, sosteniendo una barra con agarre supino (palmas hacia arriba) y las manos "
                       "colocadas ligeramente más anchas que el ancho de los hombros. Inclínate hacia adelante desde la cintura manteniendo la "
                       "espalda recta, permitiendo que la barra cuelgue frente a ti. Mantén los codos ligeramente flexionados y lleva la barra "
                       "hacia la parte baja del pecho, contrayendo los músculos de la espalda alta. Desciende la barra de manera controlada de "
                       "vuelta a la posición inicial y repite el movimiento. "
    },
    "Remo con barra": {
        "difficulty": ADVANCED,
        "effectiveness": 4,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate de pie, con los pies a la altura de los hombros, y sujeta una barra con ambas manos, manteniendo las palmas hacia "
                       "abajo. Inclínate hacia adelante desde la cadera, manteniendo la espalda recta, hasta que tu torso esté paralelo al suelo. "
                       "Levanta la barra hacia tu abdomen, manteniendo los codos cerca del cuerpo y apretando los omóplatos al final del "
                       "movimiento. Desciende la barra de manera controlada y repite el ejercicio. "
    },
    "Remo Kroc": {
        "difficulty": ADVANCED,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate de pie junto a un banco, con una mancuerna en una mano y el pie del mismo lado apoyado en el banco. Inclínate "
                       "hacia adelante desde la cadera, manteniendo la espalda recta, y deja que la mancuerna cuelgue directamente debajo de ti. "
                       "Luego, realiza un movimiento de remo levantando la mancuerna hacia la cadera, manteniendo el codo cerca del cuerpo. "
                       "Extiende completamente el brazo hacia abajo en cada repetición y alterna entre ambos lados. "
    }
}

push_exercises = {
    "Press de banca": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 4,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Acuéstate en un banco plano de levantamiento de pesas con los pies firmemente en el suelo. Coloca una barra cargada en "
                       "posición sobre tu pecho, con las manos un poco más anchas que el ancho de los hombros. Despega la barra del soporte y "
                       "lentamente baja el peso hacia tu pecho, doblando los codos. Una vez que el peso toque tu pecho, empújalo hacia arriba hasta "
                       "que los brazos estén completamente extendidos. Baja de nuevo el peso y repite el movimiento. "
    },
    "Prensa de pecho convergente": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en la máquina de prensa de pecho convergente con los brazos a los lados y los codos doblados. Agarra los mangos "
                       "con las palmas de las manos mirando hacia adelante. Presiona los mangos hacia adelante y entre sí, llevando los brazos "
                       "hacia el centro de tu cuerpo. Extiende completamente los brazos y luego regresa controladamente a la posición inicial. "
                       "Mantén una postura estable durante todo el movimiento. Repite el ejercicio. "
    },
    "Prensa de mancuernas en banco": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Acuéstate en un banco horizontal con una mancuerna en cada mano, sosteniéndolas sobre tu pecho con los codos doblados. "
                       "Asegúrate de que tus pies estén firmemente apoyados en el suelo. Presiona las mancuernas hacia arriba hasta que los brazos "
                       "estén completamente extendidos, luego baja las mancuernas de manera controlada hacia los lados de tu pecho. Mantén una "
                       "forma controlada y repite el movimiento. "
    },
    "Prensa de banca en máquina Smith": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Acuéstate en un banco plano debajo de la barra guiada de la máquina Smith. Asegura la barra a la altura adecuada para tus "
                       "preferencias. Coloca tus manos un poco más anchas que el ancho de tus hombros y desengancha la barra. Baja la barra hacia "
                       "tu pecho de manera controlada y luego empújala hacia arriba hasta que tus brazos estén extendidos. "
    },
    "Prensa Spoto": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una barra cargada, pero no toques el pecho con la barra durante el ejercicio (como lo "
                       "harías en una press de pecho convencional). En lugar de eso, detén el descenso justo antes de que la barra toque el pecho, "
                       "manteniendo los músculos bajo tensión. Luego, vuelve a subir la barra a la posición inicial sin rebote. "
    },
    "Prensa de banca con agarre cerrado": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una barra, pero esta vez coloca tus manos más cerca una de la otra, manteniendo los codos "
                       "cerca del cuerpo. Desciende la barra controladamente hacia el pecho y luego empújala hacia arriba, "
                       "extendiendo completamente los brazos. "
    },
    "Prensa con barra de fútbol": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano y agarra una barra de fútbol, que tiene múltiples agarres neutrales. Alinea la barra con tu "
                       "pecho y presiona hacia arriba, extendiendo los brazos. Baja la barra de nuevo hacia el pecho de manera controlada y repite "
                       "el movimiento. "
    },
    "Prensa de mancuernas con agarre invertido": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una mancuerna en cada mano. En lugar de tener las palmas mirando hacia adelante, "
                       "gira las muñecas para que las palmas de las manos miren hacia ti (agarre invertido). Asegúrate de que los codos estén "
                       "ligeramente doblados y presiona las mancuernas hacia arriba, extendiendo los brazos. Controla el descenso al bajar las "
                       "mancuernas de nuevo a la posición inicial. Realiza repeticiones manteniendo el agarre invertido durante todo el ejercicio. "
    },
    "Prensa guitollina": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una barra, pero en lugar de bajar la barra hacia el centro del pecho, desciéndela hacia la "
                       "parte superior del pecho, cerca de la línea del cuello. Asegúrate de mantener los codos apuntando hacia afuera durante todo "
                       "el movimiento. Presiona la barra hacia arriba hasta que los brazos estén extendidos y luego baja controladamente. "
    },
    "Prensa inclinada en máquina": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Ajusta el asiento y el respaldo de la máquina para que estén en un ángulo inclinado. Siéntate en la máquina y agarra las "
                       "empuñaduras con las manos. Presiona las empuñaduras hacia adelante y hacia arriba, extendiendo tus brazos, hasta que tus "
                       "brazos estén casi completamente rectos. Luego, baja controladamente las empuñaduras de vuelta a la posición inicial. "
    },
    "Prensa inclinada": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco inclinado con un ángulo de aproximadamente 15 a 30 grados, sosteniendo una barra o mancuernas a la "
                       "altura de los hombros. Asegúrate de que tus pies estén apoyados en el suelo. Luego, empuja la barra o las mancuernas hacia "
                       "arriba, extendiendo completamente los brazos. Desciende controladamente el peso de vuelta a la posición inicial, "
                       "manteniendo los codos ligeramente doblados. Repite el movimiento. "
    },
    "Prensa alterna de mancuernas": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una mancuerna en cada mano, sosteniéndolas sobre tus hombros con los codos doblados. "
                       "Levanta una mancuerna hacia arriba mientras mantienes la otra en la posición inicial. Extiende completamente el brazo "
                       "levantado y luego baja la mancuerna de manera controlada. Alterna entre ambos brazos, manteniendo un ritmo constante. "
    },
    "Prensa de mancuernas inclinado con agarre invertido": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Recuéstate en un banco inclinado con mancuernas en cada mano, pero con las palmas de las manos hacia ti (agarre invertido). "
                       "Ajusta el banco para que esté inclinado a un ángulo cómodo. Levanta las mancuernas sobre tu pecho con los codos ligeramente "
                       "doblados. Desde esta posición, presiona las mancuernas hacia arriba, extendiendo los brazos. Luego, baja las mancuernas de "
                       "manera controlada de vuelta a la posición inicial. "
    },
    "Prensa en el suelo": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en el suelo, preferiblemente en un rack de potencia o con las piernas extendidas. Sostén una barra con pesas o "
                       "mancuernas directamente sobre tu pecho con los codos ligeramente flexionados. Asegúrate de que los codos toquen ligeramente "
                       "el suelo. Desde esta posición, presiona la barra o las mancuernas hacia arriba, extendiendo completamente los brazos. Baja "
                       "controladamente el peso de vuelta a la posición inicial sin dejar que los codos toquen el suelo. Repite el movimiento. "
    },
    "Prensa en máquina landmine": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Coloca una barra en la máquina Landmine, sujetando un extremo de la barra con ambas manos. Párate con los pies a la altura "
                       "de los hombros y realiza una ligera flexión en las rodillas. Contrae los músculos del pecho y los hombros, luego presiona "
                       "la barra hacia afuera frente a ti, manteniendo un agarre firme y apretando los músculos del pecho en la parte superior del "
                       "movimiento. Regresa la barra controladamente a la posición inicial y repite. "
    },
    "Prensa con hexágono": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una mancuerna hexagonal (hexágono) en cada mano. Mantén las mancuernas directamente sobre "
                       "tu pecho, con las palmas enfrentadas y los codos ligeramente doblados. Desde esta posición, presiona las mancuernas hacia "
                       "arriba, extendiendo completamente los brazos. Controla el descenso al bajar las mancuernas de nuevo a la posición inicial. "
                       "Repite el movimiento. "
    },
    "Apertura con polea baja": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Para realizar las aperturas de pectorales con polea baja, colócate de pie frente a una máquina de polea con las poleas en "
                       "la posición más baja. Sujeta un asa en cada mano, con los brazos extendidos hacia los lados y ligeramente doblados. Mantén "
                       "un pie adelante para mayor estabilidad. Luego, cruza las manos frente a tu cuerpo de manera controlada, manteniendo una "
                       "ligera flexión en los codos, hasta que sientas un estiramiento en el pecho. Regresa las manos a la posición inicial y "
                       "repite el movimiento. "
    },
    "Apertura con mancuernas": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Acuéstate en un banco plano con una mancuerna en cada mano, sosteniéndolas sobre tu pecho con los brazos extendidos y las "
                       "palmas mirándose entre sí. Baja lentamente los brazos hacia los lados, manteniendo una ligera flexión en los codos, "
                       "hasta que sientas un estiramiento en el pecho. Luego, regresa las mancuernas a la posición inicial, contrayendo los "
                       "músculos del pecho. "
    },
    "Apertura con polea alta": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Colócate de pie frente a una máquina de poleas con las poleas ajustadas en la posición más alta. Agarra las poleas con "
                       "ambas manos, una en cada mano, y da un paso hacia atrás para que tus brazos estén extendidos frente a ti. Mantén una ligera "
                       "flexión en los codos. Con control, lleva tus brazos hacia abajo y hacia adelante, como si estuvieras abrazando a alguien, "
                       "manteniendo la misma flexión en los codos. Luego, vuelve a la posición inicial, manteniendo el control en todo momento. "
                       "Repite el movimiento. "
    },
    "Máquina contractora con brazos flexionados": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Siéntate en la máquina contractora con los brazos doblados en un ángulo de aproximadamente 90 grados. Asegúrate de que los "
                       "codos estén alineados con tus hombros. Agarra las asas de la máquina con las palmas hacia adentro. Luego, empuja las asas "
                       "juntando los codos frente a tu pecho, contrae los músculos pectorales y luego regresa lentamente a la posición inicial. "
                       "Mantén una suave flexión en los codos durante todo el movimiento. Repite según sea necesario. "
    },
    "Apertura con cables en banco inclinado": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Acuéstate en un banco inclinado, asegurando que esté ajustado a un ángulo moderado. Con un cable en cada mano, "
                       "situados a ambos lados del banco, realiza un movimiento de apertura hacia afuera y hacia abajo, manteniendo una ligera "
                       "flexión en los codos. Lleva las manos hacia el centro de tu pecho y contrae los músculos pectorales. Luego, "
                       "regresa controladamente a la posición inicial. "
    },
    "Apertura con polea": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Colócate de pie entre dos poleas ajustables en un gimnasio, con ambas poleas posicionadas a la altura de tus hombros. "
                       "Sujeta una manija en cada mano y da unos pasos hacia adelante para crear tensión en los cables. Con los codos ligeramente "
                       "flexionados, lleva las manos hacia el frente y entre sí, como si estuvieras abrazando a alguien. Contrae los músculos del "
                       "pecho en la parte superior del movimiento y luego regresa controladamente a la posición inicial. Repite el movimiento. "
    },
    "Fondo": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 5,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Colócate entre dos barras paralelas con las manos apoyadas en cada barra y los brazos extendidos. Mantén el cuerpo recto y "
                       "los pies ligeramente elevados del suelo. Flexiona los codos para bajar el cuerpo hacia abajo, manteniendo el torso "
                       "vertical. Luego, extiende los codos para elevar tu cuerpo de nuevo a la posición inicial. Repite el movimiento. "
    },
    "Flexión en desnivel con peso": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 5,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Coloca una plataforma o superficie elevada, como una caja, bajo tus manos y otra bajo tus pies. Asegura una placa de peso "
                       "en tu espalda o usa una mochila con peso. Luego, adopta la posición de flexión con las manos en la plataforma y los pies en "
                       "la plataforma elevada. Realiza una flexión manteniendo una línea recta desde los hombros hasta los pies. Empuja hacia "
                       "arriba hasta que los brazos estén completamente extendidos y luego baja el cuerpo controladamente. Repite el movimiento. "
    },
    "Flexión en anillas": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Para realizar las flexiones en anillas, asegúrate de tener un par de anillas ajustables suspendidas de una barra o "
                       "estructura estable a una altura adecuada. Agarra las anillas con las palmas hacia abajo y colócate en posición de plancha "
                       "alta con el cuerpo recto, los brazos extendidos y las piernas juntas. Baja tu cuerpo flexionando los codos mientras "
                       "mantienes el equilibrio en las anillas. Lleva el pecho hacia abajo y luego presiona hacia arriba para volver a la posición "
                       "inicial. Ajusta la altura de las anillas según tu nivel de dificultad. "
    },
    "Flexión de brazos": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 6,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Comienza en una posición de plancha con las manos colocadas ligeramente más anchas que la anchura de los hombros. Mantén el "
                       "cuerpo en línea recta desde la cabeza hasta los talones, con los codos extendidos. Desciende el cuerpo hacia el suelo "
                       "doblando los codos, manteniendo el cuerpo alineado, y luego vuelve a la posición inicial extendiendo los codos. Asegúrate "
                       "de mantener el núcleo contraído durante todo el movimiento. Repite el ejercicio. "
    },
    "Flexión declinada": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 25,
        "priority": ASSISTANCE,
        "description": "Colócate en posición de plancha con tus manos apoyadas en el suelo y tus pies elevados sobre un banco o una superficie "
                       "elevada. Mantén tu cuerpo recto desde la cabeza hasta los talones. Realiza una flexión bajando el cuerpo hacia el suelo y "
                       "luego vuelve a la posición inicial, manteniendo el núcleo comprometido. "
    },
    "Flexión con banda de resistencia": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 25,
        "priority": ASSISTANCE,
        "description": "Coloca una banda de resistencia alrededor de tu espalda y sujeta los extremos con las manos, de manera que la banda cruce "
                       "tu espalda. Adopta la posición de flexión con las manos separadas a la altura de los hombros y los pies apoyados en el "
                       "suelo. Realiza flexiones manteniendo la resistencia de la banda, descendiendo tu cuerpo hacia el suelo y luego empujándolo "
                       "hacia arriba. "
    },
    "Flexión diamante": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 6,
        "max_reps": 25,
        "priority": ASSISTANCE,
        "description": "Comienza en posición de plancha con las manos colocadas debajo del pecho, formando un diamante con los pulgares y los "
                       "índices. Mantén el cuerpo en línea recta desde la cabeza hasta los talones. Baja el cuerpo flexionando los codos y "
                       "acercando el pecho al suelo, manteniendo los codos cerca del cuerpo. Luego, empuja hacia arriba para volver a la posición "
                       "inicial. Repite el movimiento. "
    },
    "Flexión con palmada": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 4,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Comienza en posición de flexión con las manos colocadas ligeramente más anchas que los hombros. Realiza una flexión normal, "
                       "pero al empujarte hacia arriba con fuerza, levanta las manos del suelo y aplaude en el aire antes de volver a colocarlas en "
                       "posición para la siguiente repetición. "
    },
    "Flexión en plancha": {
        "difficulty": ADVANCED,
        "effectiveness": 3,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Comienza en una posición de plancha, con las manos colocadas en el suelo, los brazos completamente extendidos y el cuerpo "
                       "en línea recta desde la cabeza hasta los pies. Desplaza gradualmente el peso hacia adelante, permitiendo que tus hombros se "
                       "muevan más allá de tus muñecas. Mientras mantienes esta posición, realiza una flexión de brazos descendiendo tu torso hacia "
                       "el suelo y luego vuelve a la posición inicial, extendiendo los brazos. "
    },
    "Vuelo en Anillas": {
        "difficulty": ADVANCED,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 15,
        "priority": TERTIARY,
        "description": "Cuelga anillas a una altura adecuada y agarra cada anilla con las palmas mirándose entre sí. Extiende los brazos hacia los "
                       "lados manteniendo una ligera flexión en los codos. Con control, baja el cuerpo hacia adelante y hacia abajo, "
                       "abriendo los brazos en forma de vuelo, hasta que sientas un estiramiento en el pecho. Luego, utiliza la fuerza del pecho "
                       "para volver a la posición inicial cerrando los brazos. "
    }
}

pull_exercises = {
    "Polea al pecho con agarre cerrado/neutro": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en una máquina de polea alta con una barra o empuñadura cerrada y neutral. Agarra la barra o empuñadura con las "
                       "manos a una distancia cercana o con las palmas enfrentándose entre sí. Extiende completamente los brazos y luego tira de la "
                       "barra hacia abajo hacia la parte superior del pecho mientras mantienes la espalda recta. Contrae los músculos de la espalda "
                       "durante el movimiento. Luego, vuelve a estirar los brazos para regresar a la posición inicial. Repite el ejercicio. "
    },
    "Tirón diagonal iliaco": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Arrodillate en una máquina de poleas alta de manera que quedes a un ángulo diagonal con respecto a la polea. Agarra el asa "
                       "con una mano, estirada por encima de tu hombro en la dirección diagonal de la polea. Tira hacia abajo, llevando el asa "
                       "hacia la cadera opuesta mientras mantienes la espalda recta y los codos doblados. Luego, regresa el asa a la posición "
                       "inicial de manera controlada. Repite el movimiento. "
    },
    "Polea al pecho con agarre supino": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en una máquina de polea alta con una barra de agarre ancho y las palmas de las manos mirando hacia ti (agarre "
                       "supinado). Asegúrate de que tus rodillas estén debajo de las almohadillas y los muslos estén fijos. Extiende completamente "
                       "los brazos y luego tira de la barra hacia abajo hacia tu pecho, llevando los codos hacia abajo y hacia atrás. Mantén la "
                       "contracción en la parte superior por un segundo y luego vuelve a la posición inicial de manera controlada. Repite el "
                       "movimiento. "
    },
    "Pullover con polea alta": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie frente a una máquina de poleas con una barra larga o una cuerda en la polea alta, sujeta la barra o cuerda con las "
                       "manos un poco más anchas que el ancho de los hombros. Mantén los codos ligeramente doblados y los pies firmemente en el "
                       "suelo. Inclínate ligeramente hacia adelante desde la cintura, manteniendo la espalda recta. Luego, tira hacia abajo de la "
                       "barra o cuerda, llevándola hacia la parte superior de tu pecho. Extiende los brazos hacia arriba y repite el movimiento. "
    },
    "Polea al pecho con agarre amplio": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en una máquina de polea alta con un asiento ajustable y un agarre en forma de barra amplia. Asegúrate de que tus "
                       "muslos estén sujetos debajo de los rodillos acolchados y que tus pies estén planos en el suelo. Agarra la barra con las "
                       "manos colocadas más allá del ancho de tus hombros. Tira de la barra hacia abajo hacia la parte superior de tu pecho, "
                       "manteniendo los codos apuntando hacia abajo y hacia atrás. Luego, regresa la barra de manera controlada a la posición "
                       "inicial, estirando completamente los brazos. Repite el movimiento. "
    },
    "Dominada": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 3,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Cuelga de una barra de dominadas con las palmas de las manos mirando hacia afuera y a una distancia un poco más ancha que "
                       "el ancho de los hombros. Extiende los brazos completamente. Mantén tu cuerpo recto y luego, utilizando la fuerza de tus "
                       "brazos y espalda, levanta tu cuerpo hacia la barra hasta que tu barbilla esté por encima de ella. Baja tu cuerpo de manera "
                       "controlada hasta que tus brazos estén completamente extendidos nuevamente. Repite el movimiento. "
    },
    "Dominada supina": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 3,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Cuelga de una barra horizontal con las palmas de las manos hacia ti, aproximadamente a la anchura de los hombros. Asegúrate "
                       "de que tus brazos estén completamente extendidos. Luego, lleva tu cuerpo hacia arriba al flexionar los codos, "
                       "manteniendo la barbilla por encima de la barra. Desciende lentamente tu cuerpo hasta que los brazos estén completamente "
                       "extendidos nuevamente y repite el movimiento. "
    },
    "Dominada con agarre neutro": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 3,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Agarra una barra horizontal con las palmas de las manos mirándose entre sí, en una posición de agarre neutral. Cuelga del "
                       "soporte y asegúrate de que tu cuerpo esté completamente extendido. Luego, con la fuerza de tus brazos y la espalda, "
                       "levanta tu cuerpo hacia la barra. Mantén los codos cerca de tu cuerpo durante el ascenso y desciende lentamente hasta que "
                       "tus brazos estén completamente extendidos nuevamente. Repite el movimiento. "
    },
    "Pullover": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 10,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con solo tu parte superior de la espalda y tus hombros apoyados en el banco. Sujeta una "
                       "mancuerna con ambas manos, manteniendo los brazos extendidos sobre tu pecho. Lentamente, baja la mancuerna hacia atrás y "
                       "por encima de tu cabeza, manteniendo una ligera flexión en los codos. Luego, regresa la mancuerna a la posición inicial "
                       "sobre tu pecho. "
    },
    "Polea trasnuca": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en una máquina de polea alta con una barra larga en la parte superior. Agarra la barra con las manos separadas a "
                       "una distancia un poco mayor que el ancho de los hombros, con las palmas mirando hacia adelante. Inclina ligeramente el "
                       "torso hacia adelante y tira de la barra hacia abajo detrás de la cabeza, llevando la barra hacia la nuca. Luego, "
                       "lentamente regresa la barra a la posición inicial. "
    },
    "Muscle Up": {
        "difficulty": ADVANCED,
        "effectiveness": 5,
        "min_reps": 2,
        "max_reps": 10,
        "priority": MAIN_MOVEMENT,
        "description": "Comienza colgando de una barra fija con las manos colocadas más anchas que el ancho de los hombros y las palmas mirando "
                       "hacia adelante. Luego, realiza una dominada explosiva para llevar tu pecho por encima de la barra. En el punto más alto de "
                       "la dominada, inclina tu torso hacia adelante y empuja hacia arriba con tus manos para pasar por encima de la barra. "
                       "Finaliza estirando los brazos por completo. Luego, invierte el movimiento para volver a la posición inicial, "
                       "bajando de manera controlada. Repite el movimiento. "
    }
}

press_exercises = {
    "Press militar con barra": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 5,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "De pie, coloca una barra sobre tus hombros, con las manos ligeramente más anchas que el ancho de los hombros. Asegúrate de "
                       "que tus pies estén a la altura de los hombros. Presiona la barra hacia arriba sobre tu cabeza, extendiendo completamente "
                       "los brazos. Baja la barra de manera controlada de regreso a la posición inicial, manteniendo los codos ligeramente "
                       "flexionados. Repite el movimiento. "
    },
    "Prensa de sobrecarga con barra trampa": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 5,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Párate en el centro de una barra trampa (hexagonal), con los pies a la altura de los hombros. Agarra las asas de la barra "
                       "con las palmas mirando hacia adentro. Levanta la barra hacia arriba, extendiendo completamente los brazos sobre tu cabeza. "
                       "Asegúrate de mantener una postura erguida y controla el movimiento al bajar la barra de nuevo a la posición inicial. "
    },
    "Prensa de hombros en máquina": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 5,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en la máquina de prensa de hombros con la espalda bien apoyada y ajusta el asiento según tu altura. Coloca tus "
                       "manos en las asas de la máquina a la altura de los hombros. Presiona las asas hacia arriba, extendiendo completamente los "
                       "brazos. Asegúrate de controlar el movimiento durante la fase ascendente y baja las asas lentamente a la posición inicial. "
    },
    "Prensa de hombros con mancuernas sentado": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Siéntate en un banco con respaldo vertical, sosteniendo una mancuerna en cada mano a la altura de los hombros. Mantén la "
                       "espalda recta y los pies apoyados en el suelo. Desde esta posición, levanta las mancuernas hacia arriba sobre tu cabeza, "
                       "extendiendo completamente los brazos. Asegúrate de mantener la estabilidad y control durante todo el movimiento. Baja las "
                       "mancuernas lentamente de regreso a la posición inicial y repite. "
    },
    "Prensa inclinada con agarre cerrado": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 5,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco inclinado, con las manos sosteniendo la barra a una distancia más estrecha que el ancho de los "
                       "hombros. Asegúrate de que la inclinación del banco esté configurada adecuadamente. Desciende la barra hacia el centro de tu "
                       "pecho, manteniendo los codos cerca de tu cuerpo. Luego, impulsa la barra hacia arriba hasta que los brazos estén "
                       "completamente extendidos. "
    },
    "Prensa atrás del cuello": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie, sostén una barra con ambas manos a la altura de los hombros, pero ubicada detrás de tu cuello. Los pies deben estar "
                       "separados a la altura de los hombros. Presiona la barra hacia arriba, extendiendo completamente los brazos, y luego baja la "
                       "barra de regreso a la posición inicial detrás del cuello. "
    },
    "Press de banca inclinado": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco inclinado con mancuernas en cada mano, colocadas a la altura de los hombros. Asegúrate de que el "
                       "banco esté inclinado a un ángulo de aproximadamente 15 a 30 grados. Con los pies apoyados en el suelo, baja las mancuernas "
                       "hacia los lados de tu pecho, manteniendo los codos ligeramente doblados. Luego, impulsa las mancuernas hacia arriba hasta "
                       "que los brazos estén completamente extendidos. Desciende las mancuernas controladamente y repite el movimiento. "
    },
    "Prensa inclinada en máquina": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Ajusta la máquina de prensa inclinada de manera que el respaldo esté en un ángulo inclinado. Siéntate en la máquina y "
                       "ajusta la altura del asiento para que tus manos queden a la altura de tus hombros. Agarra las asas o barras de la máquina "
                       "con las manos y empuja hacia adelante, extendiendo completamente los brazos. Controladamente, baja la resistencia de la "
                       "máquina hacia tu pecho y luego vuelve a la posición inicial. Repite el movimiento. "
    },
    "Prensa Arnold": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Siéntate en un banco con respaldo vertical, sosteniendo una mancuerna en cada mano a la altura de los hombros, "
                       "con las palmas de las manos mirándote. Inicia el movimiento elevando las mancuernas mientras rotas tus muñecas, "
                       "de modo que al final del movimiento, las palmas de las manos estén orientadas hacia adelante y los brazos estén "
                       "completamente extendidos sobre la cabeza. Desciende las mancuernas de manera controlada, revirtiendo la rotación de las "
                       "muñecas. Repite el movimiento. "
    },
    "Prensa con barra en una sola mano": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Coloca una barra en el suelo y asegúrala en un ángulo fijo con una almohadilla protectora. Parado junto a la barra, "
                       "agarra el extremo libre con una mano, manteniendo el codo flexionado. Desde esta posición, empuja la barra hacia arriba, "
                       "extendiendo completamente el brazo. Luego, baja la barra de manera controlada de vuelta a la posición inicial. Realiza el "
                       "ejercicio con una sola mano y repite en ambos lados. "
    },
    "Prensa de balancín": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Comienza de pie, sosteniendo una mancuerna en cada mano a los lados del cuerpo, con las palmas mirando hacia adelante. "
                       "Eleva una mancuerna directamente sobre la cabeza mientras mantienes la otra cerca del hombro. Alterna presionando una "
                       "mancuerna hacia arriba mientras la otra permanece en la posición inicial. "
    },
    "Flexión en anillas con declive": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 8,
        "min_reps": 5,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate en posición de plancha con los pies elevados y apoyados en anillas suspendidas a baja altura. Asegúrate de que las "
                       "anillas estén alineadas con tus hombros. Realiza flexiones manteniendo el cuerpo en línea recta, descendiendo el pecho "
                       "hacia las anillas y luego empujando hacia arriba para volver a la posición inicial. "
    },
    "Flexión declinada": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 5,
        "min_reps": 5,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate en posición de plancha con los pies elevados sobre una superficie elevada, como un banco o una plataforma. Mantén "
                       "las manos en el suelo, ligeramente más anchas que el ancho de los hombros. Realiza una flexión bajando el cuerpo hacia el "
                       "suelo y luego vuelve a la posición inicial, manteniendo el cuerpo en línea recta. "
    },
    "Prensa de mancuerna de circo": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 5,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Colócate de pie con las piernas separadas a la altura de los hombros. Levanta una mancuerna de forma unilateral, "
                       "llevándola al hombro. Mantén una postura estable y presiona la mancuerna hacia arriba sobre tu cabeza hasta que el brazo "
                       "esté completamente extendido. Baja la mancuerna de manera controlada a la posición inicial. "
    },
    "Flexión en pino": {
        "difficulty": ADVANCED,
        "effectiveness": 9,
        "min_reps": 3,
        "max_reps": 12,
        "priority": MAIN_MOVEMENT,
        "description": "Comienza en una posición de pino contra una pared, con las manos colocadas firmemente en el suelo y los talones apoyados "
                       "contra la pared. Mantén el cuerpo en línea recta y baja lentamente la cabeza hacia el suelo doblando los codos, "
                       "luego presiona hacia arriba para volver a la posición inicial. "
    },
}

shoulders_exercises = {
    "Elevación lateral con cable": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 10,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate de pie junto a una máquina de poleas con el brazo de la polea ajustado a la altura más baja. Sujeta el mango con "
                       "una mano y mantén una ligera flexión en el codo. Eleva el brazo lateralmente hasta que esté paralelo al suelo, "
                       "manteniendo la posición por un momento. Luego, baja el brazo de manera controlada. "
    },
    "Tracción facial con anillas": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Colócate debajo de unas anillas suspendidas, agarrándolas con ambas manos y extendiendo los brazos frente a ti. Inclínate "
                       "hacia atrás manteniendo el cuerpo recto y tira de las anillas hacia tu rostro, manteniendo los codos elevados y paralelos "
                       "al suelo. Lleva las anillas hacia los lados de tu cabeza, enfocándote en activar los músculos del hombro y la parte "
                       "superior de la espalda. Vuelve a la posición inicial de manera controlada y repite. "
    },
    "Elevación lateral egipcia": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Párate con los pies a la altura de los hombros, utilizando una máquina de cable. El cable debe pasar entre tus piernas. "
                       "Sujeta el asa con una mano y realiza una elevación lateral, manteniendo el brazo ligeramente doblado. Lleva el brazo hasta "
                       "la altura de los hombros o un poco más arriba, luego baja de manera controlada a la posición inicial. Repite el movimiento "
                       "con la otra mano. "
    },
    "Tracción facial con cable": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Conéctate a un sistema de poleas con una cuerda o una banda en posición alta. Párate frente a la máquina, agarra la cuerda "
                       "con ambas manos y retrocede unos pasos. Mantén los codos elevados a la altura de los hombros y tira de la cuerda hacia tu "
                       "cara, asegurándote de mantener los codos en alto y separados. Contrae los músculos de la parte superior de la espalda y los "
                       "hombros al realizar el movimiento. Luego, regresa la cuerda controladamente a la posición inicial. "
    },
    "Elevación vertical": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie, sostén una barra con ambas manos, colocadas ligeramente más estrechas que el ancho de tus hombros. Levanta la barra "
                       "hacia arriba, manteniéndola cerca de tu cuerpo, hasta que llegue justo debajo de tu barbilla. Asegúrate de que tus codos "
                       "estén apuntando hacia afuera. Desciende la barra lentamente de regreso a la posición inicial y repite el movimiento. "
    },
    "Elevación lateral con mancuernas": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 10,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Párate con los pies separados a la anchura de los hombros, con una mancuerna en cada mano a los lados del cuerpo y las "
                       "palmas mirando hacia dentro. Mantén una ligera flexión en los codos y levanta ambos brazos hacia afuera y hacia arriba "
                       "hasta que estén paralelos al suelo, manteniendo los codos ligeramente flexionados. Luego, baja lentamente las mancuernas de "
                       "regreso a la posición inicial. Controla el movimiento y evita usar impulso. "
    },
    "Remo con mancuerna para deltoides posterior": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Ponte de pie con las piernas separadas al ancho de los hombros, sosteniendo una mancuerna en cada mano. Inclínate "
                       "ligeramente hacia adelante desde la cintura, manteniendo la espalda recta. Con los brazos extendidos hacia abajo y las "
                       "palmas mirando hacia adentro, lleva las mancuernas hacia arriba y hacia los lados, doblando los codos y manteniendo los "
                       "brazos cerca del cuerpo. Contrae los músculos de los hombros mientras llevas las mancuernas hacia arriba y luego baja "
                       "lentamente a la posición inicial. "
    },
    "Elevación en banco inclinado": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Acuéstate en un banco inclinado, con el pecho hacia abajo y los pies apoyados en el suelo. Sujeta una mancuerna en cada "
                       "mano, colgando directamente debajo de los hombros. Eleva los brazos hacia los lados, manteniendo los codos ligeramente "
                       "flexionados, hasta que estén en línea con los hombros. Desciende las mancuernas de manera controlada y repite el movimiento. "
    },
    "Elevación Lu": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "De pie con los pies a la altura de los hombros, sostén una mancuerna en cada mano a los costados del cuerpo, con las palmas "
                       "mirándose entre sí. Levanta ambos brazos hacia los lados y continúa el movimiento más allá de la posición normal, "
                       "permitiendo que las mancuernas choquen ligeramente sobre la cabeza. Asegúrate de mantener una buena forma y control en todo "
                       "momento. Luego, baja las mancuernas de manera controlada a la posición inicial. "
    },
    "Elevación lateral invertida": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 10,
        "max_reps": 30,
        "priority": TERTIARY,
        "description": "Siéntate en un banco con una mancuerna en cada mano, con los pies apoyados en el suelo. Inclínate hacia adelante desde la "
                       "cintura, manteniendo la espalda recta. Deja que los brazos cuelguen directamente debajo de los hombros, con las palmas "
                       "enfrentadas entre sí. Levanta las mancuernas hacia los lados, manteniendo los codos ligeramente flexionados, hasta que tus "
                       "brazos estén paralelos al suelo. Luego, baja las mancuernas de manera controlada a la posición inicial y repite el "
                       "movimiento. "
    },
    "Elevación frontal con pulgares hacia arriba": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "De pie, sostén una mancuerna en cada mano con los brazos extendidos hacia abajo y las palmas mirando hacia tu cuerpo con "
                       "los pulgares hacia arriba. Manteniendo los brazos rectos, levanta las mancuernas hacia adelante hasta que estén paralelas "
                       "al suelo. Luego, baja las mancuernas lentamente a la posición inicial. "
    },
    "Elevación amplia con cable": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Colócate de pie en el centro de una máquina de cables con las poleas posicionadas en los lados bajos. Agarra las asas con "
                       "las palmas de las manos hacia abajo y las manos cruzadas frente a ti. Mantén una ligera flexión en los codos y levanta los "
                       "brazos hacia los lados hasta que estén paralelos al suelo. Contrae los músculos de los hombros en la parte superior del "
                       "movimiento y luego baja los brazos de manera controlada a la posición inicial. "
    },
    "Balanceo de deltoides posterior en banco inclinado": {
        "difficulty": ADVANCED,
        "effectiveness": 5,
        "min_reps": 6,
        "max_reps": 15,
        "priority": TERTIARY,
        "description": "Acuéstate boca abajo en un banco inclinado, con el torso extendido y la cabeza en la parte superior del banco. Sujeta una "
                       "mancuerna en cada mano, colgando hacia el suelo. Desde esta posición, realiza un movimiento de balanceo hacia arriba y "
                       "hacia afuera con los brazos, enfocándote en contraer los deltoides posteriores. Mantén los codos ligeramente flexionados y "
                       "controla el movimiento en todo momento. Retorna a la posición inicial y repite el ejercicio. "
    }
}

curl_exercises = {
    "Curl predicador": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Siéntate en el banco Scott con el pecho apoyado contra el soporte acolchado. Agarra la barra Z (Ez-bar) con las manos en "
                       "una posición más estrecha que el ancho de los hombros, permitiendo que los brazos cuelguen rectos hacia abajo. Con los "
                       "codos apoyados en el banco, levanta la barra hacia arriba mediante la flexión de los codos, llevando la barra hacia tus "
                       "hombros. Haz una pausa en la contracción y luego baja la barra de manera controlada hasta la posición inicial. Repite el "
                       "movimiento. "
    },
    "Curl de araña": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 6,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate boca abajo en un banco inclinado de manera que tus hombros y pecho estén fuera del banco. Sujeta una barra EZ con "
                       "un agarre en supinación (palmas hacia arriba) y asegúrate de que tus brazos cuelguen libremente hacia el suelo. Desde esta "
                       "posición, realiza el curl flexionando los codos, llevando la barra hacia la parte superior de tu frente. Mantén los codos "
                       "fijos en su lugar y contrae los músculos del bíceps en la parte superior del movimiento antes de bajar la barra de nuevo "
                       "hacia abajo. Repite el proceso. "
    },
    "Curl con barra EZ de agarre cerrado": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Parado, agarra una barra EZ con las manos colocadas más cerca que el ancho de los hombros, manteniendo los codos pegados al "
                       "cuerpo. Con las palmas hacia arriba, lleva la barra hacia arriba contrayendo los músculos de los bíceps. Luego, "
                       "baja la barra lentamente hasta la posición inicial, manteniendo el control. Repite el movimiento. "
    },
    "Curl con barra Z": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 6,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "De pie, sostén una barra Z con ambas manos, con las palmas hacia adelante y las manos separadas a una distancia cómoda. "
                       "Mantén los codos pegados al cuerpo y levanta la barra hacia los hombros mediante la flexión de los codos. Asegúrate de "
                       "contraer los músculos del bíceps en la parte superior del movimiento. Luego, baja la barra de manera controlada hasta la "
                       "posición inicial. Repite el movimiento. "
    },
    "Curl predicador con mancuernas": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Siéntate en un banco Scott (con respaldo inclinado y almohadilla para los codos) sosteniendo una mancuerna en cada mano, "
                       "con los brazos extendidos y las palmas hacia arriba. Asegúrate de que tus brazos estén apoyados en el banco y que tus "
                       "axilas estén alineadas con la parte superior del banco. Flexiona los codos para levantar las mancuernas hacia tus hombros, "
                       "manteniendo los brazos en contacto con el banco. Luego, baja las mancuernas de manera controlada hasta la posición inicial. "
    },
    "Curl con cable": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate frente a una máquina de poleas con un agarre de cable en cada mano, manteniendo los codos cerca del cuerpo. Mantén "
                       "los pies a la altura de los hombros. Inicia el movimiento doblando los codos y llevando las manos hacia los hombros, "
                       "contrayendo los músculos del bíceps. Luego, baja lentamente las manos a la posición inicial. "
    },
    "Curl con mancuernas de pie": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie, sostén una mancuerna en cada mano a los lados del cuerpo, con las palmas mirando hacia adelante. Mantén los codos "
                       "cerca del cuerpo y levanta las mancuernas hacia los hombros, contrae los músculos del bíceps en la parte superior del "
                       "movimiento. Luego, baja las mancuernas de manera controlada a la posición inicial. Repite el movimiento. "
    },
    "Curl de barra": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie, con los pies separados a la altura de los hombros, sujeta una barra con ambas manos, manteniendo las palmas hacia "
                       "adelante y los codos cerca del cuerpo. Lentamente levanta la barra hacia los hombros, contrae los músculos del bíceps en la "
                       "parte superior del movimiento. Desciende la barra de manera controlada de vuelta a la posición inicial. Repite el "
                       "movimiento. "
    },
    "Curl de cable por detrás de la espalda": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "De pie frente a una máquina de cables, ajusta la polea para que esté a la altura más baja. Colócate de espaldas a la "
                       "máquina y agarra las cuerdas con un agarre supino, con las manos separadas y los brazos completamente extendidos. Mantén "
                       "los codos pegados al cuerpo y lleva las manos hacia los hombros al contraer los bíceps. Luego, baja lentamente las cuerdas "
                       "de vuelta a la posición inicial. Repite el movimiento. "
    },
    "Curl de molinillo": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "De pie, sostén una mancuerna en cada mano a los lados del cuerpo con las palmas de las manos mirando hacia adelante. Mantén "
                       "una posición erguida y, manteniendo el codo pegado al cuerpo, realiza un curl con una mancuerna hacia el hombro mientras la "
                       "otra mancuerna permanece en posición baja. Alterna los curls de manera que siempre haya una mancuerna en la posición alta y "
                       "la otra en la posición baja. "
    },
    "Curl concentrado": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Siéntate en un banco con las piernas separadas. Sujeta una mancuerna en una mano y apoya el codo en la parte interna del "
                       "muslo de la pierna del mismo lado. Asegúrate de que el brazo que sostiene la mancuerna cuelgue libremente. Realiza el curl "
                       "al flexionar el codo, llevando la mancuerna hacia el hombro. Controla el movimiento y contrae el bíceps en la parte "
                       "superior del movimiento. Luego, baja la mancuerna de manera controlada a la posición inicial. Repite con la cantidad "
                       "deseada de repeticiones antes de cambiar al otro brazo. "
    },
    "Curl de bíceps con polea alta": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Ponte de pie frente a una máquina de poleas con la polea ajustada a la altura de tus hombros. Agarra las manijas o la barra "
                       "con un agarre supino (palmas hacia arriba), manteniendo los codos cerca de tu torso. Mantén una posición estable y contrae "
                       "los músculos del bíceps mientras flexionas los codos y llevas las manos hacia tus hombros. Haz una pausa en la posición "
                       "contraída y luego baja lentamente las manos de vuelta a la posición inicial. Repite el movimiento. "
    },
    "Curl martillo": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "De pie, sostén una mancuerna en cada mano a los lados del cuerpo, con las palmas de las manos mirando hacia los muslos. "
                       "Mantén los codos pegados al cuerpo y levanta las mancuernas hacia los hombros, manteniendo las palmas mirando hacia dentro "
                       "en todo momento. Baja las mancuernas de manera controlada a la posición inicial y repite el movimiento. "
    },
    "Curl de mancuernas sentado": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Siéntate en un banco con respaldo vertical, con una mancuerna en cada mano a los costados y los codos apoyados en las "
                       "piernas. Asegúrate de que los pies estén en el suelo. Realiza el curl levantando ambas mancuernas hacia los hombros, "
                       "manteniendo los codos pegados a las piernas. Haz una pausa en la posición contraída y luego baja las mancuernas de manera "
                       "controlada a la posición inicial. Repite el movimiento. "
    },
    "Curl en anillas": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Cuelga anillas de una barra a una altura adecuada. Sujeta las anillas con un agarre supino, manteniendo los brazos "
                       "extendidos. Eleva las manos hacia los hombros, doblando los codos y contrayendo los músculos del bíceps. Luego, "
                       "baja lentamente al punto inicial, manteniendo el control. "
    },
    "Curl pelícano": {
        "difficulty": ADVANCED,
        "effectiveness": 6,
        "min_reps": 5,
        "max_reps": 15,
        "priority": TERTIARY,
        "description": "Cuelga unas anillas a una altura adecuada, agarra las anillas con ambas manos y colócate en posición de suspensión. Mantén "
                       "las piernas extendidas y los brazos completamente estirados. Desde esta posición, flexiona los codos y lleva las manos "
                       "hacia los hombros, doblando los brazos mientras mantienes el cuerpo en posición horizontal. Luego, extiende los codos para "
                       "volver a la posición inicial. Repite el movimiento. "
    }
}

extend_exercises = {
    "Press banca con agarre cerrado": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 6,
        "max_reps": 15,
        "priority": MAIN_MOVEMENT,
        "description": "Acuéstate en un banco plano con una barra, pero en lugar de un agarre amplio, coloca las manos más cerca una de la otra, "
                       "con los dedos apuntando hacia arriba. Desciende la barra controladamente hacia la parte baja del pecho, manteniendo los "
                       "codos cerca del cuerpo. Luego, impulsa la barra de vuelta a la posición inicial, extendiendo completamente los brazos. "
    },
    "Press banca con barra suiza": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 6,
        "max_reps": 20,
        "priority": MAIN_MOVEMENT,
        "description": "Acuéstate en un banco plano y agarra una barra suiza con las manos colocadas en las distintas empuñaduras paralelas que "
                       "ofrece. Asegúrate de que tus pies estén firmemente apoyados en el suelo. Desciende la barra hacia tu pecho controladamente "
                       "y luego impúlsala hacia arriba, extendiendo completamente los brazos. "
    },
    "Extensión de cable por encima de la cabeza": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie frente a una máquina de poleas con una cuerda o barra conectada, toma la cuerda o la barra con ambas manos y "
                       "levántala sobre tu cabeza. Mantén los codos cerca de tus orejas. Luego, extiende los codos para llevar la cuerda o la barra "
                       "hacia abajo, estirando tus brazos completamente. Finalmente, vuelve a la posición inicial manteniendo el control y repite "
                       "el movimiento. "
    },
    "Extensión de tríceps acostado": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano o una superficie plana, sostén una barra EZ o recta sobre tu cabeza. Extiende los brazos "
                       "verticalmente hacia el techo, manteniendo los codos cerca de tu cabeza. Desde esta posición, dobla los codos lentamente "
                       "para bajar la barra hacia atras de tu cabeza, manteniendo los codos apuntando hacia el techo. Luego, extiende los brazos "
                       "nuevamente para volver a la posición inicial. "
    },
    "Prensa francesa": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie o sentado, sostén una mancuerna con ambas manos, manteniendo los codos doblados y los brazos extendidos sobre tu "
                       "cabeza. Asegúrate de que tus pies estén colocados de manera estable. Luego, baja la mancuerna detrás de tu cabeza "
                       "flexionando los codos y mantén la posición por un momento. Finalmente, vuelve a la posición inicial extendiendo los brazos. "
    },
    "Rompecráneos con polea": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate frente a una máquina de poleas con una barra recta o una cuerda conectada al cable. Acuéstate en un banco "
                       "horizontal y sujeta la barra o cuerda con un agarre de pronación, llevándola sobre tu cabeza. Mantén los codos fijos en "
                       "posición y flexiona los codos para bajar la barra o cuerda hacia tu frente, permitiendo que tus antebrazos se muevan hacia "
                       "atrás. Luego, extiende los codos para elevar la barra o cuerda de nuevo a la posición inicial. Repite el movimiento. "
    },
    "Rompecráneos con mancuernas": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Acuéstate en un banco plano con una mancuerna en cada mano, extendidas sobre tu pecho con los codos ligeramente "
                       "flexionados. Mantén las piernas en un ángulo cómodo. Dobla los codos y baja las mancuernas hacia los lados de la cabeza, "
                       "manteniendo los brazos perpendiculares al suelo. Extiende los codos para volver a la posición inicial, evitando bloquear "
                       "completamente los brazos en la parte superior del movimiento. Repite el ejercicio. "
    },
    "Empuje con cuerda": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate frente a una máquina de poleas con una cuerda o asa sujeta a la polea en posición alta. Agarra la cuerda con ambas "
                       "manos y mantén los codos cerca de tu cuerpo. Empuja la cuerda hacia adelante y hacia abajo, extendiendo completamente los "
                       "brazos. Luego, regresa a la posición inicial controladamente flexionando los codos. Repite el movimiento. "
    },
    "Empuje con barra-V": {
        "difficulty": BEGINNER,
        "effectiveness": 8,
        "min_reps": 10,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Para realizar este ejercicio, usa una máquina de polea con una barra en forma de \"V\" o un accesorio similar. De pie "
                       "frente a la máquina, sujeta la barra en V con un agarre supino, manteniendo los codos cerca de tu torso y los brazos "
                       "doblados en un ángulo de 90 grados. Extiende los codos y empuja la barra hacia abajo hasta que los brazos estén "
                       "completamente extendidos. Luego, regresa la barra a la posición inicial controlando el movimiento. "
    },
    "Empuje de tríceps con cuerda": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Para este ejercicio, estarás de pie frente a una máquina de poleas con una cuerda o asa de cuerda sujeta al cable superior. "
                       "Sujeta la cuerda con ambas manos, manteniendo los codos cerca de tu torso y los antebrazos perpendiculares al suelo. "
                       "Extiende los codos mientras empujas la cuerda hacia abajo, contrayendo tus tríceps al final del movimiento. Luego, "
                       "vuelve a la posición inicial manteniendo el control. "
    },
    "Empuje reverso": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Parado frente a una máquina de polea con la barra en posición alta, utiliza una empuñadura supinada (palmas hacia arriba) "
                       "para agarrar la barra de cable. Mantén los codos cerca del cuerpo y las manos a la altura de los hombros. Extiende los "
                       "codos hacia abajo, llevando la barra hacia tus muslos y contrae tus tríceps al final del movimiento. Luego, "
                       "controladamente, regresa la barra a la posición inicial manteniendo la resistencia en los tríceps. Repite el movimiento. "
    },
    "Extensión de cable hacia atrás": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Conéctate a una máquina de cable con una polea baja. De pie, coloca tu cuerpo de lado con una pierna ligeramente hacia "
                       "adelante y la otra hacia atrás. Sujeta la manija del cable con la mano más alejada de la máquina y lleva tu codo hacia "
                       "atrás. Extiende tu brazo completamente hacia atrás, sintiendo la contracción en el tríceps, y luego vuelve a la posición "
                       "inicial de manera controlada. "
    },
    "Fondos de tríceps": {
        "difficulty": BEGINNER,
        "effectiveness": 2,
        "min_reps": 6,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Colócate entre dos superficies elevadas, como bancos paralelos o sillas, con las manos apoyadas en los bordes y los pies "
                       "extendidos hacia adelante. Baja lentamente tu cuerpo doblando los codos, manteniendo la espalda cerca de las superficies y "
                       "los codos apuntando hacia atrás. Desciende hasta que tus codos estén cerca de los 90 grados y luego impúlsate hacia arriba "
                       "extendiendo los codos. Repite el movimiento. "
    },
    "Extensión con cable a un brazo": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Parado frente a una máquina de poleas con un agarre de cable ajustable en posición baja, agarra el cable con una mano y da "
                       "un paso hacia adelante para crear tensión en el cable. Mantén el codo ligeramente flexionado y realiza una extensión hacia "
                       "arriba, llevando la mano desde una posición baja a una posición alta. Controla el movimiento y vuelve a la posición inicial. "
    },
    "Extensión con mancuerna a un brazo por detrás de la cabeza": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "De pie o sentado, sostén una mancuerna con una mano y levántala sobre tu cabeza, con el codo apuntando hacia adelante. "
                       "Luego, flexiona el codo para bajar la mancuerna hacia la parte posterior de tu cuello, manteniendo el brazo en línea con la "
                       "cabeza. Extiende el brazo de nuevo para volver a la posición inicial. Asegúrate de mantener el codo apuntando hacia "
                       "adelante y el cuerpo estable durante todo el movimiento. Repite con el otro brazo si es necesario. "
    },
    "Flexión diamante": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 4,
        "min_reps": 6,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Comienza en posición de plancha con las manos colocadas debajo del pecho, formando un diamante con los pulgares y los "
                       "índices. Mantén el cuerpo en línea recta desde la cabeza hasta los talones. Baja el cuerpo flexionando los codos y "
                       "acercando el pecho al suelo, manteniendo los codos cerca del cuerpo. Luego, empuja hacia arriba para volver a la posición "
                       "inicial. Repite el movimiento. "
    },
    "Empuje con cable a un brazo": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Parado frente a una máquina de poleas con una barra de tracción alta, ajusta la polea con un agarre de cuerda. Toma la "
                       "cuerda con una mano y coloca el codo en un ángulo de 90 grados. Mantén el codo pegado al costado del cuerpo. Extiende el "
                       "brazo hacia abajo, llevando la cuerda hacia el muslo, enfocándote en la contracción del tríceps. Regresa el brazo a la "
                       "posición inicial de manera controlada y repite el movimiento. Luego, cambia de brazo. "
    },
    "Extensión de tríceps con peso corporal": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 3,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Comienza en una posición de plancha alta con las manos colocadas directamente debajo de los hombros y los codos extendidos. "
                       "Mantén el cuerpo en línea recta desde la cabeza hasta los talones. Dobla los codos y baja el cuerpo hacia el suelo, "
                       "manteniendo los codos cerca del torso. Extiende los codos para volver a la posición inicial. "
    }
}

abs_exercises = {
    "Abdominal declinado": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 8,
        "max_reps": 25,
        "priority": ASSISTANCE,
        "description": "Asegura tus pies en un banco declinado o una plataforma inclinada, manteniendo tus rodillas ligeramente dobladas. Cruza los "
                       "brazos sobre el pecho o coloca las manos detrás de la cabeza. Desciende hacia atrás lentamente, controlando el movimiento, "
                       "y contrae los músculos abdominales para levantar tu torso hacia adelante. "
    },
    "Elevación de rodillas colgado": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 8,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Cuelga de una barra fija con los brazos completamente extendidos y los hombros relajados. Levanta las rodillas hacia el "
                       "pecho doblando las piernas mientras contraes los músculos abdominales. Asegúrate de controlar el movimiento y evitar "
                       "balancear el cuerpo. Después, baja las rodillas lentamente a la posición inicial. "
    },
    "Abdominal arrodillado con cable": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Arrodíllate frente a una máquina de cables con una polea alta, utilizando un accesorio de cuerda. Agarra las cuerdas con "
                       "ambas manos y colócalas a los lados de tu cabeza. Mantén las rodillas en el suelo y realiza un encogimiento hacia abajo, "
                       "llevando tus codos hacia tus rodillas mientras contraes los músculos abdominales. Asegúrate de mantener la espalda recta "
                       "durante todo el movimiento. Luego, estira lentamente los abdominales y vuelve a la posición inicial. Repite el ejercicio. "
    },
    "Abdominal": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Acuéstate boca arriba en una superficie firme, flexiona las rodillas y coloca los pies planos en el suelo. Cruzando los "
                       "brazos sobre el pecho o colocándolos detrás de la cabeza, contrae los músculos abdominales para levantar el torso hacia las "
                       "rodillas. Asegúrate de mantener la parte inferior de la espalda en contacto con el suelo. Desciende lentamente de vuelta a "
                       "la posición inicial y repite el movimiento. "
    },
    "Elevación de rodillas en silla romana": {
        "difficulty": BEGINNER,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Colócate en una silla romana con la espalda apoyada y los antebrazos en los soportes acolchados. Sujeta tus manos en las "
                       "empuñaduras, asegurándote de que tus codos estén ligeramente doblados. Levanta las rodillas hacia el pecho contrayendo los "
                       "músculos abdominales, manteniendo el control del movimiento. Después, baja lentamente las piernas de vuelta a la posición "
                       "inicial sin tocar completamente el suelo. "
    },
    "Encongimiento invertido": {
        "difficulty": BEGINNER,
        "effectiveness": 6,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Acuéstate boca arriba en una esterilla con las manos colocadas a los lados y las piernas extendidas hacia arriba. Dobla las "
                       "rodillas y levanta las piernas hacia el pecho mientras levantas la pelvis del suelo. Asegúrate de contraer los músculos "
                       "abdominales en la parte superior del movimiento. Luego, baja lentamente las piernas hacia la posición inicial sin que "
                       "toquen el suelo. "
    },
    "Encongimiento con cable de pie": {
        "difficulty": BEGINNER,
        "effectiveness": 4,
        "min_reps": 10,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Colócate frente a una máquina de poleas con una cuerda o barra conectada en la parte superior. Sujeta la cuerda o barra con "
                       "ambas manos y lleva tus manos hacia abajo, manteniendo los codos ligeramente flexionados. Desde esta posición, "
                       "contrae tus abdominales y flexiona la parte superior de tu cuerpo hacia adelante, llevando los codos hacia las rodillas. "
                       "Asegúrate de mantener la tensión en los abdominales en todo momento. Luego, vuelve a la posición inicial de manera "
                       "controlada. Repite el movimiento. "
    },
    "Escaladroes": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 15,
        "max_reps": 40,
        "priority": ASSISTANCE,
        "description": "Comienza en una posición de plancha con las manos directamente debajo de los hombros. Mantén el cuerpo en línea recta desde "
                       "la cabeza hasta los talones. Lleva una rodilla hacia el pecho y luego alterna rápidamente con la otra pierna, "
                       "como si estuvieras corriendo en el lugar en posición horizontal. "
    },
    "Giro en barra terrestre": {
        "difficulty": BEGINNER,
        "effectiveness": 9,
        "min_reps": 8,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Coloca una barra en el extremo de una barra terrestre (o en un rincón adecuado para la misma). Carga la barra con un peso "
                       "moderado. Párate de lado a la barra, agarrándola con ambas manos y extendiendo tus brazos frente a ti. Mantén los pies a la "
                       "altura de los hombros y las rodillas ligeramente flexionadas. Gira tu torso y caderas hacia un lado, luego vuelve al centro "
                       "y gira hacia el otro lado. Mantén el control del movimiento y repite alternando los lados. "
    },
    "Elevación de vela": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 15,
        "max_reps": 40,
        "priority": TERTIARY,
        "description": "Acuéstate boca arriba en una superficie plana, con las piernas extendidas hacia arriba y los brazos extendidos hacia atrás "
                       "en el suelo. Eleva las piernas directamente hacia el techo usando la fuerza de los músculos abdominales, manteniendo los "
                       "brazos y la parte superior del cuerpo en el suelo. Baja las piernas lentamente hacia el suelo sin tocarlo y luego repite el "
                       "movimiento. "
    },
    "Peso muerto maleta": {
        "difficulty": BEGINNER,
        "effectiveness": 5,
        "min_reps": 8,
        "max_reps": 15,
        "priority": TERTIARY,
        "description": "Colócate de pie con las piernas separadas a la altura de los hombros, con una pesa (como una mancuerna o kettlebell) en una "
                       "mano a tu lado, como si llevaras una maleta. Mantén la espalda recta y el núcleo comprometido. Inclínate hacia adelante "
                       "desde las caderas, bajando la pesa hacia el suelo mientras mantienes la pierna del lado opuesto ligeramente flexionada. "
                       "Mantén el brazo recto y baja la pesa lo más cerca posible de la pierna sin torcer la espalda. Luego, vuelve a la posición "
                       "inicial, llevando la pesa de vuelta al costado. Alterna entre los lados para realizar repeticiones equitativas. "
    },
    "Inclinación en plancha lateral": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 15,
        "max_reps": 30,
        "priority": TERTIARY,
        "description": "Comienza en una posición de plancha lateral, apoyándote en un antebrazo y asegurándote de que tu cuerpo forme una línea "
                       "recta desde la cabeza hasta los pies. Desciende la cadera hacia el suelo, manteniendo el cuerpo en línea, y luego vuelve a "
                       "elevarla a la posición inicial. Realiza el mismo movimiento de inclinación de cadera hacia el suelo y elevación varias "
                       "veces antes de cambiar de lado. "
    },
    "Limpiaparabrisas": {
        "difficulty": BEGINNER,
        "effectiveness": 3,
        "min_reps": 15,
        "max_reps": 30,
        "priority": TERTIARY,
        "description": "Acuéstate boca arriba en el suelo con los brazos extendidos a los lados y las piernas levantadas hacia el techo. Mantén las "
                       "piernas juntas y, sin doblar las rodillas, realiza un movimiento de lado a lado, como el movimiento de limpiaparabrisas de "
                       "un automóvil. Controla el movimiento y mantén la parte superior del cuerpo en contacto con el suelo. Alterna de un lado a "
                       "otro, manteniendo la tensión en los músculos abdominales y lumbares. "
    },
    "Elevación de piernas colgado": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 7,
        "min_reps": 10,
        "max_reps": 25,
        "priority": ASSISTANCE,
        "description": "Colócate en una barra horizontal o en unas barras paralelas con las manos, manteniendo los brazos rectos. Levanta las "
                       "piernas extendidas hacia arriba, manteniendo el cuerpo lo más recto posible. "
    },
    "Flexión de escápulas": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 5,
        "min_reps": 10,
        "max_reps": 30,
        "priority": TERTIARY,
        "description": "Comienza en posición de plancha con los brazos completamente extendidos y las manos colocadas debajo de los hombros. Enfoca "
                       "tu atención en las escápulas (omóplatos) y, en lugar de doblar los codos, realiza el movimiento al contraer y expandir las "
                       "escápulas. Hunde el pecho hacia abajo, juntando las escápulas, y luego eleva el pecho hacia arriba, alejando las escápulas "
                       "entre sí. Mantén los codos prácticamente bloqueados durante todo el ejercicio. "
    },
    "Giro ruso": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 6,
        "min_reps": 8,
        "max_reps": 30,
        "priority": TERTIARY,
        "description": "Siéntate en el suelo con las rodillas dobladas y los pies apoyados en el suelo. Inclina ligeramente tu torso hacia atrás "
                       "sin redondear la espalda. Sostén una pesa o bola medicinal con ambas manos frente a ti. Levanta los pies del suelo si "
                       "deseas aumentar la intensidad. Desde esta posición, gira tu torso hacia un lado y toca el suelo cerca de tu cadera con la "
                       "pesa, luego gira hacia el otro lado y repite el movimiento. "
    },
    "Caminata de oso": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 2,
        "min_reps": 15,
        "max_reps": 40,
        "priority": TERTIARY,
        "description": "Comienza en una posición de tabla con tus manos directamente debajo de los hombros y las rodillas debajo de las caderas. "
                       "Levanta las rodillas ligeramente del suelo y mueve la mano derecha y el pie izquierdo hacia adelante al mismo tiempo, "
                       "seguido por la mano izquierda y el pie derecho. Mantén el core contraído y el cuerpo en línea recta. Continúa alternando "
                       "los movimientos de manos y pies, avanzando en una \"caminata del oso\". "
    },
    "Extensión abdominal con barra": {
        "difficulty": ADVANCED,
        "effectiveness": 9,
        "min_reps": 5,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Arrodíllate en el suelo con una barra cargada con discos frente a ti. Agarra la barra con ambas manos, manteniendo las "
                       "manos separadas a la anchura de los hombros. Lentamente rueda la barra hacia adelante, estirando tus brazos y bajando tu "
                       "torso hacia el suelo. Mantén tu núcleo contraído para controlar el movimiento. Luego, utiliza la fuerza de tus músculos "
                       "abdominales para tirar de la barra y volver a la posición inicial. Evita que tu espalda se arquee excesivamente durante el "
                       "movimiento. Repite el ejercicio. "
    },
    "Rodillo para abdominales": {
        "difficulty": ADVANCED,
        "effectiveness": 6,
        "min_reps": 5,
        "max_reps": 15,
        "priority": ASSISTANCE,
        "description": "Comienza arrodillado en el suelo con un rodillo para abdominales frente a ti. Sujeta las empuñaduras del rodillo con ambas "
                       "manos y coloca el rodillo justo delante de tus rodillas. Mantén tu núcleo contraído y tu espalda recta mientras ruedas el "
                       "rodillo hacia adelante, extendiendo tus brazos lo más posible. Luego, revierte el movimiento, utilizando tus músculos "
                       "abdominales para tirar del rodillo de vuelta hacia tus rodillas. Asegúrate de mantener el control y evitar que tu espalda "
                       "se arquee. Repite el movimiento. "
    },
    "Toque a la barra": {
        "difficulty": ADVANCED,
        "effectiveness": 4,
        "min_reps": 8,
        "max_reps": 20,
        "priority": ASSISTANCE,
        "description": "Colócate en una barra horizontal, suspendido con los brazos completamente extendidos. Desde esta posición, "
                       "eleva las piernas, manteniéndolas rectas, hasta que toquen la barra con los dedos de los pies. Controla el movimiento al "
                       "bajar las piernas de nuevo a la posición inicial, evitando el balanceo excesivo del cuerpo. "
    },
    "Bandera del dragón": {
        "difficulty": ADVANCED,
        "effectiveness": 8,
        "min_reps": 6,
        "max_reps": 20,
        "priority": TERTIARY,
        "description": "Acuéstate boca arriba en un banco plano con agarre firme en los bordes. Levanta tus piernas directamente hacia arriba, "
                       "manteniendo los brazos extendidos y agarrados al banco para mantener el equilibrio. Luego, eleva tu torso y tus caderas del "
                       "banco, manteniendo las piernas en posición vertical. Forma una línea recta con tu cuerpo desde los hombros hasta los pies. "
                       "Baja lentamente el torso y las piernas hacia abajo sin tocar el banco y luego vuelve a la posición inicial. "
    }
}

calves_exercises = {
    "Elevación de gemelos sentado": {
        "difficulty": BEGINNER,
        "effectiveness": 10,
        "min_reps": 12,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Siéntate en una máquina de elevación de talones en el gimnasio con los pies apoyados en una plataforma y las rodillas "
                       "dobladas en ángulo recto. Asegúrate de que tus rodillas queden debajo de tus hombros. Coloca el peso en tus muslos, "
                       "y sujeta los agarres de la máquina para estabilizarte. Luego, eleva los talones hacia arriba lo más alto que puedas, "
                       "contrayendo los músculos de la pantorrilla. Después, baja los talones de regreso a la posición inicial. Repite el "
                       "movimiento. "
    },
    "Elevación de gemelos parado": {
        "difficulty": INTERMEDIATE,
        "effectiveness": 9,
        "min_reps": 12,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Ponte de pie con los pies a la altura de los hombros y coloca una barra o una máquina de peso en los hombros, "
                       "o sostén mancuernas en tus manos a los lados. Mantén las piernas rectas y levanta los talones del suelo al estirar los "
                       "tobillos, elevando los talones lo más alto posible. Luego, baja los talones de manera controlada hasta que sientas un "
                       "estiramiento en los músculos de la pantorrilla. Repite el movimiento. "
    },
    "Elevación de gemelos en prensa de piernas": {
        "difficulty": ADVANCED,
        "effectiveness": 8,
        "min_reps": 12,
        "max_reps": 30,
        "priority": ASSISTANCE,
        "description": "Comienza sentado en una máquina de prensa de piernas con los pies colocados en la plataforma a la altura de los hombros y "
                       "los dedos de los pies apuntando hacia adelante. Lentamente, presiona la plataforma hacia arriba usando la fuerza de tus "
                       "pantorrillas, elevando los talones tanto como puedas. Luego, baja la plataforma de manera controlada hasta que sientas un "
                       "estiramiento en los músculos de la pantorrilla. Repite el movimiento. "
    }
}

movement_patterns = {
    "hinge": {
        "exercises": hinge_exercises,
        "min_beginner_sets": 3,
        "max_beginner_sets": 6,
        "min_intermediate_sets": 4,
        "max_intermediate_sets": 10,
        "min_advanced_sets": 6,
        "max_advanced_sets": 14,
    },
    "squat": {
        "exercises": squat_exercises,
        "min_beginner_sets": 3,
        "max_beginner_sets": 8,
        "min_intermediate_sets": 4,
        "max_intermediate_sets": 10,
        "min_advanced_sets": 6,
        "max_advanced_sets": 14,
    },
    "row": {
        "exercises": row_exercises,
        "min_beginner_sets": 2,
        "max_beginner_sets": 6,
        "min_intermediate_sets": 4,
        "max_intermediate_sets": 8,
        "min_advanced_sets": 8,
        "max_advanced_sets": 12,
    },
    "push": {
        "exercises": push_exercises,
        "min_beginner_sets": 2,
        "max_beginner_sets": 8,
        "min_intermediate_sets": 6,
        "max_intermediate_sets": 12,
        "min_advanced_sets": 8,
        "max_advanced_sets": 16,
    },
    "pull": {
        "exercises": pull_exercises,
        "min_beginner_sets": 4,
        "max_beginner_sets": 8,
        "min_intermediate_sets": 6,
        "max_intermediate_sets": 12,
        "min_advanced_sets": 8,
        "max_advanced_sets": 16,
    },
    "press": {
        "exercises": press_exercises,
        "min_beginner_sets": 3,
        "max_beginner_sets": 6,
        "min_intermediate_sets": 4,
        "max_intermediate_sets": 8,
        "min_advanced_sets": 8,
        "max_advanced_sets": 10,
    },
    "shoulders": {
        "exercises": shoulders_exercises,
        "min_beginner_sets": 4,
        "max_beginner_sets": 8,
        "min_intermediate_sets": 6,
        "max_intermediate_sets": 12,
        "min_advanced_sets": 10,
        "max_advanced_sets": 18,
    },
    "curl": {
        "exercises": curl_exercises,
        "min_beginner_sets": 0,
        "max_beginner_sets": 4,
        "min_intermediate_sets": 2,
        "max_intermediate_sets": 8,
        "min_advanced_sets": 6,
        "max_advanced_sets": 12,
    },
    "extend": {
        "exercises": extend_exercises,
        "min_beginner_sets": 0,
        "max_beginner_sets": 4,
        "min_intermediate_sets": 2,
        "max_intermediate_sets": 8,
        "min_advanced_sets": 6,
        "max_advanced_sets": 12,
    },
    "abs": {
        "exercises": abs_exercises,
        "min_beginner_sets": 2,
        "max_beginner_sets": 4,
        "min_intermediate_sets": 4,
        "max_intermediate_sets": 6,
        "min_advanced_sets": 6,
        "max_advanced_sets": 14,
    },
    "calves": {
        "exercises": calves_exercises,
        "min_beginner_sets": 0,
        "max_beginner_sets": 4,
        "min_intermediate_sets": 2,
        "max_intermediate_sets": 8,
        "min_advanced_sets": 6,
        "max_advanced_sets": 12,
    }
}

modifiers = {
    "sets": {
        AGE: {
            40: .8,
            60: .5
        },
        PHYSICAL_CONDITION: {
            "baja": .75,
            "media": 1,
            "alta": 1.25
        },
        SPORT_EXPERIENCE: {
            "nula": .75,
            "poca": 1,
            "promedio": 1,
            "mucha": 1
        },
        OBJECTIVE: {
            "fuerza": 1.5,
            "hipertrofia": 1,
            "resistencia": .75
        }
    },
    "reps": {
        AGE: {
            40: 1.25,
            60: 1.75
        },
        PHYSICAL_CONDITION: {
            "baja": 1.1,
            "media": 1,
            "alta": .9
        },
        SPORT_EXPERIENCE: {
            "nula": 1.25,
            "poca": 1.1,
            "promedio": 1,
            "mucha": .9
        },
        OBJECTIVE: {
            "fuerza": .75,
            "hipertrofia": 1,
            "resistencia": 1.5
        }
    }
}
