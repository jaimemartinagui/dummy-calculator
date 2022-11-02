# dummy-calculator

A simple calculator without using arithmetic operations.

To use the calculator:

  1. Clone this repository:

  `git clone https://github.com/jaimemartinagui/dummy-calculator.git`

  2. Build the Docker image:

  `docker build -t <IMAGE_NAME> <PATH_TO_DOCKERFILE>` (e.g. `docker build -t dummy-calculator .`)

  3. Create a container from the image:

  `docker run -i --rm <IMAGE_NAME>` (e.g. `docker run -i --rm dummy-calculator`)
