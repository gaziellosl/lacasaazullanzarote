# coding=utf-8
import os

def parseCSV(dir):

    with open(dir, 'r') as file:
        text = file.read()

    text = text.replace('\r\n', '\n')
    ntext = text.split('\n')

    text = []
    for i in range(len(ntext)):
        if ntext[i] != '':
            text += [ntext[i]]

    for i in range(len(text)):
        text[i] = text[i].split(';')

    #Clean empty
    for item in text[0]:
        if item == '':
            text[0].remove(item)
    #Clean spaces
    for i in range(len(text[0])):
        text[0][i] = text[0][i].replace(" ", "")

    data = {}
    for i in range(1,len(text)):
        if text[i][0] != '':
            data[text[i][0]] = {}
            for j in range(1, len(text[0])):
                if text[i][0] == "imgs":
                    data[text[i][0]][text[0][j]] = [x.strip() for x in text[i][j].split(',')]

                else:
                    data[text[i][0]][text[0][j]] = text[i][j].strip()


                # elif text[0][j] == "simulated":
                #     data[last][text[0][j]] = (data[last][text[0][j]] == "TRUE")

    return data

def generateHTMLFile(dir, data, sections, language):

    text = ""
    text += """
<!DOCTYPE html>
<html>
<title>%s</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link type="text/css" rel="stylesheet" href="./css/styles.css">
<link type="text/css" rel="stylesheet" href="./css/slideshow.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
<!-- Scripts -->
<script src="./js/scripts.js"></script>
<!-- Libraries -->
<!-- AOS -->
<link rel="stylesheet" href="./lib/aos/aos.css" />
<script src="./lib/aos/aos.js"></script>

<style>
body {font-family: "Times New Roman", Georgia, Serif;}
h1, h2, h3, h4, h5, h6 {
  font-family: "Playfair Display";
  letter-spacing: 5px;
}
</style>
<body>

<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-padding w3-card" style="letter-spacing:4px;">
    <a href="#home" class="w3-bar-item w3-button">La Casa Azul</a>
    <div class="w3-right w3-hide-small" id="links">
      <a href="#about" class="w3-bar-item w3-button">Apartamentos</a>
      <a href="#reserve" class="w3-bar-item w3-button">Reserva</a>
    </div>
    <!-- "Hamburger menu" / "Bar icon" to toggle the navigation links -->
    <a href="javascript:void(0);" class="w3-bar-item w3-button w3-right w3-show-small" onclick="hamburgerMenu()">
      <i class="fa fa-bars"></i>
    </a>
    <!-- Right-sided navbar links. Hide them on small screens -->
    <div class="w3-show-small" style="display:none;" id="hamburguer_links">
      <hr style="margin-bottom:0;margin-top:45px">
      <a href="#about" class="w3-bar-block w3-button" onclick="hamburgerMenu()" >Apartamentos</a>
      <hr style="margin:0">
      <a href="#reserve" class="w3-bar-block w3-button" onclick="hamburgerMenu()">Reserva</a>
    </div>
  </div>
</div>

<header class="fullScreen" style="background-image:url(./img/casa_azul/piscina_natural.jpg)" id="home">
  <img class="w3-display-topright w3-padding-xlarge w3-right widthLogo" style="position:relative;" src="./img/logo_casa_azul.jpg" alt="Logo">
  <div class="w3-display-bottomleft w3-padding-large">
    <h1 class="bigFont" style="color:white">La Casa Azul</h1>
  </div>
</header>

<!-- Page content -->
<div class="w3-content" style="max-width:1100px">

""" % (data["home"][language])
    for i in range(len(sections)):
        section = sections[i]
        text += """

<!-- {} Section -->

  <div class="w3-row w3-padding-64" id="{}">
""".format(section['id'], section['id'])
        if i%2: #impares
            text += insertSlidesShow(i, section, language)

        text += """

    <div class="w3-col m6 w3-padding-xlarge" data-aos="fade-right" data-aos-anchor-placement="center-bottom">
      <h1 class="w3-center">{}</h1><br>
      <h5 class="w3-center">{}</h5>
      <p class="w3-large">{}</p>
      <p class="w3-large w3-text-grey w3-hide-medium">{}
      </p>
    </div>
""".format(section['title'][language],section['subtitle'][language],section['description'][language],section['subdescription'][language])
        if not (i%2): #impares
            text += insertSlidesShow(i, section, language)
        text += """
    </div>
"""
#         text += """
#
# <div class="w3-col m6 w3-padding-large w3-show-small" id="slideshow-container_{}" style="height:100%;margin:0;margin-top:80px;margin-bottom:auto" data-aos="fade-left" data-aos-anchor-placement="center-bottom">
# """.format(section['id'])
#         text += insertSlidesShow(i, section, language)
#         text += """
# </div>
# """

        text += """
  <hr>
"""

    text += """"

  <!-- Reserve Section -->
  <div class="w3-container w3-padding-64" id="reserve">
    <h1>Reserva</h1><br>
    <p>Complete el formulario y le contestaremos con la mayor brevedad posible.</p>
    <form action="/action_page.php" target="_blank">
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Nombre" required name="Name"></p>
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Correo electrónico" required name="Email"></p>
      <p><input class="w3-input w3-padding-16" type="number" placeholder="Número de personas" required name="People"></p>
      <p class="w3-input w3-padding-16" style="color:grey;">
        Apartamento:
      <select class="dropdown" required name="Appartment">
        <option value="Cualquiera">Cualquiera</option>
        <option value="Timanfaya">Timanfaya</option>
        <option value="Jameos">Jameos</option>
        <option value="La Cueva">La Cueva</option>
        <option value="Mirador">Mirador</option>
      </select>
      </p>
      <p><input class="w3-input w3-padding-16" type="number" placeholder="Número de noches" required name="Noches"></p>
      <p class="w3-input w3-padding-16" style="color:grey;">A partir del:     <input class="dropdown" type="datetime-local" placeholder="Date and time" required name="date" value="2019-01-01T16:00"></p>
      <p><input class="w3-input w3-padding-16" type="text" placeholder="Message" required name="Message"></p>
      <p><button class="w3-button w3-light-grey w3-section" type="submit">Solicitar reserva</button></p>
    </form>
  </div>

</div>

<footer class="w3-center w3-light-grey w3-padding-32">
    <div class="w3-row">
        <!-- <div class="w3-left w3-padding-large">
            <img class src="./img/logo_casa_azul.jpg" alt="">
        </div> -->
        <div class="w3-left m6 w3-padding-large">
            <img class="widthLogo" src="./img/logo_casa_azul.jpg" alt="Logo">
            <p>Calle las Salinas, 30, 35542 Punta Mujeres, Las Palma</p>
            <p><a href="gaziellosl@gmail.com" title="Email Address">gaziellosl@gmail.com</a></p>
            <p><a href="tel:+34 670727113" title="Telephone number">+34 670 727 113</a></p>

        </div>
        <div class="w3-right m6 w3-padding-large">

            <a target="_blank" href="https://www.instagram.com/pharmaseal.co/">
                <div class="social__circle"><i class="fab fa-instagram fa-1x"></i></div>
            </a>

            <a target="_blank" href="https://www.linkedin.com/company/pharmaseal/">
                <div class="social__circle"><i class="fab fa-linkedin-in fa-1x"></i></div>
            </a>

            <a target="_blank" href="https://twitter.com/pharmaseal">
                <div class="social__circle"><i class="fab fa-twitter fa-1x"></i></div>
            </a>

            <a target="_blank" href="https://www.facebook.com/casaazullanzarote">
                <div class="social__circle"><i class="fab fa-facebook-f fa-1x"></i></div>
            </a>

        </div>
      </div>

      <div class="w3-row">

        <div class="w3-right m6 w3-padding-large">

            <a href="/sitemap.xml/" class="has-text-white">Sitemap</a>

            <a href="/cookie-policy/" class="has-text-white">Cookies</a>

            <a href="/privacy-policy/" class="has-text-white">Privacy Policy</a>

            <a href="/terms-conditions/" class="has-text-white">Terms and conditions</a>

        </div>
    </div>
</footer>

<script src="./js/execute.js"></script>
</body>
</html>
"""
    with open(dir+'/../index.html', 'w') as file:
        file.write(text)

def insertSlidesShow(n, section, language):

    text = ""
    text += """
    <div class="w3-col m6 w3-padding-xlarge w3-hide-small" id="slideshow-container_{}" data-aos="zoom-left" data-aos-anchor-placement="top-bottom">

    <!-- Slideshow container -->
    <div class="slideshow-container" style="max-width:90%;padding-top:15%">

      <!-- Full-width images with number and caption text -->
""".format(section['id'])

    for i in range(len(section['imgs']['id'])):
        text += """
      <div class="slides fade slides_{}">
        <div class="numbertext">{} / 3</div>
        <img src="./img/{}/{}" style="width:100%">
        <div class="text">{}</div>
      </div>
""".format(section['id'], i+1, section['id'], section['imgs']['id'][i], section['imgs'][language][i])

    text += """
      <!-- Next and previous buttons -->
      <a class="prev" onclick="showSlidesPlus({}, '{}',-1)">&#10094;</a>
      <a class="next" onclick="showSlidesPlus({}, '{}',+1)">&#10095;</a>
    </div>
    <br>

    <!-- The dots/circles -->
    <div style="text-align:center">
""".format(n, section['id'], n, section['id'])

    for i in range(len(section['imgs']['id'])):
        text += """
      <span class="dot dot_{}" onclick="showSlides({}, '{}', to={})"></span>
""".format(section['id'], n, section['id'], i)

    text += """
    </div>
    </div>
    <script type="text/javascript">
    slideIndex.push(0);
    showSlides({}, '{}');
    initDivMouseOver('{}');
    setInterval(showSlidesPlusWithCheck, 5{}00, {}, '{}', 1);
    </script>
""".format(n, section['id'], section['id'], i, n, section['id'])

    return text


def main():
    dir = os.path.dirname(os.path.abspath(__file__))
    data = parseCSV(dir+"/definitions.csv")
    files = os.listdir(dir+"/sections/")
    files.sort()
    sections = []
    for i in range(len(files)):
        sections.append(parseCSV(dir+"/sections/"+files[i]))
        sections[-1]['id'] = files[i][1:-4]
    generateHTMLFile(dir, data, sections, "spanish")

if __name__ == '__main__':
    main()
