import json
import jsonschema
from jsonschema import validate
import multiprocessing
from multiprocessing import Value
import datetime

start_time = datetime.datetime.now()

# JSON Schema
# Gender - Male / Female / Others
# HeighCm - 1cm - 300cm
# WeightKg - 1kg - 450kg
schema = {
	"title" : "BMI Schema",
	"properties" : {
    	"Gender"   : {"type" : "string", "enum": ["Male", "Female", "Others"]},
		"HeightCm" : {"type" : "number", "minimum" : 1, "maximum" : 300},
		"WeightKg" : {"type" : "number", "minimum" : 1, "maximum" : 450}
	},
	"required" : [
		"Gender",
		"HeightCm",
		"WeightKg"
	]
}

overweight_counter = None

def validate_json(input_list):
	try:
		for record in input_list:
			record_str = json.dumps(record)
			jsonData = json.loads(record_str)
			validate(instance=jsonData, schema=schema)
	except jsonschema.exceptions.ValidationError:
		return 'Invalid JSON'
	else:
		return 'Valid JSON'

def init(args):
	global overweight_counter
	overweight_counter = args

def calculate_bmi(record):
	global overweight_counter
	bmi = round(record['WeightKg']/((record['HeightCm']/100)*(record['HeightCm']/100)),1)
	record['bmi'] = bmi
	if bmi <= 18.4:
		record['bmi_category'], record['health_risk'] = 'Underweight' , 'Malnutrition risk'
	elif bmi >= 18.5 and bmi <= 24.9:
		record['bmi_category'], record['health_risk'] = 'Normal weight' , 'Low risk'
	elif bmi >= 25 and bmi <= 29.9:
		record['bmi_category'], record['health_risk'] = 'Overweight' , 'Enhanced risk'
		with overweight_counter.get_lock():
			overweight_counter.value += 1
	elif bmi >= 30 and bmi <= 34.9:
		record['bmi_category'], record['health_risk'] = 'Moderately obese' , 'Medium risk'
	elif bmi >= 35 and bmi <= 39.9:
		record['bmi_category'], record['health_risk'] = 'Severely obese' , 'High risk'
	elif bmi >= 40:
		record['bmi_category'], record['health_risk'] = 'Very Severely obese' , 'Very high risk'
	return record

if __name__ == '__main__':
	try:
		# relative or absolute path of the input json file
		file = r'testfile.json'
		with open(file, "r") as f:
			input_list = json.load(f)
		result = validate_json(input_list)

		if result == 'Valid JSON':
			overweight_counter = Value('i',0)
			pool = multiprocessing.Pool(multiprocessing.cpu_count()-2, initializer = init, initargs = (overweight_counter, ))
			output_async = pool.map_async(calculate_bmi, input_list)
			output_async.wait()
			output = output_async.get()
			print('output', output)
			print('overweight_counter', overweight_counter.value)

		else:
			print('Invalid JSON')
	except Exception as e:
		print(e)
	
	end_time = datetime.datetime.now()
	process_time = end_time - start_time
	print('process_time', process_time)