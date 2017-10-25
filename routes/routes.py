
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/extra",
			extra.dbHandler
		),
		(
			r"/notes",
			home.notesHandler
		),
		(
			r"/backup",
			backup.backUpAllHandler
		),
		(
			r"/restore",
			backup.restoreHandler
		),
		(
			r"/backup/delete",
			backup.deleteDataHandler
		),
		(
			r"/account/login",
			auth.loginHandler
		),
		(
			r"/data/([^/]+)",
			backup.getDataHandler
		),
		(
			r"/osl",
			home.oslHandler
		),
		# ********************************* Encryption ***************************************************
		(
			r"/encrypt",
			extra.encryptHandler
		),
		# ********************************* ADMIN ***************************************************
		(
			r"/admin/users",
			admin.usersHandler
		)





		# mobile computing
		,
		(
			r"/mobile/data",
			mobile.dataHandler
		),
		(
			r"/mobile/allData",
			mobile.allDataHandler
		)

]