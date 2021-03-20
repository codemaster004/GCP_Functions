gcloud functions deploy MyFirstApi --region=europe-west3 --entry-point=hello_world --runtime=python38 --source=MyFirstApi/src --max-instances=1 --trigger-http --allow-unauthenticated
