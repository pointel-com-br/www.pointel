# Tecnologia frontend web - SPA e PWA

SPA (Single Page Application) e PWA (Progressive Web Application) são duas tecnologias amplamente utilizadas no desenvolvimento frontend web para criar experiências de usuário ricas e interativas. Embora compartilhem algumas semelhanças, elas têm finalidades e características distintas. Vamos explorar cada uma delas:

1. SPA (Single Page Application):

- Uma Single Page Application é uma aplicação web que funciona dentro de uma única página, onde o conteúdo da página é dinamicamente atualizado conforme o usuário interage com a aplicação, sem a necessidade de recarregar a página inteira.
- As SPAs são construídas usando JavaScript, geralmente com frameworks como React, Angular ou Vue.js, que permitem a renderização dinâmica do conteúdo na página.
- Quando um usuário navega em uma SPA, apenas os dados necessários são solicitados ao servidor, geralmente por meio de APIs RESTful, e a resposta é usada para atualizar a página sem recarregá-la completamente.
- As SPAs oferecem uma experiência de usuário suave e rápida, sem interrupções entre as transições de página. Elas são amplamente utilizadas para criar aplicativos web complexos, como aplicativos de e-commerce, ferramentas de produtividade e plataformas de mídia social.

1. PWA (Progressive Web Application):
- Uma Progressive Web Application é uma aplicação web que utiliza recursos e tecnologias modernas para fornecer uma experiência semelhante a um aplicativo nativo, mesmo sendo acessada através de um navegador.
- As PWAs são construídas com HTML, CSS e JavaScript e são projetadas para serem responsivas, confiáveis e envolventes, independentemente do dispositivo ou navegador usado pelo usuário.
- Uma das principais características das PWAs é a capacidade de serem instaladas e executadas offline. Elas usam Service Workers, um recurso do navegador, para armazenar em cache recursos essenciais e fornecer funcionalidades offline.
- As PWAs podem ser adicionadas à tela inicial de um dispositivo, como um aplicativo nativo, e oferecem notificações push, acesso a recursos do dispositivo (como câmera e localização) e carregamento rápido.
- As PWAs são uma abordagem popular para fornecer experiências de usuário de alta qualidade em dispositivos móveis, proporcionando descoberta fácil, instalação simplificada e engajamento contínuo.

Em resumo, as SPAs são aplicativos web que funcionam em uma única página, atualizando o conteúdo dinamicamente, enquanto as PWAs são aplicativos web que aproveitam recursos modernos para fornecer uma experiência semelhante a um aplicativo nativo, incluindo instalação, notificações e funcionalidade offline. Ambas as tecnologias desempenham um papel importante no desenvolvimento frontend web e podem ser combinadas para criar aplicativos web avançados e de alto desempenho.

## O que são Progressive Web Apps?

- Os três pilares de uma aplicação
- Capazes
- Confiáveis
- Instaláveis

- O melhor de dois mundos

A web é uma plataforma incrível. Sua combinação de onipresença entre dispositivos e sistemas operacionais, seu modelo de segurança centrado no usuário e o fato de que nem sua especificação nem sua implementação são controladas por uma única empresa tornam a web uma plataforma única para o desenvolvimento de software. Combinado com sua capacidade de link inerente, é possível pesquisar e compartilhar o que você encontrou com qualquer pessoa, em qualquer lugar. Sempre que você acessa um site, ele está atualizado e sua experiência com esse site pode ser tão efêmera ou permanente quanto você desejar. Os aplicativos Web podem alcançar _qualquer pessoa, em qualquer lugar, em qualquer dispositivo_ com uma única base de código.

As aplicações criadas para plataformas específicas são conhecidas por serem incrivelmente ricas e confiáveis. Elas estão sempre presentes, nas telas iniciais, nos docks e nas barras de tarefas. Elas funcionam independentemente da conexão de rede. Elas são lançadas em seu próprio ambiente local. Elas podem ler e gravar arquivos do sistema de arquivos local, acessar hardware conectado via USB, serial ou bluetooth e até mesmo interagir com dados armazenados em seu dispositivo, como contatos e eventos de calendário. Nessas aplicações, você pode fazer coisas como tirar fotos, ver a reprodução de músicas listadas na tela inicial ou controlar a reprodução de músicas em outro aplicativo. As aplicações criadas para plataformas específicas parecem _parte_ do dispositivo em que são executadas.

Capacidades versus alcance de aplicações de plataformas específicas, aplicações web e aplicações web progressivas.

Se você pensar em aplicações de plataformas específicas e aplicações web em termos de recursos e alcance, as aplicações de plataformas específicas representam o melhor em termos de capacidades, enquanto as aplicações web representam o melhor em termos de alcance. Então, onde se encaixam as Progressive Web Apps?

Progressive Web Apps - PWA (aplicações web progressivas) são desenvolvidas e aprimoradas com APIs modernas para fornecer recursos aprimorados, confiabilidade e capacidade de instalação, ao mesmo tempo que alcançam _qualquer pessoa, em qualquer lugar, em qualquer dispositivo_ com uma única base de código.

### Os três pilares de uma aplicação

As Progressive Web Apps são aplicações web que foram projetadas para serem capazes, confiáveis e instaláveis. Esses três pilares as transformam em uma experiência que parece uma aplicação de plataforma específica.

#### Capazes

A web, por si só, já é bastante capaz. Por exemplo, você pode construir um aplicativo de chat de vídeo hiper-local usando WebRTC, geolocalização e notificações push. Você pode tornar esse aplicativo instalável e permitir conversas virtuais com WebGL e WebVR. Com a introdução do Web Assembly, os desenvolvedores podem explorar outros ecossistemas, como C, C++ e Rust, e trazer décadas de trabalho e recursos para a web também. O Squoosh.app, por exemplo, aproveita tudo isso para sua compressão de imagem avançada.

Até recentemente, apenas aplicações de plataformas específicas tinham essas capacidades. Embora alguns recursos ainda estejam fora do alcance da web, APIs novas e futuras estão procurando mudar isso, expandindo o que a web pode fazer com recursos como acesso ao sistema de arquivos, controles de mídia, emblemas de aplicativos e suporte total à área de transferência. Todos esses recursos são desenvolvidos com o modelo de permissão seguro e centrado no usuário da web, de forma a garantir que entrar num site jamais seja uma proposta assustadora para os usuários.

Dentre as APIs modernas, Web Assembly e novas e futuras APIs, as aplicações web são mais capazes do que nunca, e esses recursos não param de crescer.

#### Confiáveis

Uma Progressive Web App confiável parece rápida e confiável, independentemente da rede.

A velocidade é fundamental para fazer com que os usuários _usufruam_ da sua experiência. Na verdade, conforme o tempo de carregamento da página vai de 1 segundo a dez segundos, a probabilidade de um usuário saltar fora aumenta em 123%. O desempenho não para depois do evento `onload`. Os usuários nunca devem se perguntar se sua interação - por exemplo, ao clicar em um botão - foi registrada ou não. A rolagem e a animação devem ser suaves. O desempenho afeta toda a sua experiência, desde como os usuários percebem sua aplicação até a forma como ela realmente funciona.

Finalmente, aplicações confiáveis precisam ser utilizáveis independentemente da conexão de rede. Os usuários esperam que as aplicações sejam capazes de iniciar em conexões de rede lentas ou instáveis ou mesmo quando estão offline. Eles esperam que o conteúdo mais recente com o qual interagiram, como faixas de mídia ou ingressos e itinerários, esteja disponível e seja utilizável, mesmo que seja difícil obter uma solicitação para o seu servidor. Quando uma solicitação não é possível, eles esperam ser informados de que há problemas em vez de assistir à aplicação falhar ou travar silenciosamente.

Os usuários adoram aplicações que respondem à interação num piscar de olhos e em experiências nas quais podem confiar.

#### Instaláveis

Progressive Web Apps instaladas são executadas numa janela independente em vez de numa aba do navegador. Elas podem ser iniciadas na tela inicial do usuário, no dock, na barra de tarefas ou na prateleira. É possível procurá-las num dispositivo e alternar entre elas com o alternador de aplicações, fazendo com que pareçam parte do dispositivo em que estão instaladas.

Novas capacidades são abertas depois da instalação de uma aplicação web. Os atalhos de teclado normalmente reservados durante a execução no navegador tornam-se disponíveis. As Progressive Web Apps podem se registrar para aceitar conteúdo de outras aplicações ou para ser a aplicação default para lidar com diferentes tipos de arquivos.

Quando uma Progressive Web App sai de uma aba e vai para uma janela de aplicação standalone, ela transforma a maneira como os usuários pensam sobre ela e como interagem com ela.

### O melhor de dois mundos

Em sua essência, as Progressive Web Apps são apenas aplicações web. Através de um aprimoramento progressivo, novos recursos são ativados em navegadores modernos. Usando service workers e um manifesto de web app, sua aplicação web torna-se confiável e instalável. Se os novos recursos não estiverem disponíveis, os usuários ainda terão a experiência essencial.

Os números não mentem! As empresas que lançaram Progressive Web Apps obtiveram resultados impressionantes. Por exemplo, o Twitter teve um aumento de 65% nas páginas por sessão, 75% mais Tweets e uma redução de 20% na taxa de rejeição, tudo isso enquanto reduzia o tamanho do aplicativo em mais de 97%. Depois de mudar para uma PWA, a Nikkei recebeu 2,3 vezes mais tráfego orgânico, 58% mais assinaturas e 49% mais usuários ativos diários. O Hulu substituiu sua experiência desktop de plataforma específica por uma Progressive Web App e viu um aumento de 27% nas visitas de retorno.

As Progressive Web Apps fornecem a você uma oportunidade única de oferecer uma experiência na web que seus usuários irão adorar. Usando os mais recentes recursos da web para trazer recursos aprimorados e confiabilidade, as Progressive Web Apps permitem que o que você constrói seja instalado por _qualquer pessoa, em qualquer lugar, em qualquer dispositivo_ com uma única base de código.
