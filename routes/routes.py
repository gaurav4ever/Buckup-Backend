
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
		)
]