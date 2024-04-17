update_env:
	@echo "Updating the 'maximum_path_sum_python' Conda environment from environment.yml..."
	conda env update --name maximum_path_sum_python --file environment.yml
	@echo "Please activate the Conda environment with the following command: conda activate maximum_path_sum_python"