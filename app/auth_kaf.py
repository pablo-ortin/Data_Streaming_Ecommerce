conf = {'bootstrap.servers': "YOUR CONFLUENT CLOUD CLUSTER SERVER", # Bootstrap server Confluent Cloud (AWS, Azure, Google)
        'security.protocol':'SASL_SSL',        
        'sasl.mechanisms':'PLAIN',
        'sasl.username' : 'YOUR API KEY', # API Key Confluent Cloud
        'sasl.password' : 'YOUR SECRET'}  # Secret Confluent Cloud