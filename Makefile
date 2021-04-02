analyze:run repo_details.json
	python3 Analysis/api_call.py && python3 Analysis/get_depend.py
run:input.py
	python3 input.py