<br/>
<p align="center">
  <h3 align="center">April</h3>

  <p align="center">
    A Programming Language to make API's !!
    <br/>
    <br/>
    <a href="https://github.com/merwin-asm/april"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/merwin-asm/april/issues">Report Bug</a>
    .
    <a href="https://github.com/merwin-asm/april/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/merwin-asm/april?color=dark-green) ![Forks](https://img.shields.io/github/forks/merwin-asm/april?style=social) ![Stargazers](https://img.shields.io/github/stars/merwin-asm/april?style=social) ![Issues](https://img.shields.io/github/issues/merwin-asm/april) ![License](https://img.shields.io/github/license/merwin-asm/april) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)
* [Acknowledgements](#acknowledgements)

## About The Project

![Screen Shot](https://cdn.discordapp.com/attachments/951417646191083551/1193927724616654909/image.png?ex=65ae7ed7&is=659c09d7&hm=5fd754a6776bb2998fd877218a1993f8aec01fa8de6a57cee7b3b4bb4e41858e&)

This language was made for making API's great ease and more efficiency. 

The language connects each API endpoint to a specific program/command, in case you want to write the code for the endpoint '/home' in python and '/generate' in Cpp - this can be done.

The language have packages for multiple languages for adapting april to the wanted language (some packages are made by the community too!!) . In case you dont find the required package for utilizing april in your wanted language - don't worry its easy to make a package for your own.

## Built With

- Written in python3
- Makes use of FASTAPI

## Getting Started


### Prerequisites

- Python3
- Pip3
- Redis server

### Installation

WIndows :
```sh
pip install aprillang
```

Linux / MacOs:
```sh
pip3 install aprillang
```

## Usage

Get the list of allowed commands
```sh
april -h
```

Get info of the language
```sh
april -a
```

Compile an .apl file (april file):
- This converts the april code to python3 code
- Compiled file is saved as filename without extention apl + '_apl.py'

```sh
april -c file.apl
```

Run an .apl file (start the API server):
- Format for the command is - april -r <filename> <host:port>

```sh
april -r file.apl 0.0.0.0:8080
```

Get the version of april:

```sh
april -v
```


## Roadmap

See the [open issues](https://github.com/merwin-asm/april/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/merwin-asm/april/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/merwin-asm/april/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See [LICENSE](https://github.com/merwin-asm/april/blob/main/LICENSE.md) for more information.

## Authors

* **Merwin** - *Comp Sci Student* - [Merwin](https://github.com/merwin-asm/) - *Main programmer*

## Contributors

* []()

