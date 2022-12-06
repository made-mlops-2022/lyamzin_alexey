Мною был использован [оффициальный docker-compose](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) для последнего релиза Airflow.
Все нужные модификации для того, чтобы это запускалось на Ubuntu представлены в приложенном docker-compose файле.

1) Необходимо собрать все docker-образы из папки images. Пример запуска
```
docker build -t generate-dataset images/airflow-generate-dataset/.
```
2) После этого нужно через UI задать переменную `model_path` для корректного импорта дага predict.
