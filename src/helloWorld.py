from datetime import datetime


def lambda_handler(event, context):
    maintenant = datetime.today().strftime("%Y-%m-%d, %H:%M:%S")
    print(f"Hello world V1 @{maintenant}")
