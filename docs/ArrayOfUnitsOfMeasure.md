# ArrayOfUnitsOfMeasure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entities** | [**List[RestV10CompaniesCompanyIdUomsGet200ResponseInner]**](RestV10CompaniesCompanyIdUomsGet200ResponseInner.md) |  | [optional] 
**errors** | [**List[ArrayOfUnitsOfMeasureErrorsInner]**](ArrayOfUnitsOfMeasureErrorsInner.md) |  | [optional] 

## Example

```python
from procore_sdk.models.array_of_units_of_measure import ArrayOfUnitsOfMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfUnitsOfMeasure from a JSON string
array_of_units_of_measure_instance = ArrayOfUnitsOfMeasure.from_json(json)
# print the JSON string representation of the object
print(ArrayOfUnitsOfMeasure.to_json())

# convert the object into a dict
array_of_units_of_measure_dict = array_of_units_of_measure_instance.to_dict()
# create an instance of ArrayOfUnitsOfMeasure from a dict
array_of_units_of_measure_from_dict = ArrayOfUnitsOfMeasure.from_dict(array_of_units_of_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


