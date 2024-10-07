# Resource2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Resource id | [optional] 
**name** | **str** | Resource name | [optional] 
**source_uid** | **str** | The unique identifier for this resource from the external system which owns the schedule data. | [optional] 

## Example

```python
from procore_sdk.models.resource2 import Resource2

# TODO update the JSON string below
json = "{}"
# create an instance of Resource2 from a JSON string
resource2_instance = Resource2.from_json(json)
# print the JSON string representation of the object
print(Resource2.to_json())

# convert the object into a dict
resource2_dict = resource2_instance.to_dict()
# create an instance of Resource2 from a dict
resource2_from_dict = Resource2.from_dict(resource2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


