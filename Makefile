pep8_res:
	pep8 point.py; pep8 convex_polygon.py;

pylint_point:
	pylint point.py;

pylint_convex:
	pylint convex_polygon.py;

coverage:
	nosetests --with-coverage --cover-html --cover-package='point' --cover-package='convex_polygon'
