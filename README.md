## Backedn Lab2-3 - Basic REST API development
Коваленко Владислав Юрійович ІМ-24

Variant: number in group % 3 = 6 % 3 = 0 - Accounting for income

# Usage
> [!IMPORTANT]
> To use code, you need Python on your pc

1. Clone this repo `git clone https://github.com/VladiusVostokus/Backend-lab2`
2. cd into project `cd Backend-lab2`
3. Create virtual environment `python3 -m venv env`
4. Activate virtual environment `source ./env/bin/activate`
5. Install requirements `pip install -r requirements.txt`
6. Run project `flask --app src/app run`

To run in Docker container 
1. Build image `docker build . -t <image_name>:latest`
2. Run container `docker run -it --rm --network=host -e PORT=<your_port> <image_name>:latest`
3. Use `docker-compose build` and `docker-compose up` to use docker-compose
