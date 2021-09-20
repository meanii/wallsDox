# wallsDox

Is platform to share high quality wallpapers for various platforms.

## Configuration

Rename `config.env` file to `.env`

#### Database configuration

- `DATABASE_URL`: put here postgres sql database URL.

- `CONN_MAX_AGE` : database connection max age. Default set is 0 ( Recommend )

- `DEBUG`: Django developement mode or production mode.

#### Cloudinary configuration

- Create account in [cloudinary](https://cloudinary.com/).

- put `CLOUD_NAME`,  `API_KEY` and `API_SECRET` in [.env](./sample.env) file.


## Installation

Use `pip3 install -r` to install python packages through `requirements.txt file` .

```bash

pip3 install -r requirements.txt

```

## Deployment

```bash

python3 manage.py makemigrations  && python3 manage.py migrate && python3 manage.py runserver

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/meanii/wallsDox/blob/master/LICENSE)

## Copyright

Copyright (C) 2021 [meanii](https://github.com/meanii)
