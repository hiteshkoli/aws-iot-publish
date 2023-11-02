# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import time as t
import json
import AWSIoTPythonSDK.MQTTLib as AWSIoTPyMQTT

#Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1, MESSAGE, TOPIC, and RANGE
ENDPOINT = "<AWS-ENDPOINT>"
CLIENT_ID = "<CLIENT_ID>"
PATH_TO_CERTIFICATE = "<PATH_TO_CERTIFICATE>"
PATH_TO_PRIVATE_KEY = "<PATH_TO_PRIVATE_KEY>"
PATH_TO_AMAZON_ROOT_CA_1 = "<PATH_TO_AMAZON_ROOT_CA_1>"
MESSAGE = "<MESSAGE>"
TOPIC = "<TOPIC_TO_PUBLISH>"
RANGE = 20

myAWSIoTMQTTClient = AWSIoTPyMQTT.AWSIoTMQTTClient(CLIENT_ID)
myAWSIoTMQTTClient.configureEndpoint(ENDPOINT, 8883)
myAWSIoTMQTTClient.configureCredentials(PATH_TO_AMAZON_ROOT_CA_1, PATH_TO_PRIVATE_KEY, PATH_TO_CERTIFICATE)

myAWSIoTMQTTClient.connect()
print("Connected!")
print('Begin Publish')
for i in range (RANGE):
    data = "{} [{}]".format(MESSAGE, i+1)
    message = {"message" : data}
    myAWSIoTMQTTClient.publish(TOPIC, json.dumps(message), 1) 
    print("Published: '" + json.dumps(message) + "' to the topic: " + "'test/topic'")
    t.sleep(0.1)
print('Publish End')
myAWSIoTMQTTClient.disconnect()