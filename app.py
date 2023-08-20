import os
import sqlite3
from flask import Flask, jsonify, send_from_directory, request

app = Flask(__name__)

app.static_folder = "images"


@app.route("/images/<path:filename>")  # Imagens do diretório do projeto
def get_image(filename):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(os.path.join(root_dir, app.static_folder), filename)


def create_database_if_not_exists():  # Criação do Banco de Dados caso não ele não exista
    if not os.path.exists("jogos.db"):
        conn = sqlite3.connect("jogos.db")
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            data_lancamento TEXT,
            console TEXT,
            vendas TEXT,
            capa TEXT,
            avaliacao REAL,
            sinopse TEXT,
            gameplay1 TEXT,
            gameplay2 TEXT,
            gameplay3 TEXT
        );
        """

        cursor.execute(create_table_query)
        conn.commit()
        conn.close()


def insert_initial_data():  # Inserção dos jogos ao BD
    conn = sqlite3.connect("jogos.db")
    cursor = conn.cursor()

    check_empty_query = "SELECT COUNT(*) FROM jogos"
    cursor.execute(check_empty_query)
    count = cursor.fetchone()[0]

    if count == 0:
        base_url = "http://127.0.0.1:5000"

        jogos_iniciais = [
            (
                "Donkey Kong",
                "1981-07-09",
                "Arcade",
                "N/A",
                f"{base_url}/images/capas/donkeykong.jpg",
                7.8,
                "Donkey Kong, lançado em 1981 como arcade pela Nintendo, marcou a estreia de Mario (na época chamado de Jumpman) em um jogo. Criado por Shigeru Miyamoto, o jogo apresentou o icônico gorila Donkey Kong, que sequestra a donzela Pauline e escala estruturas. Jumpman, mais tarde renomeado para Mario, precisa enfrentar obstáculos, como barris e chamas, para resgatar Pauline. A jogabilidade de plataformas e a necessidade de cronometrar movimentos capturaram a atenção dos jogadores. Com quatro fases, o jogo foi um sucesso instantâneo e estabeleceu as bases para a carreira brilhante de Mario. Donkey Kong não apenas definiu um gênero, mas também lançou as bases para uma das franquias mais icônicas dos videogames.",
                f"{base_url}/images/gameplay/donkeykong1981_1.png",
                f"{base_url}/images/gameplay/donkeykong1981_2.png",
                f"{base_url}/images/gameplay/donkeykong1981_3.webp",
            ),
            (
                "Mario Bros.",
                "1983-06-14",
                "Arcade",
                "N/A",
                f"{base_url}/images/capas/mario1983.webp",
                8.0,
                "Mario Bros., lançado em 1983 como arcade pela Nintendo, é um título que antecede a famosa série Super Mario. Desenvolvido por Shigeru Miyamoto, o jogo introduziu muitos elementos que se tornariam características marcantes da franquia. Nele, os jogadores controlam Mario e Luigi em esgotos, enfrentando criaturas como os Shellcreepers e Sidesteppers, enquanto tentam derrotar inimigos chutando-os e virando-os. Com mecânicas de plataformas e a habilidade de atacar de baixo para cima, o jogo se destacou por sua jogabilidade cooperativa ou competitiva de dois jogadores. Mario Bros. estabeleceu as bases para o legado duradouro de Mario e sua influência continua a ser sentida na série até hoje.",
                f"{base_url}/images/gameplay/mario_bros_1983_1.mp4",
                f"{base_url}/images/gameplay/mario_bros_1983_2.mp4",
                f"{base_url}/images/gameplay/mario_bros_1983_3.mp4",
            ),
            (
                "Super Mario Bros.",
                "1985-09-13",
                "NES",
                "40.24 milhões",
                f"{base_url}/images/capas/mario1.png",
                9.0,
                "Lançado em 1985 para o NES, Super Mario Bros. é um marco nos videogames, definindo o gênero de plataforma. Desenvolvido pela Nintendo e criado por Shigeru Miyamoto, o jogo segue Mario em sua jornada para resgatar a Princesa Peach do vilão Bowser, através de mundos temáticos repletos de inimigos icônicos. Com controles precisos e criatividade de design, introduziu mecânicas de salto e power-ups, como o cogumelo que aumenta Mario. Com mais de 40 milhões de cópias vendidas, a trilha sonora icônica de Koji Kondo e sua jogabilidade cativante, Super Mario Bros. deixou um legado duradouro, definindo os padrões para os jogos de plataforma e estabelecendo a base para a icônica franquia Super Mario.",
                f"{base_url}/images/gameplay/mario1_1.png",
                f"{base_url}/images/gameplay/mario1_2.webp",
                f"{base_url}/images/gameplay/mario1_3.webp",
            ),
            (
                "Super Mario Bros.: The Lost Levels",
                "1986-06-03",
                "NES",
                "N/A",
                f"{base_url}/images/capas/mario2japan.jpg",
                8.0,
                "Mario Bros.: The Lost Levels, conhecido originalmente como Super Mario Bros. 2 no Japão, é uma sequência desafiadora do jogo original de NES. Lançado em 1986, expande a dificuldade e complexidade com níveis intrincados e armadilhas traiçoeiras. Mario e Luigi embarcam em uma nova jornada para resgatar a Princesa Peach, enfrentando variações de inimigos familiares e novas mecânicas de gameplay, como ventos fortes. Com a adição de cogumelos venenosos e saltos mais precisos, o jogo exige habilidades avançadas dos jogadores. The Lost Levels oferece uma experiência desafiadora que foi considerada muito difícil para audiências ocidentais e, como resultado, a Nintendo lançou uma versão diferente como Super Mario Bros. 2 fora do Japão.",
                f"{base_url}/images/gameplay/marioll_1.png",
                f"{base_url}/images/gameplay/marioll_2.png",
                f"{base_url}/images/gameplay/marioll_3.jpg",
            ),
            (
                "Super Mario Bros. 2",
                "1988-10-09",
                "NES",
                "10.58 milhões",
                f"{base_url}/images/capas/mario2.jpg",
                8.5,
                "Super Mario Bros. 2, lançado em 1988 para o NES, destaca-se por suas mecânicas únicas e abordagem diferenciada em relação ao seu antecessor. O jogo não era originalmente um título Mario, mas uma adaptação de um jogo chamado Doki Doki Panic. Apresentando quatro personagens jogáveis - Mario, Luigi, Peach e Toad - cada um com habilidades distintas, o jogo permitia escolher entre eles. A jogabilidade envolvia cavar, pegar e lançar itens, criando uma experiência única de plataforma e resolução de quebra-cabeças. Com cenários variados e inimigos peculiares, Super Mario Bros. 2 ofereceu uma abordagem criativa e refrescante à série, mostrando a capacidade da Nintendo de experimentar e inovar enquanto mantinha o espírito da franquia.",
                f"{base_url}/images/gameplay/mario2_1.webp",
                f"{base_url}/images/gameplay/mario2_2.webp",
                f"{base_url}/images/gameplay/mario2_3.png",
            ),
            (
                "Super Mario Land",
                "1989-04-21",
                "Game Boy",
                "18.14 milhões",
                f"{base_url}/images/capas/marioland.png",
                7.5,
                "Super Mario Land, lançado em 1989 para o Game Boy, é uma adaptação da série para o console portátil da Nintendo. Introduzindo Mario em uma aventura em Sarasaland para resgatar a Princesa Daisy do vilão Tatanga, o jogo apresenta novos inimigos e mecânicas únicas. Com quatro mundos temáticos, como Egito e China, o jogo se destaca por sua abordagem compacta e design criativo, apesar das limitações técnicas do Game Boy. Novos power-ups, como a Superball Flower, adicionaram variações à jogabilidade. Embora mais curto em comparação com outros títulos, Super Mario Land manteve o espírito da série e estabeleceu a presença de Mario nos consoles portáteis, provando que a diversão e a inovação podiam ser levadas para qualquer lugar.",
                f"{base_url}/images/gameplay/marioland_1.webp",
                f"{base_url}/images/gameplay/marioland_2.webp",
                f"{base_url}/images/gameplay/marioland_3.webp",
            ),
            (
                "Super Mario Bros. 3",
                "1988-10-23",
                "NES",
                "17.28 milhões",
                f"{base_url}/images/capas/mario3.png",
                9.5,
                "Super Mario Bros. 3, lançado em 1988 para o NES, é um marco na série e nos jogos de plataforma. Introduzindo novos power-ups, como a Super Leaf que transformava Mario em Tanooki, permitindo voar e atacar com a cauda, o jogo ampliou a experiência de gameplay. Com oito mundos distintos, repletos de níveis desafiadores, o jogo incentivou a exploração e ofereceu uma variedade impressionante de inimigos e obstáculos. A adição do mapa do mundo e minijogos deu uma sensação de aventura e recompensa. Sua jogabilidade refinada, trilha sonora memorável e design criativo solidificaram a posição de Super Mario Bros. 3 como um dos jogos mais influentes de todos os tempos, influenciando gerações de jogos de plataforma.",
                f"{base_url}/images/gameplay/mario3_1.png",
                f"{base_url}/images/gameplay/mario3_2.png",
                f"{base_url}/images/gameplay/mario3_3.webp",
            ),
            (
                "Super Mario World",
                "1990-11-21",
                "SNES",
                "20.61 milhões",
                f"{base_url}/images/capas/marioworld.jpg",
                9.5,
                "Super Mario World, lançado em 1990 para o Super Nintendo Entertainment System (SNES), é uma joia da série Mario. Desenvolvido por Shigeru Miyamoto, o jogo introduziu Mario em um novo patamar de design e jogabilidade. Ambientado na Ilha dos Dinossauros, Mario e Luigi enfrentam Bowser e seus Koopalings para resgatar a Princesa Peach. Com gráficos coloridos e expansivos, o jogo apresenta um mapa do mundo interconectado, permitindo uma exploração não linear e níveis secretos. Novos power-ups foram introduzidos, incluindo a Capa e Yoshi, o dinossauro amigo que adicionou uma nova camada estratégica à jogabilidade. Com uma trilha sonora icônica e desafios criativos, Super Mario World consolidou o sucesso da série e estabeleceu o padrão para os jogos de plataforma, continuando a ser adorado por fãs de todas as idades.",
                f"{base_url}/images/gameplay/marioworld_1.webp",
                f"{base_url}/images/gameplay/marioworld_2.png",
                f"{base_url}/images/gameplay/marioworld_3.webp",
            ),
            (
                "Super Mario Land 2: 6 Golden Coins",
                "1992-10-21",
                "Game Boy",
                "11.18 milhões",
                f"{base_url}/images/capas/marioland2.jpg",
                9.0,
                "Super Mario Land 2: 6 Golden Coins, lançado em 1992 para o Game Boy, é uma sequência que expandiu e refinou a fórmula estabelecida pelo seu antecessor. O jogo apresenta uma aventura mais ambiciosa, na qual Mario deve recuperar seis moedas douradas para retomar sua casa do maligno Wario. Com uma jogabilidade mais ampla, o jogo introduz transformações, permitindo que Mario se torne diferentes personagens, cada um com habilidades únicas. Cada mundo temático possui níveis variados e desafios cativantes, com destaque para os estágios da Árvore da Mamãe-Pássaro. A adição de elementos de exploração e um overworld interconectado aumentaram a profundidade. Super Mario Land 2 é elogiado por sua originalidade, controles precisos e variação de gameplay, consolidando sua posição como um dos melhores jogos do Game Boy e um destaque na série Mario.",
                f"{base_url}/images/gameplay/marioland2_1.webp",
                f"{base_url}/images/gameplay/marioland2_2.webp",
                f"{base_url}/images/gameplay/marioland2_3.webp",
            ),
            (
                "Super Mario 64",
                "1996-09-29",
                "N64",
                "11.89 milhões",
                f"{base_url}/images/capas/mario64.jpg",
                9.0,
                "Super Mario 64, lançado em 1996 para o Nintendo 64, revolucionou os jogos 3D ao introduzir um vasto mundo aberto tridimensional para explorar. Dirigido por Shigeru Miyamoto, o jogo estabeleceu novos padrões de design e jogabilidade. Na pele de Mario, os jogadores exploram o Castelo da Princesa Peach e saltam para retratos que os levam a mundos distintos. Com movimentos fluídos e uma câmera ajustável, Super Mario 64 desafiou as convenções e permitiu uma exploração mais envolvente. O jogo trouxe power-ups icônicos, como a tampa de voo e o chapéu invisível, e marcou a estreia de personagens como Yoshi em 3D. Com sua música marcante e variedade de desafios, Super Mario 64 é um marco na evolução dos videogames e definiu as bases para futuros jogos 3D.",
                f"{base_url}/images/gameplay/mario64_1.webp",
                f"{base_url}/images/gameplay/mario64_2.webp",
                f"{base_url}/images/gameplay/mario64_3.webp",
            ),
            (
                "Super Mario Sunshine",
                "2002-07-19",
                "GameCube",
                "6.28 milhões",
                f"{base_url}/images/capas/mariosunshine.png",
                8.5,
                "Super Mario Sunshine, lançado em 2002 para o Nintendo GameCube, trouxe uma abordagem única à série Mario, introduzindo uma atmosfera tropical e uma nova jogabilidade centrada em torno do dispositivo de jateamento de água chamado F.L.U.D.D. (Flash Liquidizer Ultra Dousing Device). Mario visita a ilha paradisíaca de Isle Delfino, mas é erroneamente acusado de poluir a ilha. Com a ajuda de F.L.U.D.D., ele limpa a ilha, enfrentando inimigos e resolvendo quebra-cabeças em um ambiente mais aberto. A mecânica de jateamento de água acrescentou profundidade e inovação, permitindo aos jogadores resolverem desafios de maneira criativa. A estética colorida e a trilha sonora alegre contribuíram para uma experiência única. Embora tenha sido uma partida ousada da fórmula tradicional, Super Mario Sunshine continua a ser lembrado como um título distinto e amado na série.",
                f"{base_url}/images/gameplay/mariosunshine_1.webp",
                f"{base_url}/images/gameplay/mariosunshine_2.webp",
                f"{base_url}/images/gameplay/mariosunshine_3.webp",
            ),
            (
                "New Super Mario Bros.",
                "2006-05-15",
                "DS",
                "30.80 milhões",
                f"{base_url}/images/capas/newsupermariobros.jpg",
                9.0,
                "New Super Mario Bros., lançado em 2006 para o Nintendo DS, trouxe uma abordagem moderna à jogabilidade clássica de plataforma 2D da série Mario. Desenvolvido para comemorar o 20º aniversário de Super Mario Bros., o jogo retorna às raízes, oferecendo uma experiência nostálgica com gráficos atualizados e novos elementos. A história segue Mario enquanto ele resgata a Princesa Peach das garras de Bowser, enfrentando inimigos familiares e novos desafios. O jogo introduziu power-ups como o Mega Mushroom e o Blue Shell, permitindo interações criativas com o ambiente. A adição de multiplayer cooperativo e competitivo acrescentou uma dimensão social à jogabilidade. Com design de níveis cuidadoso e uma combinação de elementos clássicos e inovadores, New Super Mario Bros. cativou tanto jogadores antigos quanto novos, provando que o espírito de Mario permanece intemporal.",
                f"{base_url}/images/gameplay/nsmb_1.webp",
                f"{base_url}/images/gameplay/nsmb_2.png",
                f"{base_url}/images/gameplay/nsmb_3.png",
            ),
            (
                "Super Mario Galaxy",
                "2007-11-01",
                "Wii",
                "12.80 milhões",
                f"{base_url}/images/capas/mariogalaxy.png",
                9.5,
                "Super Mario Galaxy, lançado em 2007 para o Nintendo Wii, é um marco na série Mario que leva os jogadores a uma jornada espacial única. Com direção de Shigeru Miyamoto e desenvolvimento pela Nintendo EAD Tokyo, o jogo inova ao incorporar elementos de gravidade e planetas em sua jogabilidade 3D. Mario viaja por galáxias e mundos para resgatar a Princesa Peach das garras de Bowser. A mecânica de gravidade permite que Mario salte e explore de maneira revolucionária, enfrentando desafios que vão desde plataformas flutuantes até ações anti-gravitacionais em esferas celestiais. Cada galáxia oferece um cenário único e cativante, repleto de criatividade e desafios diversificados. A trilha sonora arrebatadora de Mahito Yokota e Koji Kondo eleva a experiência, capturando o espírito de aventura no espaço. Com visuais deslumbrantes e uma sensação de maravilha constante, Super Mario Galaxy é amplamente considerado uma obra-prima da série Mario e dos jogos em geral.",
                f"{base_url}/images/gameplay/mariogalaxy_1.webp",
                f"{base_url}/images/gameplay/mariogalaxy_2.webp",
                f"{base_url}/images/gameplay/mariogalaxy_3.webp",
            ),
            (
                "New Super Mario Bros. Wii",
                "2009-11-15",
                "Wii",
                "30.26 milhões",
                f"{base_url}/images/capas/newsupermariobroswii.png",
                9.0,
                "New Super Mario Bros. Wii, lançado em 2009 para o Nintendo Wii, expandiu o sucesso do seu antecessor, trazendo uma experiência multiplayer ainda mais dinâmica. O jogo segue Mario, Luigi e os Toads em uma missão para resgatar a Princesa Peach das garras de Bowser. Introduzindo o multiplayer cooperativo, até quatro jogadores podem jogar simultaneamente, enfrentando níveis desafiadores e derrotando inimigos. O jogo trouxe novos power-ups, como o Propeller Mushroom, e trouxe de volta o clássico Super Mario World Map. A jogabilidade cooperativa permitiu interações engraçadas e caóticas, enquanto os níveis bem projetados mantiveram o desafio e a diversão. New Super Mario Bros. Wii continuou a tradição da série, proporcionando uma experiência colaborativa única e reforçando o status de Mario como um ícone dos jogos.",
                f"{base_url}/images/gameplay/nsmbwii_1.webp",
                f"{base_url}/images/gameplay/nsmbwii_2.webp",
                f"{base_url}/images/gameplay/nsmbwii_3.webp",
            ),
            (
                "Super Mario Galaxy 2",
                "2010-05-23",
                "Wii",
                "7.66 milhões",
                f"{base_url}/images/capas/mariogalaxy2.png",
                9.7,
                "Super Mario Galaxy 2, lançado em 2010 para o Nintendo Wii, é a sequência incrivelmente bem recebida do jogo original que elevou os elementos cósmicos a um novo patamar. Desenvolvido pela Nintendo EAD Tokyo e supervisionado por Shigeru Miyamoto, o jogo continua a história de Mario enquanto ele viaja por galáxias para resgatar a Princesa Peach e coletar Estrelas Verdes. A jogabilidade mantém a inovação do primeiro jogo, adicionando novos power-ups como a Brocheta Cósmica e o Cloud Flower. A exploração galáctica é aprimorada com níveis criativos, desafios variados e mecânicas únicas em cada galáxia. A trilha sonora marcante de Mahito Yokota e Koji Kondo mais uma vez contribui para a atmosfera envolvente. Super Mario Galaxy 2 aprofunda a experiência com seu design meticuloso e criatividade desenfreada, reafirmando sua posição como um dos maiores jogos da série e da história dos videogames.",
                f"{base_url}/images/gameplay/mariogalaxy2_1.webp",
                f"{base_url}/images/gameplay/mariogalaxy2_2.webp",
                f"{base_url}/images/gameplay/mariogalaxy2_3.webp",
            ),
            (
                "Super Mario 3D Land",
                "2011-11-13",
                "3DS",
                "14.83 milhões",
                f"{base_url}/images/capas/mario3dland.png",
                9.0,
                "Super Mario 3D Land, lançado em 2011 para o Nintendo 3DS, é um título que uniu elementos de jogos 2D e 3D da série Mario. Mario embarca em uma missão para resgatar a Princesa Peach das garras de Bowser, explorando níveis em perspectivas variadas. O jogo apresenta uma jogabilidade híbrida, combinando plataformas clássicas em 2D com exploração tridimensional em ambientes 3D. Novos power-ups, como o Super Leaf e o Boomerang Flower, foram introduzidos, adicionando estratégia e diversão. A utilização do efeito 3D do console permitiu que os jogadores avaliassem profundidade e distância, melhorando a percepção dos desafios. Com uma progressão equilibrada de dificuldade e a celebração da nostalgia da série, Super Mario 3D Land marcou uma fusão de estilos e continua a ser um destaque no catálogo do 3DS.",
                f"{base_url}/images/gameplay/mario3dland_1.webp",
                f"{base_url}/images/gameplay/mario3dland_2.webp",
                f"{base_url}/images/gameplay/mario3dland_3.webp",
            ),
            (
                "New Super Mario Bros. 2",
                "2012-07-28",
                "3DS",
                "30.89 milhões",
                f"{base_url}/images/capas/newsupermariobros2.png",
                8.5,
                "New Super Mario Bros. 2, lançado em 2012 para o Nintendo 3DS, concentra-se na coleção extravagante de moedas e tesouros. Mario embarca em uma busca para coletar 1 milhão de moedas e resgatar a Princesa Peach, enquanto enfrenta os Koopalings e Bowser. O jogo mantém a jogabilidade clássica de plataforma 2D da série, introduzindo o Gold Flower, que transforma inimigos e blocos em moedas. Além disso, os níveis estão repletos de ouro, oferecendo uma abordagem centrada na riqueza. Com modos de jogo adicionais e suporte para o StreetPass, que permite a troca de níveis personalizados, New Super Mario Bros. 2 incentivou os jogadores a mergulhar em uma busca por fortuna. A ênfase nas moedas proporcionou um novo giro à fórmula, tornando-o uma adição interessante à série.",
                f"{base_url}/images/gameplay/nsmb2_1.webp",
                f"{base_url}/images/gameplay/nsmb2_2.webp",
                f"{base_url}/images/gameplay/nsmb2_3.webp",
            ),
            (
                "New Super Mario Bros. U",
                "2012-11-18",
                "Wii U",
                "5.88 milhões",
                f"{base_url}/images/capas/newsupermariobrosu.png",
                8.0,
                "New Super Mario Bros. U, lançado em 2012 para o Wii U, continuou a tradição da série New Super Mario Bros., oferecendo uma experiência de plataforma 2D aprimorada. Mario, Luigi e Toads embarcam em uma jornada para resgatar a Princesa Peach do vilão Bowser e dos Koopalings. O jogo apresenta uma série de novos power-ups, incluindo o Acorn Mushroom, que permite planar, e o Baby Yoshi, que oferece habilidades únicas. A adição do modo Challenge e do Boost Rush ofereceu variações à jogabilidade, enquanto o Miiverse permitiu que os jogadores compartilhassem mensagens e dicas. Com níveis criativos e um design cuidadoso, New Super Mario Bros. U manteve o espírito da série e aproveitou as capacidades do Wii U para proporcionar uma experiência envolvente e desafiadora.",
                f"{base_url}/images/gameplay/nsmbu_1.webp",
                f"{base_url}/images/gameplay/nsmbu_2.webp",
                f"{base_url}/images/gameplay/nsmbu_3.webp",
            ),
            (
                "Super Mario 3D World",
                "2013-11-22",
                "Wii U",
                "12.68 milhões",
                f"{base_url}/images/capas/mario3dworld.png",
                9.5,
                "Super Mario 3D World, lançado em 2013 para o Wii U e posteriormente em 2021 para o Nintendo Switch como Super Mario 3D World + Bowser's Fury, é um jogo de plataforma 3D que combina elementos familiares com inovações criativas. Mario, Luigi, Peach e Toad embarcam em uma jornada para resgatar fadas raptadas pelo vilão Bowser. O jogo introduziu o recurso de cat power-up, permitindo que os personagens se transformassem em gatos para escalar paredes e atacar inimigos. Com fases variadas, desde níveis tradicionais até desafios únicos, o jogo destacou-se por seu multiplayer cooperativo e competitivo, que oferecia uma experiência social envolvente. Super Mario 3D World marcou um equilíbrio entre o estilo 2D e 3D, proporcionando uma experiência divertida, desafiadora e expansiva para os jogadores da série Mario.",
                f"{base_url}/images/gameplay/mario3dland_1.webp",
                f"{base_url}/images/gameplay/mario3dland_2.webp",
                f"{base_url}/images/gameplay/mario3dland_3.webp",
            ),
            (
                "Super Mario Maker",
                "2015-09-10",
                "Wii U",
                "4.00 milhões",
                f"{base_url}/images/capas/mariomaker.png",
                9.0,
                "Super Mario Maker, lançado em 2015 para o Wii U e posteriormente em 2016 para o Nintendo 3DS e 2019 para o Nintendo Switch como Super Mario Maker 2, revolucionou a maneira como os jogadores interagem com a série Mario. Oferecendo ferramentas de criação, o jogo permite que os jogadores construam e compartilhem seus próprios níveis. Com uma interface intuitiva, é possível escolher entre diferentes estilos visuais, mecânicas e elementos de jogos anteriores da série. Os jogadores podem criar desafios criativos ou recriar níveis clássicos. A comunidade online compartilha níveis, o que aumenta a diversidade e desafio. O jogo se destaca pela sua capacidade de unir a criatividade dos jogadores e expandir a experiência Mario além dos níveis pré-fabricados, tornando-se uma plataforma colaborativa onde a imaginação é o limite.",
                f"{base_url}/images/gameplay/mariomaker_1.webp",
                f"{base_url}/images/gameplay/mariomaker_2.webp",
                f"{base_url}/images/gameplay/mariomaker_3.webp",
            ),
            (
                "Super Mario Odyssey",
                "2017-10-27",
                "Switch",
                "20.23 milhões",
                f"{base_url}/images/capas/marioodyssey.png",
                9.5,
                "Super Mario Odyssey, lançado em 2017 para o Nintendo Switch, é uma aventura 3D que leva Mario a mundos variados e emocionantes para resgatar a Princesa Peach das garras de Bowser. Destacando-se por sua jogabilidade expansiva e exploração aberta, o jogo introduziu o chapéu Cappy, que permite a Mario possuir inimigos e objetos, adicionando uma camada única de estratégia e resolução de quebra-cabeças. Cada reino temático oferece um ambiente rico e interativo para explorar, com uma ampla variedade de desafios e segredos. Super Mario Odyssey abraçou a diversidade de jogabilidade e estilos visuais, desde áreas urbanas a desertos e florestas exuberantes. Com uma trilha sonora memorável e um senso de maravilha contínua, o jogo modernizou a fórmula Mario, redefinindo o gênero de plataforma 3D e provando que a série continua a evoluir com inovação e criatividade.",
                f"{base_url}/images/gameplay/marioodyssey_1.webp",
                f"{base_url}/images/gameplay/marioodyssey_2.webp",
                f"{base_url}/images/gameplay/marioodyssey_3.webp",
            ),
            (
                "New Super Mario Bros. U Deluxe",
                "2019-01-11",
                "Nintendo Switch",
                "8.32 milhões",
                f"{base_url}/images/capas/nsmbudeluxe.webp",
                8.5,
                "New Super Mario Bros. U Deluxe, lançado em 2019 para o Nintendo Switch, oferece uma aventura de plataforma 2D aprimorada e expansiva. Como uma versão deluxe do jogo original, os jogadores podem explorar mundos coloridos e desafiantes enquanto Mario, Luigi e seus amigos se esforçam para resgatar a Princesa Peach dos Koopalings. Com a inclusão do jogo New Super Luigi U e novos personagens jogáveis, como Toadette, que pode se transformar em Peachette, as opções de gameplay são variadas. Os níveis são projetados para testar as habilidades dos jogadores, enquanto power-ups como o Super Acorn e a Super Crown introduzem mecânicas únicas. A adição do modo multiplayer coop e competitivo aumenta a diversão social. New Super Mario Bros. U Deluxe é uma celebração da jogabilidade clássica, proporcionando desafios e diversão para jogadores de todas as idades.",
                f"{base_url}/images/gameplay/nsmbudeluxe_1.jpg",
                f"{base_url}/images/gameplay/nsmbudeluxe_2.jpg",
                f"{base_url}/images/gameplay/nsmbudeluxe_2.jpg",
            ),
            (
                "Super Mario Maker 2",
                "2019-06-28",
                "Switch",
                "7.15 milhões",
                f"{base_url}/images/capas/mariomaker2.png",
                9.3,
                "Super Mario Maker 2, lançado em 2019 para o Nintendo Switch, é a sequência do aclamado Super Mario Maker, permitindo aos jogadores criar e compartilhar seus próprios níveis de Mario. Desenvolvido pela Nintendo, o jogo expande as opções de criação, oferecendo novos elementos, mecânicas e estilos visuais. Os jogadores podem criar níveis em estilo 2D e 3D, personalizar terrenos e usar uma ampla variedade de itens e inimigos icônicos da série. A adição do Modo História oferece níveis predefinidos com desafios únicos. A comunidade online permite que os jogadores compartilhem, joguem e classifiquem níveis, criando uma plataforma interativa e diversificada. Super Mario Maker 2 estimula a criatividade e oferece uma experiência duradoura, celebrando o legado de Mario e o poder da imaginação dos jogadores.",
                f"{base_url}/images/gameplay/mariomaker2_1.jpg",
                f"{base_url}/images/gameplay/mariomaker2_2.webp",
                f"{base_url}/images/gameplay/mariomaker2_3.webp",
            ),
            (
                "Super Mario 3D All-Stars",
                "2020-09-18",
                "Nintendo Switch",
                "9.01 milhões",
                f"{base_url}/images/capas/mario3dallstar.jpg",
                8.8,
                "Super Mario 3D All-Stars, lançado em 2020 para o Nintendo Switch, é uma coletânea que reúne três clássicos jogos 3D de Mario: Super Mario 64, Super Mario Sunshine e Super Mario Galaxy. Cada jogo trazido para a modernidade com gráficos otimizados e suporte para o Switch. Em Super Mario 64, os jogadores revisitam a pioneira jornada tridimensional de Mario para resgatar Peach das garras de Bowser. Super Mario Sunshine leva Mario para uma ilha tropical onde ele utiliza um dispositivo de jateamento de água para limpar a ilha e resolver enigmas. Já em Super Mario Galaxy, Mario viaja pelo espaço, pulando entre planetas e luas para salvar Peach e o universo. A coletânea oferece a oportunidade de reviver essas experiências lendárias em uma plataforma moderna, celebrando a história e a inovação da série Mario.",
                f"{base_url}/images/gameplay/mario3dallstar_1.jpg",
                f"{base_url}/images/gameplay/mario3dallstar_2.webp",
                f"{base_url}/images/gameplay/mario3dallstar_3.jpg",
            ),
            (
                "Super Mario 3D World + Bowser's Fury",
                "2021-02-12",
                "Switch",
                "8.32 milhões",
                f"{base_url}/images/capas/mario3dworldbowser.jpg",
                9.5,
                "Super Mario 3D World + Bowser's Fury, lançado para o Nintendo Switch em 2021, une o adorado Super Mario 3D World com a inovadora expansão Bowser's Fury. No primeiro, os jogadores exploram cenários vibrantes em uma combinação única de jogabilidade 2D e 3D, enquanto Mario e seus amigos buscam resgatar a Princesa Peach das garras de Bowser. Já em Bowser's Fury, uma ilha de mundo aberto, Mario se junta a Bowser Jr. para combater uma forma furiosa de Bowser, explorando ambientes expansivos e interagindo com novas mecânicas. A experiência oferece uma mistura cativante de nostalgia e inovação, reforçando o legado duradouro de Mario no mundo dos videogames.",
                f"{base_url}/images/gameplay/mario3dworldbowser_1.webp",
                f"{base_url}/images/gameplay/mario3dworldbowser_2.webp",
                f"{base_url}/images/gameplay/mario3dworldbowser_3.webp",
            ),
        ]

        insert_query = """
        INSERT INTO jogos (nome, data_lancamento, console, vendas, capa, avaliacao, sinopse, gameplay1, gameplay2, gameplay3)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        for jogo in jogos_iniciais:
            cursor.execute(insert_query, jogo)

        conn.commit()
    conn.close()


@app.route("/api/jogos", methods=["GET"])  # Rota para a consulta completa dos dados
def get_jogos():
    conn = sqlite3.connect("jogos.db")
    cursor = conn.cursor()

    console_filter = request.args.get("console")
    ano_filter = request.args.get("ano")

    select_query = "SELECT * FROM jogos"

    if console_filter or ano_filter:
        select_query += " WHERE"
        conditions = []

        if console_filter:
            conditions.append(f" console = '{console_filter}'")
        if ano_filter:
            conditions.append(f" data_lancamento LIKE '{ano_filter}%'")

        select_query += " AND".join(conditions)

    cursor.execute(select_query)
    jogos = cursor.fetchall()

    conn.close()

    if not jogos:
        return jsonify({"mensagem": "Não há registros."})

    jogos_completos = []
    for jogo in jogos:
        jogo_dict = {
            "id": jogo[0],
            "nome": jogo[1],
            "data_lancamento": jogo[2],
            "console": jogo[3],
            "vendas": jogo[4],
            "capa": jogo[5],
            "avaliacao": jogo[6],
            "sinopse": jogo[7],
            "gameplay1": jogo[8],
            "gameplay2": jogo[9],
            "gameplay3": jogo[10],
        }
        jogos_completos.append(jogo_dict)

    return jsonify(jogos_completos)


@app.route("/api/jogos/<int:id>", methods=["GET"])  # Consulta individual de jogos
def get_jogo(id):
    conn = sqlite3.connect("jogos.db")
    cursor = conn.cursor()

    select_query = "SELECT * FROM jogos WHERE id = ?"
    cursor.execute(select_query, (id,))
    jogo = cursor.fetchone()

    conn.close()

    if jogo is None:
        return jsonify({"mensagem": "Jogo não encontrado"}), 404

    jogo_dict = {
        "id": jogo[0],
        "nome": jogo[1],
        "data_lancamento": jogo[2],
        "console": jogo[3],
        "vendas": jogo[4],
        "capa": jogo[5],
        "avaliacao": jogo[6],
        "sinopse": jogo[7],
        "gameplay1": jogo[8],
        "gameplay2": jogo[9],
        "gameplay3": jogo[10],
    }

    return jsonify(jogo_dict)  # Retorno json


if __name__ == "__main__":
    create_database_if_not_exists()
    insert_initial_data()
    app.run(debug=True)
