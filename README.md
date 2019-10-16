# Movies and TV Shows API Documentation

#### by Bernard Bollinger

This API was created as three AWS Lambda functions written in python with Lambda proxy integration to pass data to and from an API deployed in AWS API Gateway. Each Lambda function takes in parameters from the query string of an incoming request, then requests movie or show data from a free API at themoviedb.org. It then returns the same JSON data returned by themoviedb.org as a response to the initial request. Below is the syntax for calls to the API. The Movies and TV Shows API requires no API key.
