#!/bin/bash

#DEFINE VARIABLES
PORT=8080
MEMORY=2Gi
INGRESS=all
IMAGE_NAME=model
REGION=us-central1
PROJECT=debtrust001 
SERVICE_NAME=model-service

#ENABLE APIS
echo "Start to enable service"
gcloud services enable run.googleapis.com --project=$PROJECT
gcloud services enable containerregistry.googleapis.com --project=$PROJECT
echo "Enabled services successfully"

#AUTHENTICATE TO GOOGLE CONTAINER REGISTORY
echo "Start to authenticate with docker"
gcloud auth configure-docker
echo "Authenticate successfully"

#BUILD TAG AND PUSH DOCKER IMAGE TO CONTAINER REGISTORY
echo "Building docker image"
docker image build -t $IMAGE_NAME:latest .
docker image tag $IMAGE_NAME:latest gcr.io/$PROJECT/$IMAGE_NAME:latest
docker image push gcr.io/$PROJECT/$IMAGE_NAME:latest
echo "Image build successfully"

#DEPLOY CLOUD RUN
echo "Deploy model"
gcloud run deploy $SERVICE_NAME --image=gcr.io/$PROJECT/$IMAGE_NAME:latest \
--memory=$MEMORY --port=$PORT --region=$REGION --ingress=$INGRESS \
--allow-unauthenticated --project=$PROJECT
echo "Model deployed successfully"