Title: Criando o Pocket Operator Television
Date: 2025-03-18 16:00
Lang: pt
Slug: making-the-pocket-operator-television
Translation: true

Esse ano o pocket operator completou dez anos desde a sua criação. E, pra celebrar essa marca, a Teenage Engineering decidiu fazer um concurso de criações DIY que envolvam o pocket operator de alguma forma, o `#PO10DIY`. É claro que eu tinha que participar.

Na verdade, quando vi a publicação pela primeira vez, não consegui pensar em nada que pudesse fazer pra entrar. Mas não conseguia tirar da cabeça a ideia de um braço mecânico dançando em conjunto com um pocket operator.

Recentemente estava lendo um artigo publicado por uma equipe de robótica da Apple que experimentou com um robô de mesa que tenta integrar movimentos mais expressivos a sua rotina ([ELEGNT: Expressive and Functional Movement Design for Non-anthropomorphic Robot](https://arxiv.org/pdf/2501.12493)). Esse tipo de robótica (e computação) que tenta fugir de um utilitarismo raso é algo que mora no fundo do meu coração. A própria Teenage Engineering já experimentou com algo muito parecido no ["R", um robô de mesa](https://robosecafe.substack.com/p/criando-o-pocket-operator-television#:~:text=%22R%22%2C%20um%20rob%C3%B4%20de%20mesa) que tinha "emoção" como função.

Esse artigo da Apple reascendeu uma vontade antiga que tenho de tentar criar um robô como o R. Mas, desenvolver (durante os fins de semana) um robô como esses e fazê-lo ser capaz de "ouvir" o meu pocket operator a tempo do prazo do concurso seria uma tarefa hercúlea. Esquece, seria legal, mas não vai dar dessa vez. Deixa pra lá.

Mas e se eu simplificasse um pouco? Na verdade, e se eu simplificasse bastante? Talvez saísse algo legal daí. E se, por exemplo, em vez de fazer um braço robótico eu fizesse um display com uma animação simples de um braço robótico? Daí, quem sabe, quando eu finalmente tiver tempo de montar o meu braço robótico, eu use o aprendizado desse projeto pra fazer o robô dançar ao som do pocket operator.

E se, em vez de uma simples animação de um robô, as pessoas pudessem facilmente modificar código pra adicionar os frames que elas quisessem? Seria como o PO-33 Knock Out, que te permite gravar seus próprios samples, mas para animação. Foi aí que surgiu na minha cabeça a ideia do Pocket Operator Television.

## PO television

O pocket operator television é um dispositivo DIY feito para exibir animações em sincronia com um ou vários pocket operator. Ele usa o PO-Sync para sincronizar automaticamente os quadros de animação com sua música. Funciona no modo `SY5`, se você quiser encadear mais dispositivos, ou no modo `SY4`, se você quiser conectar um fone de ouvido, alto-falante etc.

O PO television permite que você alterne entre padrões de animação com o pressionar de um botão. Ele vem carregado com algumas animações, mas você pode facilmente adicionar seus próprios "animation samples" ao código.

O pocket operator television é feito inteiramente de componentes prontos para uso e peças impressas em 3D. Seu design tenta imitar o pocket operator: placas de circuito pretas expostas, partes douradas e cores fortes em partes de destaque. É fácil construir um pra você!

- [Repositório no GitHub com o código e os modelos 3D](https://github.com/EEmery/po-television)

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
  <iframe 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/iwwsih4J6I4?si=kv8-9qZDV77j-oZn" 
    title="YouTube video player" 
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
    allowfullscreen>
  </iframe>
</div>

## Eletrônica

### Lista de componentes

- 1x Raspberry Pi Pico W – o cérebro do PO television
- 2x conector de áudio de 3,5 m – funcionará como a linha de entrada e saída do dispositivo
- 1x botão – para alternar entre animações
- 2x interruptores – um para ligar/desligar o dispositivo e outro para alternar entre os modos de sincronização (`SY4`/`SY5`)
- 1x display de matriz de LEDs (8x8) – para emitir nossas animações
- 1x level shifter – para converter o sinal de `3,3` V do Raspberry Pi em um sinal de `5 V` para enviar ao display
- 1x conversor buck step-down – para converter uma fonte de alimentação externa para `5 V` e alimentar nosso circuito
- 1x suporte para baterias AAA – você pode usar outras fontes de alimentação, já que usaremos um conversor buck step-down, mas eu recomendaria AAAs, pois são os mesmos usados ​​no pocket operator, então você não precisa carregar vários tipos diferentes com você
- 5x `100k` resistores de `1 ohms`, 1 resistor de `470 ohms` e 1 capacitor de `1000 uF` – serão usados ​​em todo o circuito, mais detalhes abaixo

### O circuito

![Diagrama do circuito]({static}/images/Pasted%20image%2020251102024634.png)

#### Notas sobre a leitura do sinal de entrada de áudio

Queremos ouvir dois sinais vindos da entrada de áudio do dispositivo: o sinal PO-Sync e o sinal de áudio em si. Passaremos ambos por um divisor de tensão (os resistores `r1`) em vez de ler diretamente da fonte. Como a divisão de tensão é feita pela metade, não precisamos usar resistores de `100k` ohms especificamente, você pode usar qualquer valor, desde que sejam iguais.

#### Notas sobre a conexão do botão de troca da animação

O resistor `r1` conectado ao botão de energia garante que tenhamos uma referência de aterramento para quando o botão não for pressionado. Usei um resistor de `100k ohms` porque já estava usando um de mesmo valor no circuito divisor de tensão na leitura do sinal de entrada de áudio, conforme explicado acima. Aqui, você também pode usar valores diferentes para esse resistor no botão de troca da animação, se preferir.

#### Notas sobre o interruptor de troca de modos do PO-Sync

Entre a entrada e saída de áudio, existe um interruptor que permite a troca entre o modo `SY5`, que repassa o sinal de clock do PO-Sync para que outros dispositivos sejam conectados em cadeia, e o modo `SY4`, que copia o sinal de áudio para as duas entradas e permite ouvir o som produzido em um alto falante ou um fone de ouvido.

#### Notas sobre como ligar o display de matriz de LED

Eu conectei o display de matriz de LED conforme recomendado pela equipe da Adafruit no guia do NeoPixel. Você pode aprender mais sobre como usá-los corretamente por lá, especialmente se você quiser modificar seu pocket operator television para funcionar com diferentes displays ou tiras de LED.

![Placa perfurada com os componentes do circuito]({static}/images/Pasted%20image%2020251102025050.png)

## Hardware

Para juntar tudo, depois de prototipar em uma breadboard, encontrei uma placa de circuito preta e dourada que era a coisa mais próxima que consegui encontrar de um pocket operator. Eu queria que o dispositivo final se parecesse o máximo possível com um pocket operator. Soldei todos os componentes eletrônicos mencionados anteriormente, seguindo o diagrama do circuito.

A case impressa em 3D é muito simples. Ela tem como objetivo manter o display, a placa de circuito e o botão de troca de animação juntos. O display de matriz de LED que comprei veio com um cabo JST soldado a ele, então o usei para conectar à placa. Para manter a consistência, também usei um cabo JST para conectar o botão de troca de animação à placa de circuito. A case principal e o cap traseiro podem ser juntados usando parafusos e porcas M2.

Você pode encontrar os modelos 3D que usei nos arquivos `.stl` [na pasta `models`](https://github.com/EEmery/po-television/tree/main/models). Sinta-se à vontade para modificá-los para melhor atendê-lo, já que pode ser necessário alterá-lo para caber na sua placa de circuito e display, caso eles não tenham as mesmas dimensões que os meus.

![O pocket operator television construído]({static}/images/Pasted%20image%2020251102025146.png)

### Adicionando cores na impressão 3D

Se você tem uma impressora com suporte a multi-filamentos, essa etapa fica bem mais fácil. Adicionar algumas cores na impressão 3D vai fazer o pocket operator television ficar mais próximo da estética do pocket operator: partes em dourado e outras em alguma cor de destaque.

Na impressão 3D, eu adicionei textos e fiz uma pequena extrusão neles pra criar um vale, coisa de 0.5 milimetro. Daí eu vim com um pincel com tinta acrílica da cor que eu queria e coloquei a tinta dentro desse pequeno vale. Logo em seguida, passei um papel pra limpar o que sujou por fora, deixando apenas e tinta que ficou presa dentro dos vales do texto. Depois de duas ou três camadas, o resultado ficou razoável.

Como eu construí o PO television tentando seguir a ideia de poder criar seus próprios samples que o PO-33 K.O. oferece, decidi usar laranja como a cor de destaque. O texto "pocket operator" no topo ficou em dourado e o texto "television" e o destaque nas laterais do botão frontal ficaram em laranja.

### O código

#### Setup

Você pode [baixar o repositório](https://github.com/EEmery/po-television) como um `.zip` ou clonar o repositório com `git clone git@github.com:EEmery/po-television.git`. O código usa MicroPython e você precisará instalar o firmware na sua placa, [mas é um processo simples](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3).

Uma vez com o repositório e o firmware instalado, podemos copiar os arquivos da pasta local `src/` para a placa que você estiver usando. Este repositório estabelece no arquivo de requerimentos (`requirements/dev.txt`) uma série de ferramentas para facilitar o desenvolvimento com MicroPython, como o `thonny`, `rshell` e `pipkin`. Para ativar o ambiente virtual com essas ferramentas, basta rodar no seu terminal:

1. `python3 -m venv .venv`

2. `source .venv/bin/activate`

3. `python3 -m pip install -r requirements/dev.txt`

O repositório já contém os arquivos da biblioteca do `neopixel`, que é utilizada para comunicar com o display de LED, então não é necessário fazer a instalação. Mas, caso você sinta a necessidade de re-instalar essa biblioteca, basta rodar o comando abaixo enquanto estiver com o computador conectado a sua placa:

`python3 -m pipkin install neopixel`

Para enviar o código do seu repositório local para a placa, basta usar o comando de cópia do `rshell`:

`rshell cp -r src/* pyboard/`

Se você preferir o desenvolvimento com o `thonny`, que é bem popular quando se trata de desenvolvimento em MicroPython, ao invés de usar o `pipkin` para instalar as bibliotecas e o `rshell` para enviar o código para a placa, basta rodar:

`python3 -m thonny`

#### Mergulhando no código

O código é bem simples. Eu o desenvolvi com MicroPython, já que Python é uma linguagem popular entre hackers. Não usei algoritmos de processamento de sinais digitais complexos ou nada parecido, pelo menos ainda não. Encorajo você a brincar com o código e compartilhar suas criações. Estou planejando experimentar adicionar alguma função que execute uma transformada rápida de Fourier (FFT) ou outras funções de processamento de sinais digitais (DSP). Deve ser interessante ver o que podemos adicionar à lógica da animação para fazê-la responder a informações mais complexas da música que estamos tocando.

Mas mergulhando no código, basicamente temos algo semelhante a uma estrutura de "sense-plan-act" (percepção-planejamento-ação), comum no mundo da robótica. O código primeiro lê o sinal de entrada de áudio e o trata em parâmetros mais fáceis de consumir nos passos seguintes.

Em cada mudança de passo (pulso de clock), chamamos a função de animação para solicitar um novo frame para ser exibido. Esta é a fase de "planejamento" do nosso framework. Passamos para a função de animação alguns parâmetros que conseguimos coletar do pocket operator, para que possamos usá-los (ou não) para construir o próximo frame. A lista de parâmetros [pode ser vista no código](https://github.com/EEmery/po-television/blob/main/src/animation_robot_eyes.py#L141-L168).

A função de animação [retornará 2 parâmetros](https://github.com/EEmery/po-television/blob/main/src/animation_robot_eyes.py#L190). O primeiro é o novo frame, que consiste em uma lista 2D 8x8 onde cada valor é um trio (tupla) representando os valores RGB do pixel (vermelho-verde-azul). Cada elemento no pixel pode ir de 0 a 255. O segundo valor que ele retorna é chamado de memory e deve ser usado como o desenvolvedor desejar. A ideia por trás disso é permitir a passagem de qualquer "estado" entre a chamada de função anterior e a atual, para que o código possa "lembrar" informações relevantes de suas execuções anteriores. Isso poderia ter sido alcançado com um objeto em vez de uma função, mas sinto que poderia ter tornado o código um pouco mais complexo de modificar, dado que um "estado" pode ser alcançado com um parâmetro de função simples, como o que usamos.

Finalmente, com um novo quadro em mãos, atualizamos o display com ele. Este é o nosso estágio de "ação" do framework e o final. Então, prosseguimos para o loop e começamos a "perceber" o sinal na entrada de áudio mais uma vez.

Durante esse loop, também continuamos verificando se o botão de animação foi pressionado. Quando isso acontece, o código alterna a função de animação dentre uma lista de funções de animação disponíveis para uso.

#### Adicionando sua própria animação

Adicionar a sua animação é fácil, você pode começar replicando alguma das animações já existentes pra criar a sua própria.

1. [Animação do braço robótico `animation_robot_arm.py`](https://robosecafe.substack.com/p/criando-o-pocket-operator-television#:~:text=1.%20Anima%C3%A7%C3%A3o%20do%20bra%C3%A7o%20rob%C3%B3tico)

	Essa é a mais simples de todas as funções de animação. Basicamente temos 16 frames na animação e iteramos um a um à medida que a função é chamada em um novo passo. Essa função não utiliza boa parte dos argumentos passados pra ela. O código está comentado para melhor entendimento.

2. [Animação da onda `animation_wave.py`](https://github.com/EEmery/po-television/blob/main/src/animation_wave.py)

	Essa animação é muito semelhante a anterior, com a diferença que ela permite usar qualquer número de frames, não precisa ser exatamente 16, o que acaba tornando um código flexível para ser reutilizado com frequência.

	Aqui, nós guardamos a informação do "cursor" da animação atual na "memory" para lembrarmos onde paramos na próxima chamada da função. Assim, podemos iterar entre os frames um por um. O código está comentado para melhor entendimento.

3. [Animação dos olhos robóticos `animation_robot_eyes.py`](https://github.com/EEmery/po-television/blob/main/src/animation_robot_eyes.py)

	Como mencionado anteriormente, a animação `animation_wave.py` serve como um bom template para ser replicado em outras animações, já que ele permite a flexibilidade de um número qualquer de frames. Essa animação, a `animation_robot_eyes`, é praticamente uma cópia da `animation_wave`, com a única diferença sendo os frames usados, que formam outro desenho.

4. [Animação da visualização da música `animation_music_visualization.py`](https://github.com/EEmery/po-television/blob/main/src/animation_music_visualization.py)

	Essa é uma animação um pouco mais complexa, se comparada às outras. Ela serve principalmente pra demonstrar um possível uso dos parâmetros que são calculados a partir da entrada de áudio do pocket operator. Nela, nós desenhamos uma representação da intensidade do sinal de som em cada um dos passos. O código está comentado em cada etapa para um melhor entendimento.

**Adicione uma chamada à sua nova função de animação**

Seja copiando uma animação já existente e modificando-a ou criando uma nova do zero, é preciso adicionar uma chamada à nova função no loop principal do código. Para isso, no arquivo `main.py`, basta [importar a função](https://github.com/EEmery/po-television/blob/main/src/main.py#L3-L6) e adicionar na [lista de funções chamada `ANIMATIONS`](https://github.com/EEmery/po-television/blob/main/src/main.py#L8-L14).
