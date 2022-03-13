<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#additional information">Additional information</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

This project was created by Joanna Kosmalska for the needs of her master's thesis. 

The core idea of this program is searching and filtering law acts.

![law_acts](https://user-images.githubusercontent.com/94289267/147792975-eaae2bf0-a639-4d3b-a3ae-7f59429f35fa.PNG)

### Built With

Technologies used to implementation:

* [Python](https://www.python.org/downloads/)
* [Requests](https://docs.python-requests.org/en/latest/)
* [PyQt6](https://pypi.org/project/PyQt6/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

Below there are basic informations about that how to run app.

### Prerequisites

To run app just download _"Law_acts.exe"_ file from release tab on github project page and run it.

If you have any troubles please see below to Installation section.

### Installation

The easiest way to run program is to just download _"Law_acts.exe"_ file from release tab on github project page and run it

Second option is that:
1. Clone repository with command ```git clone https://github.com/kosmalska/Law_Acts.git``` or just download project from github.
2. Open CMD in local project directory.
3. Execute in CMD that command: ```python gui.py```

If you cannot run app from _"Law_acts.exe"_ file:
1. Download and install Python in version 3.9 from page [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Clone repository with command ```git clone https://github.com/kosmalska/Law_Acts.git``` or just download project from github.
3. Go to project directory and run in CMD this command ```pip install -r requirements.txt```
4. Try to run app from _"Law_acts.exe"_ file.
5. If problem still exists or there are any other problems please open file gui.py in any code editor like e.x. VS Code and then build project in editor.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE -->
## Usage

To start searching you should choose at least one of the available filters or if this is a date range you sholud set proper date range and then you can click on _"Search"_ button. After that if there are any search results you can see on the right panel information about searched law acts like below:
* standard act filename which is clickable link to PDF file and if you click it, it should be open in your default web browser,
* kind of document,
* status.

Search results are limited to 5000 which is caused by security reasons.

If you click on _"I"_ icon it will be open an information window.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Joanna Kosmalska - kosmalska.as@gmail.com

Project Link: [https://github.com/kosmalska/Law_Acts](https://github.com/kosmalska/Law_Acts)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ADDITIONAL INFORMATION -->
## Additional information

To realize this project was needed to use ISAP open API which can be accessed by below link:

* [ISAP API](http://isap.sejm.gov.pl/api/isap/)

<p align="right">(<a href="#top">back to top</a>)</p>
