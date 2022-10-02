.PHONY: fix
fix:
	black app
	isort app

.PHONY: lint
lint:
	black app
	isort app

.PHONY: test
test:
	pytest app

.DEFAULT_GOAL :=