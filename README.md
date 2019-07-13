# CSV Streamer with PubSub and BigQuery

Stream CSV data via PubSub and into BigQuery using simple Python scripts and the Google Cloud libaries for PubSub and Bigquery. 
For best results use Python 3.

# Install dependencies

```
pip3 install requirements.txt
```

# Stream to PubSub

```
python3 stream_and_pub.py
```

# Listen and insert into BigQuery

```
python3 sub_and_insert.py
```
