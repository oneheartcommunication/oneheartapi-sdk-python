# -*-coding:utf-8 -*

import http.client
import base64
import json
import sys

class OneHeartAPIClient:
	
	_clientid = None
	_clientsecret = None
	
	def __init__(self, clientid, clientsecret):
		self._clientid = clientid
		self._clientsecret = clientsecret
		self.players = OneHeartAPI_Module(self, "players")
		self.users = OneHeartAPI_Module(self, "users")
		self.videos = OneHeartAPI_Module(self, "videos")
		self.events = OneHeartAPI_Module(self, "events")
		self.news = OneHeartAPI_Module(self, "news")
		self.spots = OneHeartAPI_Module(self, "spots")
		self.urls = OneHeartAPI_Module(self, "urls")
		self.actions = OneHeartAPI_Module(self, "actions")
		self.causes = OneHeartAPI_Module(self, "causes")
	
	def _request(self, path, params, method):
		body = "?"
		for paramkey in params.keys():
			body += str(paramkey)+"="+str(params[paramkey])+"&"
		userAndPass = base64.b64encode(bytearray(self._clientid+":"+self._clientsecret, 'utf-8')).decode("ascii")
		headers = { 'Authorization' : 'Basic %s' %  userAndPass }
		httpclient = http.client.HTTPConnection("www.oneheart.fr")
		httpclient.request(method, "/api/"+path+body, headers=headers)
		response = httpclient.getresponse()
		return json.loads(response.read().decode('utf-8'))


class OneHeartAPI_Module:
	
	_master = None
	_collection = None
	
	def __init__(self, master, collection):
		self._collection = collection
		self._master = master
	
	def summary(self, offset = 0, max = 10, fields = None, sort = None):
		params = {"offset":offset, "max":max}
		fieldsstr = ""
		if(fields != None):
			for field in fields:
				fieldsstr += ","+field
			params['fields'] = fieldsstr
		if(sort != None):
			params['sort'] = sort
		return self._master._request(self._collection, params, "GET")
	
	def single(self, id, fields = None):
		fieldsstr = ""
		params = {}
		if(fields != None):
			for field in fields:
				fieldsstr += ","+field
			params['fields'] = fieldsstr
		return self._master._request(self._collection+"/"+id, params, "GET")
	
	def action(self, id, action_id):
		return self._master._request(self._collection+"/"+id+"/"+action_id, {}, "POST")
		
