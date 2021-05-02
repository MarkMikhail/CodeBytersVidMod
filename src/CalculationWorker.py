#################################################################
# Agora Digital Solutions Inc.
# ###############################################################
# Copyright 2020 Agora Digital Solutions IncS.

# All rights reserved in Agora Digital Solutions Inc. authored and generated code (including the selection and arrangement of the source code base regardless of the authorship of individual files), but not including any copyright interest(s) owned by a third party related to source code or object code authored or generated by non- Agora Digital Solutions Inc. personnel.
# Any use, disclosure and/or reproduction of source code is prohibited unless in compliance with the AGORA SOFTWARE DEVELOPMENT KIT LICENSE AGREEMENT.
#################################################################
from WorkerThread import WorkerThread
from HBM_PythonAppManagerBindings import *
import time
import logging
#import numpy as np

class CalculationWorker(WorkerThread):

	privateRun = False
	privateBusClient = None
	privateDataOutEndpoint = ""

	def __init__(self):
		WorkerThread.__init__(self)
		self.setName("CalculationWorker")
		self.privateRun = False

		#setup the IOs
		self.privateA = IO_POINT_T()
		self.privateB = IO_POINT_T()
		self.privateC = IO_POINT_T()

		self.privateA.name = "io-a"
		self.privateB.name = "io-b"
		self.privateC.name = "io-c"

		self.privateA.ion_data_type = 8
		self.privateB.ion_data_type = 8
		self.privateC.ion_data_type = 8

		self.privateA.io_id = 1
		self.privateB.io_id = 2
		self.privateC.io_id = 3

	def Configure(self, serializer):
		logging.debug("New config received")

	def Initialize(self, name, busClient, dataOutEndpoint):
		logging.debug("Initialize thread CalculationWorker")
		self.privateBusClient = busClient
		self.privateDataOutEndpoint = dataOutEndpoint
		
	def HandleData(self, serializer):
		logging.debug("handleData thread CalculationWorker")

	def run(self):
		logging.debug("running thread CalculationWorker")
		self.privateRun = True
		while(self.privateRun == True):
			if (self.stopped() == True):
				logging.debug("Stopping thread CalculationWorker")
				self.privateRun = False
			else:
				time.sleep(1)
				logging.debug("Thread running")
				#tropico = np.array([[1,2], [3, 4], [5, 6]])
				#bool_idx = (tropico > 2) 
				#logging.debug(tropico[bool_idx])  