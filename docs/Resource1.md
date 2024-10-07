# Resource1

Resource object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The Name of the Resource | [optional] 
**source_uid** | **str** | The unique identifier for this resource from the external system which owns the schedule data. | [optional] 

## Example

```python
from procore_sdk.models.resource1 import Resource1

# TODO update the JSON string below
json = "{}"
# create an instance of Resource1 from a JSON string
resource1_instance = Resource1.from_json(json)
# print the JSON string representation of the object
print(Resource1.to_json())

# convert the object into a dict
resource1_dict = resource1_instance.to_dict()
# create an instance of Resource1 from a dict
resource1_from_dict = Resource1.from_dict(resource1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


