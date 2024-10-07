# IncidentUnitOfMeasure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The display value for the unit of measure. | [optional] 
**value** | **str** | The value actually stored as the unit of measure. | [optional] 

## Example

```python
from procore_sdk.models.incident_unit_of_measure import IncidentUnitOfMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of IncidentUnitOfMeasure from a JSON string
incident_unit_of_measure_instance = IncidentUnitOfMeasure.from_json(json)
# print the JSON string representation of the object
print(IncidentUnitOfMeasure.to_json())

# convert the object into a dict
incident_unit_of_measure_dict = incident_unit_of_measure_instance.to_dict()
# create an instance of IncidentUnitOfMeasure from a dict
incident_unit_of_measure_from_dict = IncidentUnitOfMeasure.from_dict(incident_unit_of_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


