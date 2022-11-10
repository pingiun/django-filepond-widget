.PREFIXES:

.PHONY: build
build: src/django_filepond_widget/static/django_filepond_widget/js/filepond.min.js src/django_filepond_widget/static/django_filepond_widget/css/filepond.min.css src/django_filepond_widget/static/django_filepond_widget/js/js-cookie.min.js
	python3 -m build --sdist

node_modules: package.json yarn.lock
	yarn install

src/django_filepond_widget/static/django_filepond_widget/js/filepond.min.js: node_modules
	cp node_modules/filepond/dist/filepond.min.js src/django_filepond_widget/static/django_filepond_widget/js/filepond.min.js

src/django_filepond_widget/static/django_filepond_widget/css/filepond.min.css: node_modules
	cp node_modules/filepond/dist/filepond.min.css src/django_filepond_widget/static/django_filepond_widget/css/filepond.min.css

src/django_filepond_widget/static/django_filepond_widget/js/js-cookie.min.js: node_modules
	cp node_modules/js-cookie/dist/js.cookie.js src/django_filepond_widget/static/django_filepond_widget/js/js.cookie.min.js

.PHONY: clean
clean:
	@rm -rf dist
	@rm -rf src/django_filepond_widget/static/django_filepond_widget/js/filepond.min.js
	@rm -rf src/django_filepond_widget/static/django_filepond_widget/css/filepond.min.css
	@rm -rf src/django_filepond_widget/static/django_filepond_widget/js/js.cookie.min.js
	@rm -rf node_modules
