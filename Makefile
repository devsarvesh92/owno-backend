migrate:
	@echo "Migrating database..."
	@piccolo migrations new owno --auto
	@piccolo migrations forward owno

run-server:
	@echo "Running server..."
	@piccolo run