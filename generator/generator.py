# coding=utf-8

# TODO
# - Apartado localización y como llegar. Tambien proponer traslado aeropuerto
# - Actividades extra (turismo disponible)
# - Reserva boton gordo inciio
# -

import os

def parseCSV(dir, stdout=0):

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
    for i in range(1,len(text)): #lines
        if text[i][0] != '':
            data[text[i][0]] = {}
            for j in range(1, (min(len(text[0]),len(text[i])))):
                if stdout:
                    print(i,j)
                    print(text[i][0])
                    print(text[0][j])
                    print(text[i][j].strip())
                if text[i][0] == "imgs":
                    data[text[i][0]][text[0][j]] = [x.strip() for x in text[i][j].split(',')]

                else:
                    data[text[i][0]][text[0][j]] = text[i][j].strip()


                # elif text[0][j] == "simulated":
                #     data[last][text[0][j]] = (data[last][text[0][j]] == "TRUE")

    return data

def generateHTMLFile(dir, data, sections, language, name):

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
""" % (data["home"][language])

    text += """

<!-- Navbar (sit on top) -->
<div class="w3-top">
  <div class="w3-bar w3-white w3-padding w3-card" style="letter-spacing:4px;">
    <a href="#home" class="w3-bar-item w3-button">{}</a>
    <div class="w3-right w3-hide-small" id="links">
      <a href="#{}" class="w3-bar-item w3-button">{}</a>
      <a href="#location" class="w3-bar-item w3-button">{}</a>
      <a href="#reserve" class="w3-bar-item w3-button">{}</a>
      <a href="javascript:void(0);" class="w3-bar-item w3-button w3-right w3-hide-small" onclick="dropDownClick(3)" id="dropdown_language_button">
        <i class="fa fa-globe"></i>
      </a>
      <div id="dropdown_language" class="w3-medium w3-dropdown-content w3-bar-block w3-border"  style="margin-right: 15px;margin-top: 40px; right:0;float:right;">
        <a href="es" onclick="selectLanguage('es')" class="w3-bar-item w3-button">Español</a>
        <a href="en" onclick="selectLanguage('en')" class="w3-bar-item w3-button" value="Timanfaya">English</a>
        <a href="fr" onclick="selectLanguage('fr')" class="w3-bar-item w3-button" value="Jameos">Français</a>
        <a href="it" onclick="selectLanguage('it')" class="w3-bar-item w3-button" value="La Cueva">Italiano</a>
        <a href="de" onclick="selectLanguage('de')" class="w3-bar-item w3-button" value="Mirador">Deutsch</a>
      </div>
    </div>
    <!-- "Hamburger menu" / "Bar icon" to toggle the navigation links -->
    <a href="javascript:void(0);" class="w3-bar-item w3-button w3-right w3-show-small" onclick="dropDownClick(1)" id="dropdown_hamburguer_button">
      <i class="fa fa-bars"></i>
    </a>
    <!-- Right-sided navbar links. Hide them on small screens -->
    <div class="w3-show-small" style="display:none;" id="dropdown_hamburguer">
      <hr style="margin-bottom:0;margin-top:45px">
      <a href="#{}" class="w3-bar-block w3-button" style="width:100%;text-align:left" onclick="dropDownClick(1)" >{}</a>
      <hr style="margin:0">
      <a href="#location" class="w3-bar-block w3-button" style="width:100%;text-align:left" onclick="dropDownClick(1)">{}</a>
      <hr style="margin:0">
      <a href="#reserve" class="w3-bar-block w3-button" style="width:100%;text-align:left" onclick="dropDownClick(1)">{}</a>
      <hr style="margin:0">
      <a class="w3-bar-block w3-button" style="width:100%;text-align:left" onclick="dropDownClick(2)" id="dropdown_language_hamburguer_button">{}</a>
    </div>
    <div id="dropdown_language_hamburguer" class="w3-medium w3-dropdown-content w3-bar-block w3-border"  style="margin-right: 15px;">
        <a href="es" onclick="dropDownClick(2, setLanguage('es'))" class="w3-bar-item w3-button">Español</a>
        <a href="en" onclick="dropDownClick(2, setLanguage('en'))" class="w3-bar-item w3-button" value="Timanfaya">English</a>
        <a href="fr" onclick="dropDownClick(2, setLanguage('fr'))" class="w3-bar-item w3-button" value="Jameos">Français</a>
        <a href="it" onclick="dropDownClick(2, setLanguage('it'))" class="w3-bar-item w3-button" value="La Cueva">Italiano</a>
        <a href="de" onclick="dropDownClick(2, setLanguage('de'))" class="w3-bar-item w3-button" value="Mirador">Deutsch</a>
    </div>
  </div>
</div>

<header class="fullScreen" style="background-image:url(./img/casa_azul/piscina_natural.jpg)" id="home">
  <img class="w3-display-topright w3-padding-xlarge w3-right widthLogo" style="position:relative;" src="./img/logo_casa_azul.jpg" alt="Logo">
  <div class="w3-display-bottomleft w3-padding-large">
    <h1 class="bigFont" style="color:white">{}</h1>
  </div>
</header>

<!-- Page content -->
<div class="w3-content" style="max-width:1100px">

""".format(data["home"][language],
        sections[0]['id'],
        data["appartment"][language],
        data["location"][language],
        data["reserve"][language],
        sections[0]['id'],
        data["appartment"][language],
        data["location"][language],
        data["reserve"][language],
        data["language"][language],
        data["home"][language])

        #<a href="#reserve" class="redButton"> <br style="line-height:105px"> RESERVA <br> AHORA!</a>



    for i in range(len(sections)):
        section = sections[i]
        text += """

<!-- {} Section -->

  <div class="w3-row w3-padding-64 slider_container" id="{}">
""".format(section['id'], section['id'])

        text += insertSlidesShow(i, section, language)

        text += """

    <div class="w3-col m6 w3-padding-xlarge slide_container_middle" data-aos="fade-right" data-aos-anchor-placement="center-bottom">
      <h1 class="w3-center">{}</h1><br>
      <h5 class="w3-center">{}</h5>
      <p class="w3-large">{}</p>
      <p class="w3-large w3-text-grey w3-hide-medium">{}</p>
""".format(section['title'][language],section['subtitle'][language],section['description'][language],section['subdescription'][language])

        if 'price' in section:
            text += """
      <p class="w3-large w3-tag w3-light-grey">{}: {}€/{}</p>""".format(data["price"][language], section["price"]['id'], data["night"][language])

        text += """
    </div>
  </div>
<hr>
"""
    text += """

<!-- Map Section -->
<div class="w3-container w3-padding-64" style="margin-right:5vw;margin-left:5vw" id="location">
  <div class="w3-col m6 w3-padding-large slide_container_middle" data-aos="fade-right" data-aos-anchor-placement="center-bottom">
    <h1 class="w3-center">{}</h1><br>
    <p class="w3-large">{}</p>
    <h5 class="w3-center">{}</h5>
    <p class="w3-large">{}</p>
  </div>
  <div class="w3-col m6 w3-padding-large slide_container_left" data-aos="flip-left" data-aos-anchor-placement="top-bottom">
     <iframe style="width:100%;height:55vh;" id="gmap_canvas" src="https://maps.google.com/maps?q=Calle%20las%20Salinas%2C%2030%2C%2035542%20Punta%20Mujeres%2C%20Las%20Palma&t=&z=13&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0">
     </iframe>
     <p class="w3-text-grey">Calle las Salinas, 30.      35542, Punta Mujeres, Las Palmas</p>
  </div>
</div>
<hr>
""".format(data["find"][language],
    data["directions"][language],
    data["transfer"][language],
    data["transfer_description"][language],
    data["people"][language]
    )

    text += """
  <!-- Reserve Section -->
  <div class="w3-container w3-padding-64" style="margin-right:5vw;margin-left:5vw" id="reserve">
    <h1>{}</h1><br>
    <p class="w3-large">{}</p>
    <form onsubmit="sendEmail(); return false;">
      <p class="w3-large"><input class="w3-input w3-padding-16" type="text" placeholder="{}" required name="Name"></p>
      <p class="w3-large"><input class="w3-input w3-padding-16" type="text" placeholder="{}" required name="Email"></p>
      <p class="w3-large"><input class="w3-input w3-padding-16" type="number" placeholder="{}" required name="People"></p>
      <div class="w3-dropdown-click" style="position:absolute;margin-left:120px;">
      <button onclick="dropDownClick(0)" class="w3-button w3-large w3-light-grey" id="dropdown_reserve_button" type="button">{}</button>
      <div id="dropdown_reserve" class="w3-large w3-dropdown-content w3-bar-block w3-border">
        <div class="w3-bar-item w3-button" onclick="dropDownClick(0, setDropDownButtonName(0, 'Mirador'))" value="Mirador">Mirador</div>
        <div class="w3-bar-item w3-button" onclick="dropDownClick(0, setDropDownButtonName(0, 'Timanfaya'))" value="Timanfaya">Timanfaya</div>
        <div class="w3-bar-item w3-button" onclick="dropDownClick(0, setDropDownButtonName(0, 'Jameos'))" value="Jameos">Jameos</div>
        <div class="w3-bar-item w3-button" onclick="dropDownClick(0, setDropDownButtonName(0, 'La Cueva'))" value="La Cueva">La Cueva</div>
      </div>
      </div>
      <p class="w3-large w3-input w3-padding-16" style="color:grey;" id="appartmentFormTitle" >{}:</p>
      <p class="w3-large"><input class="w3-input w3-padding-16" type="number" placeholder="{}" required name="Noches"></p>
      <p class="w3-large w3-input w3-padding-16" style="color:grey;" id="dateFormTitle">{}     <input id="dateForm" class="dropdown" type="date" placeholder="Date" required name="date" ></p>
      <p class="w3-large"><input class="w3-input w3-padding-16" type="text" placeholder="{}" ></p>
      <p class="w3-large"><button class="w3-button w3-light-grey w3-section w3-right" type="submit">{}</button></p>
    </form>
  </div>

</div>

""".format(data["reserve"][language],
    data["reserve_description"][language],
    data["name"][language],
    data["email"][language],
    data["people"][language],
    data["appartment"][language],
    data["appartment"][language],
    data["nights"][language],
    data["from"][language],
    data["message"][language],
    data["reserveButton"][language]
    )

    text += """

<footer class="w3-center w3-light-grey w3-padding-32">
    <div class="w3-row">
      <div class="w3-left m6 w3-padding-large">
          <img class="widthLogo" src="./img/logo_casa_azul.jpg" alt="Logo">
      </div>
      <div class="w3-centered m6 w3-padding-large">
          <p>Calle las Salinas, 30.      35542, Punta Mujeres, Las Palmas</p>
          <p><a href="mailto: gaziellosl@gmail.com" title="Email Address">gaziellosl@gmail.com</a></p>
          <p><a href="tel:+34 670727113" title="Telephone number">+34 670 727 113</a></p>
          <a href="https://www.facebook.com/casaazullanzarote" style="text-decoration: none;">
            <div class=" w3-button">
              <div class="icon_logo" style="background-image:url(./img/logo/facebook.png)"></div>
            </div>
          </a>
          <a href="https://www.airbnb.com/users/show/174871850" style="text-decoration: none;">
            <div class=" w3-button">
              <div class="icon_logo" style="background-image:url(./img/logo/airbnb.png)"></div>
            </div>
          </a>
          <a href="https://www.booking.com/hotel/es/casa-azul-punta-mujeres.es.html" style="text-decoration: none;">
            <div class=" w3-button">
              <div class="icon_logo" style="background-image:url(./img/logo/booking.png)"></div>
            </div>
          </a>
      </div>
    </div>
</footer>

<script src="./js/execute.js"></script>
</body>
</html>
"""
    with open(dir+'/../'+ name, 'w') as file:
        file.write(text)

def insertSlidesShow(n, section, language):

    text = ""
    if (n%2==0):
        text += """
    <div class="w3-col m6 w3-padding-xlarge slide_container_right" id="slideshow-container_{}" data-aos="flip-left" data-aos-anchor-placement="top-bottom">
""".format(section['id'])
    else:
        text += """
    <div class="w3-col m6 w3-padding-xlarge slide_container_left" id="slideshow-container_{}" data-aos="flip-left" data-aos-anchor-placement="top-bottom">
""".format(section['id'])

    text += """
    <!-- Slideshow container -->
    <div class="slideshow-container" style="max-width:90%;padding-top:15%">

      <!-- Full-width images with number and caption text -->
"""

    for i in range(len(section['imgs']['id'])):
        text += """
      <div class="slides fade slides_{}">
        <div class="numbertext">{} / 3</div>
        <div class="img_container" style="background-image: url(./img/{}/{})"></div>
        <div class="textSlides">{}</div>
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
    initDivMouseOver('slideshow-container_{}');
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
    generateHTMLFile(dir, data, sections, "spanish", "es.html")
    generateHTMLFile(dir, data, sections, "english", "en.html")
    generateHTMLFile(dir, data, sections, "french", "fr.html")

if __name__ == '__main__':
    main()
