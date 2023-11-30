<a name="readme-top"></a>
<br />
<div align="center">

  <h1 align="center">WcTool</h3>

  <p align="center">
    John Crickett's coding challenge I
    <br />
    <a href="https://codingchallenges.substack.com/p/coding-challenge-1"><strong>See the coding challenge »</strong></a>
    <br />
    <br />
  </p>
</div>

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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

`wctool` is the (aspiring) clone of Linux's `wc` command. Print newline, word, and byte counts for each file

### Built With
* Python
* Typer
* Poetry

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Poetry
  ```sh
  pip install poetry
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/manishtrouble/jccodingchallenge.git
   ```
2. Go to the project directory
   ```sh
   cd jccodingchallenge/wctool/wctool
   ```
3. Install dependencies
   ```sh
   poetry install
   ```
4. Create a new virtual environment
   ```sh
   poetry shell
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

    ccwc [OPTION]... [FILE]...

### Description
Print newline, word, and byte counts for each FILE. A
word is a non-zero-length sequence of characters delim‐
ited by white space. It supports the following options:

    -c, --bytes
            print the byte counts

    -m, --chars
            print the character counts

    -l, --lines
            print the newline counts

    -w, --words
            print the word counts

    --help display this help and exit

<p align="right">(<a href="#readme-top">back to top</a>)</p>