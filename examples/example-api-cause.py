# -*-coding:utf-8 -*

from neural import Neural
from oneheart import OneHeartAPIClient

api = OneHeartAPIClient("app_id", "app_secret")
cause = api.causes.single('55efd5ad8ead0e3efe06fd90')
print(cause)